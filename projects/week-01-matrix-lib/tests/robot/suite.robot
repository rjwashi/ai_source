*** Settings ***
Library           ../resources/matrix_keywords.py
Suite Setup       Setup Matrix Library
Suite Teardown    Teardown Matrix Library
Test Timeout      5 minutes

*** Variables ***
${SMALL_N}        5
${MEDIUM_N}       100
${LARGE_N}        300

*** Test Cases ***
Matrix Multiplication Correctness Small
    [Tags]    correctness
    Create Random Matrix    ${SMALL_N}    ${SMALL_N}    seed=42
    Create Random Matrix    ${SMALL_N}    ${SMALL_N}    seed=7
    Matrix Multiply And Verify Against Numpy

Matrix Inversion Numerical Stability Medium
    [Tags]    numerical
    Create Nearly Singular Matrix    ${MEDIUM_N}
    Invert Matrix And Validate Condition Number    max_cond=1e8

Eigenvalue Power Method Converges
    [Tags]    correctness
    Create Symmetric Matrix    ${SMALL_N}
    Run Power Method And Verify Dominant Eigenpair

Performance: Matrix Multiply Large
    [Tags]    performance
    Create Random Matrix    ${LARGE_N}    ${LARGE_N}
    Measure Matrix Multiply Time    max_ms=2000

