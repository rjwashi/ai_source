AI Engineering 12‑Month Study Plan

This single Markdown file contains a complete one‑year AI Engineering curriculum, month-by-month. Each month includes:

    learning goals

    weekly breakdown

    curated resources (papers, courses, notebooks)

    deliverables and an evaluation rubric

Save this content as AI_Engineering_12_Month_Plan.md and use it for printing, sharing by email, or as the master syllabus in your ai_source repository.
Month 01 — Math and Python Foundations
Learning goals

    Build strong intuition in linear algebra, calculus, and probability as they apply to machine learning.

    Gain fluency writing clean, testable Python and using NumPy for numerical work.

    Understand numeric stability, conditioning, floating-point formats, and how they affect ML systems.

Weekly breakdown

    Week 1: Linear algebra basics — vectors, matrix operations, norms, dot products, eigenvalues, condition number, and numerical stability.

    Week 2: Calculus essentials — derivatives, gradients, chain rule, Jacobian, Hessian; apply to simple optimization and gradient-based learning.

    Week 3: Probability and statistics — discrete/continuous distributions, expectation, variance, Bayes' theorem, concentration bounds, and bootstrap.

    Week 4: Python engineering — virtual environments, packaging, NumPy idioms, profiling, unit tests, reproducible experiments, and simple benchmarking.

Curated resources

    Gilbert Strang, Linear Algebra (MIT OCW lectures and notes).

    Khan Academy — Calculus courses.

    Harvard Stat 110 — Introduction to Probability.

    NumPy quickstart and reference guides; Jupyter notebooks on numerical stability; short articles on floating point (e.g., “What Every Computer Scientist Should Know About Floating-Point Arithmetic”).

Deliverables and evaluation rubric

    Deliverables: Python package with matrix utilities; a small optimization solver demonstrating gradients; a Monte Carlo statistics notebook; unit tests; a 2–3 page report explaining numeric stability experiments.

    Rubric:

        Correctness: core functions pass unit tests and implemented algorithms are correct (40%).

        Numerical understanding: report explains conditioning, rounding errors, and mitigation strategies with concrete examples (20%).

        Code quality: modular design, docstrings, tests, and a clear README (20%).

        Reproducibility and presentation: notebooks run end-to-end and results are clearly presented (20%).

Month 02 — Software Engineering Essentials
Learning goals

    Master command-line tools, advanced Git workflows, and container basics to support reproducible ML engineering.

    Learn API fundamentals and how to design simple, secure microservices for model serving.

    Understand logging, monitoring, and basic CI/CD concepts.

Weekly breakdown

    Week 1: Linux command-line, shell scripting, environment isolation (venv, direnv), process management.

    Week 2: Git advanced workflows, branching strategies, commit hygiene, pull requests and code reviews, and PR templates.

    Week 3: REST API design and best practices, OpenAPI spec, input/output validation, and a small FastAPI/Flask service.

    Week 4: Docker basics, container best practices, build reproducible images, and add basic monitoring/logging endpoints.

Curated resources

    freeCodeCamp and GitHub Learning for Git and GitHub workflows.

    FastAPI official tutorial and Flask quickstarts.

    Twelve-Factor App principles.

    Prometheus + Grafana quickstarts; GitHub Actions CI examples and templates.

Deliverables and evaluation rubric

    Deliverables: Containerized API that serves a small model or utility; CI pipeline for tests; logging and health endpoints; deployment README with run instructions.

    Rubric:

        Reliability: API passes integration tests and exposes health and metrics endpoints (30%).

        Reproducibility: clear Dockerfile, image build steps, and documented run instructions (25%).

        Observability: meaningful logs, metrics and a simple monitoring setup (20%).

        Dev workflow: sensible Git branching, PR template, and CI integration (25%).

Month 03 — Algorithms and Systems
Learning goals

    Understand core data structures, algorithms, and their complexity—essential for system-level ML engineering.

    Learn memory models, performance profiling, and numerical precision tradeoffs in real systems.

Weekly breakdown

    Week 1: Data structures and complexity analysis — arrays, linked lists, trees, heaps, hash tables, amortized analysis.

    Week 2: Graph algorithms, shortest paths, search algorithms (BFS/DFS/A*/Dijkstra) and applying them to data flow problems.

    Week 3: Memory layout, caching behavior, floating-point formats, and strategies to mitigate precision issues.

    Week 4: Concurrency basics, thread safety primitives, asynchronous patterns, and practical profiling (time & memory).

