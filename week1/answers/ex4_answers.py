"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "This function call will return a list of venues in Edinburgh that can accommodate at least 300 people and have vegan options. The response will include the names of the venues, which can then be used to fetch individual details using the `get_venue_details` function."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
When we changed The Albanach's status to 'full' in mcp_venue_server.py and re-ran the script, the agent dynamically selected The Haymarket Vaults instead, updating its final answer to 1 Dalry Road, Edinburgh. Notably, we didn't need to change any code in the LangGraph client (exercise4_mcp_client.py) because the server's state and tools are dynamically fetched over the MCP protocol.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 8   # count in exercise2_langgraph.py (imports and explicit tool list)
LINES_OF_TOOL_CODE_EX4 = 1   # count in exercise4_mcp_client.py (dynamic discovery: tools, _ = await discover_tools(...))

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
Beyond simply separating files, MCP establishes a robust protocol that dynamically provides agents with tools, endpoints, and JSON schemas on demand. This decoupling means multiple agent frameworks, UI clients, or command lines can interact securely with the same server without maintaining duplicating adapter code. Additionally, tools can be versioned, added, or removed entirely without restarting or risking crashes in the core LangGraph reasoning agent.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- LangGraph Coordinator: This engine acts as the dynamic, central researcher that iterates over open-ended problems, autonomously selecting which APIs or web scrapes to perform until it reaches its objective.
- Rasa Dialogue Manager: This module safely handles the structured, user-facing conversation or outbound phone calls, mapping utterances into strict intents without letting the AI hallucinate random responses.
- MCP Tool Server: This layer isolates external integrations (like venue checking, web search tools, or emails) behind a unified schema, ensuring our researchers can blindly query them across different environments securely.
- Cross-session Memory Layer: This datastore persists conversation context, tracking specific client requirements like accessibility or catering so our agent doesn't incorrectly clear constraints between chat sessions.
- System Orchestrator: This control structure bridges the distinct functional components together, routing precise confirmation dialogues directly to Rasa while handing complex exploration searches dynamically to the LangGraph researcher.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph is ideal for the research component because it natively utilizes a flexible "Think-Act-Observe" loop; I observed it automatically pivoting from searching venues to finding capacity and querying details. Conversely, Rasa is required for the call component because phone calls demand a rigid, predictable turn-by-turn state machine where skipping intents leads to failure. Swapping them is problematic: a deterministic Rasa agent is far too rigid to dynamically adjust sequential web scraping, whereas a non-deterministic LangGraph agent managing a call might hallucinate venue constraints or deviate dangerously off-script during a real client phone interaction.
"""
