from agents import (
    create_research_agent,
    create_writer_agent,
    create_reviewer_agent,
)

researcher = create_research_agent()
writer = create_writer_agent()
reviewer = create_reviewer_agent()

print("✅ Research Agent :", researcher.role)
print("✅ Writer Agent   :", writer.role)
print("✅ Reviewer Agent :", reviewer.role)

