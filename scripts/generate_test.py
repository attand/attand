#!/usr/bin/env python3
import subprocess
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate Playwright test using codegen")
    parser.add_argument("--url", default="https://the-internet.herokuapp.com", help="Starting URL")
    parser.add_argument("--output", "-o", default="test_generated.py", help="Output file path")
    parser.add_argument("--viewport", default="1280,720", help="Viewport size (width,height)")

    args = parser.parse_args()

    cmd = [
        "playwright", "codegen",
        args.url,
        "--output", args.output,
        "--viewport-size", args.viewport
    ]

    print(f"Starting Playwright Codegen...\nCommand: {' '.join(cmd)}")
    print("Press Ctrl+C in the terminal to stop if not using the codegen window close button.")

    try:
        subprocess.run(cmd, check=True)
        print(f"Test generated successfully at {args.output}")
    except subprocess.CalledProcessError as e:
        print(f"Error running codegen: {e}")
    except KeyboardInterrupt:
        print("\nCodegen interrupted.")

if __name__ == "__main__":
    main()
