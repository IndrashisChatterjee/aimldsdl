# FinanceAgent Crew

Welcome to the FinanceAgent Crew project, powered by [crewAI](https://crewai.com). This template helps you set up a multi-agent AI system with ease, leveraging the flexible framework provided by crewAI. Agents collaborate on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed. This project uses [UV](https://docs.astral.sh/uv/) for dependency management.

Install uv:
```bash
pip install uv
```

Install dependencies:
```bash
uv pip install -r requirements.txt
```

To generate a `requirements.txt` from your environment:
```bash
uv pip freeze > requirements.txt
```

## Configuration

- Add your `OPENAI_API_KEY` and other secrets to the `.env` file.
- Edit `src/finance_agent/config/agents.yaml` to define agents.
- Edit `src/finance_agent/config/tasks.yaml` to define tasks.
- Edit `src/finance_agent/crew.py` to customize logic, tools, and arguments.

## Running the Project

To run the crew and generate a report from the command line:
```bash
python src/finance_agent/main.py
```

## FastAPI Backend & Streamlit Frontend

This project includes a FastAPI backend and a Streamlit UI for interactive execution.

### Start the FastAPI backend:
```bash
uvicorn src.finance_agent.backend.api:app --reload
```

### Start the Streamlit frontend:
```bash
streamlit run src/finance_agent/frontend/app.py
```

- Enter your input in the UI and click "Run Crew".
- The output report will be displayed in an expander.

## Understanding Your Crew

The FinanceAgent Crew consists of multiple AI agents, each with unique roles and tools. Agents and tasks are configured in the `src/finance_agent/config/` directory.

## Support

For support, questions, or feedback:
- [Documentation](https://docs.crewai.com)
- [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with crewAI!