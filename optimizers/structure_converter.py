import json
import xml.etree.ElementTree as ET
from typing import Dict, Any, Union

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
                else:
                    child.text = str(value)
        
        root = ET.Element(root_name)
        _dict_to_xml(data, root)
        return ET.tostring(root, encoding='unicode', method='xml')
    
    @staticmethod
    def create_context_object(topic: str, keywords: list, content: str) -> Dict[str, Any]:
        """Create a structured context object"""
        return {
            "ctx": {
                "topic": topic,
                "keywords": keywords,
                "content": content
            }
        }
