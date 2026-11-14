# 🚀 Antigravity Plugins & Skills Pack (AGY v2)

Коллекция нативных, адаптированных и очищенных плагинов и скиллов для **Google Antigravity (AGY v2)** на платформе **Android ARM64 / Linux**.

Все плагины в этом репозитории спроектированы под реальную среду Android-устройства (POCO F7 Ultra, Snapdragon 8 Elite, HyperOS 3.0):
- ❌ **Без Docker и bwrap:** 100% совместимость с native Android userspace.
- ❌ **Без спама в контекст:** удалены принудительные токсичные правила и раздутые prompt-файлы.
- ✅ **Нативная интеграция:** поддержка elevated ADB (`uid=2000`), фонового планировщика `agy-daemon`, Three.js WebGL, SQLite и правил строгой изоляции хранилища.

---

## 📦 Каталог плагинов

| Плагин | Скилл | Назначение |
| :--- | :--- | :--- |
| **`android-adb-toolkit`** | `android-adb-toolkit` | Разработка и отладка Android: фильтрация logcat (крэши, fatal), управление APK (`pm install -r`), активности (`am start`), память, батарея и доступ к защищенным директориям через нативный ADB loopback. |
| **`threejs-3d-craft`** | `threejs-3d-craft` | Процедурная генерация 3D моделей (Wavefront OBJ, STL, GLTF) в `/storage/emulated/0/Antigravity/3д модели/` и рендеринг интерактивных сцен Three.js через Generative UI прямо в чате. |
| **`security-audit`** | `security-auditor` | Автономный аудит безопасности кода без Docker: OWASP Top 10, утечки API-токенов/ключей, инспекция `AndroidManifest.xml` (exported компоненты, cleartext HTTP, insecure storage). |
| **`sqlite-inspector`** | `sqlite-inspector` | Быстрое исследование локальных баз данных SQLite и Room (схемы таблиц, целостность, выборки данных, миграции) через нативный Python `sqlite3`. |
| **`git-workflow`** | `git-workflow` | Стандарты Conventional Commits, генерация release tags, оформление PR и автоматическое решение проблем с `dubious ownership` на разделах Android shared storage. |
| **`prompt-architect`** | `prompt-architect` | Проектирование системных промптов, мета-промптов с XML-структурой и шаблоновfew-shot. Сохранение шаблонов в `/storage/emulated/0/Antigravity/промты/`. |
| **`agy-automation`** | `agy-automation-recommender` | Анализирует кодовую базу любого проекта и рекомендует кастомизации под Antigravity AGY v2 (скиллы `.agents/skills/`, правила `AGENTS.md`, демоны `agy-daemon`, команды ADB). |
| **`google-antigravity`** | `google-antigravity` | Стандарты планирования Google Antigravity (`implementation_plan.md`, `walkthrough.md`) и дизайн-система Google AI Studio (палитры, микроанимации, стекломорфизм). |
| **`karpathy-skills`** | `karpathy-guidelines` | Принципы Андрея Карпатого: хирургические правки, минимализм, отказ от лишних спекулятивных абстракций и верификация кода тестами. |
| **`agent-reach`** | `agent-reach` | Чтение и поиск по открытым данным соцсетей (GitHub, Reddit, Twitter/X, Bilibili, YouTube) без API-ключей. |

---

## 🛠 Быстрая установка

### 1. Установка всех плагинов в глобальный конфиг
```bash
cp -r plugins/* ~/.gemini/config/plugins/
```

### 2. Настройка серверов MCP (без Docker)
Файл конфигурации: `~/.gemini/config/mcp_config.json`
Вместо Docker сервер GitHub запускается нативно через `npx`:
```json
{
  "mcpServers": {
    "github-mcp-server": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_TOKEN_HERE"
      }
    }
  }
}
```

---

## 📱 Стандарты изоляции хранилища Android

Все создаваемые агентом данные сохраняются строго в изолированные разделы:
- `/storage/emulated/0/Antigravity/программы/` — проекты и код
- `/storage/emulated/0/Antigravity/3д модели/` — 3D модели (OBJ, STL, GLTF)
- `/storage/emulated/0/Antigravity/промты/` — готовые системные промпты
- `/storage/emulated/0/Antigravity/изображения/` — сгенерированные арты
- `/storage/emulated/0/Antigravity/видео/` — видеоматериалы (Google Veo)
- `/storage/emulated/0/Antigravity/песочница/` — дампы и временные тесты

---

## 👤 Автор

**Outrot174** (GitHub: [Outrot174](https://github.com/Outrot174))  
Репозиторий проекта: [https://github.com/Outrot174/antigravity-plugins](https://github.com/Outrot174/antigravity-plugins)
