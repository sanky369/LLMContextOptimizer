import json
import xml.etree.ElementTree as ET
from typing import Dict, Any, Union, List, Optional

class StructureConverter:
    """Converts text to structured formats like JSON and XML"""

    @staticmethod
    def to_json(data: Dict[str, Any]) -> str:
        """Convert dictionary to minimal JSON"""
        return json.dumps(data, separators=(',', ':'))

    @staticmethod
    def from_json(json_str: str) -> Dict[str, Any]:
        """Parse JSON string to dictionary"""
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {str(e)}")

    @staticmethod
    def to_xml(data: Dict[str, Any], root_name: str = "root") -> str:
        """Convert dictionary to minimal XML"""
        def _dict_to_xml(data: Dict[str, Any], parent: ET.Element):
            for key, value in data.items():
                child = ET.SubElement(parent, str(key))
                if isinstance(value, dict):
                    _dict_to_xml(value, child)
                elif isinstance(value, list):
                    for item in value:
                        item_elem = ET.SubElement(child, "item")
                        item_elem.text = str(item)
                else:
                    child.text = str(value)

        root = ET.Element(root_name)
        _dict_to_xml(data, root)
        return ET.tostring(root, encoding='unicode', method='xml')

    @staticmethod
    def create_context_object(topic: str, 
                            keywords: List[str], 
                            content: str,
                            semantic_triggers: Optional[str] = None) -> Dict[str, Any]:
        """Create a structured context object with semantic optimization"""
        context = {
            "ctx": {
                "topic": topic,
                "keywords": keywords,
                "content": content
            }
        }

        if semantic_triggers:
            context["ctx"]["semantic_triggers"] = semantic_triggers

        return context