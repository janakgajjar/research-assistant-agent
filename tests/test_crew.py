from crew import ResearchCrew

crew = ResearchCrew(
    topic="Artificial Intelligence"
)

result = crew.run()

print("\n")
print("=" * 60)
print("FINAL OUTPUT")
print("=" * 60)

print(result)