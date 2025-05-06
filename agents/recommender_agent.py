from typing import Dict, Any
from .base_agent import BaseAgent
import json

class RecommenderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Recommender",
            instructions="""Generate a Cover Letter by taking info from my resume—such as skills, experiences, and phrasing—to better align with the job description and increase my chances of selection."""
        )

    async def run(self, messages: list) -> Dict[str, Any]:
        """Generate Cover Letter"""
        print("💡 Recommender: Generating Cover Letter")

        workflow_context = eval(messages[-1]["content"])
        try:
            # Extract the content from the last message
            content = messages[-1].get("content", "{}")
            input_data = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Error parsing input data: {e}")
            return {
                "title": [],
                "match_timestamp": "N/A",
                "match_score": 0,
                "analysis": "Error processing the match.",  
            }


        # Extract analysis results and job description
        analysis_results = input_data.get("analysis_results", {})
        job_description = input_data.get("job_description", "")

                # Prepare the prompt for Ollama
        prompt = f"""
        You are an AI Cover Letter Generator. Generate a cover letter for the following candidate profile and job description.
        
        Candidate Profile:
        {json.dumps(analysis_results, indent=2)}
        
        Job Description:
        {job_description}

        """

        # Query Ollama for matching results
        recommendation = self._query_ollama(prompt)

        return {
            "final_recommendation": recommendation,
            "recommendation_timestamp": "2025-03-14",
            "confidence_level": "high",
        }
