*** Settings ***
Library    ../resources/bert_keywords.py

*** Test Cases ***
Masking Ratio Is Correct
    [Tags]    correctness
    Create Masked Batches    mask_prob=0.15
    Mask Ratio Should Be Near    0.15    tolerance=0.02

MLM Training Loss Improves
    [Tags]    training
    Run MLM Pretrain    epochs=3
    Final Per-Token Loss Should Be Less Than    4.0

