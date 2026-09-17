from agents import (
    create_research_agent,
    create_writer_agent,
    create_reviewer_agent
)

from tasks import (
    create_research_task,
    create_writer_task,
    create_reviewer_task
)

topic = "Artificial Intelligence"

researcher = create_research_agent()
writer = create_writer_agent()
reviewer = create_reviewer_agent()

research_task = create_research_task(topic, researcher)
writer_task = create_writer_task(topic, writer)
reviewer_task = create_reviewer_task(topic, reviewer)

print("✅", research_task.description[:80])
print("✅", writer_task.description[:80])
print("✅", reviewer_task.description[:80])