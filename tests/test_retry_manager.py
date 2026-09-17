from ai.retry_manager import RetryManager

retry = RetryManager()

def fake_task(llm):
    print("Using:", llm.model)
    return "Success"

result = retry.execute(fake_task)

print(result)