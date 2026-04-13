EDINBURGH AGENT

REPO: https://github.com/sovereignagents/sovereign-agent-lab 

WHAT YOU ARE BUILDING THIS WEEK

Rod sends a WhatsApp ("sort the pub for tonight, 160 people, vegan options, confirm by 5pm") and disappears for three hours. We are building the two agents that handle it. 

The Headless Automator searches venues, checks the weather, estimates catering costs, and generates a flyer. Autonomous. No human in the loop. 

The Digital Employee takes the call from the pub manager, confirms the booking, and enforces our limits. Structured, auditable, no improvising. 

You build both this week. They grow together across all five weeks into a combined system. Week 5, we apply the whole thing to something from our own work. 

GETTING STARTED

1. Fork the repo (do not just clone: fork so we can receive our updates)
2. cp .env.example .env and add your Nebius key (NEBIUS_KEY)
3. make install to set up the main environment
4. make smoke should print a checkmark


For Exercise 3 (Rasa) we will also need a free Rasa Pro licence key: https://rasa.com/rasa-pro-developer-edition-license-key-request 

Takes two minutes and they email it to us. Add it to .env as RASA_PRO_LICENSE, then run make install-rasa. 

The README walks through everything step by step. 

Type make help at any point to see all available commands. 

 WHEN WE ARE STUCK

Run the command directly instead of through make to get the full error. Open a ticket in the repo with the exercise number, the command you ran, your OS, and your uv --version. 

 SUBMITTING

Run make check-submit before we push. 

It tells us exactly what is missing. 

Submit your entire fork: we pull from it directly. 

See GRADING_OVERVIEW.md in the repo for the full 30/40/30 breakdown.