import os
import sys
import argparse
import subprocess
from datetime import datetime

def main():
    # 1. Generate Timestamp and Paths
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_results_dir = os.path.join(os.getcwd(), "test-results", timestamp)
    screenshots_dir = os.path.join(base_results_dir, "screenshots")
    report_dir = os.path.join(base_results_dir, "report")
    playwright_dir = os.path.join(base_results_dir, "playwright")

    # 2. Create Directories
    os.makedirs(screenshots_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)
    os.makedirs(playwright_dir, exist_ok=True)

    print(f"Test Run: {timestamp}")
    print(f"Artifacts will be stored in: {base_results_dir}")

    # 3. Set Environment Variable for Framework to use
    env = os.environ.copy()
    env["SCREENSHOT_DIR"] = screenshots_dir

    # 4. Construct Pytest Command
    # Pass through any arguments provided to this script (e.g., test files)
    pytest_args = sys.argv[1:]
    cmd = [
        "pytest",
        f"--alluredir={report_dir}",
        f"--output={playwright_dir}",
    ] + pytest_args

    print(f"Running command: {' '.join(cmd)}")

    try:
        subprocess.run(cmd, env=env, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
    except Exception as e:
        print(f"Error running tests: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
