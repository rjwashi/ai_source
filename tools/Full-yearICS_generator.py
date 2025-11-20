#!/usr/bin/env python3
from datetime import datetime, date, time, timedelta
from uuid import uuid4
from icalendar import Calendar, Event, Alarm, vText

TZID = "America/Chicago"
START_DATE = date(2026, 1, 12)
TOTAL_WEEKS = 48

DAY_THEMES = {
    0: ("Theory", "Mon"),
    1: ("Build", "Tue"),
    2: ("Evaluate", "Wed"),
    3: ("Optimize", "Thu"),
    4: ("Demo", "Fri"),
}

DURATION_ROTATION = [15, 20, 25, 30, 35]

MICRO_PROMPTS = {
    "Theory": "Map key concepts; derive one equation; write 3 insight bullets; note one open question.",
    "Build": "Implement one minimal slice; write a failing test first; commit with a clear message; push branch.",
    "Evaluate": "Pick 2 metrics; run a small eval set; log 3 failure cases; file one issue to fix.",
    "Optimize": "Profile one hotspot; apply one tweak; compare before/after; document the result concisely.",
    "Demo": "Record a 60–90s clip; draft a 5-sentence summary; publish README snippet; share link.",
}

PLAN = [...]  # reuse the PLAN list from the standard-library script

def vary_am_start(week_idx, day_idx, slot_idx):
    hour = 6 + ((week_idx + day_idx + slot_idx) % 6)  # 6..11
    minute = [0, 15, 30, 45][(week_idx + 2*day_idx + slot_idx) % 4]
    return hour, minute

def vary_pm_end(week_idx, day_idx):
    hour = 18 + ((week_idx + day_idx) % 4)  # 18..21
    minute = [0, 15, 30, 45][(week_idx + day_idx) % 4]
    return hour, minute

def pick_duration(week_idx, day_idx, session_idx):
    return DURATION_ROTATION[(week_idx + day_idx + session_idx) % len(DURATION_ROTATION)]

def build_description(theme_label, week_text, month_deliv, mid_cp, end_demo, extra=None):
    micro = MICRO_PROMPTS.get(theme_label, "")
    desc = "\n".join([
        f"Theme: {theme_label}",
        week_text,
        "",
        f"Micro-prompt: {micro}",
        "",
        f"Month deliverables emphasis: {month_deliv}",
        f"Mid-month checkpoint: {mid_cp}",
        f"End-of-month demo: {end_demo}",
        "",
        (extra or ""),
        "",
        "Workflow: dedicated Git branch; keep CI green; daily notes; weekly demo; journal 300–800 words on Sunday.",
        "Reminder: 30-minute notification before session."
    ])
    return desc

def add_alarm(evt):
    alarm = Alarm()
    alarm.add('action', 'DISPLAY')
    alarm.add('trigger', timedelta(minutes=-30))
    alarm.add('description', 'Reminder')
    evt.add_component(alarm)

