*** Settings ***
Library    ../resources/sim_keywords.py
Suite Setup    Setup Simulation Env

*** Variables ***
${RUNS}    10000

*** Test Cases ***
Monty Hall Empirical Probability
    [Tags]    correctness;stats
    Run Monty Hall Experiment    ${RUNS}
    Should Be True    ${win_rate} > 0.65

Bayesian Coin Posterior Convergence
    [Tags]    correctness
    Run Bayesian Update Simulation    heads=30    tails=70    prior_alpha=1    prior_beta=1
    Posterior Mean Should Be Near    expected=0.3    tolerance=0.02

