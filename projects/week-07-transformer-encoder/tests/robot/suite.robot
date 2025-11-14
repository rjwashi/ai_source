*** Settings ***
Library    ../resources/transformer_keywords.py

*** Test Cases ***
Attention Output Shape Matches
    [Tags]    correctness
    Create Sample Batch    batch_size=4    seq_len=16
    MultiHeadAttention Output Should Have Shape    4    16    64

Transformer Training Quick Run
    [Tags]    training
    Training Run Encoder    epochs=2    small_dataset=true
    Validate Classification Accuracy    min_acc=0.6

