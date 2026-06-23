# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Prompt used to generate the suite:**

```
Identify three edge-case inputs that might still break my guessing game's parse_guess(raw, low, high) function, then write a pytest suite that verifies the game handles each one gracefully (returns ok=False with a helpful message instead of crashing or accepting it). Use the Normal range of 1 to 100.
```

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative number (`-5`) | (prompt above) | `test_negative_number_is_rejected` — expects `ok=False` and a "range" message | ✅ Yes | A negative is a valid int but outside the range, so it must be rejected, not given a hint. |
| Decimal (`33.6`) | (prompt above) | `test_decimal_is_rejected` — expects `ok=False` and a "whole number" message | ✅ Yes | The original code truncated decimals to win, so the game must now reject them outright. |
| Extremely large value (`999999999999`) | (prompt above) | `test_extremely_large_value_is_rejected` — expects `ok=False` and a "range" message | ✅ Yes | A huge number could be wrongly accepted or break expectations; it should fall out of range. |
| Range boundaries (`1` and `100`) | (prompt above) | `test_boundaries_are_accepted` — expects `(True, value, None)` | ✅ Yes | Added to confirm the range check is inclusive and doesn't over-reject valid edge values. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
