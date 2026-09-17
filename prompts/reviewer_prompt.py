"""
Reviewer Prompt

Quality assurance.
"""

def get_reviewer_prompt(topic: str):
    return f"""
Review the report about

"{topic}"

Verify:

- Accuracy
- Completeness
- Grammar
- Formating
- Logical Flow
- Headings
- Professional Language

Improve the report if needed.

Return only the final polished version.
"""