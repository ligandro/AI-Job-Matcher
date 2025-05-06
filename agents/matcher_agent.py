from typing import Dict, Any
from .base_agent import BaseAgent
import ast

import json


from typing import Dict, Any, List
from .base_agent import BaseAgent
import json
import ast
import re
import sqlite3

class MatcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Matcher",
            instructions="""Match candidate profiles with given job description.
            Consider: skills match, experience level, and other relevant factors.
            Provide detailed reasoning and compatibility scores.
            Return analysis of match with the job in JSON format with title, match_score, and location fields.""",
        )

    async def run(self, messages: list) -> Dict[str, Any]:
        """Match candidate with the provided job description"""
        print("🎯 Matcher: Matching resume with job description")

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

        if not analysis_results or not job_description:
            print("Missing analysis results or job description.")
            return {
                "title": [],
                "match_timestamp": "N/A",
                "match_score": 0,
                "analysis": "Error processing the match.",  
            }

        # Prepare the prompt for Ollama
        prompt = f"""
        You are an AI job matcher. Match the following candidate profile with the provided job description.
        
        Candidate Profile:
        {json.dumps(analysis_results, indent=2)}
        
        Job Description:
        {job_description}
        
        Provide a JSON response with the following fields:
        - title: The job title.
        - match_score: The compatibility score as a percentage from 0 to 100
        - analysis: A detailed analysis of the match stating why the candidate is a good fit or not in relation to the job description. Give this in dict format with keys
           as "reasons_for_high_match_score", "reasons_for_moderate_match_score", and "reasons_for_low_match_score" and with the values as strings.
        """

        # Query Ollama for matching results
        try:
            response = self._query_ollama(prompt)
            match_results = self._parse_json_safely(response)
        except Exception as e:
            print(f"Error querying Ollama: {e}")
            return {
                "title": [],
                "match_timestamp": "N/A",
                "match_score": 0,
                "analysis": "Error processing the match.",  
            }

        # Return the matching results
        return {
            "title": match_results.get("title", []),
            "match_timestamp": "2025-05-05",  # Use the current date
            "analysis": match_results.get("analysis", "No analysis provided."),
            "match_score": len(match_results.get("matched_jobs", [])),
        }