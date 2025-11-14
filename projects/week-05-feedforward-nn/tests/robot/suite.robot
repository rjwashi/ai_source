*** Settings ***
Library    ../resources/nn_keywords.py
Test Setup    Prepare MNIST Subsample

*** Test Cases ***
Training Loss Decreases
    [Tags]    correctness;training
    Train Small NN    epochs=5    batch=64
    Final Loss Should Be Less Than    0.7

Gradient Check Passes
    [Tags]    correctness;grad
    Numerical Gradient Check    layer=0    epsilon=1e-4    tolerance=1e-5

