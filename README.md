# 🚀 Antigravity Plugins & Skills Pack (AGY v2)

Коллекция нативных, адаптированных и очищенных плагинов, скиллов и MCP-коннекторов для **Google Antigravity (AGY v2)** на платформе **Android ARM64 / Linux**.

Все плагины в этом репозитории спроектированы под реальную среду Android-устройства (POCO F7 Ultra, Snapdragon 8 Elite, HyperOS 3.0):
- ❌ **Без Docker и bwrap:** 100% совместимость с native Android userspace.
- ❌ **Без спама в контекст:** удалены принудительные токсичные правила и раздутые prompt-файлы.
- ✅ **Нативная интеграция:** поддержка elevated ADB (`uid=2000`), фонового планировщика `agy-daemon`, Three.js WebGL, FFmpeg, SQLite, Jetpack Compose, Python CLI и долговременной памяти MCP.

---

## 📦 Каталог плагинов (16 плагинов)

| Плагин | Скилл | Назначение |
| :--- | :--- | :--- |
| **`token-optimizer`** | `token-efficiency-craft` | **Экономия токенов и сжатие контекста:** фильтрация вывода терминала (logcat, git diff, grep), чтение файлов по узким диапазонам строк (`StartLine`/`EndLine`), хирургические точечные правки (`replace_file_content`), маскирование наблюдений и устранение разговорного шума. |
| **`freellm-manager`** | `freellm-proxy` | **Шлюз бесплатных LLM-моделей (FreeLLMAPI):** управление локальным прокси-сервером на 87 провайдеров и 328+ бесплатных моделей через CLI `freellm` (start/stop/restart/status/key/test) и OpenAI-совместимый эндпоинт `http://127.0.0.1:3001/v1`. |
| **`python-artisan`** | `python-artisan` | Архитектура автономных Python CLI-утилит под Android userspace: zero-dependency шаблоны, управление путями и шебангами (`agy-fix-paths`), интеграция с Google AI Studio / Gemini API (`google_ai.json`) и обход ограничений `noexec`. |
| **`kotlin-compose`** | `kotlin-compose-expert` | Стандарты современной разработки под Android: Kotlin Coroutines, Jetpack Compose UDF, `StateFlow`, оптимизация рекомпозиций (`@Immutable`, `@Stable`, Lazy-ключи), Material 3 и Edge-to-Edge для Android 16 (SDK 36). |
| **`android-adb-toolkit`** | `android-adb-toolkit` | Разработка и отладка Android: фильтрация logcat (крэши, fatal), управление APK (`pm install -r`), активности (`am start`), память, батарея и доступ к защищенным директориям через нативный ADB loopback. |
| **`media-toolkit`** | `ffmpeg-media-craft` | Процессинг аудио и видео через нативный `$PREFIX/bin/ffmpeg`: сжатие H.264, мгновенная нарезка без перекодирования (`-c copy`), извлечение кадров/аудио и создание высококачественных палитровых GIF. |
| **`api-tester`** | `api-tester` | Тестирование REST API, HTTP-эндпоинтов, вебхуков и WebSockets: замеры задержки (TTFB, DNS, TLS), валидация JSON-схем и многопоточные бенчмарки на чистом Python. |
| **`threejs-3d-craft`** | `threejs-3d-craft` | Процедурная генерация 3D моделей (Wavefront OBJ, STL, GLTF) в `/storage/emulated/0/Antigravity/3д модели/` и рендеринг интерактивных сцен Three.js через Generative UI прямо в чате. |
| **`security-audit`** | `security-auditor` | Автономный аудит безопасности кода без Docker: OWASP Top 10, утечки API-токенов/ключей, инспекция `AndroidManifest.xml` (exported компоненты, cleartext HTTP, insecure storage). |
| **`sqlite-inspector`** | `sqlite-inspector` | Быстрое исследование локальных баз данных SQLite и Room (схемы таблиц, целостность, выборки данных, миграции) через нативный Python `sqlite3`. |
| **`git-workflow`** | `git-workflow` | Стандарты Conventional Commits, генерация release tags, оформление PR и автоматическое решение проблем с `dubious ownership` на разделах Android shared storage. |
| **`prompt-architect`** | `prompt-architect` | Проектирование системных промптов, мета-промптов с XML-структурой и шаблонов few-shot. Сохранение шаблонов в `/storage/emulated/0/Antigravity/промты/`. |
| **`agy-automation`** | `agy-automation-recommender` | Анализирует кодовую базу любого проекта и рекомендует кастомизации под Antigravity AGY v2 (скиллы `.agents/skills/`, правила `AGENTS.md`, демоны `agy-daemon`, команды ADB). |
| **`google-antigravity`** | `google-antigravity` | Стандарты планирования Google Antigravity (`implementation_plan.md`, `walkthrough.md`) и дизайн-система Google AI Studio (палитры, микроанимации, стекломорфизм). |
| **`karpathy-skills`** | `karpathy-guidelines` | Принципы Андрея Карпатого: хирургические правки, минимализм, отказ от лишних спекулятивных абстракций и верификация кода тестами. |
| **`agent-reach`** | `agent-reach` | Чтение и поиск по открытым данным соцсетей (GitHub, Reddit, Twitter/X, Bilibili, YouTube) без API-ключей. |

---

## ⚡ FreeLLMAPI (Локальный шлюз бесплатных моделей)

FreeLLMAPI агрегирует 87 провайдеров и предоставляет 328+ бесплатных моделей через единый локальный OpenAI-совместимый интерфейс.

