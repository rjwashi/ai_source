import os
import subprocess
import sys
import logging

# --- Configuration ---
ENV_NAME = os.path.basename(os.getcwd())
REQUIREMENTS_FILE = "requirements.txt"

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_venv_pip_path():
    """Helper to determine the correct pip executable path inside the VENV."""
    if os.name == 'nt': # Windows
        pip_path = os.path.join(ENV_NAME, "Scripts", "pip.exe")
    else: # macOS/Linux/POSIX
        pip_path = os.path.join(ENV_NAME, "bin", "pip")
    
    if not os.path.exists(pip_path):
        logger.error(f"Pip executable not found at {pip_path}. Environment may not be set up correctly.")
        sys.exit(1)
    return pip_path

def create_venv():
    """Creates a virtual environment using the venv module."""
    if not ENV_NAME:
        logger.error("Could not determine the current directory name. Cannot create environment.")
        sys.exit(1)

    if os.path.exists(ENV_NAME):
        logger.info(f"Virtual environment '{ENV_NAME}' already exists. Skipping creation.")
        return

    logger.info(f"Attempting to create virtual environment '{ENV_NAME}'...")
    try:
        # Create a clean, isolated environment
        subprocess.run(
            [sys.executable, "-m", "venv", "--clear", "--without-pip", ENV_NAME], 
            check=True, 
            capture_output=True, 
            text=True
        )
        logger.info("Virtual environment created successfully (without system site packages).")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to create virtual environment: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred during venv creation: {e}")
        sys.exit(1)

def install_base_pip_in_venv():
    """Installs pip and setuptools into the newly created isolated venv."""
    logger.info(f"Installing base 'pip' and 'setuptools' into the new venv...")
    try:
        # Use ensurepip to bootstrap pip within the new environment
        subprocess.run(
            [sys.executable, "-m", "ensurepip", "--upgrade", "--default-pip"],
            cwd=os.path.abspath(ENV_NAME), # Run this command from within the new venv directory context
            check=True, 
            capture_output=True, 
            text=True
        )
        logger.info("Base pip installation successful.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to install pip in venv: {e.stderr}")
        sys.exit(1)

def generate_requirements_from_venv_only():
    """
    Detects installed packages using pip freeze *within the specific VENV only* 
    and writes them to the requirements.txt file in the parent directory.
    """
    pip_path = get_venv_pip_path()
    
    logger.info(f"Running 'pip freeze' inside '{ENV_NAME}' to generate '{REQUIREMENTS_FILE}'...")
    
    try:
        # Run pip freeze using the VENV's specific pip executable
        result = subprocess.run(
            [pip_path, "freeze"], 
            check=True, 
            capture_output=True, 
            text=True
        )
        packages = result.stdout
        
        with open(REQUIREMENTS_FILE, "w") as f:
            f.write(packages)
        
        # The requirements file will likely just contain pip/setuptools/wheel entries
        logger.info(f"Successfully generated '{REQUIREMENTS_FILE}' with packages found *only* in the new venv.")
        logger.info(f"Contents of {REQUIREMENTS_FILE}:\n---\n{packages}---")

    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to run 'pip freeze' in venv: {e.stderr}")
        sys.exit(1)
    except IOError as e:
        logger.error(f"Failed to write to '{REQUIREMENTS_FILE}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    logger.info("--- Starting Isolated Virtual Environment Setup Script ---")
    
    # Step 1: Create the new, clean virtual environment (isolated)
    create_venv()
    
    # Step 2: Ensure pip is installed within the new venv
    install_base_pip_in_venv()

    # Step 3: Now that the venv exists, detect packages ONLY from within it.
    generate_requirements_from_venv_only()
    
    logger.info("--- Setup Complete ---")
    print(f"\nTo activate your environment '{ENV_NAME}', use one of the following commands:")
    print(f"  macOS/Linux: source {ENV_NAME}/bin/activate")
    print(f"  Windows (CMD): {ENV_NAME}\\Scripts\\activate.bat")
    print(f"  Windows (PS): {ENV_NAME}\\Scripts\\Activate.ps1")

