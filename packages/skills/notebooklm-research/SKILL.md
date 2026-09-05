---
name: notebooklm-research
description: Use NotebookLM Hub as a source-grounded research backend from coding agents. Query notebooks, compare evidence, identify gaps, verify claims, and preserve research as durable artifacts before implementation.
---

# NotebookLM Hub Research Skill

Use NotebookLM as an evidence layer, not as an unquestioned oracle.

## Trigger

Use this skill when a task:

- references a NotebookLM notebook or notebook URL;
- depends on a curated research corpus;
- asks for source-grounded verification before coding;
- requires comparing several research sources or notebook findings;
- needs research converted into reusable project knowledge;
- asks Claude Code, Codex, or another coding agent to use NotebookLM.

## Operating model

```text
question
  ↓
NotebookLM Hub backend
  ↓
grounded result + citations
  ↓
coverage check
  ↓
follow-up research if incomplete
  ↓
research artifact
  ↓
implementation / verification
```

## Rules

1. **Separate evidence from interpretation.** Record what NotebookLM says and what the agent infers from it.
2. **Check coverage.** A plausible answer is not automatically a complete answer.
3. **Use follow-ups deliberately.** Ask targeted questions for missing constraints, contradictions, dates, edge cases, or implementation details.
4. **Preserve citations/provenance.** Keep notebook IDs, source references, and query context with generated research artifacts.
5. **Do not bury research in chat.** Important findings should be written into `research/`, `docs/`, ADRs, test plans, or project memory.
6. **Verify implementation claims independently.** NotebookLM evidence can guide architecture, but code behavior should be tested.
7. **Treat transports as replaceable.** Use the Hub client/backend rather than coupling project logic directly to browser selectors, one MCP package, or one unofficial RPC implementation.

## Standard workflows

### Research

Ask a precise question, capture the result, then evaluate:

- established facts;
- uncertainties;
- source disagreements;
- implementation consequences;
- unanswered questions.

Suggested durable artifact:

```yaml
research_question: "..."
notebook_id: "..."
established_facts: []
uncertainties: []
contradictions: []
implementation_implications: []
follow_up_questions: []
```

### Verify

Given a proposed design or implementation:

1. list its factual assumptions;
2. query NotebookLM for support or contradiction;
3. mark each assumption as supported, unsupported, contradicted, or unresolved;
4. create tests for assumptions that can be falsified in code.

### Compare

When comparing approaches, ask NotebookLM for evidence under the same criteria rather than asking separate vague questions. Preserve the comparison matrix in a project artifact.

### Research completeness loop

Do not stop at the first answer if it omits part of the user's request.

```text
original question
      ↓
NotebookLM answer
      ↓
coverage review
  ┌───┴────┐
complete  gaps
  │        │
  │     follow-up
  │        │
  └────┬───┘
       ↓
 synthesis
```

## Agent roles

A useful multi-agent pattern is:

- **NotebookLM**: curated evidence and source-grounded synthesis.
- **Claude Code**: architecture, exploration, refactoring, implementation planning.
- **Codex**: independent critique, implementation, testing, and falsification.

Both coding agents should be able to query the same Hub backend so disagreements can be traced to interpretation rather than different source corpora.

## Publication

When research is mature enough to publish, use the Hub publisher to build an immutable static knowledge-site version. Research changes should produce a new numbered build rather than silently overwriting old published state.

## Legacy note

The historical AvaTar-ArTs NotebookLM skill used Python + Patchright browser automation with `run.py`, notebook library management, persistent authentication, batch query/history/export tools, and a mandatory follow-up loop. Those behaviors are useful lineage, but the Hub skill intentionally specifies behavior independently of any single transport.
