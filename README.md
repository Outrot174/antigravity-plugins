# 🚀 Antigravity Coding Plugins & Skills Pack (AGY v2)

Коллекция нативных, адаптированных и легковесных плагинов и скиллов для **Google Antigravity (AGY v2)** на платформе **Android ARM64 / Linux**, сфокусированная **исключительно на разработке программного обеспечения, архитектуре и качестве кода**.

Все плагины в этом репозитории спроектированы под реальную среду Android-устройства (POCO F7 Ultra, Snapdragon 8 Elite, HyperOS 3.0):
- ❌ **Без тяжелых демонов и Docker:** 100% совместимость с native Android userspace.
- ❌ **Без лишней нагрузки на контекст:** никаких тяжелых генераторов и избыточных промптов.
- ✅ **Фокус на коде:** отладка Android, Kotlin Compose, Python CLI, REST API, аудит безопасности OWASP, SQLite, Git и оптимизация токенов.

---

## 📦 Каталог плагинов разработки (13 плагинов)

| Плагин | Скилл | Назначение |
| :--- | :--- | :--- |
| **`token-optimizer`** | `token-efficiency-craft` | **Экономия токенов и сжатие контекста:** фильтрация вывода терминала (logcat, git diff, grep), чтение файлов по узким диапазонам строк (`StartLine`/`EndLine`), хирургические точечные правки (`replace_file_content`), маскирование наблюдений и устранение разговорного шума. |
| **`kotlin-compose`** | `kotlin-compose-expert` | **Android & Kotlin архитектура:** стандарты современной разработки под Android — Kotlin Coroutines, Jetpack Compose UDF, `StateFlow`, оптимизация рекомпозиций (`@Immutable`, `@Stable`, Lazy-ключи), Material 3 и Edge-to-Edge для Android 16 (SDK 36). |
| **`python-artisan`** | `python-artisan` | **Автономная разработка на Python:** архитектура автономных Python CLI-утилит под Android userspace: zero-dependency шаблоны, управление путями и шебангами (`agy-fix-paths`), интеграция с Google AI Studio / Gemini API и обход ограничений `noexec`. |
| **`android-adb-toolkit`** | `android-adb-toolkit` | **Диагностика и тестирование Android:** фильтрация logcat (крэши, ANR, fatal), управление APK (`pm install -r`), запуск активностей (`am start`), мониторинг памяти/батареи и доступ к защищенным директориям через нативный ADB loopback (`uid=2000`). |
| **`security-audit`** | `security-auditor` | **Аудит безопасности кода:** автономный аудит безопасности кода без внешних тяжелых сканеров — OWASP Top 10, поиск утечек API-токенов/ключей, инспекция `AndroidManifest.xml` (exported компоненты, cleartext HTTP, insecure storage). |
| **`api-tester`** | `api-tester` | **Тестирование сетевых API:** тестирование REST API, HTTP-эндпоинтов, вебхуков и WebSockets: замеры задержки (TTFB, DNS, TLS), валидация JSON-схем и многопоточные бенчмарки на чистом Python. |
| **`sqlite-inspector`** | `sqlite-inspector` | **Инспекция баз данных:** быстрое исследование локальных баз данных SQLite и Room (схемы таблиц, целостность, диагностические запросы, проверка миграций) через нативный Python `sqlite3`. |
| **`git-workflow`** | `git-workflow` | **Управление версиями:** стандарты Conventional Commits, генерация release tags, оформление PR и автоматическое решение проблем с `dubious ownership` на разделах Android shared storage. |
| **`karpathy-skills`** | `karpathy-guidelines` | **Качество кода по принципам Андрея Карпатого:** хирургические правки, минимализм, отказ от лишних спекулятивных абстракций и строгая верификация кода тестами. |
| **`google-antigravity`** | `google-antigravity` | **Паттерны Google AI:** стандарты планирования Google Antigravity (`implementation_plan.md`, `walkthrough.md`) и дизайн-система Google AI Studio. |
| **`agy-automation`** | `agy-automation-recommender` | **Рекомендации автоматизаций:** анализ кодовой базы проектов и подбор оптимальных кастомизаций под Antigravity AGY v2 (скиллы, правила `AGENTS.md`, демоны `agy-daemon`, команды ADB). |
| **`freellm-manager`** | `freellm-proxy` | **Шлюз локальных моделей разработчика:** управление локальным шлюзом к 87 провайдерам и 328+ бесплатным моделям через CLI `freellm` (порт `3001`). |
| **`agent-reach`** | `agent-reach` | **Чтение документации и открытых данных:** чтение и поиск по открытым репозиториям GitHub, issues, PR и профильной технической информации. |

---

## ⚡ FreeLLMAPI (Локальный шлюз моделей разработчика)

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

- **Base URL:** `http://127.0.0.1:3001/v1`
- **Port:** `3001` (изолирован от системных портов Antigravity `45157`/`45158`)
- **Формат запросов:** Стандартный OpenAI Chat Completions API (`POST /v1/chat/completions`)

---

## 🛠️ Установка в Antigravity

Все плагины подключаются напрямую в `~/.gemini/config/plugins/`:
```bash
mkdir -p ~/.gemini/config/plugins
cp -r plugins/* ~/.gemini/config/plugins/
```
