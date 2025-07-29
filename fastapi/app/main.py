from fastapi import FastAPI
from dotenv import load_dotenv
import os
import sys

""""load environment variables """

load_dotenv()

"""configure langsmith tracing """
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "FITNESSPLANNER"

environment = os.getenv("ENVIRONNEMENT")
print("environment", environment)

if environment == "dev":
    print("detected dev environment")
    sys.path.append("fast_api")
else:
    sys.path.append("fast_api")
