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
        """Minify code by removing comments and unnecessary whitespace"""
        # Remove single-line comments
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
        
        # Remove multi-line comments
        code = re.sub(r'"""[\s\S]*?"""', '', code)
        
        # Remove empty lines
        code = re.sub(r'\n\s*\n', '\n', code)
        
        # Remove trailing whitespace
        code = re.sub(r'\s+$', '', code, flags=re.MULTILINE)
        
        return code.strip()
    
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
