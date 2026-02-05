#!/usr/bin/env python3
"""
Resume Optimizer Agent
Automatically tailors your resume to match job descriptions using AI analysis.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional
import anthropic


class ResumeOptimizer:
    """Agent for optimizing resumes based on job descriptions."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the optimizer with Anthropic API key."""
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY must be set in environment or passed to constructor")
        self.client = anthropic.Anthropic(api_key=self.api_key)
        
    def analyze_job_description(self, job_description: str) -> Dict:
        """Extract key requirements and keywords from job description."""
        prompt = f"""Analyze this job description and extract:
1. Required skills (technical and soft skills)
2. Key responsibilities
3. Important keywords that should appear in a resume
4. Experience level required
5. Industry-specific terminology

Job Description:
{job_description}

Provide your analysis in JSON format with keys: required_skills, key_responsibilities, keywords, experience_level, industry_terms"""

        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract JSON from response
        response_text = message.content[0].text
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return {}
    
    def optimize_resume(self, resume: str, job_description: str, 
                       preserve_truthfulness: bool = True) -> str:
        """Generate an optimized version of the resume for the job description."""
        
        analysis = self.analyze_job_description(job_description)
        
        optimization_prompt = f"""You are a professional resume optimizer. Given the following resume and job description analysis, create an optimized version of the resume.

IMPORTANT RULES:
1. {'NEVER add false information or skills the candidate does not have' if preserve_truthfulness else 'You may suggest additions based on the job requirements'}
2. Reorder and emphasize existing experiences to match job priorities
3. Use keywords from the job description naturally
4. Quantify achievements where possible
5. Tailor the summary/objective to the role
6. Highlight relevant skills prominently
7. Keep the same overall structure and formatting

Original Resume:
{resume}

Job Requirements Analysis:
{json.dumps(analysis, indent=2)}

Job Description:
{job_description}

Provide the optimized resume, maintaining truthfulness while maximizing relevance to the position."""

        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            messages=[{"role": "user", "content": optimization_prompt}]
        )
        
        return message.content[0].text
    
    def suggest_improvements(self, resume: str, job_description: str) -> List[str]:
        """Provide specific suggestions for improving the resume."""
        
        prompt = f"""Review this resume against the job description and provide specific, actionable improvement suggestions.

Resume:
{resume}

Job Description:
{job_description}

Provide 5-10 specific suggestions as a bulleted list. Focus on:
- Missing keywords or skills that could be added (if truthful)
- Better ways to phrase existing experience
- Sections that need more emphasis
- Formatting improvements
- Achievement quantification opportunities"""

        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        suggestions = message.content[0].text.strip().split('\n')
        return [s.strip() for s in suggestions if s.strip()]
    
    def calculate_match_score(self, resume: str, job_description: str) -> Dict:
        """Calculate how well the resume matches the job description."""
        
        prompt = f"""Analyze how well this resume matches the job description. Provide:
1. Overall match score (0-100)
2. Keyword match percentage
3. Skills coverage percentage
4. Experience relevance score
5. Brief explanation of the scores

Resume:
{resume}

Job Description:
{job_description}

Respond in JSON format with keys: overall_score, keyword_match, skills_coverage, experience_relevance, explanation"""

        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )
        
        response_text = message.content[0].text
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return {}


def main():
    """Example usage of the ResumeOptimizer."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Optimize your resume for a job description')
    parser.add_argument('--resume', required=True, help='Path to resume file')
    parser.add_argument('--job-description', required=True, help='Path to job description file')
    parser.add_argument('--output', default='optimized_resume.txt', help='Output file path')
    parser.add_argument('--suggestions-only', action='store_true', 
                       help='Only show suggestions without creating optimized version')
    parser.add_argument('--score', action='store_true', 
                       help='Calculate and display match score')
    
    args = parser.parse_args()
    
    # Read input files
    with open(args.resume, 'r') as f:
        resume = f.read()
    
    with open(args.job_description, 'r') as f:
        job_description = f.read()
    
    # Initialize optimizer
    optimizer = ResumeOptimizer()
    
    # Calculate match score if requested
    if args.score:
        print("\n📊 Calculating match score...\n")
        score = optimizer.calculate_match_score(resume, job_description)
        print(f"Overall Score: {score.get('overall_score', 'N/A')}/100")
        print(f"Keyword Match: {score.get('keyword_match', 'N/A')}%")
        print(f"Skills Coverage: {score.get('skills_coverage', 'N/A')}%")
        print(f"Experience Relevance: {score.get('experience_relevance', 'N/A')}/100")
        print(f"\nExplanation: {score.get('explanation', 'N/A')}")
        print("\n" + "="*60 + "\n")
    
    # Show suggestions if requested
    if args.suggestions_only:
        print("💡 Analyzing and generating suggestions...\n")
        suggestions = optimizer.suggest_improvements(resume, job_description)
        print("Suggestions for improvement:\n")
        for suggestion in suggestions:
            print(suggestion)
    else:
        # Generate optimized resume
        print("🔄 Optimizing resume...\n")
        optimized = optimizer.optimize_resume(resume, job_description)
        
        # Save to file
        with open(args.output, 'w') as f:
            f.write(optimized)
        
        print(f"✅ Optimized resume saved to: {args.output}")
        
        # Also show suggestions
        print("\n💡 Additional suggestions:")
        suggestions = optimizer.suggest_improvements(resume, job_description)
        for suggestion in suggestions[:5]:  # Show top 5
            print(suggestion)


if __name__ == '__main__':
    main()
