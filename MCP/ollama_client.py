import ollama
import json
from typing import List, Dict, Any

class OllamaClient:
    def __init__(self, model: str = "mistral"):
        self.model = model
        self.client = ollama.Client()
        
    def format_tools_for_ollama(self, tools: List[Dict]) -> str:
        """Convert MCP tools format to a string description for Ollama"""
        tool_descriptions = []
        for tool in tools:
            name = tool["name"]
            description = tool["description"]
            schema = tool["input_schema"]
            
            # Extract parameters from schema
            params = []
            if "properties" in schema:
                for param_name, param_info in schema["properties"].items():
                    param_type = param_info.get("type", "string")
                    param_desc = param_info.get("description", "")
                    params.append(f"  - {param_name} ({param_type}): {param_desc}")
            
            params_str = "\n".join(params) if params else "  No parameters"
            
            tool_desc = f"""
Tool: {name}
Description: {description}
Parameters:
{params_str}
"""
            tool_descriptions.append(tool_desc)
        
        return "\n".join(tool_descriptions)
    
    def create_system_prompt(self, tools: List[Dict]) -> str:
        """Create a system prompt that includes tool information"""
        tools_info = self.format_tools_for_ollama(tools)
        
        return f"""You are a research assistant with access to the following tools:

{tools_info}

When you need to use a tool, respond with a JSON object in this exact format:
{{"tool_call": {{"name": "tool_name", "arguments": {{"param1": "value1", "param2": "value2"}}}}}}

When you don't need to use a tool, respond normally with text.

Always be helpful and provide detailed information about research papers when available."""

    def chat(self, message: str, tools: List[Dict], conversation_history: List[Dict] = None) -> Dict[str, Any]:
        """Send a chat message to Ollama"""
        if conversation_history is None:
            conversation_history = []
        
        # Add system message with tools info
        messages = [
            {
                "role": "system", 
                "content": self.create_system_prompt(tools)
            }
        ]
        
        # Add conversation history
        messages.extend(conversation_history)
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        try:
            response = self.client.chat(
                model=self.model,
                messages=messages,
                stream=False
            )
            
            content = response['message']['content'].strip()
            
            # Try to parse if it's a tool call
            try:
                if content.startswith('{') and 'tool_call' in content:
                    parsed = json.loads(content)
                    if 'tool_call' in parsed:
                        return {
                            'type': 'tool_call',
                            'tool_name': parsed['tool_call']['name'],
                            'arguments': parsed['tool_call']['arguments'],
                            'raw_response': content
                        }
            except json.JSONDecodeError:
                pass
            
            return {
                'type': 'text',
                'content': content,
                'raw_response': content
            }
            
        except Exception as e:
            return {
                'type': 'error',
                'content': f"Error communicating with Ollama: {str(e)}",
                'raw_response': str(e)
            }