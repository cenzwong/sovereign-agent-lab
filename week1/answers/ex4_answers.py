"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Albanach (Baseline) / The Haymarket Vaults (Experiment)"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh (Baseline) / 1 Dalry Road, Edinburgh (Experiment)"
QUERY_2_FINAL_ANSWER  = "No Edinburgh venues in the database can accommodate 300 people; the maximum capacity is 200 (The Guilford Arms)."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
After marking 'The Albanach' as 'full' in `mcp_venue_server.py`, the agent immediately pivoted. In the first run, it chose The Albanach as the best match. In the second run, it chose The Haymarket Vaults instead. Notably, not a single line of code in the agent client (`exercise4_mcp_client.py`) needed to be changed or even restarted; the agent dynamically discovered the updated availability via the MCP server bridge.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 10   # Imports (~5) + registration (~5)
LINES_OF_TOOL_CODE_EX4 = 0    # 0 lines to ADD a tool (discovery is automatic)

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides a standardized interface for dynamic tool discovery and execution. This allows the tool logic (the server) to evolve independently of the agent (the client). You can add, remove, or modify tool logic in one central place, and every MCP-compatible agent—regardless of whether it's built with LangGraph, Rasa, or a custom loop—instantly inherits those capabilities without requiring code changes, re-imports, or constant re-deployment of the client logic.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- The MCP Venue Server provides a decoupled tool layer that exposes venue data and image generation to any client.
- The LangGraph Research Agent (Planner/Executor) handles complex open-ended tasks like finding venues and calculating costs.
- The Rasa CALM Digital Employee manages the deterministic, high-stakes business logic of the final voice booking call.
- A Shared Memory (CLAUDE.md) ensures that the context from the initial research phase is preserved for the booking assistant.
- Safety Guardrails (Week 5) monitor the server calls to ensure no unauthorized tool execution or budget overruns occur.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
For the research phase, the LangGraph agent is superior because it can handle the unpredictable, multi-step reasoning of 'find matches, then fetch details' without a rigid flow. For the final call, Rasa CALM is better because it enforces strict business rules (like the 16:45 cutoff) that an LLM-only agent might 'negotiate' away. Swapping them feels wrong because you'd lose the reliability of the booking assistant and the flexibility of the researcher.
"""
