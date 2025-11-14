*** Settings ***
Library    ../resources/benchmark_keywords.py

*** Test Cases ***
Latency And Throughput Benchmarks
    [Tags]    performance
    Benchmark Model    model=ggml-small    batch_sizes=1,4,8
    Throughput Should Exceed    model=ggml-small    batch=1    min_qps=1

Quality On Summarization Task
    [Tags]    correctness;evaluation
    Run Model On Task    model=ggml-small    dataset=summ_sample
    Evaluate Bleu Rouge    bleu_min=0.1    rouge_min=0.2

