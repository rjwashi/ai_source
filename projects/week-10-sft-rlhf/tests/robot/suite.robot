*** Settings ***
Library    ../resources/sft_keywords.py

*** Test Cases ***
SFT Training Produces Checkpoint
    [Tags]    correctness
    Run SFT Pipeline    epochs=3
    Checkpoint Exists    path=checkpoints/sft.ckpt

Preference Model Improves Reward
    [Tags]    correctness;rlhf
    Simulate Preferences And Train Reward Model
    Reward Model Improvement Should Be Positive

