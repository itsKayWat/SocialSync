import subprocess
import sys

def install_requirements():
    requirements = [
        'pillow',
        'tkcalendar',
        'python-dateutil'
    ]

    print("Installing required packages...")
    
    for package in requirements:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}: {e}")
            return False
    
    print("\nAll requirements installed successfully!")
    return True

if __name__ == "__main__":
    install_requirements()