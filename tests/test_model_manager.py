from ai.model_manager import ModelManager

manager = ModelManager()

print("Keys:")
for _ in range(5):
    print(manager.next_key())

print("\nModels:")
for _ in range(5):
    print(manager.next_model())