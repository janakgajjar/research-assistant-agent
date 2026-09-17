"""
Writer Agent Prompt

Creates a professional report.
"""

def get_writer_prompt(topic: str):
    return f"""
Using the research provided,
write a professional report on 

"{topic}"

Follow this structure:

# {topic}
## Introduction
## Defination
## Key Concepts
## Architecture
## Applications
## Latest Trends
## Advantages
## Challenges
## Conclusion.

Requirements:

- 500-700 words
- Professional tone
- Easy to understand
- Suitable for MCA students
- Use headings
- Use bullet points
- Don't invent facts.
""" 