Curated resources

    CLRS (selected chapters on data structures and graphs).

    Articles and blog posts on memory layout and cache-friendly code.

    Tools: valgrind, perf, Python cProfile, memory_profiler; examples in lower-level languages for system insight.

Deliverables and evaluation rubric

    Deliverables: Implementations of selected algorithms with benchmarks; a memory and performance report; a performance-optimized microservice or library component.

    Rubric:

        Algorithmic correctness and complexity analysis (35%).

        Depth of performance benchmarking and profiling insights (30%).

        System design reasoning and tradeoffs documented (20%).

        Code quality, tests, and reproducible benchmarks (15%).

Month 04 — Machine Learning Fundamentals
Learning goals

    Learn supervised and unsupervised learning algorithms, model evaluation, and common pitfalls like overfitting.

    Implement an end-to-end ML pipeline: preprocessing, train/val/test splits, metrics, and model selection strategies.

Weekly breakdown

    Week 1: Linear regression, logistic regression, loss functions, gradient descent and optimization basics.

    Week 2: Decision trees, ensembles (random forests, gradient boosting), clustering (k-means), and bias–variance tradeoff.

    Week 3: Model evaluation metrics (accuracy, precision/recall, ROC/AUC, RMSE), cross-validation, hyperparameter search and model selection.

    Week 4: Feature engineering, data pipelines, basic interpretability techniques and simple fairness checks.

Curated resources

    Andrew Ng’s Machine Learning (Coursera).

    scikit-learn documentation and example gallery.

    Kaggle tutorials and mini-project notebooks for applied practice.

Deliverables and evaluation rubric

    Deliverables: An ML pipeline implementing multiple algorithms, cross-validation experiments, and an evaluation report comparing methods with justifications.

    Rubric:

        Experimental rigor and reproducibility (30%).

        Appropriate choice and calculation of evaluation metrics and validation strategies (30%).

        Quality of feature engineering and data handling (20%).

        Interpretation of results and discussion of failure modes (20%).

Month 05 — Deep Learning Foundations
Learning goals

    Master fundamentals of neural networks, backpropagation, regularization, and training best practices.

    Implement core deep learning components from scratch (NumPy) and using a framework (PyTorch or TensorFlow).

Weekly breakdown

    Week 1: Feedforward neural networks, activation functions, weight initialization, and optimizers (SGD, Adam).

    Week 2: Convolutional neural networks (CNNs) and practical applications in vision or basic sequence tasks.

    Week 3: Recurrent neural networks (RNNs), LSTMs/GRUs, sequence modeling, teacher forcing and truncated BPTT.

    Week 4: Introduction to transformers, attention mechanisms, and implementing encoder/decoder blocks on a small scale.

Curated resources

    fast.ai — Practical Deep Learning for Coders.

    “Attention Is All You Need” paper and accessible transformer tutorials.

    minGPT, Annotated Transformer tutorials, and PyTorch beginner guides.

Deliverables and evaluation rubric

    Deliverables: Working implementations of a small feedforward network, a simple CNN or RNN, and a toy transformer encoder; training notebooks with experiments and ablations.

    Rubric:

        Implementation correctness and gradient-checking where applicable (30%).

        Training stability and demonstration of convergence (25%).

        Clear experiments comparing architectures or hyperparameters (25%).

        Documentation, reproducible notebooks, and code quality (20%).

Month 06 — Foundation Models and Model Selection
Learning goals

    Deepen understanding of transformer internals, tokenization, and model scaling tradeoffs.

    Learn model selection criteria including licensing, cost, and performance considerations for production use.

Weekly breakdown

    Week 1: Transformer internals (multi-head attention, residuals, layer norm) and implementation exercises.

    Week 2: Tokenization methods (BPE, WordPiece, SentencePiece) and preprocessing pipelines for language models.

    Week 3: Model scaling laws (e.g., Chinchilla), compute vs data tradeoffs, and efficient training heuristics.

    Week 4: Model comparison framework — open-weight vs API models, licensing implications, and cost/performance tradeoffs.

Curated resources

    Chinchilla scaling law paper; papers on tokenization design and efficiency.

    Hugging Face Transformers tutorials and tokenizers docs.

    Model hub benchmarking repositories and community analyses.

