from string import Formatter
from typing import List

from llama_index.llms.base import LLM


def get_template_vars(template_str: str) -> List[str]:
    """Get template variables from a template string."""
    formatter = Formatter()

    return [
        variable_name
        for _, variable_name, _, _ in formatter.parse(template_str)
        if variable_name
    ]


def is_chat_model(llm: LLM) -> bool:
    return llm.metadata.is_chat_model
