#!/usr/bin/env python3
import datetime
import os
import shutil
import subprocess

def main():
    # Determine current month/week
    today = datetime.date.today()
    month = today.strftime("%B %Y")
    week_number = today.isocalendar()[1]

    # Paths
    template = "README_TEMPLATE.md"
    output = f"README_{month.replace(' ', '_')}_Week{week_number}.md"

    # Copy template
    shutil.copy(template, output)

    # Replace placeholders
    with open(output, "r") as f:
        content = f.read()
    content = content.replace("{{MONTH}}", month).replace("{{WEEK}}", str(week_number))
    with open(output, "w") as f:
        f.write(content)

    print(f"Created {output}. Opening editor...")
    # Open in default editor
    if os.name == "nt":  # Windows
        os.startfile(output)
    elif os.uname().sysname == "Darwin":  # macOS
        subprocess.call(["open", output])
    else:  # Linux
        subprocess.call(["xdg-open", output])

    input("Press Enter after saving and closing the README...")

    # Git automation
    try:
        subprocess.check_call(["git", "add", output])
        commit_msg = f"Add demo report for {month}, Week {week_number}"
        subprocess.check_call(["git", "commit", "-m", commit_msg])
        subprocess.check_call(["git", "push"])
        print("✅ README committed and pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print("⚠️ Git command failed. Please check your repo setup and credentials.")
        print(e)

if __name__ == "__main__":
    main()