Deliverables and evaluation rubric

    Deliverables: Tokenization pipelines; small transformer experiments exploring scaling effects; a model selection matrix comparing 3 candidate models with licensing and cost analysis.

    Rubric:

        Depth of transformer understanding and reproducible demos (30%).

        Quality and insight of scaling experiments and plots (30%).

        Thoughtful model selection criteria including licensing and cost (20%).

        Reproducible benchmarking and documentation (20%).

Month 07 — Evaluation and Testing
Learning goals

    Build robust evaluation pipelines that measure quality, hallucination, bias, and safety concerns for generative models.

    Combine automated metrics with human evaluation methodologies for comprehensive assessment.

Weekly breakdown

    Week 1: Implement standard metrics for language tasks — BLEU, ROUGE, perplexity, and embedding-based semantic similarity.

    Week 2: Design and implement automated testing pipelines and functional correctness scenarios for model outputs.

    Week 3: Build tools for measuring hallucination rates, toxicity scoring, and bias metrics using prebuilt detectors or models.

    Week 4: Set up human evaluation workflows, annotation guidelines, and measure inter-annotator agreement.

Curated resources

    sacreBLEU, rouge-score, and sentence-transformers libraries.

    Annotation tools: doccano, Prodigy (or open-source alternatives).

    Papers and blogs on NLG evaluation best practices and human evaluation methodologies.

Deliverables and evaluation rubric

    Deliverables: Evaluation harness computing multiple metrics; annotation templates and a short guide for human evaluators; an analysis report on biases and hallucinations.

    Rubric:

        Coverage and correct implementation of metrics (30%).

        Practical human evaluation pipeline with guidelines and sample annotations (25%).

        Depth of analysis on hallucinations, toxicity and proposed mitigations (25%).

        Tooling integration and reproducibility (20%).

Month 08 — Retrieval‑Augmented Generation (RAG)
Learning goals

    Build retrieval systems integrated with generative models to ground outputs in documents.

    Understand embedding techniques, vector stores, document chunking, and hybrid retrieval strategies.

Weekly breakdown

    Week 1: Document ingestion, chunking strategies and metadata management.

    Week 2: Embedding pipeline and vector store population using FAISS, Qdrant, or similar.

    Week 3: Implement dense, sparse, and hybrid retrieval methods; experiment with reranking strategies.

    Week 4: Integrate retrieval with a generation model (RAG) and optimize for latency and relevance.

Curated resources

    RAG paper and dense retrieval literature.

    FAISS, Qdrant, Weaviate documentation; sentence-transformers tutorials.

    Hugging Face RAG demos and open-source end-to-end pipelines.

Deliverables and evaluation rubric

    Deliverables: RAG demo ingesting a small corpus, performing retrieval, and generating grounded answers; evaluation notebook comparing retrieval strategies.

    Rubric:

        Correctness and latency of retrieval system (30%).

        Relevance and grounding quality of retrieved context (30%).

        Engineering robustness of ingestion and chunking pipeline (20%).

        Documentation and reproducible end-to-end demo (20%).

Month 09 — Finetuning Techniques
Learning goals

    Learn parameter-efficient fine-tuning approaches (PEFT), distillation, model merging, and multi-task finetuning strategies.

    Evaluate tradeoffs between compute, memory, and downstream performance.

Weekly breakdown

    Week 1: Parameter-efficient fine-tuning: LoRA, adapters, and related techniques.

    Week 2: Knowledge distillation techniques to train smaller student models from large teachers.

    Week 3: Model merging, adapter stacking, and multi-task finetuning experiments.

    Week 4: Evaluate and compare PEFT versus full finetuning across compute, memory, and accuracy metrics.

Curated resources

    LoRA and adapters papers; foundational knowledge distillation literature.

    PEFT libraries and Hugging Face finetuning examples.

    Practical guides on checkpointing, gradient accumulation, and memory management.

Deliverables and evaluation rubric

    Deliverables: PEFT experiments (LoRA/adapters); a distilled student model; a comparison report documenting resource vs performance tradeoffs.

    Rubric:

        Correct application and evaluation of PEFT (30%).

        Distillation quality measured on held-out tasks (30%).

        Clear resource vs performance analysis and charts (25%).

        Reproducible scripts and checkpoint handling (15%).

Month 10 — Prompt Engineering and Agent Systems
Learning goals

    Master effective prompt design, in-context learning strategies, and prompt robustness.

    Build multi-tool agents with planning, memory, and secure tool execution patterns.

