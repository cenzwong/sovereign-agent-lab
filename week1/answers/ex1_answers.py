"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
In this clean baseline setting, the Llama-3.3-70B model correctly processed all formats. It returned "The Haymarket Vaults" without formatting and "The Albanach" for XML and SANDWICH, both of which are valid answers according to the parameters of the constraint, showing the baseline signal-to-noise ratio was high enough for the model to parse standard unformatted structures without issue.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The hardest distractor was "The Holyrood Arms", because it satisfied both the capacity capability and the dietary constraint properly, failing only the final status condition (status="full"). This forces the model to carefully screen all parameters before locking in an answer instead of skimming for early hits.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Because the 70B model correctly handled all distractors cleanly across all three formats, Part C was run to see if systematically crippling the model size (down to Llama-3.1-8B) would reveal the context tracking effect. However, the 8B model also successfully identified "The Haymarket Vaults" across the Plain, XML, and Sandwich conditions without failing on the distractors, showing surprisingly strong attention to detail.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Event smaller 8b parameter model coped with the task, but 
in real world scenarios with larger context and more complex constraints, 
structured formatting like XML or the sandwich method would be critical 
to ensure reliability and prevent hallucinations.
"""
