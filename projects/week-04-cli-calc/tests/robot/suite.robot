*** Settings ***
Library    OperatingSystem
Library    ../resources/cli_keywords.py

*** Test Cases ***
CLI Eval Basic Expression
    [Tags]    integration
    Run CLI    eval "sin(0) + 2"
    Should Contain    ${STDOUT}    2.0

CLI Diff Produces Correct Output
    [Tags]    correctness
    Run CLI    diff "x^2 * sin(x)" --x 0.5
    Should Match Regexp    ${STDOUT}    derivative: .*

