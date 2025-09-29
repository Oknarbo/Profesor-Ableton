#!/usr/bin/env python3
"""
🎸 Profesor Ableton - Setup Script 🎵
Groovy installation helper for all platforms!
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def print_groovy(message, emoji="🎵"):
    """Print message with groovy style"""
    print(f"{emoji} {message}")

def run_command(command, description):
    """Run command with groovy feedback"""
    print_groovy(f"Running: {description}...", "⚡")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print_groovy(f"SUCCESS: {description}", "✅")
        return True
    except subprocess.CalledProcessError as e:
        print_groovy(f"ERROR: {description} failed", "❌")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print_groovy("Checking Python version...")
    
    if sys.version_info < (3, 8):
        print_groovy("ERROR: Python 3.8+ required! Far out, man - upgrade your Python!", "❌")
        return False
    
    print_groovy(f"GROOVY: Python {sys.version_info.major}.{sys.version_info.minor} detected", "✅")
    return True

def setup_virtual_environment():
    """Create and activate virtual environment"""
    print_groovy("Setting up virtual environment...")
    
    # Create venv if it doesn't exist
    if not os.path.exists("venv"):
        if not run_command(f"{sys.executable} -m venv venv", "Creating virtual environment"):
            return False
    
    # Get activation script path
    if os.name == 'nt':  # Windows
        activate_script = "venv\\Scripts\\activate.bat"
        pip_path = "venv\\Scripts\\pip"
    else:  # Linux/Mac
        activate_script = "venv/bin/activate"
        pip_path = "venv/bin/pip"
    
    print_groovy(f"Virtual environment ready! Activate with: {activate_script}", "🌟")
    return pip_path

def install_dependencies(pip_path):
    """Install required Python packages"""
    print_groovy("Installing groovy dependencies...")
    
    if not run_command(f"{pip_path} install --upgrade pip", "Upgrading pip"):
        return False
    
    if not run_command(f"{pip_path} install -r requirements.txt", "Installing requirements"):
        return False
    
    print_groovy("All dependencies installed! Righteous!", "🎉")
    return True

def setup_configuration():
    """Setup configuration files"""
    print_groovy("Setting up configuration...")
    
    # Copy env example if .env doesn't exist
    if not os.path.exists(".env"):
        if os.path.exists("env_example.txt"):
            shutil.copy("env_example.txt", ".env")
            print_groovy("Created .env file from template", "📝")
        else:
            # Create basic .env
            with open(".env", "w") as f:
                f.write("# 🎸 Profesor Ableton Configuration 🎵\n")
                f.write("# Add your Groq API key here (get free at: https://console.groq.com/keys)\n")
                f.write("GROQ_API_KEY=your_groq_api_key_here\n")
                f.write("AI_PROVIDERS=groq,fallback\n")
            print_groovy("Created basic .env file", "📝")
    else:
        print_groovy(".env file already exists - keeping your settings", "👍")
    
    return True

def test_installation():
    """Test if installation works"""
    print_groovy("Testing installation...")
    
    try:
        # Test imports
        import socketio
        import tkinter
        print_groovy("Core imports working", "✅")
        
        # Test optional imports
        try:
            import pystray
            print_groovy("System tray support available", "✅")
        except ImportError:
            print_groovy("System tray support not available (optional)", "⚠️")
        
        return True
    except ImportError as e:
        print_groovy(f"Import test failed: {e}", "❌")
        return False

def print_next_steps():
    """Print instructions for next steps"""
    print("\n" + "="*60)
    print_groovy("🎸 INSTALLATION COMPLETE! 🎵", "🎉")
    print("="*60)
    
    print_groovy("Next steps:", "📋")
    print("1. Get FREE Groq API key:")
    print("   → Visit: https://console.groq.com/keys")
    print("   → Register (no credit card needed!)")
    print("   → Copy your API key")
    
    print("\n2. Add API key to .env file:")
    print("   → Open .env in text editor")
    print("   → Replace 'your_groq_api_key_here' with your key")
    
    print("\n3. Launch Profesor Ableton:")
    if os.name == 'nt':  # Windows
        print("   → Double-click: start_copilot.bat")
        print("   → Or run: python launch_copilot.py")
    else:
        print("   → Run: source venv/bin/activate")
        print("   → Then: python launch_copilot.py")
    
    print("\n4. Start grooving!")
    print("   → Ask questions like:")
    print("   → 'How do I make a house beat?'")
    print("   → 'What is sidechain compression?'")
    print("   → 'Best way to mix vocals?'")
    
    print_groovy("Far out! Welcome to the groovy world of AI music production! 🌈", "🎸")

def main():
    """Main setup function"""
    print("="*60)
    print_groovy("🎸 PROFESOR ABLETON SETUP 🎵", "🎸")
    print("="*60)
    print_groovy("Welcome to the groovy setup experience!", "👋")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Setup virtual environment
    pip_path = setup_virtual_environment()
    if not pip_path:
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies(pip_path):
        sys.exit(1)
    
    # Setup configuration
    if not setup_configuration():
        sys.exit(1)
    
    # Test installation
    if not test_installation():
        print_groovy("Installation test failed - but you might still be groovy!", "⚠️")
    
    # Print next steps
    print_next_steps()

if __name__ == "__main__":
    main()
