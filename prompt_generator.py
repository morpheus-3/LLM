from langchain_core.prompts import PromptTemplate
# -------- Prompt Template --------
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
Include equations if present and explain simply.

2. Analogies:
Use relatable analogies to simplify complex ideas.

If info not available, say "Insufficient information available".

Ensure clarity and accuracy.
""",
    input_variables=["paper_input", "style_input", "length_input"],
)
template.save('template.json')