import base64
import binascii
from typing import Tuple

class Encoders:
    """Handles various encoding strategies"""
    
    @staticmethod
    def to_base64(text: str) -> str:
        """Convert text to base64 encoding"""
        try:
            return base64.b64encode(text.encode('utf-8')).decode('utf-8')
        except Exception as e:
            raise ValueError(f"Base64 encoding failed: {str(e)}")
    
    @staticmethod
    def from_base64(encoded_text: str) -> str:
        """Decode base64 text"""
        try:
            return base64.b64decode(encoded_text).decode('utf-8')
        except (binascii.Error, UnicodeDecodeError) as e:
            raise ValueError(f"Base64 decoding failed: {str(e)}")
    
    @staticmethod
    def create_semantic_hash(text: str, prefix: str = "CTX") -> Tuple[str, str]:
        """Create a semantic hash reference for text"""
        # Create a simple hash of the content
        hash_value = str(hash(text))[-6:]  # Last 6 digits of hash
        reference = f"{prefix}_{hash_value}"
        return reference, text