def main():
    cal = Calendar()
    cal.add('prodid', '-//AI Engineering Plan//EN')
    cal.add('version', '2.0')
    cal.add('calscale', 'GREGORIAN')
    cal.add('X-WR-TIMEZONE', vText(TZID))

    week_start = START_DATE
    week_idx = 0

    for month_title, weeks in PLAN:
        for w in range(4):
            for day_offset in range(5):
                day_date = week_start + timedelta(days=day_offset)
                theme, theme_day = DAY_THEMES[day_offset]
                week_text = weeks[w]
                month_deliv = weeks[4]
                mid_cp = weeks[5]
                end_demo = weeks[6]

                # AM1
                am1_h, am1_m = vary_am_start(week_idx, day_offset, 0)
                am1_dur = pick_duration(week_idx, day_offset, 0)
                am1_start = datetime.combine(day_date, time(am1_h, am1_m))
                am1_end = am1_start + timedelta(minutes=am1_dur)
                am1 = Event()
                am1.add('uid', str(uuid4()))
                am1.add('dtstamp', datetime.utcnow())
                am1.add('summary', f"{month_title} — Week {w+1} — {theme_day} {theme} — AM Session 1")
                am1.add('description', build_description(theme, week_text, month_deliv, mid_cp, end_demo, "AM1 focus: intent-setting, define 1–2 high-impact tasks."))
                am1.add('dtstart', am1_start)
                am1.add('dtend', am1_end)
                add_alarm(am1)
                cal.add_component(am1)

                # AM2
                am2_h, am2_m = vary_am_start(week_idx, day_offset, 1)
                am2_start = datetime.combine(day_date, time(am2_h, am2_m))
                if am2_start < am1_start + timedelta(minutes=45):
                    am2_start = am1_start + timedelta(minutes=45)
                am2_dur = pick_duration(week_idx, day_offset, 1)
                am2_end = am2_start + timedelta(minutes=am2_dur)
                am2 = Event()
                am2.add('uid', str(uuid4()))
                am2.add('dtstamp', datetime.utcnow())
                am2.add('summary', f"{month_title} — Week {w+1} — {theme_day} {theme} — AM Session 2")
                am2.add('description', build_description(theme, week_text, month_deliv, mid_cp, end_demo, "AM2 focus: hands-on progress; capture notes; push commits."))
                am2.add('dtstart', am2_start)
                am2.add('dtend', am2_end)
                add_alarm(am2)
                cal.add_component(am2)

                # PM
                pm_end_h, pm_end_m = vary_pm_end(week_idx, day_offset)
                pm_end = datetime.combine(day_date, time(pm_end_h, pm_end_m))
                pm_dur = pick_duration(week_idx, day_offset, 2)
                if (w == 1 and day_offset == 2) or (w == 3 and day_offset == 4):
                    pm_dur += 15
                pm_start = pm_end - timedelta(minutes=pm_dur)
                pm = Event()
                pm.add('uid', str(uuid4()))
                pm.add('dtstamp', datetime.utcnow())
                pm.add('summary', f"{month_title} — Week {w+1} — {theme_day} {theme} — PM Consolidation")
                pm.add('description', build_description(theme, week_text, month_deliv, mid_cp, end_demo, "PM focus: consolidate, document, mini-demo, update README."))
                pm.add('dtstart', pm_start)
                pm.add('dtend', pm_end)
                add_alarm(pm)
                cal.add_component(pm)

            # Mid-month checkpoint
            if w == 1:
                checkpoint_day = week_start + timedelta(days=2)
                cp_end = datetime.combine(checkpoint_day, time(19, 35))
                cp_start = cp_end - timedelta(minutes=50)
                cp = Event()
                cp.add('uid', str(uuid4()))
                cp.add('dtstamp', datetime.utcnow())
                cp.add('summary', f"{month_title} — Week 2 — Mid-month checkpoint (deep review)")
                cp.add('description', "\n".join([
                    "Checkpoint focus: align outputs to deliverables; resolve blockers; plan remaining tasks.",
                    weeks[5],
                    "Artifacts: issues triage, updated roadmap, status notes, brief screen capture.",
                    "Reminder: 30-minute notification before session."
                ]))
                cp.add('dtstart', cp_start)
                cp.add('dtend', cp_end)
                add_alarm(cp)
                cal.add_component(cp)

            # End-of-month sprint and demo
            if w == 3:
                sprint_day = week_start + timedelta(days=4)
                sp_end = datetime.combine(sprint_day, time(20, 45))
                sp_start = sp_end - timedelta(minutes=55)
                sp = Event()
                sp.add('uid', str(uuid4()))
                sp.add('dtstamp', datetime.utcnow())
                sp.add('summary', f"{month_title} — Week 4 — Deliverables sprint (portfolio polish)")
                sp.add('description', "\n".join([
                    "Sprint checklist: finalize tests, polish docs, record demo, update portfolio and website.",
                    weeks[4],
                    "Targets: tests green; README & docs complete; demo published; portfolio entry created.",
                    "Reminder: 30-minute notification before session."
                ]))
                sp.add('dtstart', sp_start)
                sp.add('dtend', sp_end)
                add_alarm(sp)
                cal.add_component(sp)

                demo_end = datetime.combine(sprint_day, time(21, 0))
                demo_start = demo_end - timedelta(minutes=40)
                demo = Event()
                demo.add('uid', str(uuid4()))
                demo.add('dtstamp', datetime.utcnow())
                demo.add('summary', f"{month_title} — Week 4 — End-of-month demo (public)")
                demo.add('description', "\n".join([
                    "Public demo: present outcomes, key metrics, and lessons learned.",
                    weeks[6],
                    "Publish to: Google Docs summary, GitHub releases/tags, www.ronaldjwashington.com.",
                    "Reminder: 30-minute notification before session."
                ]))
                demo.add('dtstart', demo_start)
                demo.add('dtend', demo_end)
                add_alarm(demo)
                cal.add_component(demo)

            week_start += timedelta(days=7)
            week_idx += 1
            if week_idx >= TOTAL_WEEKS:
                break
        if week_idx >= TOTAL_WEEKS:
            break

    # Recurring Sunday reflection (note: icalendar recurrence; Google honors RRULE)
    first_sunday = START_DATE + timedelta(days=(6 - START_DATE.weekday()) % 7)
    reflect_start = datetime.combine(first_sunday, time(19, 0))
    reflect_end = reflect_start + timedelta(minutes=30)
    reflect = Event()
    reflect.add('uid', str(uuid4()))
    reflect.add('dtstamp', datetime.utcnow())
    reflect.add('summary', "Reflect & showcase — Weekly journal and portfolio update")
    reflect.add('description', "\n".join([
        "Write 300–800 word journal in Google Docs.",
        "Update GitHub repos and project showcase.",
        "Push demos to www.ronaldjwashington.com.",
        "Reminder: 30-minute notification before session."
    ]))
    reflect.add('dtstart', reflect_start)
    reflect.add('dtend', reflect_end)
    reflect.add('rrule', {'FREQ': ['WEEKLY'], 'BYDAY': ['SU']})
    add_alarm(reflect)
    cal.add_component(reflect)

    with open('ai_engineering_full_year_icalendar.ics', 'wb') as f:
        f.write(cal.to_ical())
    print("Wrote ai_engineering_full_year_icalendar.ics")

if __name__ == "__main__":
    main()
