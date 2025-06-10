# MCP Research Assistant with Ollama Mistral

A complete Model Context Protocol (MCP) client-server setup for research paper discovery and analysis using Ollama's Mistral model.

## 🌟 Features

- **Paper Search**: Search arXiv for research papers by topic
- **Paper Information**: Extract detailed information about specific papers
- **Local AI**: Uses Ollama Mistral model (runs locally, no API keys needed)
- **MCP Protocol**: Follows standard MCP client-server architecture
- **Interactive Chat**: Natural language interface for research queries

## 📋 Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running

## 🚀 Quick Start

### 1. Install Ollama
```bash
# Visit https://ollama.ai/ to install Ollama for your system
# Then pull the Mistral model:
ollama pull mistral
```

### 2. Set Up the Project
```bash
# Clone or download all the files to a directory
# Make sure you have these files:
# - research_server.py (your existing server)
# - mcp_chatbot.py
# - ollama_client.py
# - requirements.txt
# - setup.py

# Run the setup script
python setup.py
```

### 3. Start the Assistant
Run the MCP server
```bash
mcp dev research_server.py
```
Access the server Url and click on "Connect" <br>
Run the Ollama server
```bash
ollama run mistral
```
Run the application
```bash
python mcp_chatbot.py
```

## 📁 Project Structure

```
mcp-research-assistant/
├── research_server.py      # MCP server with arXiv tools
├── mcp_chatbot.py         # Main client application
├── ollama_client.py       # Ollama interface wrapper
├── requirements.txt       # Python dependencies
├── setup.py              # Automated setup script
├── README.md             # This file
└── papers/               # Created automatically for storing papers
```

## 🎯 Usage Examples

Once the chatbot is running, try these queries:

```
🎯 Query: Search for papers about machine learning

🎯 Query: Find recent papers on quantum computing

🎯 Query: What are the latest developments in natural language processing?

🎯 Query: Extract information about paper ID 2301.12345
```

## 🔧 Available Tools

The research server provides these MCP tools:

- **search_papers**: Search arXiv by topic and store paper information
- **extract_info**: Get detailed information about a specific paper by ID

## 🛠️ Manual Installation

If the setup script doesn't work, install manually:

```bash
# Install Python dependencies
pip install arxiv fastmcp mcp ollama python-dotenv nest-asyncio typing-extensions

# Install and setup Ollama
# Visit https://ollama.ai/ for installation instructions
ollama pull mistral
ollama serve  # Start Ollama server
```

## 🐛 Troubleshooting

### Ollama Issues
- **Error**: "Ollama connection failed"
  - **Solution**: Make sure Ollama is running: `ollama serve`
  - **Solution**: Install mistral model: `ollama pull mistral`

### Server Connection Issues
- **Error**: "Failed to connect to server"
  - **Solution**: Ensure `research_server.py` is in the same directory
  - **Solution**: Check that all dependencies are installed

### Import Errors
- **Error**: Module not found
  - **Solution**: Install missing packages: `pip install -r requirements.txt`

## 🔄 How It Works

1. **MCP Server** (`research_server.py`): Provides tools for arXiv paper search and information extraction
2. **MCP Client** (`mcp_chatbot.py`): Connects to the server and manages the conversation flow
3. **Ollama Client** (`ollama_client.py`): Interfaces with the local Mistral model for natural language understanding
4. **User Interface**: Interactive command-line chat interface

## 🌐 Architecture

```
User Input → Ollama Mistral → Tool Decision → MCP Server → arXiv API
     ↑                                            ↓
User Output ← Ollama Analysis ← Tool Results ← Paper Data
```

## 📝 Configuration

The system uses these default settings:
- **Model**: Ollama Mistral
- **Max Results**: 5 papers per search
- **Storage**: Local `papers/` directory
- **Transport**: stdio (standard input/output)

## 🤝 Contributing

Feel free to enhance the system by:
- Adding more research databases
- Implementing paper download features
- Adding visualization capabilities
- Improving the conversation flow

## 📄 License

This project is open source. Use and modify as needed for your research purposes.

---

**Happy Researching! 🔬📚**