#!/usr/bin/env bash
# mras_submit_local.sh — LOCAL-ONLY MRAS submission runner
#
# WHY THIS EXISTS
# ---------------
# The cloud execution environment (Google Cloud Shell / Cloud Run) blocks
# outbound HTTPS traffic to feedback.gsa.gov (Qualtrics).  The mras_discover.py
# and mras_submitter.py scripts cannot reach survey URLs from that environment.
#
# This wrapper must be run from a LOCAL machine (or any environment with
# unrestricted outbound access to *.gsa.gov and *.qualtrics.com).
#
# USAGE
# -----
#   bash scripts/mras_submit_local.sh [SLUG]
#
#   SLUG  optional — the opportunity slug from working/mras-inbox/ (e.g.
#         doj-fbi-dssu-program-support).  If omitted, runs full discover +
#         triage + submit pipeline for all queued opportunities.
#
# PREREQUISITES
# -------------
#   pip install requests beautifulsoup4 google-auth google-auth-oauthlib
#   A working Gmail OAuth token at ~/.config/mras/gmail_token.json
#   (run  python scripts/mras_discover.py --auth  once to create it)
#
# ENVIRONMENT
# -----------
#   MRAS_DRY_RUN=1   Print what would be submitted without actually submitting
#   MRAS_VERBOSE=1   Extra logging

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

SLUG="${1:-}"
DRY_RUN="${MRAS_DRY_RUN:-0}"
VERBOSE="${MRAS_VERBOSE:-0}"

echo "=== MRAS Local Submission Runner ==="
echo "Repo:    $REPO_ROOT"
echo "Slug:    ${SLUG:-<all queued>}"
echo "Dry run: $DRY_RUN"
echo ""

# 1. Connectivity check
echo "[1/4] Checking connectivity to feedback.gsa.gov..."
if ! curl -sf --max-time 10 -o /dev/null "https://feedback.gsa.gov"; then
  echo "ERROR: Cannot reach feedback.gsa.gov from this machine."
  echo "       This script must be run locally — not in Cloud Shell."
  exit 1
fi
echo "      OK"

# 2. Discover / pull inbox (skipped if slug provided — assume already queued)
if [ -z "$SLUG" ]; then
  echo "[2/4] Pulling MRAS inbox from Gmail..."
  python scripts/mras_discover.py
  python scripts/mras_inbox_dedup.py
else
  echo "[2/4] Skipping discover (slug provided: $SLUG)"
fi

# 3. Classify / map answers
echo "[3/4] Classifying opportunities and mapping answers..."
if [ -n "$SLUG" ]; then
  python scripts/mras_triage_classify.py --slug "$SLUG"
  python scripts/mras_map_answers.py     --slug "$SLUG"
else
  python scripts/mras_triage_classify.py
  python scripts/mras_map_answers.py
fi

# 4. Submit
echo "[4/4] Submitting surveys..."
if [ "$DRY_RUN" = "1" ]; then
  echo "      DRY RUN — would submit:"
  if [ -n "$SLUG" ]; then
    python scripts/mras_submitter.py --slug "$SLUG" --dry-run
  else
    python scripts/mras_submitter.py --dry-run
  fi
else
  if [ -n "$SLUG" ]; then
    python scripts/mras_submitter.py --slug "$SLUG"
  else
    python scripts/mras_submitter.py
  fi
fi

echo ""
echo "=== Done. Check working/mras-inbox/ for updated queue files. ==="
echo "    Commit the updated queue files to record the run in git."
