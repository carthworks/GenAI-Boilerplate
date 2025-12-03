
# ⚡ GenAI Boilerplate

A clean, production-ready template for building robust Generative AI applications with modular architecture, multi-LLM support, caching, rate limiting, error handling, and prompt engineering utilities.

![GenAI Project](https://github.com/honestsoul/generative_ai_project/blob/96dae125f58ede47f1bc3034790498f103903772/examples/genai_project.jpg)

---

## 🚀 Core Features

* **Modular Architecture** (clear separation of LLM clients, prompts, utilities)
* **Multi-Provider Support**: OpenAI (GPT) + Anthropic (Claude)
* **Built-In Tools**

  * Prompt templates & chaining
  * Rate limiting
  * Token counting
  * Local caching
  * Centralized logging
* **Robust Error Handling** with exponential backoff
* **Type-Safe Python code** with full type hints
* **Examples + Jupyter Notebooks** ready to run

---

## 📁 Project Structure

```
generative_ai_project/
├── config/
│   ├── model_config.yaml
│   ├── prompt_templates.yaml
│   └── logging_config.yaml
│
├── src/
│   ├── llm/
│   │   ├── base.py
│   │   ├── openai_client.py
│   │   ├── claude_client.py
│   │   └── utils.py
│   │
│   ├── prompt_engineering/
│   │   ├── templates.py
│   │   ├── few_shot.py
│   │   └── chain.py
│   │
│   ├── utils/
│   │   ├── rate_limiter.py
│   │   ├── token_counter.py
│   │   ├── cache.py
│   │   └── logger.py
│   │
│   └── handlers/error_handler.py
│
├── data/
├── examples/
├── notebooks/
├── logs/
├── test_setup.py
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## ⚙️ Installation

### Prerequisites

* Python **3.8+**
* API keys for OpenAI / Anthropic

### Setup

```bash
git clone https://github.com/carthworks/GenAI-Boilerplate.git
cd generative_ai_project
```

Create a virtual environment:

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment:

```bash
cp .env.example .env
# Add your API keys inside .env
```

Verify:

```bash
python test_setup.py
```

Expected:

```
✅ All components verified successfully!
```

---

## 🔥 Quick Usage Examples

### 1. OpenAI GPT

```python
from src.llm.openai_client import OpenAIClient

client = OpenAIClient(model="gpt-4o")
resp = client.generate("Explain quantum computing simply.")
print(resp)
```

### 2. Anthropic Claude

```python
from src.llm.claude_client import ClaudeClient

client = ClaudeClient(model="claude-3-opus-20240229")
print(client.generate("Write a haiku about AI."))
```

### 3. Cache

```python
from src.utils.cache import Cache
cache = Cache()
cache.set("key", "value")
print(cache.get("key"))
```

### 4. Rate Limiting

```python
from src.utils.rate_limiter import limit_calls

@limit_calls(max_calls=5, period=60)
def api_call():
    pass
```

---

## 🧠 Configuration

### `config/model_config.yaml`

```yaml
openai:
  default_model: "gpt-4o"
  api_key: "${OPENAI_API_KEY}"

anthropic:
  default_model: "claude-3-opus-20240229"
  api_key: "${ANTHROPIC_API_KEY}"
```

### `.env`

```
OPENAI_API_KEY=sk-xxxx
ANTHROPIC_API_KEY=sk-ant-xxxx
LOG_LEVEL=INFO
```

---

## 🛠 Development Details

### LLM Clients (`src/llm`)

* Abstract interface (`base.py`)
* GPT + Claude implementations
* Token counting
* Sync + async generation
* Automatic retries & backoff

### Prompt Engineering (`src/prompt_engineering`)

* Template loader
* Few-shot builder
* Prompt chaining

### Utilities (`src/utils`)

* Rate limiting
* Token counting
* File-based caching
* Centralized logging

### Adding a New LLM Provider

1. Create a new class in `src/llm/`
2. Inherit from `BaseLLMClient`
3. Implement `generate()`, `generate_async()`, and `get_token_count()`

---

## 🧪 Testing

```bash
python test_setup.py
```

Checks:

* Imports
* Client initialization
* Cache operations
* Rate limiter

---

## 📊 Logging

Logs stored in `logs/app.log`:

* Timestamp
* Log level
* Module + Line
* Message

View logs:

```bash
cat logs/app.log
```

---

## 🤝 Contributing

1. Fork
2. Create a feature branch
3. Commit + push
4. Open a PR

---

## 📄 License

MIT License.
See `LICENSE`.

---

## 👤 Author

**Brij Kishore Pandey**
GitHub: [https://github.com/carthworks](https://github.com/carthworks/GenAI-Boilerplate)
Email: [tkarthikeyan@gmail.com](mailto:tkarthikeyan@gmail.com)

---

## ⭐ Useful References

* [https://platform.openai.com/docs](https://platform.openai.com/docs)
* [https://docs.anthropic.com](https://docs.anthropic.com)
* [https://www.promptingguide.ai](https://www.promptingguide.ai)

