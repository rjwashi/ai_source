*** Settings ***
Library    ../resources/router_keywords.py
Library    RequestsLibrary

*** Test Cases ***
Router Routes Based On Latency Constraint
    [Tags]    integration
    Start Router Service
    Post Prediction Request    payload=request_small    latency_requirement_ms=200
    Response Should Contain    model_used

Cost-Aware Selection Favors Cheap Model
    [Tags]    correctness
    Simulate Workload And Verify Cost Savings    expected_reduction=0.2