### Управление через CLI `freellm`
```bash
freellm status   # Проверка статуса, порта и PID сервиса
freellm start    # Запуск фонового демона FreeLLMAPI
freellm stop     # Остановка сервиса
freellm restart  # Перезапуск сервиса
freellm key      # Просмотр активного единого API-ключа
freellm logs     # Просмотр последних логов сервера
freellm test     # Экспресс-тест эндпоинта /v1/chat/completions
```

### Настройки подключения
- **Base URL:** `http://127.0.0.1:3001/v1`
- **Port:** `3001` (изолирован от системных портов Antigravity `45157`/`45158`)
- **Формат запросов:** Стандартный OpenAI Chat Completions API (`POST /v1/chat/completions`)
- **Популярные модели:** `auto`, `fusion`, `glm-5.3`, `qwen3.8-max`, `deepseek-chat`, `gpt-4o-mini`

---

## 🔌 Нативные и облачные MCP-коннекторы (Без Docker)

Конфигурационный файл: `~/.gemini/config/mcp_config.json` (шаблон в `config-templates/mcp_config.json`).
Оптимальный набор из 7 серверов (строго в рамках рекомендуемого лимита 4–7 серверов для экономии токенов):

| Сервер | Тип / Среда | Назначение |
| :--- | :--- | :--- |
| **`sequential-thinking`** | Node.js (локально) | Динамические цепочки логических рассуждений (Dynamic Thought Chains), перепроверка архитектуры и пошаговый поиск багов. |
| **`context7`** | HTTPS / Remote SSE | Подгрузка актуальной документации библиотек в реальном времени (без устаревших методов и галлюцинаций API). |
| **`android-adb`** | Python 3 (локально) | Моментальная диагностика крэшей Android (`adb_crash_analyzer`), управление пакетами и системные метрики устройства. |
| **`github-mcp-server`** | Node.js (`npx`) | Управление репозиториями, коммитами, PR и issues через GitHub REST/GraphQL API. |
| **`memory-mcp-server`** | Node.js (`npx`) | Граф долговременной памяти и сущностей между сессиями диалога. |
| **`filesystem-mcp-server`** | Node.js (`npx`) | Безопасная работа с файловой структурой `/storage/emulated/0/Antigravity`. |
| **`higgsfield`** | HTTPS / Remote SSE | Облачный коннектор для генерации медиа и видео. |

```json
{
  "mcpServers": {
    "higgsfield": {
      "url": "https://mcp.higgsfield.ai/mcp",
      "headers": {
        "Authorization": "Key YOUR_HIGGSFIELD_KEY_HERE"
      }
    },
    "context7": {
      "url": "https://mcp.context7.com/mcp"
    },
    "github-mcp-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_TOKEN_HERE"
      }
    },
    "memory-mcp-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem-mcp-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/storage/emulated/0/Antigravity"]
    },
    "sequential-thinking": {
      "command": "node",
      "args": ["/data/user/0/com.agy/files/usr/bin/mcp-server-sequential-thinking"]
    },
    "android-adb": {
      "command": "python",
      "args": ["/data/user/0/com.agy/files/services/adb-mcp/server.py"]
    }
  }
}
```

---

## 🤖 Специализированный штат субагентов (12 агентов)

В репозитории спроектирована и задокументирована команда из 12 узкоспециализированных ИИ-субагентов, работающих по принципу единственной ответственности (SRP) в изолированных контекстных окнах.

Подробное описание ролей, системных промптов и параметров вызова: [Каталог субагентов](agents/README.md).

- 🎬 `video-creator` — генерация видео (Google Veo 3.1 & Higgsfield)
- 🎨 `image-artist` — генерация 1K/2K/4K графики (Google Nano Banana & Gemini Image)
- 🧠 `prompt-architect` — проектирование XML-промптов и ролевых шаблонов
- 📐 `3d-craft-engineer` — процедурные 3D-сетки (OBJ, STL, `numpy-stl`, WebGL)
- 📱 `android-developer` — архитектура Kotlin Coroutines, Jetpack Compose, Room, ADB
- 🐍 `python-web-developer` — автономные CLI-утилиты, демоны `agy-daemon`
- 🛡️ `qa-security-auditor` — Read-Only аудит безопасности OWASP, утечек ключей и тестов
- 📝 `docs-historian` — документация, чейнджлоги и релизы на GitHub
- 🌐 `i18n-localizer` — русская локализация и AST-словари (`antigravity-ru`)
- 🎮 `game-developer` — мультиплатформенный геймдев (Kotlin SurfaceView/OpenGL, HTML5 Canvas/WebGL, физика)
- 📊 `graphics-engine-specialist` — математика и оптимизация отрисовки графиков (`grafik`)
- 🐧 `android-env-architect` — управление средой Android userspace, `pkg`, ARM64, `noexec`

---

## 📱 Стандарты изоляции хранилища Android

Все создаваемые агентом данные сохраняются строго в изолированные разделы:
- `/storage/emulated/0/Antigravity/программы/` — проекты и код
- `/storage/emulated/0/Antigravity/3д модели/` — 3D модели (OBJ, STL, GLTF)
- `/storage/emulated/0/Antigravity/промты/` — готовые системные промпты
- `/storage/emulated/0/Antigravity/изображения/` — сгенерированные арты и кадры
- `/storage/emulated/0/Antigravity/видео/` — видеоматериалы (Google Veo, клипы)
- `/storage/emulated/0/Antigravity/песочница/` — дампы и временные тесты

---

## 👤 Автор

**Outrot174** (GitHub: [Outrot174](https://github.com/Outrot174))  
Репозиторий проекта: [https://github.com/Outrot174/antigravity-plugins](https://github.com/Outrot174/antigravity-plugins)
