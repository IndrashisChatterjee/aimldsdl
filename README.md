# aimldsdl

A collection of AI, Machine Learning, Deep Learning, and Structured Data Learning projects and experiments.

This repository gathers multiple projects, notebooks, and agent-based systems that demonstrate practical applications of modern AI/ML/DL techniques. Each subdirectory contains self-contained resources, code samples, and documentation for learning and experimentation.

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
