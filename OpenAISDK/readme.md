# OpenAI SDK with MLflow in Databricks

## Overview

This notebook demonstrates how to integrate the OpenAI Agents SDK with MLflow for experiment tracking and model execution, specifically within a Databricks environment. The workflow showcases how to use external APIs (such as Google Gemini) with OpenAI-compatible schemas and how to trace, log, and run AI agent tasks with MLflow autologging.

## Features

- **Databricks Compatible**: Designed for seamless execution in Databricks notebooks.
- **OpenAI Agents SDK**: Leverages the `openai-agents` package to define and run agents.
- **MLflow Integration**: Uses MLflow for experiment management, autologging, and tracking.
- **Environment Variable Management**: Loads secrets and API keys using `dotenv`.
- **External API Support**: Demonstrates how to call external LLMs (e.g., Gemini) with OpenAI-compatible interfaces.
- **Async Execution**: Utilizes asynchronous agent execution for efficient API calls.
- **Result Visualization**: Displays the agent's final output in Markdown format within the notebook.

## File: `OpenAISDK/agents sdk.ipynb`

### Key Steps

1. **Install Required Packages**
    ```python
    !pip install openai-agents openai mlflow dotenv
    ```

2. **Restart Python Environment (Databricks Specific)**
    ```python
    dbutils.library.restartPython()
    ```

3. **Import Libraries & Load Environment Variables**
    ```python
    from dotenv import load_dotenv
    import mlflow
    # ...other imports...
    load_dotenv(override=True)
    ```

4. **Login and Set Up MLflow**
    ```python
    mlflow.login()
    mlflow.set_experiment("/Workspace/Users/<your-email>/mlruns/agentsSDK")
    mlflow.openai.autolog()
    ```

5. **Configure External API Client**
    - Example uses Google Gemini via OpenAI schema.
    - API keys are loaded from environment variables.

6. **Define and Run Agent**
    - Create an agent with instructions and a model.
    - Run the agent asynchronously using `Runner.run`.

7. **Display Results**
    - Show the agent's output in Markdown for easy reading.

### Example Usage

The notebook includes a sample agent setup and run:
```python
agent = Agent(name="Agent1", instructions="you are An AI Assistant", model=model)
result = await Runner.run(agent, "Tell the latest news with date", run_config=config)
display(Markdown(result.final_output))
```

## Prerequisites

- **Databricks Workspace** with notebook access
- **Python environment** (compatible with Databricks)
- **API Keys** for OpenAI and external providers (e.g., Google Gemini)
- **MLflow Tracking Server** (can use Databricks MLflow integration)

## How to Run

1. Open the notebook in Databricks.
2. Ensure all required libraries are installed and environment variables are set (see `.env` file for secrets).
3. Execute the cells sequentially.
4. View results and tracked experiments in MLflow UI.

## Notes

- The notebook is designed for educational and prototyping purposes.
- Adapt paths and experiment names as necessary for your Databricks workspace and MLflow setup.
- Make sure your API keys and secrets are stored securely (preferably in Databricks secrets or environment variables).

## References

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-agents)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [Databricks Documentation](https://docs.databricks.com/)
