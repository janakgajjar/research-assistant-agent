import streamlit
import crewai
import litellm
import dotenv
import reportlab
from importlib.metadata import version

print("=" * 40)
print("✅ Environment Setup Successful!")
print("=" * 40)

print(f"Python     : {version('pip')}")
print(f"Streamlit  : {streamlit.__version__}")
print(f"CrewAI     : {crewai.__version__}")
print(f"LiteLLM    : {version('litellm')}")
print(f"Dotenv     : {version('python-dotenv')}")
print(f"ReportLab  : {version('reportlab')}")

print("=" * 40)
print("🚀 All required packages are installed.")
print("=" * 40)