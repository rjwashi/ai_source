#!/usr/bin/env python3
"""
sync_local_ai_source_with_github.py

Python version of sync_local_ai_source_with_github.sh
Adds detailed comments, error handling, and timestamped logging.
Removes weekly branches and deletes all non-main branches locally and remotely.
"""

import os
import sys
import subprocess
import logging
from pathlib import Path

# ---------- Logging Setup ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def run_git_command(args, cwd=None, check=True):
    """Run a git command safely with subprocess."""
    try:
        logging.info("Running command: git %s", " ".join(args))
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            check=check,
            text=True,
            capture_output=True
        )
        if result.stdout.strip():
            logging.info(result.stdout.strip())
        if result.stderr.strip():
            logging.warning(result.stderr.strip())
        return result
    except subprocess.CalledProcessError as e:
        logging.error("Git command failed: %s", e.stderr.strip())
        raise

def main():
    # ---------- Root Directory ----------
    LOCAL_ROOT = str(Path.home() / "ai_source")
    if not os.path.isdir(LOCAL_ROOT):
        logging.error("Local path '%s' does not exist.", LOCAL_ROOT)
        sys.exit(1)

    GITHUB_USER = "rjwashi"
    REPO_NAME = "ai_source"
    REMOTE_STYLE = os.getenv("REMOTE_STYLE", "ssh")
    MAIN_BRANCH = os.getenv("MAIN_BRANCH", "main")
    ALLOW_FORCE_PUSH = os.getenv("ALLOW_FORCE_PUSH", "no")

    REMOTE_URL = (
        f"git@github.com:{GITHUB_USER}/{REPO_NAME}.git"
        if REMOTE_STYLE == "ssh"
        else f"https://github.com/{GITHUB_USER}/{REPO_NAME}.git"
    )

    logging.info("Working in %s", LOCAL_ROOT)

    # ---------- Initialize repo ----------
    if not os.path.isdir(os.path.join(LOCAL_ROOT, ".git")):
        logging.info("Initializing new git repository.")
        run_git_command(["init", "-b", MAIN_BRANCH], cwd=LOCAL_ROOT)
    else:
        logging.info("Git repository detected.")

    # ---------- Commit changes ----------
    status = run_git_command(["status", "--porcelain"], cwd=LOCAL_ROOT, check=False)
    has_commit = run_git_command(["rev-parse", "--verify", "HEAD"], cwd=LOCAL_ROOT, check=False).returncode == 0

    if status.stdout.strip():
        logging.info("Staging and committing changes.")
        run_git_command(["add", "-A"], cwd=LOCAL_ROOT)
        msg = "chore: checkpoint commit" if has_commit else "chore: initial commit"
        run_git_command(["commit", "-m", msg], cwd=LOCAL_ROOT)
    elif not has_commit:
        logging.info("Creating initial empty commit.")
        run_git_command(["commit", "--allow-empty", "-m", "chore: initial empty commit"], cwd=LOCAL_ROOT)
    else:
        logging.info("No changes to commit.")

    # ---------- Configure remote ----------
    try:
        existing_url = run_git_command(["remote", "get-url", "origin"], cwd=LOCAL_ROOT, check=False).stdout.strip()
        if existing_url != REMOTE_URL:
            logging.warning("Updating origin from %s to %s", existing_url, REMOTE_URL)
            run_git_command(["remote", "set-url", "origin", REMOTE_URL], cwd=LOCAL_ROOT)
    except Exception:
        logging.info("Adding origin remote: %s", REMOTE_URL)
        run_git_command(["remote", "add", "origin", REMOTE_URL], cwd=LOCAL_ROOT)

    # ---------- Push main branch ----------
    push_opts = ["--force"] if ALLOW_FORCE_PUSH == "yes" else []
    logging.info("Pushing branch %s to origin...", MAIN_BRANCH)
    run_git_command(["push"] + push_opts + ["-u", "origin", MAIN_BRANCH], cwd=LOCAL_ROOT)

    # ---------- Delete non-main branches ----------
    logging.info("Checking for non-main branches to delete...")

    # Local branches
    local_branches = run_git_command(["branch"], cwd=LOCAL_ROOT, check=False).stdout.splitlines()
    for branch in [b.strip().lstrip("* ") for b in local_branches if b.strip()]:
        if branch != MAIN_BRANCH:
            logging.warning("Deleting local branch: %s", branch)
            run_git_command(["branch", "-D", branch], cwd=LOCAL_ROOT, check=False)

    # Remote branches
    remote_branches = run_git_command(["branch", "-r"], cwd=LOCAL_ROOT, check=False).stdout.splitlines()
    for rb in [b.strip() for b in remote_branches if b.strip()]:
        if f"origin/{MAIN_BRANCH}" not in rb:
            branch_name = rb.split("/", 1)[1]
            logging.warning("Deleting remote branch: %s", branch_name)
            run_git_command(["push", "origin", "--delete", branch_name], cwd=LOCAL_ROOT, check=False)

    logging.info("Sync complete. Only '%s' branch remains locally and remotely.", MAIN_BRANCH)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error("Fatal error: %s", str(e))
        sys.exit(1)

