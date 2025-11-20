#!/usr/bin/env python3
import datetime as dt
import uuid

# Timezone and schedule
TZID = "America/Chicago"
START_DATE = dt.date(2026, 1, 12)  # Monday (second week of January 2026)
TOTAL_WEEKS = 12 * 4  # 48

# Session durations (minutes): vary between 15-35; some milestone sessions may go longer
DURATION_ROTATION = [15, 20, 25, 30, 35]

# Themes by weekday: 0=Mon..4=Fri
DAY_THEMES = {
    0: ("Theory", "Mon"),
    1: ("Build", "Tue"),
    2: ("Evaluate", "Wed"),
    3: ("Optimize", "Thu"),
    4: ("Demo", "Fri"),
}

# Curriculum with tailored deliverable checklists (month title, 4 weeks, deliverables, mid checkpoint, end demo)
PLAN = [
    ("Month 01 — Math and Python Foundations", [
        "Week 1: Linear algebra — vectors, matrices, norms, dot products, eigenvalues, condition number, numerical stability.",
        "Week 2: Calculus — derivatives, gradients, chain rule, Jacobian, Hessian; simple optimization and gradient-based learning.",
        "Week 3: Probability & statistics — distributions, expectation, variance, Bayes’ theorem, concentration bounds, bootstrap.",
        "Week 4: Python engineering — venv, packaging, NumPy idioms, profiling, unit tests, reproducible experiments, benchmarking.",
        "Deliverables focus: matrix utils, gradient solver, Monte Carlo notebook, numeric stability report, tests.",
        "Mid-month checkpoint checklist: matrix utils API validated; gradient descent converges on toy loss; Monte Carlo notebook stable; numeric stability examples logged.",
        "End-of-month demo checklist: tests green; publish 2–3 page stability report; README usage/examples; screencast of experiments."
    ]),
    ("Month 02 — Software Engineering Essentials", [
        "Week 1: Linux CLI, shell scripting, env isolation (venv, direnv), process management.",
        "Week 2: Git advanced workflows, branching, commit hygiene, PRs and reviews, PR templates.",
        "Week 3: REST design, OpenAPI, validation, small FastAPI/Flask service.",
        "Week 4: Docker basics, container best practices, reproducible images, logging/monitoring endpoints.",
        "Deliverables focus: containerized API, CI pipeline, logging/health endpoints, deployment README.",
        "Mid-month checkpoint checklist: branch strategy documented; PR template applied; CI passing baseline tests; minimal FastAPI with OpenAPI.",
        "End-of-month demo checklist: reproducible Docker image; health/metrics endpoints; CI on PR; verified deployment steps."
    ]),
    ("Month 03 — Algorithms and Systems", [
        "Week 1: Data structures & complexity — arrays, lists, trees, heaps, hashes, amortized analysis.",
        "Week 2: Graphs — shortest paths, BFS/DFS/A*/Dijkstra; data flow applications.",
        "Week 3: Memory layout, caching, floating-point formats, precision mitigation.",
        "Week 4: Concurrency basics, thread safety, async patterns, time & memory profiling.",
        "Deliverables focus: algorithm implementations + benchmarks, performance report, optimized component.",
        "Mid-month checkpoint checklist: DS correctness; graph benchmarks; preliminary profiling notes.",
        "End-of-month demo checklist: performance report with charts; optimized component vs baseline; reproducible benchmark suite."
    ]),
    ("Month 04 — Machine Learning Fundamentals", [
        "Week 1: Linear/logistic regression, losses, gradient descent, optimization basics.",
        "Week 2: Trees, ensembles (RF, GBM), k-means, bias–variance.",
        "Week 3: Metrics (accuracy, precision/recall, ROC/AUC, RMSE), CV, HPO, model selection.",
        "Week 4: Feature engineering, pipelines, interpretability, simple fairness checks.",
        "Deliverables focus: multi-model pipeline, CV experiments, evaluation report.",
        "Mid-month checkpoint checklist: baseline models trained; CV strategy chosen; metric calculations validated.",
        "End-of-month demo checklist: end-to-end pipeline; comparison plots/table; failure mode analysis."
    ]),
    ("Month 05 — Deep Learning Foundations", [
        "Week 1: MLPs, activations, init, optimizers (SGD, Adam).",
        "Week 2: CNNs; vision or simple sequence tasks.",
        "Week 3: RNNs, LSTM/GRU, sequence modeling, teacher forcing, truncated BPTT.",
        "Week 4: Intro to transformers, attention, small encoder/decoder blocks.",
        "Deliverables focus: MLP, simple CNN/RNN, toy transformer, training notebooks.",
        "Mid-month checkpoint checklist: gradient checks pass; CNN/RNN curves stable; overfit small batch as sanity check.",
        "End-of-month demo checklist: ablation notebook; toy transformer trains; clear docstrings/README."
    ]),
    ("Month 06 — Foundation Models and Model Selection", [
        "Week 1: Transformer internals — MHA, residuals, layer norm; implementation exercises.",
        "Week 2: Tokenization — BPE, WordPiece, SentencePiece; preprocessing pipelines.",
        "Week 3: Scaling laws (e.g., Chinchilla), compute vs data, efficient training heuristics.",
        "Week 4: Model comparison — open-weight vs API, licensing, cost/performance tradeoffs.",
        "Deliverables focus: tokenizers, small scaling experiments, model-selection matrix.",
        "Mid-month checkpoint checklist: tokenizer built & tested; small transformer experiment runs; data/compute estimates captured.",
        "End-of-month demo checklist: selection matrix (licensing/cost); scaling plots; recommendation with tradeoffs."
    ]),
    ("Month 07 — Evaluation and Testing", [
        "Week 1: Metrics — BLEU, ROUGE, perplexity, embedding similarity.",
        "Week 2: Automated testing pipelines and functional correctness scenarios.",
        "Week 3: Hallucination rates, toxicity scoring, bias metrics with detectors.",
        "Week 4: Human eval workflows, annotation guidelines, inter-annotator agreement.",
        "Deliverables focus: evaluation harness, annotation templates + guide, bias/hallucination analysis.",
        "Mid-month checkpoint checklist: metrics computed on sample set; automated checks wired; detector baselines established.",
        "End-of-month demo checklist: annotation guide; IAA stats; mitigation proposals summarized."
    ]),
    ("Month 08 — Retrieval‑Augmented Generation (RAG)", [
        "Week 1: Ingestion, chunking strategies, metadata management.",
        "Week 2: Embeddings and vector store (FAISS/Qdrant/etc.).",
        "Week 3: Dense/sparse/hybrid retrieval; reranking experiments.",
        "Week 4: Integrate retrieval with generation; optimize latency and relevance.",
        "Deliverables focus: RAG demo, strategy comparison notebook.",
        "Mid-month checkpoint checklist: corpus ingested + chunked; embeddings populated; initial retrieval works.",
        "End-of-month demo checklist: grounded answers; latency/relevance plots; best strategy documented."
    ]),
    ("Month 09 — Finetuning Techniques", [
        "Week 1: PEFT — LoRA, adapters, related techniques.",
        "Week 2: Knowledge distillation — teacher/student.",
        "Week 3: Model merging, adapter stacking, multi-task finetuning.",
        "Week 4: Compare PEFT vs full finetune: compute, memory, accuracy.",
        "Deliverables focus: PEFT experiments, distilled student, resource-performance report.",
        "Mid-month checkpoint checklist: LoRA/adapters configured; student pipeline ready; metrics defined.",
        "End-of-month demo checklist: PEFT vs full charts; student performance; resource analysis."
    ]),
    ("Month 10 — Prompt Engineering and Agent Systems", [
        "Week 1: Prompt structuring, few-shot, chain-of-thought, templates.",
        "Week 2: Robustness testing, defensive prompts, prompt injection simulations.",
        "Week 3: Agent architecture — tools, planning, memory via vector stores.",
        "Week 4: Safety guardrails, sandboxing, access control best practices.",
        "Deliverables focus: prompt library + metrics, multi-tool agent, safety evaluations.",
        "Mid-month checkpoint checklist: prompt variants compared; robustness failures captured; tool list scoped.",
        "End-of-month demo checklist: agent prototype with memory; safety report; prompt metrics dashboard."
    ]),
    ("Month 11 — Inference Optimization and Feedback", [
        "Week 1: Compression — quantization, pruning, light distillation.",
        "Week 2: Batching, parallel inference, GPU/TPU/CPU considerations.",
        "Week 3: Feedback systems — explicit/implicit, annotation, flywheel.",
        "Week 4: Monitoring, caching, feedback-driven retraining triggers.",
        "Deliverables focus: optimized inference pipeline (TTFT/TPOT), feedback prototype.",
        "Mid-month checkpoint checklist: quantization/pruning applied; throughput baseline measured; batching configured.",
        "End-of-month demo checklist: TTFT/TPOT improvements; quality preserved; feedback loop prototype demo."
    ]),
    ("Month 12 — Application Architecture, Security, Privacy & Ethics", [
        "Week 1: App architecture — routing, gateways, context construction, caching.",
        "Week 2: Security — prompt injection mitigation, adversarial inputs, tool sandboxing.",
        "Week 3: Privacy — PII detection/redaction, differential privacy basics, compliance.",
        "Week 4: Ethics & governance — audit trails, explainability, bias mitigation, GDPR/copyright.",
        "Deliverables focus: secure privacy-aware demo, PII pipeline, threat model, ethics assessment.",
        "Mid-month checkpoint checklist: routing/guardrails implemented; threat scenarios drafted; PII detection working.",
        "End-of-month demo checklist: privacy-aware demo; redaction pipeline; threat model + ethics impact assessment."
    ]),
]

