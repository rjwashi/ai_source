#!/usr/bin/env bash
# scaffold_robot_tests.sh
#
# Creates Robot Framework test folders and example suite.robot files for Weeks 1–12
# under an existing ai_source/projects/ tree.
# If a project's tests/robot folder exists it will be removed and recreated.
#
# Usage:
#   chmod +x scaffold_robot_tests.sh
#   ./scaffold_robot_tests.sh               # uses ./ai_source/projects as root
#   ./scaffold_robot_tests.sh /path/to/ai_source/projects
#   OVERWRITE=1 ./scaffold_robot_tests.sh   # will overwrite files if any exist (redundant with deletion behavior)
#
# Behavior summary:
# - For each week (week-01 .. week-12) it removes tests/robot if present, then creates:
#     projects/week-XX-*/tests/robot/
#     projects/week-XX-*/tests/robot/resources/
#     projects/week-XX-*/tests/robot/data/
#     projects/week-XX-*/tests/robot/reports/  (empty, runtime)
# - Writes a starter suite.robot with 3 example tests tailored to that week's theme
# - Writes a basic Python Robot keyword library template into resources/ (module)
# - Writes a simple README.md in the robot folder explaining how to run tests
#
# Notes:
# - This script intentionally removes existing robot test folders to ensure a clean scaffold.
# - Customize the generated keyword Python files with your project-specific imports
#   and implementations. The templates include docstrings and example keywords.
# - After scaffold: run robot from each week folder:
#     cd ai_source/projects/week-01-matrix-lib
#     robot -d tests/robot/reports tests/robot/suite.robot
#
set -euo pipefail

PROJECTS_ROOT="${1:-~/ai_source/projects}"
# Note: OVERWRITE is kept for compatibility but folder removal is unconditional for robot folder
OVERWRITE="${OVERWRITE:-0}"

# mapping week -> short folder name and friendly title
declare -A WEEK_NAME
WEEK_NAME["01"]="matrix-lib|Matrix Library"
WEEK_NAME["02"]="probability-simulator|Probability Simulator"
WEEK_NAME["03"]="symbolic-diff|Symbolic Differentiation Engine"
WEEK_NAME["04"]="cli-calc|CLI Calculator"
WEEK_NAME["05"]="feedforward-nn|Feedforward Neural Network"
WEEK_NAME["06"]="char-rnn|Character-level RNN"
WEEK_NAME["07"]="transformer-encoder|Transformer Encoder"
WEEK_NAME["08"]="small-bert|Small BERT Pretraining"
WEEK_NAME["09"]="benchmark-models|Benchmark Open-Source Models"
WEEK_NAME["10"]="sft-rlhf|SFT and RLHF Pipelines"
WEEK_NAME["11"]="scaling-laws|Analyze Scaling Laws"
WEEK_NAME["12"]="model-selector|Model Selector and Router"

echo
echo "[INFO] Scaffolding Robot tests under: $PROJECTS_ROOT"
mkdir -p "$PROJECTS_ROOT"

create_file() {
  local dest="$1"
  local content="$2"
  mkdir -p "$(dirname "$dest")"
  printf "%s\n" "$content" > "$dest"
  echo "  created: $dest"
}

for w in 01 02 03 04 05 06 07 08 09 10 11 12; do
  IFS='|' read -r short title <<< "${WEEK_NAME[$w]}"
  folder_name="week-$w-$short"
  PROJECT_DIR="$PROJECTS_ROOT/$folder_name"
  ROBOT_DIR="$PROJECT_DIR/tests/robot"
  RES_DIR="$ROBOT_DIR/resources"
  DATA_DIR="$ROBOT_DIR/data"
  REPORTS_DIR="$ROBOT_DIR/reports"

  echo
  echo "[INFO] Week $w -> $folder_name"
  # Remove existing robot folder if present
  if [ -d "$ROBOT_DIR" ]; then
    echo "  removing existing robot folder: $ROBOT_DIR"
    rm -rf "$ROBOT_DIR"
  fi

  # Recreate directories
  mkdir -p "$RES_DIR" "$DATA_DIR" "$REPORTS_DIR"
  echo "  created dirs: $RES_DIR  $DATA_DIR  $REPORTS_DIR"

  # suite.robot content (tailored minimal examples)
  read -r -d '' SUITE_ROBOT <<ROBOT
*** Settings ***
Library           ../resources/keywords_${short}.py
Library           OperatingSystem
Suite Setup       Setup Suite
Suite Teardown    Teardown Suite
Test Timeout      10 minutes
Resource          resources/common.robot

*** Variables ***
\${REPORTS_DIR}    ${REPORTS_DIR}
\${DATA_DIR}       ${DATA_DIR}

*** Test Cases ***
Smoke Test ${title}
    [Tags]    smoke    correctness
    Log To Console    Running smoke test for ${title}
    \${EMPTY} =    Create Example Artifact
    Should Be Equal As Strings    \${EMPTY}    OK

