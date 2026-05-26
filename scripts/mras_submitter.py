import asyncio
import json
import sys
from pathlib import Path
from playwright.async_api import async_playwright

async def submit_mras(harvest_json_path, capability_statement_path, dry_run=True):
    # Load the harvest data
    with open(harvest_json_path, 'r') as f:
        data = json.load(f)
    
    opportunity = data.get("opportunity", {})
    survey_url = opportunity.get("survey_url")
    
    if not survey_url:
        print("Error: No survey URL found in harvest data.")
        return

    # Company Profile (Derived from your SAM reference)
    company_profile = {
        "POC Email": "kendrick@spatialgis.com",
        "Company Name": "SpatialGIS, LLC",
        "GSA Contract Number": "47QTCK18D0004", # Example, update as needed
        "POC First Name": "Kendrick",
        "POC Last Name": "Faison",
        "POC Phone #": "240-123-4567",
        "UEI #": "XE8LEMK77DC9",
        "CAGE Code": "7RFJ7",
        "Company Website": "https://spatialgis.com"
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # Set to True for production
        context = await browser.new_context()
        page = await context.new_page()
        
        print(f"Navigating to: {survey_url}")
        await page.goto(survey_url)

        # 1. Fill Company & POC Information
        # Qualtrics forms often group these in text inputs near labels
        for label, value in company_profile.items():
            try:
                # Attempt to find by label or placeholder
                await page.get_by_label(label, exact=False).fill(value)
            except:
                print(f"Warning: Could not auto-fill {label}")

        # 2. Handle Business Size (Single Select)
        await page.get_by_text("s - small business", exact=False).click()

        # 3. Handle Socio-economic (Multi-select)
        # Example: select 'd' for Small Disadvantaged Business
        await page.get_by_text("d", exact=True).check()

        # 4. Technical Questions (Yes/No)
        # We'll default to 'Yes' for capability questions 1, 2, 3
        for i in range(1, 4):
            await page.locator(f"xpath=//div[contains(text(), '{i}. ')]/../../..//label[text()='Yes']").click()

        # 5. Handle Multiple Choice (Subcontracting/Lead Time)
        await page.get_by_text("None", exact=True).first.click() # Subcontracting
        await page.get_by_text("30 days or less", exact=True).click() # Lead Time

        # 6. Upload Capability Statement
        if capability_statement_path and Path(capability_statement_path).exists():
            print(f"Uploading statement: {capability_statement_path}")
            async with page.expect_file_chooser() as fc_info:
                await page.get_by_text("Drop files or click here to upload").click()
            file_chooser = await fc_info.value
            await file_chooser.set_files(capability_statement_path)
        else:
            print("Error: Capability Statement file not found.")

        # 7. Final Submission
        if dry_run:
            print("Dry run complete. Form is populated. Review the browser window.")
            await asyncio.sleep(60) # Keep browser open for review
        else:
            print("Submitting form...")
            await page.get_by_text("Submit").click()
            await page.wait_for_load_state("networkidle")
            print("Submission successful.")

        await browser.close()

if __name__ == "__main__":
    # Usage: python mras_submitter.py <harvest_json> <docx_path> [--submit]
    h_path = sys.argv[1] if len(sys.argv) > 1 else "/home/kendrick/.claude/projects/-home-kendrick/f1848b56-228f-4a6f-a1fe-530a65a3ba3a/tool-results/bpz5eb5mj.txt"
    f_path = sys.argv[2] if len(sys.argv) > 2 else "final/docx/technical-volume.docx"
    is_dry = "--submit" not in sys.argv
    
    asyncio.run(submit_mras(h_path, f_path, dry_run=is_dry))