import re

class TextCompressor:
    """Handles text compression through various strategies"""

    @staticmethod
    def remove_redundancies(text: str) -> str:
        """Remove redundant whitespace and common stop words"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text.strip())

        # Common stop words to remove
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'is', 'are', 'was', 'were', 'will', 'would', 'could', 'should'
        }

        words = text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]

        return ' '.join(filtered_words)

    @staticmethod
    def minify_code(code: str) -> str:
        """Minify code by removing comments, whitespace, and shortening names"""
        # Remove single-line comments
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)

        # Remove multi-line comments
        code = re.sub(r'"""[\s\S]*?"""', '', code)
        code = re.sub(r"'''[\s\S]*?'''", '', code)

        # Remove empty lines and extra whitespace
        code = re.sub(r'\n\s*\n', '\n', code)
        code = re.sub(r'[ \t]+', ' ', code)

        # Shorten common keywords and patterns
        replacements = {
            'return ': 'r ',
            'def ': 'd ',
            'class ': 'c ',
            'self.': 's.',
            'print(': 'p(',
            'True': 'T',
            'False': 'F',
            'None': 'N',
            ' and ': '&',
            ' or ': '|',
            'lambda ': 'λ',
        }

        for old, new in replacements.items():
            code = code.replace(old, new)

        return code.strip()

    @staticmethod
    def pseudo_url_references(text: str) -> str:
        """Replace long phrases with pseudo-URL references"""
        # Define patterns and their pseudo-URLs
        url_patterns = {
            r'context window size': '#ref:llm/context_size',
            r'token optimization': '#ref:llm/token_opt',
            r'natural language processing': '#ref:nlp/overview',
            r'machine learning model': '#ref:ml/models',
            r'neural network architecture': '#ref:nn/arch',
            r'training data': '#ref:ml/data',
            r'model parameters': '#ref:model/params'
        }

        result = text
        for pattern, url in url_patterns.items():
            result = re.sub(pattern, url, result, flags=re.IGNORECASE)

        return result

    @staticmethod
    def to_markdown(text: str) -> str:
        """Convert text to minimal markdown format"""
        # Convert headers
        text = re.sub(r'^(.+?)\n={3,}', r'# \1', text, flags=re.MULTILINE)
        text = re.sub(r'^(.+?)\n-{3,}', r'## \1', text, flags=re.MULTILINE)

        # Convert bold
        text = re.sub(r'\*\*(.+?)\*\*', r'**\1**', text)

        # Convert lists
        text = re.sub(r'^\s*[\-\*]\s+', '- ', text, flags=re.MULTILINE)

        return text.strip()