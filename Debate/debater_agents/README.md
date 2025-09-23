# DebaterAgents Crew

Welcome to the DebaterAgents Crew project, powered by [crewAI](https://crewai.com). This template helps you set up a multi-agent AI system where agents collaborate and compete in a debate-like environment, maximizing their collective intelligence and capabilities.

## Project Overview

DebaterAgents Crew simulates a structured debate with three specialized agents:

- **Proposer Agent:** Introduces and argues in favor of a topic.
- **Opposer Agent:** Presents counterarguments and opposes the topic.
- **Judge Agent:** Evaluates both sides, analyzes the arguments, and delivers a final judgement (in favor or against).

Each agent operates independently, using its own logic and tools, but interacts with others to simulate a realistic debate. The system is highly customizable—agents, tasks, and debate topics can be configured to suit your needs.

### Workflow

1. **Proposer** generates arguments supporting a given topic.
2. **Opposer** responds with counterarguments.
3. **Judge** reviews both sets of arguments and decides the outcome.
4. Results are saved in the `output/` folder as markdown files (`propose.md`, `oppose.md`, `decide.md`).

## Installation

Ensure you have Python >=3.10 <3.14 installed. This project uses [UV](https://docs.astral.sh/uv/) for dependency management.

Install uv:

```bash
pip install uv
```

Navigate to your project directory and install dependencies:

```bash
crewai install
```

## Customizing

- Add your `OPENAI_API_KEY` to the `.env` file.
- Edit `src/debater_agents/config/agents.yaml` to define agent roles and capabilities.
- Edit `src/debater_agents/config/tasks.yaml` to set debate topics and tasks.
- Modify `src/debater_agents/crew.py` to adjust agent logic, tools, or arguments.
- Update `src/debater_agents/main.py` for custom inputs or workflow changes.

## Running the Project

Start a debate from the root folder:

```bash
crewai run
```

This will execute the debate workflow and generate output files with each agent's contributions and the final judgement.

## Output

- `output/propose.md`: Arguments from the Proposer.
- `output/oppose.md`: Counterarguments from the Opposer.
- `output/decide.md`: Judgement and reasoning from the Judge.

## Understanding Your Crew

Agents are defined in `config/agents.yaml` and tasks in `config/tasks.yaml`. Each agent has a unique role and set of tools, collaborating and competing to simulate a real debate.

## Support

For support, questions, or feedback:
- [Documentation](https://docs.crewai.com)
- [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.