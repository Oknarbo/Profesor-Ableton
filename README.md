# 🎸 Profesor Ableton - AI Copilot for Ableton Live 🎵

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Groq](https://img.shields.io/badge/AI-Groq%20Free-orange.svg)](https://groq.com)

> *"Far out, dude! Your groovy AI assistant for mastering Ableton Live!"* 🌈

**Profesor Ableton** is a groovy AI assistant inspired by the underground comic **Fabulous Furry Freak Brothers**. It helps you learn Ableton Live with psychedelic style and technically accurate advice!

## ✨ Features

### 🧠 **Multi-AI Provider Support**
- **Groq** (FREE & Fast) - Default choice, no limits!
- **xAI Grok** (Paid) - Elon Musk's AI
- **Claude** (Paid) - Anthropic's premium AI  
- **OpenAI** (Paid) - ChatGPT models
- **Ollama** (Local) - Offline LLM models

### 🎨 **Comic Book Interface**
- **Retro 70s colors** inspired by comics
- **Comic Sans font** for authentic vibe
- **System tray integration** - always available
- **Model selector** like Cursor IDE
- **Keyboard shortcuts** (Ctrl+H/S, Escape)

### 🎵 **Ableton Live Expertise**
- **Beginner tutorials** step by step
- **Advanced production** - mixing, mastering, synthesis
- **MIDI & Audio** explanations
- **Plugin usage** - EQ, compressor, reverb, delay
- **Workflow tips** - Session vs Arrangement View

### 💬 **Groovy Personality**
- **Comic book phrases**: "Far out!", "Righteous!", "That's heavy, man!"
- **Laid-back advice** with technically accurate information
- **Underground comic vibe** from the 70s

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+**
- **Internet connection** (for AI APIs)

### 1. Installation
```bash
git clone https://github.com/your-username/profesor-ableton.git
cd profesor-ableton
pip install -r requirements.txt
```

### 2. Get FREE Groq API Key
1. Go to: [console.groq.com/keys](https://console.groq.com/keys)
2. Sign up (FREE, no credit card!)
3. Generate API key
4. Copy your key

### 3. Configuration

**Option A: .env file (Linux/Mac)**
```bash
# Copy template
cp env_example.txt .env

# Edit .env and add your key
GROQ_API_KEY=your_actual_groq_key_here
```

**Option B: Code modification (Windows - if .env doesn't work)**
If you get encoding errors with .env files on Windows:

1. Open `copilot_server.py` 
2. Find line ~63: `groq_key = os.getenv("GROQ_API_KEY")`
3. Replace with: `groq_key = "your_actual_groq_key_here"`

**Why hardcode?** Windows sometimes has .env encoding issues. Direct hardcoding works 100%.

### 4. Launch
**Windows:**
```bash
start_copilot.bat
```

**Linux/Mac:**
```bash
chmod +x start_copilot.sh
./start_copilot.sh
```

**Any Platform:**
```bash
python launch_copilot.py
```

## 🎵 First Questions to Try

```
🔵 You: What is EQ in Ableton?
🤖 Profesor: Far out! EQ is like sculpting your sound frequencies...

🔵 You: How do I make a house beat?
🤖 Profesor: Righteous question! Start with a four-on-the-floor kick...

🔵 You: Best way to record vocals?
🤖 Profesor: Heavy topic, man! First, get a decent mic and audio interface...
```

## 🧠 Switch AI Models

Use the dropdown to switch between:
- **Groq** (FREE & Fast) ⚡
- **Claude** (Paid, needs API key) 💰
- **OpenAI** (Paid, needs API key) 💰
- **xAI Grok** (Paid, needs API key) 💰
- **Ollama** (Local, free but slower) 🏠

## 🎨 GUI Features

- **System Tray** - Always available in taskbar
- **Shortcuts** - Ctrl+H (hide), Ctrl+S (show), Escape (hide)
- **Always on Top** - Checkbox to stay above other windows
- **Question History** - Use Up/Down arrows in input field
- **Model Selector** - Switch AI providers instantly

## 🛠️ Advanced Setup

### Additional AI Providers

#### xAI Grok (Paid)
```bash
# Get API key from https://console.x.ai/
# In copilot_server.py, find line ~45 and replace:
grok_key = "xai-your_key_here"
```

#### Claude (Paid)
```bash  
# Get API key from https://console.anthropic.com/
# In copilot_server.py, find line ~72 and replace:
claude_key = "sk-ant-your_key_here"
```

#### OpenAI (Paid)
```bash
# Get API key from https://platform.openai.com/
# In copilot_server.py, find line ~85 and replace:
openai_key = "sk-your_openai_key_here"
```

#### Ollama (Local/Free)
```bash
# Install Ollama: https://ollama.ai/
ollama serve
ollama pull llama3.1:8b

# In copilot_server.py, model is already configured
```

### Memory Optimization
```bash
# Disable Ollama to save RAM
python disable_ollama.py

# Re-enable later
python enable_ollama.py
```

## ❗ Troubleshooting

### Common Issues

#### "Can't connect to server"
- Make sure only one instance is running
- Try different port by restarting
- Check firewall settings

#### "All AI providers unavailable"
- Check your internet connection
- Verify your Groq API key is correctly added
- Test API key at [console.groq.com](https://console.groq.com)

#### "UnicodeEncodeError" (Windows)
- This is why we recommend hardcoding keys on Windows
- Follow "Option B" in configuration above

#### GUI Window Disappears
- Look for system tray icon
- Use Ctrl+S or click tray icon to show
- Window may be minimized, not closed

## 📊 Performance

### Speed Comparison
- **Groq**: ⚡ 1-2s (FREE!)
- **Claude**: 🐌 3-5s (Paid)
- **OpenAI**: 🐌 2-4s (Paid)  
- **Ollama**: 🐢 5-15s (Local)

### Resource Usage
- **RAM**: ~50MB (without Ollama), ~2GB (with Ollama)
- **CPU**: Minimal during idle
- **Network**: Only for AI requests

## 🎵 What You Can Ask

Profesor Ableton helps with:
- **Ableton Live basics** & advanced techniques
- **Music production workflows**  
- **Plugin usage** (EQ, compressor, reverb, etc.)
- **MIDI & audio editing**
- **Mixing & mastering tips**
- **Creative inspiration**

### Example Questions
- "How do I create automation in Ableton?"
- "What's the difference between Session and Arrangement View?"
- "Best practices for vocal recording?"
- "How to make my kick drum punch through the mix?"
- "Explain sidechain compression like I'm 5"

## 🤝 Contributing

Profesor Ableton is open source! Contributions welcome:

1. **Fork** the repository
2. **Create** feature branch (`git checkout -b groovy-feature`)
3. **Commit** changes (`git commit -am 'Add groovy feature'`)
4. **Push** to branch (`git push origin groovy-feature`)
5. **Create** Pull Request

### Development Ideas
- 🎹 **Max for Live integration** - direct Ableton interface
- 🎵 **MIDI generation** - AI creates musical patterns
- 🎧 **Audio analysis** - AI analyzes your tracks
- 🌍 **More languages** - localization
- 🎨 **Custom themes** - more comic book styles

## 🎸 Philosophy

> *"Music is the universal language, and technology should enhance creativity, not complicate it. Profesor Ableton bridges the gap between human creativity and AI assistance with a groovy, approachable personality that makes learning fun!"*

Inspired by the counterculture spirit of **Fabulous Furry Freak Brothers**, Profesor Ableton combines:
- 🎪 **Fun & Playful** interface
- 🧠 **Serious Technical** knowledge  
- 🌈 **Creative Freedom** in learning
- 🎵 **Music Production** expertise

## 📄 License

MIT License - feel free to fork, modify, and share the groovy vibes!

## 🙏 Acknowledgments

- **Gilbert Shelton** for Fabulous Furry Freak Brothers inspiration
- **Groq** for amazing free AI API
- **Ableton** for the best DAW ever
- **Python community** for fantastic libraries
- **Open source** movement for making this possible

---

**🎸 Keep it groovy, keep it creative! 🎵**

*Made with ❤️ and lots of ☕ by music lovers for music lovers*

## 🚀 Future Roadmap

### v1.1.0 - "Max for Live Integration"
- [ ] Direct Ableton Live integration
- [ ] Real-time project context awareness
- [ ] Smart device suggestions
- [ ] MIDI pattern generation

### v1.2.0 - "Expanded AI Features"  
- [ ] Audio file analysis
- [ ] Voice command support
- [ ] Multiple character personalities
- [ ] Advanced music theory integration

### v1.3.0 - "Community Features"
- [ ] Multi-language support
- [ ] Community question database
- [ ] Mobile companion app
- [ ] Social sharing features

---

**Ready to get groovy with AI music production? Let's rock! 🎸🌈**