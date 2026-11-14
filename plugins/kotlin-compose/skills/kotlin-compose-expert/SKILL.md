---
name: kotlin-compose-expert
description: Best practices for modern Android development with Kotlin Coroutines, Jetpack Compose, Material 3, and state management. Use when writing, reviewing, or refactoring Android UI, ViewModels, Compose layouts, state holders, and reactive flows.
tools: Read, Glob, Grep, Bash
---

# Kotlin Coroutines & Jetpack Compose Expert

Production architecture and performance standards for native Android development with Kotlin and Jetpack Compose.

## 1. Unidirectional Data Flow (UDF) Architecture

Keep state hoisting clean and deterministic:
```kotlin
// UI State: Immutable data class
data class ScreenUiState(
    val items: List<Item> = emptyList(),
    val isLoading: Boolean = false,
    val errorMessage: String? = null
)

// ViewModel: Single source of truth
class FeatureViewModel(
    private val repository: FeatureRepository
) : ViewModel() {
    private val _uiState = MutableStateFlow(ScreenUiState())
    val uiState: StateFlow<ScreenUiState> = _uiState.asStateFlow()

    fun loadData() {
        viewModelScope.launch(Dispatchers.IO) {
            _uiState.update { it.copy(isLoading = true) }
            try {
                val data = repository.fetchData()
                _uiState.update { it.copy(items = data, isLoading = false) }
            } catch (e: Exception) {
                _uiState.update { it.copy(errorMessage = e.localizedMessage, isLoading = false) }
            }
        }
    }
}
```

In Compose screens, always consume lifecycle-aware state:
```kotlin
@Composable
fun FeatureRoute(viewModel: FeatureViewModel = viewModel()) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    FeatureScreen(state = state, onRefresh = viewModel::loadData)
}
```

---

## 2. Compose Recomposition Performance

1. **Stability & Immutability**:
   - Annotate non-primitive state wrapper models with `@Immutable` or `@Stable` to allow smart recomposition skipping.
   - Use `kotlinx.collections.immutable` (e.g. `ImmutableList`) for lists in UI state classes to avoid unskippable composables.

2. **Keys in Lazy Layouts**:
   Always provide unique, stable keys in `LazyColumn` / `LazyRow`:
   ```kotlin
   LazyColumn {
       items(items = state.items, key = { it.id }) { item ->
           ItemRow(item = item)
       }
   }
   ```

3. **Avoid Allocation in Recomposition**:
   - Never allocate objects (formatters, Regex, lambdas that capture changing values) directly inside the composable body without `remember`.
   - Use `derivedStateOf` when deriving state from rapidly changing observables (like scroll offsets).

---

## 3. Kotlin Coroutines Best Practices

1. **Structured Concurrency**:
   - Never use `GlobalScope`.
   - Use `viewModelScope` for UI components, or a scoped `CoroutineScope(SupervisorJob() + Dispatchers.Default)` for worker objects.
2. **Dispatcher Discipline**:
   - Never block the main thread.
   - Offload disk I/O, SQLite/Room, and network calls to `Dispatchers.IO`.
   - Offload heavy CPU calculations (crypto, image/mesh parsing) to `Dispatchers.Default`.
3. **Cancelation Support**:
   - Ensure long loops check `isActive` or call `yield()` / `ensureActive()`.

---

## 4. Modern Android 16 (SDK 36) Standards

- **Edge-to-Edge**: Always enable edge-to-edge by default using `enableEdgeToEdge()` in `MainActivity.onCreate()` and apply window insets with `Modifier.systemBarsPadding()` or `Modifier.imePadding()`.
- **Material 3**: Use `MaterialTheme.colorScheme` and dynamic theming where appropriate.
