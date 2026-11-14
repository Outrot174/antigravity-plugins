---
name: freellm-proxy
description: Manage the local FreeLLMAPI proxy server for unlimited, free LLM tokens. Provides status checks, server control, unified API key retrieval, model routing, and agent configuration for 87+ free AI providers (328+ models). Use when user asks to start/stop the free LLM proxy, check free models, route completions through free tiers, or configure coding agents with unlimited tokens.
tools: Read, Glob, Grep, Bash
---

# FreeLLMAPI Controller (AGY v2)

Native management and integration of the local FreeLLMAPI proxy gateway, providing OpenAI-compatible endpoints (`/v1`) with 10+ billion monthly free tokens across 87+ AI providers.

---

## 🚀 Quick CLI Control

The proxy service is managed globally via the native `freellm` CLI:

```bash
# Check status and health
freellm status

# Start proxy server (port 3001)
freellm start

# Stop proxy server
freellm stop

# Restart server
freellm restart

# Show unified Bearer API key
freellm key

# View recent service logs
freellm logs

# Test end-to-end chat completion
freellm test
```

---

## 🔌 API & Agent Integration

### Local Endpoints:
- **Base URL:** `http://127.0.0.1:3001/v1`
- **Chat Endpoint:** `http://127.0.0.1:3001/v1/chat/completions`
- **Models Endpoint:** `http://127.0.0.1:3001/v1/models`
- **Dashboard / Keys UI:** `http://localhost:5173` (or local port)
- **Auth Header:** `Authorization: Bearer $(freellm key)`

### Supported Models:
- `model: "auto"` — Automatic smart routing to the fastest, highest-capacity free model available.
- `model: "fusion"` — Parallel multi-model draft generation with referee synthesis.
- `model: "qwen3.8-max"` / `qwen3.8-flash` — High-performance free Alibaba Qwen models.
- `model: "glm-5.3"` / `glm-5.3-flash` — Free Z.ai GLM models.
- `model: "deepseek-v4.1-flash"` — Fast reasoning model.
- `model: "gemini-3.8-flash"` — High-throughput multimodal completions.

---

## 🛠 Connecting External Coding Agents

To connect any external CLI tool or coding agent (Aider, OpenCode, Cursor, Cline) to your free proxy:

### Python OpenAI SDK:
```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:3001/v1",
    api_key="freellmapi-14c821e76ce35574e0fc698fde6da7b8269146b653d355fb",
)

response = client.chat.completions.create(
    model="auto",
    messages=[{"role": "user", "content": "Write a Kotlin coroutine flow."}],
)
print(response.choices[0].message.content)
```

### Curl Direct Call:
```bash
curl -s -X POST "http://127.0.0.1:3001/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(freellm key)" \
  -d '{
    "model": "auto",
    "messages": [{"role": "user", "content": "Hello free world!"}]
  }'
```
