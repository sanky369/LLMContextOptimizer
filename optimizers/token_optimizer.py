import re
from typing import List, Tuple, Dict, Optional

class TokenOptimizer:
    """Optimizes text for token efficiency"""

    # Common token merge patterns
    TOKEN_PATTERNS = {
        # Technical terms
        r'token ization': 'tokenization',
        r'deep learning': 'deeplearning',
        r'machine learning': 'machinelearning',
        r'data base': 'database',
        r'back end': 'backend',
        r'front end': 'frontend',
        r'neural network': 'neuralnetwork',
        r'micro service': 'microservice',
        r'type script': 'typescript',
        r'java script': 'javascript',
        r'source code': 'sourcecode',
        r'code base': 'codebase',

        # Common programming constructs
        r'if else': 'ifelse',
        r'try catch': 'trycatch',
        r'for each': 'foreach',
        r'call back': 'callback',
        r'middle ware': 'middleware',
        r'name space': 'namespace',

        # ML/AI specific
        r'tensor flow': 'tensorflow',
        r'torch script': 'torchscript',
        r'auto encoder': 'autoencoder',
        r'pre train': 'pretrain',
        r'fine tune': 'finetune',
        r'data set': 'dataset',
        r'meta data': 'metadata'
    }

    @staticmethod
    def merge_tokens(text: str) -> str:
        """Merge common token splits"""
        result = text
        for pattern, replacement in TokenOptimizer.TOKEN_PATTERNS.items():
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        return result

    @staticmethod
    def optimize_whitespace(text: str) -> str:
        """Optimize whitespace for token efficiency"""
        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text)
        # Remove spaces around punctuation
        text = re.sub(r'\s*([,.!?:;])\s*', r'\1 ', text)
        # Remove spaces inside parentheses
        text = re.sub(r'\(\s+', '(', text)
        text = re.sub(r'\s+\)', ')', text)
        # Optimize spaces around quotes
        text = re.sub(r'\s*"\s*([^"]+)\s*"\s*', r'"\1" ', text)
        return text.strip()

    @staticmethod
    def create_semantic_triggers(keywords: List[str], max_repeats: int = 2, 
                               importance_weights: Optional[Dict[str, int]] = None) -> str:
        """
        Create semantic triggers through weighted keyword repetition
        importance_weights: Optional dict mapping keywords to their importance (1-5)
        """
        if importance_weights is None:
            return ' '.join([keyword for keyword in keywords for _ in range(max_repeats)])

        result = []
        for keyword in keywords:
            weight = importance_weights.get(keyword, 1)
            repeats = min(max_repeats * weight, 5)  # Cap at 5 repetitions
            result.extend([keyword] * repeats)

        return ' '.join(result)

    @staticmethod
    def optimize_numbers(text: str) -> str:
        """Optimize number representations"""
        # Convert written numbers to digits
        number_map = {
            'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
            'ten': '10', 'hundred': '100', 'thousand': '1000', 'million': '1M',
            'billion': '1B'
        }

        result = text.lower()
        for word, digit in number_map.items():
            result = re.sub(fr'\b{word}\b', digit, result)

        # Optimize decimal number representation
        result = re.sub(r'(\d+)\.0+\b', r'\1', result)  # Remove trailing zeros
        result = re.sub(r'(\d{4,})', lambda m: f"{float(m.group(1)):.2e}", result)  # Scientific notation for large numbers

        return result

    @staticmethod
    def optimize_code_blocks(code: str) -> str:
        """Optimize code blocks for token efficiency"""
        # Remove comments
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
        code = re.sub(r'"""[\s\S]*?"""', '', code)

        # Minimize whitespace
        code = re.sub(r'\n\s*\n', '\n', code)
        code = re.sub(r'[ \t]+', ' ', code)

        # Shorten common patterns
        replacements = {
            'return ': 'ret ',
            'function': 'fn',
            'lambda ': 'λ ',
            'print(': 'p(',
            'self.': 's.',
            'True': 'T',
            'False': 'F',
            'None': 'N'
        }

        for old, new in replacements.items():
            code = code.replace(old, new)

        return code.strip()