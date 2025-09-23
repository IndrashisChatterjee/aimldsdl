from fastapi import FastAPI
from pydantic import BaseModel
from debater_agents.crew import DebaterAgents

app = FastAPI()

class DebateRequest(BaseModel):
    topic: str

@app.post("/debate")
async def debate(request: DebateRequest):
    inputs = {'topic': request.topic}
    try:
        result = DebaterAgents().crew().kickoff(inputs=inputs)
        # Read outputs from markdown files
        with open("output/propose.md", "r", encoding="utf-8") as f:
            propose = f.read()
        with open("output/oppose.md", "r", encoding="utf-8") as f:
            oppose = f.read()
        with open("output/decide.md", "r", encoding="utf-8") as f:
            decide = f.read()
        return {
            "propose": propose,
            "oppose": oppose,
            "decide": decide
        }
    except Exception as e:
        return {"error": str(e)}