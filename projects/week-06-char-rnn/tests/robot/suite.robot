*** Settings ***
Library    ../resources/rnn_keywords.py

*** Test Cases ***
One Step Forward Backward Consistency
    [Tags]    correctness
    Build Small RNN    hidden=64
    Check One Step Gradients    tolerance=1e-4

Text Generation Qualitative Check
    [Tags]    smoke
    Train Short Model    epochs=3
    Sample Text    temperature=0.8
    Should Not Be Empty    ${sample}