Functional Test ${title} Example
    [Tags]    integration
    Log    Example functional test for ${title}
    \${res} =    Run Functional Example
    Should Not Be Empty    \${res}

Performance Example ${title}
    [Tags]    performance
    Log    Example performance measurement
    Start Performance Measurement
    Sleep    0.1s
    Stop Performance Measurement And Assert    max_seconds=1.0
ROBOT

  create_file "$ROBOT_DIR/suite.robot" "$SUITE_ROBOT"

  # common.robot resource (shared simple keywords in Robot syntax)
  read -r -d '' COMMON_ROBOT <<'COMMON'
*** Keywords ***
Setup Suite
    Log    Suite setup (extend in your project)

Teardown Suite
    Log    Suite teardown (extend in your project)

Create Example Artifact
    [Return]    OK

Start Performance Measurement
    ${START} =    Set Variable    ${CURTIME}
    Set Suite Variable    ${_perf_start}    ${START}

Stop Performance Measurement And Assert
    [Arguments]    ${max_seconds}=1.0
    ${END} =    Set Variable    ${CURTIME}
    Log    Performance placeholder (implement real timing in Python keywords)
COMMON

  create_file "$ROBOT_DIR/resources/common.robot" "$COMMON_ROBOT"

  # basic Python keyword library for this week
  read -r -d '' PY_KEYLIB <<PY
# keywords_${short}.py
\"\"\"Robot Framework Python keyword library for ${title}
Place project-specific helpers here. Robot will import this module when running suite.robot.
Functions exposed are available as Robot keywords (underscores -> spaces).
\"\"\"
from robot.api import logger
import time
import json
import os

def setup_suite():
    logger.info("Python: setup_suite called")

def teardown_suite():
    logger.info("Python: teardown_suite called")

def create_example_artifact():
    \"\"\"Return a simple OK token used by the example smoke test.\"\"\"
    logger.info("Creating example artifact")
    return "OK"

def run_functional_example():
    \"\"\"Simulate a functional task and return a non-empty result string.\"\"\"
    # Replace with real calls into your project code, e.g. import and call functions
    result = "functional-result"
    logger.info(f"Functional example produced: {result}")
    return result

_perf_store = {}

def start_performance_measurement(name="default"):
    _perf_store[name] = time.time()
    logger.info(f"Performance start for {name}")

def stop_performance_measurement_and_assert(max_seconds=1.0, name="default"):
    if name not in _perf_store:
        raise AssertionError("Performance measurement not started")
    elapsed = time.time() - _perf_store[name]
    logger.info(f"Performance {name} elapsed={elapsed:.4f}s (max {max_seconds}s)")
    if elapsed > float(max_seconds):
        raise AssertionError(f"Performance threshold exceeded: {elapsed} > {max_seconds}")
    return elapsed

def write_json_report(report_path="reports/robot_example.json", content=None):
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    data = content or {"status": "ok", "ts": time.time()}
    with open(report_path, "w") as f:
        json.dump(data, f)
    logger.info(f"Wrote JSON report to {report_path}")
    return report_path

PY

  PY_FILE_PATH="$RES_DIR/keywords_${short}.py"
  create_file "$PY_FILE_PATH" "$PY_KEYLIB"
  chmod +x "$PY_FILE_PATH" || true

  # Write a simple data example (CSV)
  read -r -d '' DATA_SAMPLE <<'CSV'
# sample data for Robot tests (extend per project)
id,value
1,foo
2,bar
CSV
  create_file "$DATA_DIR/sample.csv" "$DATA_SAMPLE"

  # README for robot folder
  read -r -d '' ROBOT_README <<MD
# Robot tests for ${title}

Location: this folder contains Robot Framework test suites and supporting resources.

How to run locally:
1. Create a Python venv and install Robot Framework:
   python -m venv .venv
   source .venv/bin/activate
   pip install robotframework

2. Run the suite:
   cd $(pwd)/$ROBOT_DIR
   robot -d reports suite.robot

Artifacts:
- reports/ will contain output.xml, report.html, log.html after running.

Notes:
- Replace the example Python keyword library (resources/keywords_${short}.py) with real keywords that call your project code in src/.
- Use Robot tags (e.g., @performance, @smoke) to filter tests in CI.
MD

  create_file "$ROBOT_DIR/README.md" "$ROBOT_README"

done

echo
echo "[DONE] Robot test scaffolding complete."
echo "Next steps:"
echo " - Implement keywords in each resources/keywords_*.py to call your project code (src/)."
echo " - Add Robot and any test dependencies to each project's requirements.txt if needed."
echo " - Integrate Robot runs into CI; collect reports/ (output.xml, report.html, log.html) as artifacts."
echo
echo "Tip: the script removed any existing tests/robot folders before creating fresh scaffolds."

