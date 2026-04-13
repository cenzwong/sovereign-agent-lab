"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                                                                 
I'm sorry, I'm not trained to help with that.
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                   
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                          
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                                                                 
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking                                                                 
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                   
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                          
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit                                                                                 
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking                                                   
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                     
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                                      
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
When the user asked an out-of-scope question about parking, CALM correctly intercepted it, stated clearly that it was not trained to help with that specific topic, supplied a helpful fallback suggestion to contact the event organiser, and then immediately attempted to guide the user back into the active "confirm booking" flow.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
In Exercise 2, the LangGraph agent simply refused the out-of-scope question with a generic rejection statement, effectively terminating the interaction since it had no structured conversational context or active flow to maintain. In contrast, Rasa CALM gracefully navigated the digression without breaking the active business flow. It safely rejected the query, provided a helpful fallback response, and crucially, proactively prompted the user to resume their place in the ongoing 'confirm booking' process.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I tested the cutoff guard by temporarily modifying the condition in actions.py to always evaluate to True, forcing an immediate escalation regardless of the actual time. I then ran the Rasa server and chat interface, initiated a booking confirmation conversation, and verified that the agent escalated and provided the correct reason as soon as the modified condition was met. Finally, I reverted the change and confirmed the normal flow still works.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
This architectural simplification drastically reduces boilerplate and increases conversational flexibility. The LLM now naturally handles complex slot extraction (like parsing 'about 160' to 160) and intent routing, completely replacing rigid regex parsers and massive NLU training datasets. Crucially, Python still manages the core business rules and data validations—via the ActionValidateBooking class—since we cannot trust an LLM to reliably enforce strict numerical constraints or external API logic without hallucinating. While CALM smoothly handles unexpected human phrasing, the old approach provided absolute deterministic trust since every single dialogue path was explicitly hardcoded.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The explicit setup cost of Rasa CALM buys you rigid enterprise guardrails and conversational predictability. Unlike LangGraph, a CALM agent is strictly confined to the exact workflows defined in its `flows.yml`; it cannot improvise an undefined operational sequence, invent a new tool call, or generate a wholly hallucinated freeform response outside of the approved patterns. For a sensitive enterprise application like real-world venue booking, this inability to "go off-script" is a vital safety feature rather than a limitation, as it guarantees the assistant strictly obeys corporate compliance and explicit operational boundaries.
"""
