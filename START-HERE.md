# Start here: read, run and understand

[Course home](README.md) · [Curriculum](CURRICULUM.md) · [Glossary](reference/glossary.md)

## Begin with one case

An order records twelve boxes. A customer reports ten. The course follows the preparation, investigation and review of that discrepancy while explaining what AI can contribute and how the surrounding work should be designed. Other examples explore meeting records and request routing; the [case guide](reference/case-data-guide.md) explains their relationship.

No previous course or programming background is required. Begin with Module 1. When a new term appears, read its local explanation before following the code. The [technical foundations](reference/technical-foundations.md) and [programming patterns](reference/python-patterns.md) provide worked revision material; the glossary is a reference, not a substitute for the explanation.

## Open the prepared workspace

1. Open the course folder in VS Code.
2. Open `modules/01-standalone-foundations/01-model-and-application.md` as the written lesson, or read it in the browser.
3. Open `notebooks/01-foundations/01-model-and-application.ipynb` alongside it.
4. Select the Python kernel inside this project's `.venv` folder. A kernel is the Python process that runs cells and retains their values.
5. Read the explanation, predict the next result, run the cell and compare the output with the supplied facts.

The files are already present in a prepared checkout; no lab-file download is needed. For a fresh copy, follow the [setup guide](SETUP.md) and run `uv run --locked python scripts/setup.py` from the course folder. That command recreates the locked environment. The reader and Python notebooks are separate applications: opening a lesson in the reading website does not execute its code.

## Choose the learning route

The business route follows concepts, organisational cases and design decisions. It uses technical outputs as evidence about the mechanism without requiring Python execution. The implementation route follows the complete sequence and adds the notebook activities, including recommended live-model experiments.

For live study, follow the [live-model guide](reference/live-model-guide.md). Configure the key locally, select a supported model and set `COURSE_LIVE_MODE=1`. The first live request appears in Module 1. Later exercises add streaming, embeddings, retrieval, specialists, tool loops, durable review and the capstone. Public weights for the local inference and adaptation exercises have a separate download switch.

## Work rather than only run

An executed notebook is not evidence that its contents were understood. Record a prediction before the example. Complete the independent answer or programming task before consulting its labelled solution. Then change one input, explain why the result changes and identify the limit of the claim being made.

Restart the kernel and run the notebook from the beginning after substantial experiments. This checks that the result does not depend on a forgotten earlier cell. The core route can be verified offline; marked live cells execute actual provider calls only in live mode. The [verification guide](reference/verification.md) distinguishes these checks from claims about deployment or business outcomes.

## Carry a design record forward

Use the [workbook](WORKBOOK.md) to retain the contribution, evidence, unresolved questions, recipient, acceptance conditions, authority and recovery route. In later modules, add evaluation, capacity, context ownership, release and improvement decisions. The [research chapters](reference/literature-guide.md) develop the organisation design arguments and cite their scholarly sources.

The course should leave a learner able to explain the technology, inspect a working contribution and defend how that contribution fits into work. A successful model answer is one observation within that judgement.
