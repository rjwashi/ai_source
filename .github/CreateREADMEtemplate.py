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
    # Open in default editor (cross-platform)
    if os.name == "nt":  # Windows
        os.startfile(output)
    elif os.uname().sysname == "Darwin":  # macOS
        subprocess.call(["open", output])
    else:  # Linux
        subprocess.call(["xdg-open", output])

    print("Paste metrics and links into the file, then save and close.")
    print("After editing, run: git add {output} && git commit -m 'Add demo report' && git push")

if __name__ == "__main__":
    main()
