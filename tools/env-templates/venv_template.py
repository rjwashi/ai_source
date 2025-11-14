#!/usr/bin/env python3
"""
Hidden virtual environment setup with auto-activation and clean deactivation (Linux).

- Creates hidden venv `.venv`
- Ensures pip is installed
- Auto-activates the venv by exec'ing into a Bash subshell
- Generates requirements.txt strictly from venv packages
- Provides a clean way to deactivate back to your original shell
"""

import os
import subprocess
import sys
import logging
from pathlib import Path

# --- Configuration ---
PROJECT_ROOT = Path(os.getcwd())
ENV_NAME = ".venv"
ENV_PATH = PROJECT_ROOT / ENV_NAME
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements.txt"

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


# ---------- Path helpers ----------
def get_venv_python_path() -> Path:
    return ENV_PATH / "bin" / "python"

def get_venv_pip_path() -> Path:
    return ENV_PATH / "bin" / "pip"

def get_activation_script() -> Path:
    return ENV_PATH / "bin" / "activate"


# ---------- Subprocess helper ----------
def run(cmd, *, cwd=None, check=True, capture=True):
    logger.info("Running: %s", " ".join(map(str, cmd)))
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            check=check,
            text=True,
            capture_output=capture
        )
        if capture:
            if result.stdout:
                logger.info(result.stdout.strip())
            if result.stderr:
                logger.warning(result.stderr.strip())
        return result
    except subprocess.CalledProcessError as e:
        msg = e.stderr.strip() if capture and e.stderr else str(e)
        logger.error("Command failed: %s", msg)
        raise


# ---------- Core actions ----------
def create_venv():
    if ENV_PATH.exists():
        logger.info("Hidden venv '%s' already exists. Skipping creation.", ENV_NAME)
        return

    logger.info("Creating hidden virtual environment '%s'...", ENV_NAME)
    run([sys.executable, "-m", "venv", "--clear", "--without-pip", str(ENV_PATH)])
    logger.info("Hidden venv created successfully.")

def ensure_pip_in_venv():
    vpy = get_venv_python_path()
    vpip = get_venv_pip_path()

    if not vpy.exists():
        logger.error("Venv python not found at '%s'.", vpy)
        sys.exit(1)

    if vpip.exists():
        logger.info("pip already present in hidden venv. Skipping ensurepip.")
        return

    logger.info("Installing pip into hidden venv...")
    run([str(vpy), "-m", "ensurepip", "--upgrade", "--default-pip"])
    if not vpip.exists():
        logger.error("pip executable not found after ensurepip at '%s'.", vpip)
        sys.exit(1)
    logger.info("pip installation successful.")

def generate_requirements_from_venv_only():
    vpip = get_venv_pip_path()
    if not vpip.exists():
        logger.error("pip not found in hidden venv at '%s'.", vpip)
        sys.exit(1)

    logger.info("Generating '%s' from hidden venv packages...", REQUIREMENTS_FILE)
    result = run([str(vpip), "freeze"])
    packages = result.stdout if result.stdout else ""
    REQUIREMENTS_FILE.write_text(packages, encoding="utf-8")
    logger.info("Successfully wrote '%s' with %d bytes.", REQUIREMENTS_FILE, len(packages))
    logger.info("Contents preview:\n---\n%s---", packages.strip())

def auto_activate():
    """
    Replace the current process with a Bash shell that sources the venv's activate script.
    When you exit that shell, you return to your original environment.
    """
    activate_script = get_activation_script()
    if not activate_script.exists():
        logger.error("Activation script not found at '%s'.", activate_script)
        sys.exit(1)

    logger.info("Auto-activating venv by exec'ing into a Bash subshell...")
    logger.info("To deactivate, simply type 'exit' or press Ctrl-D.")
    os.execvp("bash", ["bash", "--rcfile", str(activate_script)])


def main():
    logger.info("--- Starting Hidden Virtual Environment Setup Script ---")
    create_venv()
    ensure_pip_in_venv()
    generate_requirements_from_venv_only()
    auto_activate()  # drop into activated shell
    # Note: execution never returns here because execvp replaces the process.


if __name__ == "__main__":
    main()

