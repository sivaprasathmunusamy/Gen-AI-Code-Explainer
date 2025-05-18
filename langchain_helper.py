import os
from openai_key import OPENAI_API_KEY

from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def explain_code_for_beginners(code_snippet: str) -> str:
    """
    Explain the given code snippet in simple terms suitable for beginners.
    """
    llm = OpenAI(temperature=0.3) # DEEPSEEK/LAMA/GOOGLE PALM AI

    prompt = PromptTemplate(
        input_variables=['code_snippet'],
        template=(
            "Explain the following code snippet in a simple and beginner-friendly way:\n\n"
            "```python\n{code_snippet}\n```\n\n"
            "Please explain what it does step-by-step, avoiding technical jargon."
        )
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    explanation = chain.run(code_snippet)
    return explanation
