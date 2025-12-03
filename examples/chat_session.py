"""
Chat Session Example
Demonstrates a multi-turn conversation with context management.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm.claude_client import ClaudeClient
from src.utils.logger import setup_logger
from src.utils.cache import Cache

class ChatSession:
    """Manages a conversation session with context."""
    
    def __init__(self, client, use_cache=True):
        self.client = client
        self.conversation_history = []
        self.cache = Cache() if use_cache else None
        self.logger = setup_logger("chat_session")
    
    def send_message(self, user_message: str) -> str:
        """Send a message and get a response."""
        
        # Check cache first
        cache_key = f"chat_{hash(str(self.conversation_history) + user_message)}"
        
        if self.cache:
            cached_response = self.cache.get(cache_key)
            if cached_response:
                self.logger.info("📦 Using cached response")
                return cached_response
        
        # Build context from conversation history
        context = "\n".join([
            f"User: {msg['user']}\nAssistant: {msg['assistant']}"
            for msg in self.conversation_history
        ])
        
        # Create full prompt with context
        full_prompt = f"{context}\nUser: {user_message}\nAssistant:" if context else user_message
        
        # Generate response
        self.logger.info(f"💬 User: {user_message}")
        response = self.client.generate(
            full_prompt,
            temperature=0.8,
            max_tokens=300
        )
        
        # Store in conversation history
        self.conversation_history.append({
            "user": user_message,
            "assistant": response
        })
        
        # Cache the response
        if self.cache:
            self.cache.set(cache_key, response)
        
        self.logger.info(f"🤖 Assistant: {response[:100]}...")
        
        return response
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
        self.logger.info("🗑️  Conversation history cleared")

def main():
    logger = setup_logger("chat_example")
    logger.info("Starting chat session example...")
    
    # Initialize Claude client
    client = ClaudeClient(model="claude-3-opus-20240229")
    
    # Create chat session
    chat = ChatSession(client, use_cache=True)
    
    # Simulate a conversation
    conversation = [
        "Hi! I'm learning about Python. Can you help me?",
        "What's the difference between a list and a tuple?",
        "Can you show me an example of when to use a tuple?",
        "Thanks! That was helpful."
    ]
    
    print("\n" + "="*60)
    print("💬 CHAT SESSION DEMO")
    print("="*60 + "\n")
    
    for message in conversation:
        print(f"\n👤 You: {message}")
        response = chat.send_message(message)
        print(f"\n🤖 Assistant: {response}\n")
        print("-" * 60)
    
    # Show conversation stats
    logger.info(f"\n📊 Conversation stats:")
    logger.info(f"   Total messages: {len(chat.conversation_history)}")
    
    print("\n✅ Chat session example completed!")

if __name__ == "__main__":
    main()
