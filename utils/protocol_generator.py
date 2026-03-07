import ollama
from rag.retriever import retrieve_context
import os

def load_prompt():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(base_dir, "prompts", "protocol_prompt.txt")

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def generate_protocol(condition, phase, intervention, sample_size):

    prompt_template = load_prompt()

    context = retrieve_context(condition)

    prompt = prompt_template.format(
        context=context,
        condition=condition,
        phase=phase,
        intervention=intervention,
        sample_size=sample_size
    )

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"]