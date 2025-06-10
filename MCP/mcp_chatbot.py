import asyncio
import json
import sys
from typing import List, Dict
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from ollama_client import OllamaClient
import nest_asyncio

nest_asyncio.apply()

class MCP_ChatBot:
    def __init__(self, model: str = "mistral"):
        self.session: ClientSession = None
        self.ollama_client = OllamaClient(model)
        self.available_tools: List[Dict] = []
        self.conversation_history: List[Dict] = []

    async def process_query(self, query: str):
        """Process a user query using available MCP tools and Ollama"""
        print(f"\n🤖 Processing: {query}")
        
        # Get response from Ollama
        response = self.ollama_client.chat(
            message=query, 
            tools=self.available_tools,
            conversation_history=self.conversation_history
        )
        
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": query})
        
        if response['type'] == 'error':
            print(f"❌ Error: {response['content']}")
            return
        
        elif response['type'] == 'tool_call':
            tool_name = response['tool_name']
            arguments = response['arguments']
            
            print(f"🔧 Calling tool: {tool_name}")
            print(f"📝 Arguments: {json.dumps(arguments, indent=2)}")
            
            try:
                # Call the MCP tool
                result = await self.session.call_tool(tool_name, arguments=arguments)
                
                print(f"✅ Tool result received")
                
                # Parse the result content
                if hasattr(result, 'content'):
                    if isinstance(result.content, list) and len(result.content) > 0:
                        tool_result = result.content[0].text if hasattr(result.content[0], 'text') else str(result.content[0])
                    else:
                        tool_result = str(result.content)
                else:
                    tool_result = str(result)
                
                # Add tool call and result to conversation history
                self.conversation_history.append({
                    "role": "assistant", 
                    "content": f"I'll use the {tool_name} tool to help you."
                })
                self.conversation_history.append({
                    "role": "user", 
                    "content": f"Tool result: {tool_result}"
                })
                
                # Get Ollama's interpretation of the results
                follow_up_response = self.ollama_client.chat(
                    message=f"Based on the tool result: {tool_result}, please provide a helpful summary and analysis.",
                    tools=self.available_tools,
                    conversation_history=self.conversation_history
                )
                
                if follow_up_response['type'] == 'text':
                    print(f"\n📊 Analysis:")
                    print(follow_up_response['content'])
                    self.conversation_history.append({
                        "role": "assistant", 
                        "content": follow_up_response['content']
                    })
                
            except Exception as e:
                print(f"❌ Error calling tool {tool_name}: {str(e)}")
                
        elif response['type'] == 'text':
            print(f"💬 Response: {response['content']}")
            self.conversation_history.append({
                "role": "assistant", 
                "content": response['content']
            })

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\n" + "="*60)
        print("🔬 MCP Research Assistant with Ollama Mistral")
        print("="*60)
        print("Available tools:")
        for tool in self.available_tools:
            print(f"  • {tool['name']}: {tool['description']}")
        print("\nType your queries or 'quit' to exit.")
        print("Examples:")
        print("  - Search for papers about machine learning")
        print("  - Find papers on quantum computing")
        print("  - Extract info for paper ID 2301.12345")
        print("-"*60)
        
        while True:
            try:
                query = input("\n🎯 Query: ").strip()
                
                if query.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if not query:
                    continue
                    
                await self.process_query(query)
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")

    async def connect_to_server_and_run(self):
        """Connect to MCP server and start the chat loop"""
        print("🚀 Starting MCP Research Assistant...")
        print("📡 Connecting to research server...")
        
        # Create server parameters for stdio connection
        server_params = StdioServerParameters(
            command="python",
            args=["research_server.py"],
            env=None,
        )
        
        try:
            # Launch the server and establish connection
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    self.session = session
                    
                    # Initialize the connection
                    await session.initialize()
                    print("✅ Connected to MCP server")

                    # List available tools from the server
                    response = await session.list_tools()
                    tools = response.tools
                    
                    print(f"🔧 Discovered {len(tools)} tools:")
                    for tool in tools:
                        print(f"  • {tool.name}")
                    
                    # Convert MCP tools to format expected by our client
                    self.available_tools = [{
                        "name": tool.name,
                        "description": tool.description,
                        "input_schema": tool.inputSchema
                    } for tool in tools]

                    # Start the interactive chat loop
                    await self.chat_loop()
                    
        except Exception as e:
            print(f"❌ Failed to connect to server: {str(e)}")
            print("💡 Make sure:")
            print("  1. research_server.py is in the same directory")
            print("  2. All dependencies are installed (pip install -r requirements.txt)")
            print("  3. Ollama is running with mistral model")
            sys.exit(1)


async def main():
    """Main function to run the MCP ChatBot"""
    print("🔍 Checking Ollama connection...")
    
    # Test Ollama connection
    try:
        from ollama_client import OllamaClient
        test_client = OllamaClient()
        test_response = test_client.chat("Hello", [])
        if test_response['type'] == 'error':
            print("❌ Ollama connection failed!")
            print("💡 Make sure Ollama is running and mistral model is installed:")
            print("   ollama pull mistral")
            print("   ollama serve")
            return
        print("✅ Ollama connection successful")
    except Exception as e:
        print(f"❌ Ollama error: {str(e)}")
        print("💡 Install Ollama and pull mistral model:")
        print("   https://ollama.ai/")
        print("   ollama pull mistral")
        return
    
    # Start the chatbot
    chatbot = MCP_ChatBot()
    await chatbot.connect_to_server_and_run()


if __name__ == "__main__":
    asyncio.run(main())