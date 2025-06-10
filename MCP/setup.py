#!/usr/bin/env python3
"""
Setup script for MCP Research Assistant
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def check_ollama():
    """Check if Ollama is installed and running"""
    print("🔍 Checking Ollama installation...")
    
    # Check if ollama command exists
    try:
        subprocess.run(["ollama", "--version"], capture_output=True, check=True)
        print("✅ Ollama is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Ollama is not installed")
        print("💡 Please install Ollama from: https://ollama.ai/")
        return False
    
    # Check if mistral model is available
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
        if "mistral" in result.stdout:
            print("✅ Mistral model is available")
            return True
        else:
            print("❌ Mistral model not found")
            print("💡 Installing mistral model...")
            return run_command("ollama pull mistral", "Installing mistral model")
    except subprocess.CalledProcessError:
        print("❌ Cannot check Ollama models")
        return False

def main():
    print("🚀 Setting up MCP Research Assistant")
    print("="*50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Install Python dependencies
    if not run_command("pip install -r requirements.txt", "Installing Python dependencies"):
        print("💡 Try: python -m pip install -r requirements.txt")
        sys.exit(1)
    
    # Check Ollama
    if not check_ollama():
        print("❌ Ollama setup failed")
        print("💡 Please install Ollama and run: ollama pull mistral")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n🚀 To start the research assistant:")
    print("   python mcp_chatbot.py")
    print("\n📝 Files created:")
    print("   • research_server.py (your existing server)")
    print("   • mcp_chatbot.py (main client)")
    print("   • ollama_client.py (Ollama interface)")
    print("   • requirements.txt (dependencies)")
    print("   • setup.py (this setup script)")

if __name__ == "__main__":
    main()