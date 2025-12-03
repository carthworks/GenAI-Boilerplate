# 📚 Examples

This directory contains practical examples demonstrating the key features of the GenAI Boilerplate.

## 🚀 Available Examples

### 1. **basic_completion.py**
Simple text generation using OpenAI GPT.

**Features:**
- Basic prompt-response pattern
- Token counting
- Error handling
- Logging

**Run:**
```bash
python examples/basic_completion.py
```

---

### 2. **chat_session.py**
Multi-turn conversation with context management.

**Features:**
- Conversation history tracking
- Context-aware responses
- Response caching
- Using Claude client

**Run:**
```bash
python examples/chat_session.py
```

---

### 3. **rate_limited_batch.py**
Batch processing with rate limiting.

**Features:**
- Rate limiting (3 calls per 10 seconds)
- Batch processing
- Cache utilization
- Performance metrics

**Run:**
```bash
python examples/rate_limited_batch.py
```

---

### 4. **multi_provider_comparison.py**
Compare responses from different LLM providers.

**Features:**
- Multi-provider support (OpenAI + Claude)
- Response comparison
- Performance benchmarking
- Token usage tracking

**Run:**
```bash
python examples/multi_provider_comparison.py
```

---

## ⚙️ Prerequisites

Before running examples, ensure you have:

1. **Installed dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configured API keys** in `.env`:
   ```
   OPENAI_API_KEY=sk-...
   ANTHROPIC_API_KEY=sk-ant-...
   ```

3. **Run from project root:**
   ```bash
   # From the project root directory
   python examples/basic_completion.py
   ```

---

## 📝 Example Output

### Basic Completion
```
📝 Response 1:
A Large Language Model is an AI system trained on vast amounts of text data...

Total tokens used: 156
```

### Chat Session
```
👤 You: What's the difference between a list and a tuple?

🤖 Assistant: In Python, lists are mutable (can be changed) while tuples are immutable...
```

### Rate Limited Batch
```
⚡ RATE LIMITED BATCH PROCESSING
Processing 8 prompts with rate limit: 3 calls/10 sec

[1/8] Processing: What is machine learning?
✅ Response: Machine learning is a subset of artificial intelligence...
```

---

## 🎯 Learning Path

**Recommended order:**
1. Start with `basic_completion.py` to understand the basics
2. Try `chat_session.py` to see context management
3. Run `rate_limited_batch.py` to learn about rate limiting
4. Explore `multi_provider_comparison.py` for advanced usage

---

## 🔧 Customization

Feel free to modify these examples:
- Change the prompts
- Adjust temperature and max_tokens
- Switch between GPT-4 and GPT-3.5
- Try different Claude models
- Modify rate limits

---

## 💡 Tips

- **Check logs:** All examples write to `logs/app.log`
- **Use cache:** The cache saves API costs on repeated requests
- **Monitor tokens:** Keep track of token usage to manage costs
- **Error handling:** Examples include robust error handling patterns

---

## 🐛 Troubleshooting

**API Key Error:**
```
OpenAI API key not found. Please set OPENAI_API_KEY environment variable.
```
→ Make sure your `.env` file is configured correctly.

**Import Error:**
```
ModuleNotFoundError: No module named 'src'
```
→ Run examples from the project root directory.

**Rate Limit Error:**
```
Rate limit reached. Sleeping for X seconds.
```
→ This is expected behavior. The rate limiter is working correctly.

---

## 📚 Next Steps

After exploring these examples:
- Check out the Jupyter notebooks in `notebooks/`
- Read the main [README.md](../README.md)
- Build your own application using the boilerplate
- Explore prompt engineering in `src/prompt_engineering/`

---

**Happy coding! 🚀**
