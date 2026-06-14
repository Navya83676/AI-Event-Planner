from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

import os

# =========================
# LOAD ENVIRONMENT
# =========================

load_dotenv()

# =========================
# API KEY VALIDATION
# =========================

groq_key = os.getenv(
    "GROQ_API_KEY"
)

if not groq_key:

    print(
        "WARNING: GROQ_API_KEY missing"
    )

# =========================
# MAIN LLM
# =========================

llm = ChatGroq(
    groq_api_key=groq_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0.2
)

# =========================
# SIMPLE LLM CALL
# =========================

def ask_llm(prompt):

    response = llm.invoke([

        HumanMessage(
            content=prompt
        )
    ])

    return response.content


# =========================
# GENERIC AGENT RESPONSE
# =========================

def run_agent_prompt(

    prompt_template,

    variables

):

    chain = (
        prompt_template
        | llm
    )

    print("\n===== LLM REQUEST =====")
    print(variables)

    response = chain.invoke(
        variables
    )

    print("\n===== LLM RESPONSE =====")
    print(response.content)

    return response.content