def dtstamp():
    return dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

def fmt_local(dt_obj):
    return dt_obj.strftime("%Y%m%dT%H%M%S")

def vtimezone(tzid):
    return f"""BEGIN:VTIMEZONE
TZID:{tzid}
BEGIN:STANDARD
DTSTART:19701101T020000
TZOFFSETFROM:-0500
TZOFFSETTO:-0600
TZNAME:CST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19700308T020000
TZOFFSETFROM:-0600
TZOFFSETTO:-0500
TZNAME:CDT
END:DAYLIGHT
END:VTIMEZONE"""

def alarm_block():
    return """BEGIN:VALARM
TRIGGER:-PT30M
ACTION:DISPLAY
DESCRIPTION:Reminder
END:VALARM"""

def event_block(summary, description, start_dt, end_dt, tzid, include_alarm=True, uid=None, rrule=None):
    if uid is None:
        uid = str(uuid.uuid4())
    parts = [
        "BEGIN:VEVENT",
        f"DTSTAMP:{dtstamp()}",
        f"UID:{uid}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{description}",
        f"DTSTART;TZID={tzid}:{fmt_local(start_dt)}",
        f"DTEND;TZID={tzid}:{fmt_local(end_dt)}",
        "TRANSP:OPAQUE",
        "STATUS:CONFIRMED",
    ]
    if rrule:
        parts.append(f"RRULE:{rrule}")
    if include_alarm:
        parts.append(alarm_block())
    parts.append("END:VEVENT")
    return "\n".join(parts)

