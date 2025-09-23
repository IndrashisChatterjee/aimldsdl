# aimldsdl

A collection of AI, Machine Learning, Deep Learning, and Structured Data Learning projects and experiments.

This repository gathers multiple projects, notebooks, and agent-based systems that demonstrate practical applications of modern AI/ML/DL techniques. Each subdirectory contains self-contained resources and guides for running experiments, tracking results, and integrating with external APIs.

---

## Repository Structure

- `kd/` — Knowledge Distillation on MNIST using PyTorch
  - Demonstrates transferring knowledge from a large teacher model to a smaller student model on the MNIST dataset.
  - Main notebook: [`kd/knowledge_distillation.ipynb`](kd/knowledge_distillation.ipynb)
  - [Project README](kd/readme.md)

- `Debate/debater_agents/` — Multi-Agent Debate System powered by crewAI
  - Simulates structured debates between proposer, opposer, and judge agents.
  - Includes a web app (Streamlit frontend, FastAPI backend) for interactive debates.
  - Output markdown files for arguments and decisions.
  - [Project README](Debate/debater_agents/README.md)

- `OpenAISDK/` — OpenAI Agents SDK with MLflow in Databricks
  - Integrates OpenAI Agents SDK with MLflow for experiment tracking and model execution in Databricks.
  - Demonstrates how to use external APIs (e.g. Gemini) with OpenAI-compatible interfaces.
  - Asynchronous agent execution and result visualization in notebooks.
  - Main notebook: [`OpenAISDK/agents sdk.ipynb`](OpenAISDK/agents%20sdk.ipynb)
  - [Project README](OpenAISDK/readme.md)

<!-- Add more project summaries here if needed -->

---

## Quick Start

Clone the repository:

```sh
git clone https://github.com/IndrashisChatterjee/aimldsdl.git
cd aimldsdl
```

### Running Knowledge Distillation (MNIST)

1. Install dependencies:
    ```sh
    pip install torch torchvision numpy pandas tqdm
    ```
2. Open `kd/knowledge_distillation.ipynb` in Jupyter or VS Code.
3. Run all cells: trains teacher and student models, evaluates results.

### Running DebaterAgents Crew

1. Install dependencies (Python >=3.10,<3.14, [uv](https://docs.astral.sh/uv/)):
    ```sh
    pip install uv
    uv pip install fastapi uvicorn streamlit requests pydantic crewai[tools]
    ```
2. Set API keys and model info in `.env` and `.streamlit/secrets.toml`.
3. Start backend:
    ```sh
    uvicorn src.debater_agents.backend.api:app --reload
    ```
4. Start frontend:
    ```sh
    streamlit run src/debater_agents/frontend/app.py
    ```
5. Use the app: Enter a debate topic and view arguments/decision.

### Running OpenAI Agents SDK with MLflow in Databricks

1. Open `OpenAISDK/agents sdk.ipynb` in Databricks.
2. Ensure all required libraries are installed:
    ```python
    !pip install openai-agents openai mlflow dotenv
    dbutils.library.restartPython()
    ```
3. Set environment variables and API keys (`.env` file recommended).
4. Run notebook cells sequentially to:
    - Import libraries, load environment variables.
    - Login and set up MLflow experiment tracking.
    - Configure external API clients (e.g., Gemini with OpenAI schema).
    - Define and run agents asynchronously.
    - Visualize results in Markdown.
5. Track experiments and results in MLflow UI.

---

## Prerequisites

- Databricks workspace (for OpenAISDK project)
- Python environment (compatible with Databricks)
- API keys for OpenAI and external providers (e.g., Google Gemini)
- MLflow Tracking Server (or Databricks MLflow integration)
- Set secrets securely using Databricks secrets or environment variables

---

## Contributing

Contributions, suggestions, and feedback are welcome!  
Feel free to submit issues or pull requests.

---

## License

MIT License

---

## Contact

Created by [Indrashis Chatterjee](https://github.com/IndrashisChatterjee).

---

## References & Project Links

- [crewAI documentation](https://docs.crewai.com)
- [crewAI GitHub](https://github.com/joaomdmoura/crewai)
- [Knowledge Distillation Paper (Hinton et al.)](https://arxiv.org/abs/1503.02531)
- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-agents)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [Databricks Documentation](https://docs.databricks.com/)