Weekly breakdown

    Week 1: Prompt structuring, few-shot prompting, chain-of-thought techniques, and prompt templates.

    Week 2: Prompt robustness testing, defensive prompt engineering, and simulated prompt injection attacks.

    Week 3: Agent architecture — tool integration, planning algorithms, memory systems backed by vector stores.

    Week 4: Agent safety guardrails, secure sandboxing for code/tool execution, and access control best practices.

Curated resources

    Chain-of-thought prompting literature; ReAct and Toolformer papers.

    LangChain, LlamaIndex, and community agent framework examples.

    Tutorials and blog posts on prompt engineering cookbooks and attack/defense patterns.

Deliverables and evaluation rubric

    Deliverables: Prompt library with experiments and metrics; a multi-tool agent prototype with memory and tool invocation; safety and robustness evaluations.

    Rubric:

        Depth and quantitative comparison of prompt experiments (30%).

        Robustness and defensive prompt engineering measures (25%).

        Agent design, secure tool integration and memory implementation (25%).

        Documentation, logs, and evaluation scenarios (20%).

Month 11 — Inference Optimization and Feedback
Learning goals

    Optimize inference for latency, throughput, and cost via quantization, pruning, and related techniques.

    Design user feedback loops and human-in-the-loop systems for continuous improvement.

Weekly breakdown

    Week 1: Model compression — quantization, pruning, and lightweight distillation techniques for inference.

    Week 2: Batching strategies, parallel inference, and hardware considerations for GPUs/TPUs/CPU stacks.

    Week 3: Feedback collection systems — explicit vs implicit feedback, annotation workflows, and flywheel design.

    Week 4: Production monitoring for inference, caching strategies, and feedback-driven retraining triggers.

Curated resources

    Surveys on quantization/pruning and framework docs (ONNX, TensorRT, bitsandbytes).

    Tutorials on batching, parallel inference, and production inference patterns.

    Papers and blogs on feedback loops, continuous learning and data flywheels.

Deliverables and evaluation rubric

    Deliverables: Optimized inference pipeline for a small model with measured TTFT/TPOT metrics; a feedback collection prototype and retraining trigger logic.

    Rubric:

        Measurable latency and throughput improvements (30%).

        Correctness preserved after optimization and quality analysis (30%).

        Design and integration of feedback loops and human-in-the-loop processes (20%).

        Documentation and reproducible deployment scripts (20%).

Month 12 — Application Architecture, Security, Privacy & Ethics
Learning goals

    Design end-to-end AI application architectures with routing, guardrails, and privacy protections.

    Understand and implement defenses against prompt injection, memorization attacks, PII leaks, and governance practices.

Weekly breakdown

    Week 1: Application architecture patterns — model routing, gateways, context construction, caching layers.

    Week 2: Security threats — prompt injection detection/mitigation, adversarial inputs, sandboxing for tool execution.

    Week 3: Privacy protections — PII detection and redaction, differential privacy basics, dataset handling for compliance.

    Week 4: Ethics and governance — audit trails, explainability, bias mitigation, GDPR and copyright implications.

Curated resources

    Differential privacy primers, adversarial ML surveys, and AI ethics frameworks.

    PII detection libraries and redaction toolkits.

    Policy resources and practical GDPR summaries for ML practitioners.

Deliverables and evaluation rubric

    Deliverables: A secure, privacy-aware demo application with routing and guardrails; PII detection/redaction pipeline; threat model document and ethics impact assessment.

    Rubric:

        Security and privacy coverage in threat model and mitigations (30%).

        Functional correctness and robustness of guardrails and redaction (25%).

        Ethics assessment and remediation actions (25%).

        Operational playbook, audit logs, and reproducible deployment (20%).

Using this Plan

Recommended workflow and habits:

    Create a dedicated Git branch per week (e.g., week-01-matrix-lib) and commit incrementally.

    Maintain a weekly journal in notes/weekly-journal/week-XX.md with a 300–800 word reflection summarizing what you built, challenges, metrics, and next steps.

    Publish polished projects to portfolio/project-showcase.md as you complete major milestones.

    Use CI (e.g., GitHub Actions) to run tests for project folders and ensure reproducibility.

    Aim for weekly demos (notebooks, small web demos, or recorded GIFs) to document progress and create a portfolio.


