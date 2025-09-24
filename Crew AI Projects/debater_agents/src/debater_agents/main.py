#!/usr/bin/env python
import sys
import warnings

from debater_agents.src.debater_agents.crew import DebaterAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Responsible AI LLMs',
    }
    
    try:
        result= DebaterAgents().crew().kickoff(inputs=inputs)
        print(result.raw)
        print("Crew finished successfully.")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
