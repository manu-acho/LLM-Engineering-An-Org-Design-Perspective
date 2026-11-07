# Module 5: Organisational knowledge and retrieval

[Curriculum](../../CURRICULUM.md) · [Setup](../../STUDY-WORKSPACE.md) · [Glossary](../../reference/glossary.md)

A policy assistant needs the current permitted evidence, not simply a plausible paragraph. At Harbour an older policy, another region's policy and a current policy can share many words, making relevance alone an inadequate selection rule.

## Harbour at this point

Harbour’s investigator needs the policy relevant to the disputed delivery. An old rule or another region’s rule can sound convincing while being unsuitable. Finance also needs to know which policy governed an account correction. Finding text is therefore part of maintaining a dependable evidence and decision process.

**Supply-chain and organisation design question:** Design a policy source register showing owner, region, effective version, correction route and response to conflicting passages.

Read [Meet Harbour](../../HARBOUR.md) for the company and cross-functional workflow, or revisit [this module’s place in the case](../../reference/harbour-learning-journey.md#module-5). The technical activity examines a selected contribution; it does not establish that the proposed arrangement has been implemented.

## Preparation and route

Complete Module 4 first, or use its worked examples to check the prerequisite concepts. For numerical and systems terms, begin with the [technical foundations](../../reference/technical-foundations.md). Unfamiliar Python syntax is explained in the [programming reference](../../reference/python-patterns.md).

1. [Lesson 5.1: How an assistant finds organisational knowledge](01-concepts.md)
2. [Lesson 5.2: Retrieve current permitted evidence](02-code-workshop.md)
3. [Lesson 5.3: A knowledge assistant is also a design of authority](03-business-and-organisation.md)
4. [Lesson 5.4: Calculate similarity and inspect what ranking means](04-vectors-and-ranking.md)
5. [Lesson 5.5: Follow filtering, vectorisation and ranking](05-source-walkthrough.md)
6. [Lesson 5.6: Build an organisational knowledge service](06-design-lab.md)

Read the concepts and business case before the code workshop. Managers can follow the design reasoning without executing Python. The implementation route follows every lesson and its notebook, predicts outputs and compares the failure cases. The organisational contribution remains the same across both routes.

## Included code and learning boundary

The original implementation is `src/ai_orgdesign/labs/m05.py`. The notebooks import that code so the explanations and checked behaviour share one implementation. The core route runs locally without paid services. Optional integrations are explicitly gated and described in the [verification guide](../../reference/verification.md).

Searching delivery evidence in north returns the active P-2 policy. It excludes the retired P-1 and the south P-3 before fitting or ranking. A query whose words do not occur in the permitted vocabulary returns no hits. Returning no evidence is different from answering that no policy exists.

## Completion exercise

Ask whether filtering after a global top-two search can lose the best permitted result. Then remove all permitted documents and decide what the service should show.

A satisfactory response explains the mechanism, interprets the observed output, identifies the relevant authority and source ownership, compares an alternative and states what additional evidence would support a business claim. The worked answers are included in the workshop and design lessons. Continue with [organisation design research](../../reference/research/02-coordination.md) for the supporting theory and scholarly references.

## Another explanation

[Sentence Transformers retrieval and reranking](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) provides a primary technical account alongside the included implementation. Use the [further learning guide](../../reference/further-learning.md) to choose additional explanations. External examples may use another task or version; completing them is not required to follow this module.

## Demonstrate the learning

- Follow filtering and lexical ranking into the returned evidence.
- Compare lexical representations with actual neural embeddings.
- Retrieve evidence, generate a brief and check its structured facts.
- Explain the case-specific acceptance, authority, correction and evaluation arrangements.

The matching notebooks provide prediction spaces, practical activities and labelled answers. Some include independent programming tasks. Use the [live-model guide](../../reference/live-model-guide.md) for recommended live work and the [case guide](../../reference/case-data-guide.md) to keep the records and route meanings distinct.