def vary_am_start(week_idx, day_idx, slot_idx):
    # AM sessions start between 06:00–12:00
    # slot_idx 0 => early AM, slot_idx 1 => mid/late AM
    base_hour = 6 + ((week_idx + day_idx + slot_idx) % 6)  # 6..11
    minute = [0, 15, 30, 45][(week_idx + 2*day_idx + slot_idx) % 4]
    return base_hour, minute

def vary_pm_end(week_idx, day_idx):
    # PM sessions end between 18:00–21:00
    hour = 18 + ((week_idx + day_idx) % 4)  # 18..21
    minute = [0, 15, 30, 45][(week_idx + day_idx) % 4]
    return hour, minute

def pick_duration(week_idx, day_idx, session_idx):
    # Default durations rotate within 15–35 minutes
    return DURATION_ROTATION[(week_idx + day_idx + session_idx) % len(DURATION_ROTATION)]

def build_description(theme_label, week_text, month_deliverables, mid_checkpoint, end_demo, checklist_extra=None):
    lines = [
        f"Theme: {theme_label}",
        week_text,
        "",
        f"Month deliverables emphasis: {month_deliverables}",
        f"Mid-month checkpoint: {mid_checkpoint}",
        f"End-of-month demo: {end_demo}",
    ]
    if checklist_extra:
        lines += ["", checklist_extra]
    lines += [
        "",
        "Workflow: dedicated Git branch; keep CI green; daily notes; weekly demo; journal 300–800 words on Sunday.",
        "Reminder: 30-minute notification before session."
    ]
    return "\\n".join(lines)

