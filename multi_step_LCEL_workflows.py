"""
Designing Multi-step LCEL Workflows
Scenarios:
- Ex. 1: Feature design workflow (idea -> requirements -> technical spec)
- Ex. 2: Service analysis workflow (summary + risks + tests in parallel)
"""


import os
from dotenv import load_dotenv
import google.generativeai as genai  

from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableMap
)

# LLM Bootstrap: Gemini via langchain-google-genai (LCEL-ready chat model)
