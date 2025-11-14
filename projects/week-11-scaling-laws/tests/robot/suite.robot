*** Settings ***
Library    ../resources/scale_keywords.py

*** Test Cases ***
Scaling Loss vs Params Sweep
    [Tags]    experiments
    Run Scaling Sweep    model_sizes=1e5,1e6,5e6
    Fit Power Law And Verify R2    min_r2=0.9

Synthetic Compute vs Data Study
    [Tags]    experiments
    Run ComputeDataExperiment    compute_steps=10000    data_sizes=1k,10k,100k
    Save Plot    reports/scale_plot.png

