# 🤖 Специализированный штат субагентов (Antigravity AGY v2)

Коллекция из 12 узкоспециализированных ИИ-субагентов для экосистемы **Google Antigravity** на платформе **Android ARM64 / Linux**.

Каждый субагент следует принципу единственной ответственности (**Single Responsibility Principle**), изолирован в собственном контекстном окне, не засоряет системный промпт других агентов и привязан к конкретным инструментам и каталогам.

---

## 📋 Каталог субагентов

| Имя субагента | Роль / Специализация | Назначение | Инструменты | Папка назначения |
| :--- | :--- | :--- | :--- | :--- |
| **`video-creator`** | Видеорежиссер и генератор видео | Создание видео, промптов движения и генерация через Google Veo 3.1 / 2.0 / Omni-Flash и Higgsfield MCP. | Терминал (`google-video-gen`, `google-veo`), MCP `higgsfield` | `/storage/emulated/0/Antigravity/видео/` |
| **`image-artist`** | Художник цифрового арта и текстур | Генерация изображений 1K/2K/4K, игровых ассетов и текстур через Google Nano Banana и Gemini Image. | Терминал (`google-nano-banana`), файлы | `/storage/emulated/0/Antigravity/изображения/` |
| **`prompt-architect`** | Архитектор промптов и мета-шаблонов | Проектирование XML-структурированных промптов, ролевых карточек и few-shot инструкций для ИИ-агентов. | Файлы, скилл `prompt-architect` | `/storage/emulated/0/Antigravity/промты/` |
| **`3d-craft-engineer`** | Инженер процедурного 3D и WebGL | Генерация сеток (OBJ, STL для 3D-печати), расчет объема/массы в `numpy-stl`, CSP-safe WebGL просмотрщики. | Python 3 (`numpy-stl`), WebGL | `/storage/emulated/0/Antigravity/3д модели/` |
| **`android-developer`** | Ведущий разработчик Android (Kotlin) | Архитектура мобильных приложений: Kotlin Coroutines, Jetpack Compose UDF, Room DB, Material 3, Android 16 (SDK 36). | MCP `android-adb`, редактор кода | `/storage/emulated/0/Antigravity/программы/<проект>/` |
| **`python-web-developer`** | Инженер Python CLI и системных сервисов | Создание автономных zero-dependency CLI, фоновых демонов `agy-daemon`, легковесных веб-модулей на JS. | Терминал (`python`, `bash`), редактор кода | `/storage/emulated/0/Antigravity/программы/<проект>/` |
| **`qa-security-auditor`** | Инспектор безопасности и качества кода | **Read-Only аудит:** проверка OWASP Top 10, поиск утечек токенов/ключей, инспекция `AndroidManifest.xml`, контроль принципов Карпатого. | Read-Only (статический анализ, тесты) | — (Аналитические отчеты) |
| **`docs-historian`** | Технический писатель и релиз-менеджер | Синхронизация README модулей, чейнджлоги (CHANGELOG.md), Conventional Commits, релизы через GitHub API. | MCP `github-mcp-server`, Markdown | Репозитории проектов |
| **`i18n-localizer`** | Специалист по локализации (`antigravity-ru`) | Поддержание словарей перевода `i18n_ru.js` (1600+ фраз), валидация AST-патчей в `main.js`, терминологический контроль. | Редакторы текста, AST-линтеры | Репозиторий `antigravity-ru` |
| **`game-prototyper`** | Креативный прототипист игр (`TrapMario`) | Быстрое создание браузерных игр на HTML5 Canvas/WebGL с мобильным тач-управлением, физикой и ретро-звуком Web Audio. | HTML5, Canvas, Web Audio | `/storage/emulated/0/Antigravity/программы/<игра>/` |
| **`graphics-engine-specialist`** | Инженер графических движков (`grafik`) | Математика графиков (сглаживание Безье, масштабирование, графические примитивы), оптимизация рендера под 60/120 FPS. | Kotlin, Skia, Compose DrawScope | `/storage/emulated/0/Antigravity/программы/grafik/` |
| **`android-env-architect`** | Системный архитектор среды Android Linux | Управление пакетами `pkg`, компиляция под ARM64, обход ограничений `noexec`, настройка ADB loopback и демонов `agy-daemon`. | `pkg`, `agy-daemon`, loopback ADB | Системные директории `$PREFIX` |

---

## 🚀 Как вызывать субагентов

Субагенты вызываются главным агентом (Оркестратором) через встроенный инструмент `invoke_subagent`:

```json
{
  "Subagents": [
    {
      "TypeName": "3d-craft-engineer",
      "Role": "3D Geometry Engineer",
      "Prompt": "Сгенерируй STL-модель шестеренки с 18 зубьями и рассчитай её объем через numpy-stl."
    }
  ]
}
```

Для задач с высокой сложностью субагент может использовать флаг `"Model": "pro"`, а для быстрых вспомогательных поисков — `"Model": "flash"` или `"flash_lite"`.
