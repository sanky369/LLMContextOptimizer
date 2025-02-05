import re
from typing import Dict, List, Tuple

class Abbreviator:
    """Handles text abbreviation and shorthand conversion"""

    # Extended common abbreviations dictionary with more domain-specific terms
    COMMON_ABBREV = {
        "natural language processing": "NLP",
        "machine learning": "ML",
        "artificial intelligence": "AI",
        "neural network": "NN",
        "deep learning": "DL",
        "reinforcement learning": "RL",
        "computer vision": "CV",
        "return on investment": "ROI",
        "rectified linear unit": "ReLU",
        "large language model": "LLM",
        "transformer model": "TFM",
        "attention mechanism": "ATT",
        "convolutional neural network": "CNN",
        "recurrent neural network": "RNN",
        "natural language understanding": "NLU",
        "natural language generation": "NLG",
        "question answering": "QA",
        "information retrieval": "IR",
        "named entity recognition": "NER",
        "part of speech": "POS",
        "retrieval augmented generation": "RAG",
        "knowledge base": "KB",
        "sequence to sequence": "Seq2Seq"
    }

    def __init__(self):
        self.custom_abbrev = {}

    def add_abbreviation(self, full_text: str, abbrev: str):
        """Add a custom abbreviation"""
        self.custom_abbrev[full_text.lower()] = abbrev

    def get_abbreviations(self) -> Dict[str, str]:
        """Get all abbreviations (common + custom)"""
        return {**self.COMMON_ABBREV, **self.custom_abbrev}

    def abbreviate_text(self, text: str) -> Tuple[str, List[Tuple[str, str]]]:
        """
        Abbreviate text using known abbreviations
        Returns: (abbreviated_text, list of used abbreviations)
        """
        used_abbrev = []
        result = text

        # Sort by length (descending) to handle longer phrases first
        sorted_abbrev = sorted(self.get_abbreviations().items(), 
                             key=lambda x: len(x[0]), 
                             reverse=True)

        for full_text, abbrev in sorted_abbrev:
            pattern = re.compile(re.escape(full_text), re.IGNORECASE)
            if pattern.search(result):
                result = pattern.sub(abbrev, result)
                used_abbrev.append((full_text, abbrev))

        return result, used_abbrev

    @staticmethod
    def create_abbreviation_header(used_abbrev: List[Tuple[str, str]]) -> str:
        """Create a header with abbreviation definitions"""
        if not used_abbrev:
            return ""

        header = "Abbreviations used:\n"
        # Sort alphabetically by abbreviation for better readability
        sorted_abbrev = sorted(used_abbrev, key=lambda x: x[1])
        for full_text, abbrev in sorted_abbrev:
            header += f"{abbrev}: {full_text}\n"

        return header