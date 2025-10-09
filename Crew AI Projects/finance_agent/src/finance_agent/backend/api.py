from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from finance_agent.crew import ResearchCrew

app = FastAPI()

class CrewRequest(BaseModel):
    company: str

class CrewResponse(BaseModel):
    result: str

@app.post("/run_crew", response_model=CrewResponse)
async def run_crew(request: CrewRequest):
    """
    Endpoint to asynchronously run the research crew.
    Accepts company name and returns the report.
    """
    crew = ResearchCrew()
    inputs = {'company': request.company}
    try:
        result = await crew.execute_async(inputs)
        return CrewResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))