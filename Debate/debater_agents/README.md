# DebaterAgents Crew

Welcome to the DebaterAgents Crew project, powered by [crewAI](https://crewai.com). This project sets up a multi-agent AI system where agents collaborate and compete in a debate-like environment, maximizing their collective intelligence and capabilities.

## Project Overview

DebaterAgents Crew simulates a structured debate with three specialized agents:

- **Proposer Agent:** Introduces and argues in favor of a topic.
- **Opposer Agent:** Presents counterarguments and opposes the topic.
- **Judge Agent:** Evaluates both sides, analyzes the arguments, and delivers a final judgement (in favor or against).

Each agent operates independently, using its own logic and tools, but interacts with others to simulate a realistic debate. The system is highly customizable—agents, tasks, and debate topics can be configured to suit your needs.

## Workflow

1. **Proposer** generates arguments supporting a given topic.
2. **Opposer** responds with counterarguments.
3. **Judge** reviews both sets of arguments and decides the outcome.
4. Results are saved in the `output/` folder as markdown files (`propose.md`, `oppose.md`, `decide.md`).

## Monitoring & Tracing

This project integrates **Opik** for monitoring and tracing:

- **CrewAI Monitoring:** All crew operations are tracked using Opik's CrewAI integration.
- **Generative AI Monitoring:** All generative AI calls are traced using Opik's GenAI integration.
- Configuration is handled in `src/debater_agents/crew.py` using your `OPIK_API_KEY` from `.env`.

## Web Application

This project includes a web interface built with **Streamlit** and a backend powered by **FastAPI**.

- **Streamlit Frontend:**  
  Located at `src/debater_agents/frontend/app.py`.  
  Allows users to input a debate topic and view the results (propose, oppose, judge's decision) in expandable panels.

- **FastAPI Backend:**  
  Located at `src/debater_agents/backend/api.py`.  
  Exposes a `/debate` endpoint that runs the debate workflow and returns the results.

### How to Run

#### 1. Install Dependencies

Make sure you have Python >=3.10,<3.14 and [uv](https://docs.astral.sh/uv/) installed.

```bash
pip install uv
uv pip install fastapi uvicorn streamlit requests pydantic crewai[tools] opik
```

#### 2. Set Environment Variables

Add your API keys and model info to `.env` and `.streamlit/secrets.toml`.

#### 3. Start the FastAPI Backend

```bash
uvicorn src.debater_agents.backend.api:app --reload
```

#### 4. Start the Streamlit Frontend

```bash
streamlit run src/debater_agents/frontend/app.py
```

#### 5. Use the App

- Enter a debate topic in the Streamlit UI.
- Click "Start Debate" to view the arguments and judge's decision in expandable panels.

## Output

- `output/propose.md`: Arguments from the Proposer.
- `output/oppose.md`: Counterarguments from the Opposer.
- `output/decide.md`: Judgement and reasoning from the Judge.

## Customizing

- Edit `src/debater_agents/config/agents.yaml` to define agent roles and capabilities.
- Edit `src/debater_agents/config/tasks.yaml` to set debate topics and tasks.
- Modify `src/debater_agents/crew.py` to adjust agent logic, tools, or arguments.
- Update Opik tracking configuration in `crew.py` as needed.

## Support Links - CrewAI

For support, questions, or feedback:
- [Documentation](https://docs.crewai.com)
- [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI!