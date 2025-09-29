import socketio
import json

# Create SocketIO client for testing
sio = socketio.SimpleClient()

def test_ai_copilot():
    try:
        # Connect to server
        sio.connect('http://localhost:12345')
        print("✅ Connected to Ableton AI Copilot!")
        
        # Test questions
        test_questions = [
            {"action": "ask_ai", "params": {"question": "What is EQ in Ableton?"}},
            {"action": "ableton_help", "params": {"topic": "compressor"}},
            {"action": "ask_ai", "params": {"question": "How to make a bass line?"}},
            {"action": "explain_midi", "params": {}}
        ]
        
        for i, cmd in enumerate(test_questions, 1):
            print(f"\n🔄 Test {i}: {cmd['action']}")
            
            # Send command
            sio.emit('command', cmd)
            
            # Wait for response (timeout 10s)
            response = sio.receive(timeout=10)
            if response:
                event, data = response
                if event == 'response':
                    print(f"📩 Response: {data.get('message', 'No response')}")
                else:
                    print(f"❓ Unexpected event: {event}")
            else:
                print("⏰ Timeout - no response")
        
        sio.disconnect()
        print("\n✅ Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🤖 Testing Ableton AI Copilot...")
    print("First run: python copilot_server.py")
    input("Press Enter when server is ready...")
    test_ai_copilot()