def main():
    cal = []
    cal.append("BEGIN:VCALENDAR")
    cal.append("PRODID:-//AI Engineering Plan//EN")
    cal.append("VERSION:2.0")
    cal.append("CALSCALE:GREGORIAN")
    cal.append(f"X-WR-TIMEZONE:{TZID}")
    cal.append(vtimezone(TZID))

    week_start = START_DATE
    week_idx = 0

    for month_title, weeks in PLAN:
        for w in range(4):  # 4 weeks in a month
            for day_offset in range(5):  # Monday..Friday
                day_date = week_start + dt.timedelta(days=day_offset)
                weekday = day_offset  # 0..4
                theme, theme_day = DAY_THEMES[weekday]

                week_text = weeks[w]
                month_deliverables = weeks[4]
                mid_checkpoint = weeks[5]
                end_demo = weeks[6]

                # AM Session 1
                am1_h, am1_m = vary_am_start(week_idx, weekday, 0)
                am1_duration = pick_duration(week_idx, weekday, 0)
                am1_start = dt.datetime.combine(day_date, dt.time(am1_h, am1_m))
                am1_end = am1_start + dt.timedelta(minutes=am1_duration)
                am1_summary = f"{month_title} — Week {w+1} — {theme_day} {theme} — AM Session 1"
                am1_desc = build_description(theme, week_text, month_deliverables, mid_checkpoint, end_demo,
                                             checklist_extra="AM1 focus: intent-setting, define today’s 1–2 high-impact tasks, quick review of blockers.")
                cal.append(event_block(am1_summary, am1_desc, am1_start, am1_end, TZID, include_alarm=True))

                # AM Session 2 (later in morning)
                am2_h, am2_m = vary_am_start(week_idx, weekday, 1)
                # Ensure AM2 is after AM1 by at least 45 minutes
                proposed_am2_start = dt.datetime.combine(day_date, dt.time(am2_h, am2_m))
                min_gap = am1_start + dt.timedelta(minutes=45)
                if proposed_am2_start < min_gap:
                    proposed_am2_start = min_gap
                am2_duration = pick_duration(week_idx, weekday, 1)
                am2_end = proposed_am2_start + dt.timedelta(minutes=am2_duration)
                # Keep within AM window (not past 12:00 start)
                if proposed_am2_start.time() < dt.time(6,0):
                    proposed_am2_start = dt.datetime.combine(day_date, dt.time(6,0))
                am2_start = proposed_am2_start
                am2_summary = f"{month_title} — Week {w+1} — {theme_day} {theme} — AM Session 2"
                am2_desc = build_description(theme, week_text, month_deliverables, mid_checkpoint, end_demo,
                                             checklist_extra="AM2 focus: hands-on progress (code/notebooks), capture notes, push incremental commits.")
                cal.append(event_block(am2_summary, am2_desc, am2_start, am2_end, TZID, include_alarm=True))

                # PM Session (ends between 18:00–21:00)
                pm_end_h, pm_end_m = vary_pm_end(week_idx, weekday)
                pm_end = dt.datetime.combine(day_date, dt.time(pm_end_h, pm_end_m))
                pm_duration = pick_duration(week_idx, weekday, 2)
                # Occasionally go longer (milestones): Week 2 Wed, Week 4 Fri => +15 mins
                if (w == 1 and weekday == 2) or (w == 3 and weekday == 4):
                    pm_duration += 15  # may exceed 35 to maximize objectives
                pm_start = pm_end - dt.timedelta(minutes=pm_duration)
                pm_summary = f"{month_title} — Week {w+1} — {theme_day} {theme} — PM Consolidation"
                pm_desc = build_description(theme, week_text, month_deliverables, mid_checkpoint, end_demo,
                                            checklist_extra="PM focus: consolidate, document, small demo/gif, update README, close 1–2 open issues.")
                cal.append(event_block(pm_summary, pm_desc, pm_start, pm_end, TZID, include_alarm=True))

            # Week 2 Mid-month checkpoint (Wednesday, longer up to 50 mins)
            if w == 1:
                checkpoint_day = week_start + dt.timedelta(days=2)  # Wednesday
                cp_end = dt.datetime.combine(checkpoint_day, dt.time(19, 35))
                cp_start = cp_end - dt.timedelta(minutes=50)  # allow >35 to maximize objectives
                cp_summary = f"{month_title} — Week 2 — Mid-month checkpoint (deep review)"
                cp_desc = "\\n".join([
                    "Checkpoint focus: align outputs to deliverables; resolve blockers; plan remaining tasks.",
                    weeks[5],
                    "Artifacts: issues triage, updated roadmap, status notes, brief screen capture."
                ]) + "\\n\\nReminder: 30-minute notification before session."
                cal.append(event_block(cp_summary, cp_desc, cp_start, cp_end, TZID, include_alarm=True))

            # Week 4 Deliverables sprint (Friday, may exceed 35)
            if w == 3:
                sprint_day = week_start + dt.timedelta(days=4)  # Friday
                sp_end = dt.datetime.combine(sprint_day, dt.time(20, 45))
                sp_start = sp_end - dt.timedelta(minutes=55)  # longer sprint to maximize objectives
                sp_summary = f"{month_title} — Week 4 — Deliverables sprint (portfolio polish)"
                sp_desc = "\\n".join([
                    "Sprint checklist: finalize tests, polish docs, record demo, update portfolio and website.",
                    weeks[4],
                    "Targets: tests green; README & docs complete; demo published; portfolio entry created."
                ]) + "\\n\\nReminder: 30-minute notification before session."
                cal.append(event_block(sp_summary, sp_desc, sp_start, sp_end, TZID, include_alarm=True))

                # Week 4 End-of-month demo (public-facing)
                demo_end = dt.datetime.combine(sprint_day, dt.time(21, 0))
                demo_start = demo_end - dt.timedelta(minutes=40)  # may exceed 35 for presentation
                demo_summary = f"{month_title} — Week 4 — End-of-month demo (public)"
                demo_desc = "\\n".join([
                    "Public demo: present outcomes, key metrics, and lessons learned.",
                    weeks[6],
                    "Publish to: Google Docs summary, GitHub releases/tags, www.ronaldjwashington.com."
                ]) + "\\n\\nReminder: 30-minute notification before session."
                cal.append(event_block(demo_summary, demo_desc, demo_start, demo_end, TZID, include_alarm=True))

            # Advance to next week
            week_start = week_start + dt.timedelta(days=7)
            week_idx += 1
            if week_idx >= TOTAL_WEEKS:
                break

        if week_idx >= TOTAL_WEEKS:
            break

    # Recurring Sunday Reflect & Showcase (19:00–19:30)
    first_sunday = START_DATE + dt.timedelta(days=(6 - START_DATE.weekday()) % 7)
    reflect_start = dt.datetime.combine(first_sunday, dt.time(19, 0))
    reflect_end = reflect_start + dt.timedelta(minutes=30)
    reflect_summary = "Reflect & showcase — Weekly journal and portfolio update"
    reflect_desc = "\\n".join([
        "Write 300–800 word journal in Google Docs.",
        "Update GitHub repos and project showcase.",
        "Push demos to www.ronaldjwashington.com.",
        "Reminder: 30-minute notification before session."
    ])
    rrule = "FREQ=WEEKLY;BYDAY=SU"
    cal.append(event_block(reflect_summary, reflect_desc, reflect_start, reflect_end, TZID, include_alarm=True, rrule=rrule))

    cal.append("END:VCALENDAR")

    ics = "\n".join(cal)
    with open("ai_engineering_plan.ics", "w", encoding="utf-8") as f:
        f.write(ics)
    print("Wrote ai_engineering_plan.ics")

if __name__ == "__main__":
    main()
