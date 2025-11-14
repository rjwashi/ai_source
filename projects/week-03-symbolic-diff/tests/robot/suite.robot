*** Settings ***
Library    ../resources/sympymin_keywords.py

*** Test Cases ***
Symbolic Differentation Product Rule
    [Tags]    correctness
    Parse Expression    x * sin(x)
    Differentiate Expression    x
    Expression Should Equal    x*sin(x).diff(x)

Numerical vs Symbolic Consistency
    [Tags]    numerical
    Parse Expression    sin(x)*x**2
    Evaluate Symbolic Derivative Numeric Check    at=0.3    tolerance=1e-6

