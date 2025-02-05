from typing import Dict, Any, Optional, Union
from optimizers import (
    TextCompressor,
    StructureConverter,
    Encoders,
    Abbreviator,
    TokenOptimizer
)

class LLMContextOptimizer:
    """Main class for optimizing context for LLMs"""

    def __init__(self):
        self.text_compressor = TextCompressor()
        self.structure_converter = StructureConverter()
        self.encoders = Encoders()
        self.abbreviator = Abbreviator()
        self.token_optimizer = TokenOptimizer()

    def optimize(self, 
                text: str,
                use_compression: bool = True,
                use_abbreviations: bool = True,
                use_base64: bool = False,
                structure_format: Optional[str] = None,
                optimize_tokens: bool = True) -> Dict[str, Any]:
        """
        Optimize text using multiple strategies
        Returns a dictionary with original and optimized versions
        """
        result: Dict[str, Any] = {"original": text}
        current_text = text

        # Apply text compression
        if use_compression:
            current_text = self.text_compressor.remove_redundancies(current_text)
            result["compressed"] = current_text

        # Apply abbreviations
        if use_abbreviations:
            abbreviated_text, used_abbrev = self.abbreviator.abbreviate_text(current_text)
            current_text = abbreviated_text
            # Store both the abbreviated text and the definitions
            result["abbreviated"] = {
                "text": current_text,
                "definitions": {full: abbr for full, abbr in used_abbrev}
            }

        # Apply token optimization
        if optimize_tokens:
            current_text = self.token_optimizer.merge_tokens(current_text)
            current_text = self.token_optimizer.optimize_whitespace(current_text)
            result["token_optimized"] = current_text

        # Convert to structured format
        if structure_format:
            if structure_format.lower() == "json":
                structured = self.structure_converter.create_context_object(
                    topic="context_optimization",
                    keywords=current_text.split()[:5],  # First 5 words as keywords
                    content=current_text
                )
                result["structured"] = self.structure_converter.to_json(structured)
            elif structure_format.lower() == "xml":
                structured = self.structure_converter.create_context_object(
                    topic="context_optimization",
                    keywords=current_text.split()[:5],
                    content=current_text
                )
                result["structured"] = self.structure_converter.to_xml(structured)

        # Apply base64 encoding
        if use_base64:
            result["base64"] = self.encoders.to_base64(current_text)

        # Create semantic hash
        hash_ref, _ = self.encoders.create_semantic_hash(current_text)
        result["semantic_hash"] = hash_ref

        return result