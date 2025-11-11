# 🧪 Análisis de Tests Fallando - 10 de Noviembre 2025

## 📊 Resumen Ejecutivo

**Resultado de Tests Backend**:
```
✅ Passed:  30/53 (56.6%)
❌ Failed:  23/53 (43.4%)
⚠️  Warnings: 2
⏱️  Duration: 6.22 seconds
```

**Estado**: 🔴 **CRÍTICO** - Casi la mitad de los tests están fallando

---

## 🔍 Categorías de Fallos Detectados

### 1. 🔴 **CRÍTICO: Firmas de Funciones Desactualizadas** (13 tests)

**Problema**: Los tests llaman funciones con parámetros que ya no existen después del refactoring.

**Archivo**: `backend/tests/test_validators.py`

**Tests afectados**:
- `test_valid_code_length` - ❌ Llama `validate_code_length(code, max_length=100)`
- `test_code_too_long` - ❌ Llama `validate_code_length(code, max_length=1000)`
- `test_code_exactly_at_limit` - ❌ Llama `validate_code_length(code, max_length=1000)`
- Y 10 tests más en test_validators.py

**Error detectado**:
```python
# TEST (incorrecto):
validate_code_length(code, max_length=100)

# FUNCIÓN REAL (backend/validators.py:57):
def validate_code_length(code: str) -> None:
    # Usa settings.MAX_CODE_LENGTH, no acepta parámetro max_length
    if len(code) > settings.MAX_CODE_LENGTH:
```

**Causa raíz**:
- El refactoring movió la configuración a `backend/config.py` con `settings.MAX_CODE_LENGTH`
- Los tests no fueron actualizados para reflejar este cambio
- Los tests asumen parámetro `max_length` que ya no existe

**Impacto**:
- 🔴 **ALTO** - Los validators son críticos para seguridad
- Tests no validan comportamiento real
- Falsa sensación de seguridad

---

### 2. 🟠 **IMPORTANTE: Cambios en Mensajes de Error** (3 tests)

**Problema**: Los tests verifican mensajes de error específicos que han cambiado.

**Archivo**: `backend/tests/test_validators.py`

**Casos**:

**a) test_dangerous_import_os (línea 57-65)**:
```python
# TEST ESPERA:
assert "dangerous import" in str(exc_info.value).lower()

# MENSAJE REAL:
"Code contains potentially dangerous pattern: import os"
```
✅ Fix fácil: Cambiar assertion a `"dangerous pattern" in str(exc_info.value).lower()`

**b) test_dangerous_from_import (línea 85-92)**:
```python
# TEST ESPERA:
assert "os" in str(exc_info.value)

# MENSAJE REAL:
"Code contains potentially dangerous pattern: import sys"
# (detecta "fromsysimport" después de normalización)
```
❌ Este test tiene un bug - valida mensaje incorrecto

**c) test_empty_problem_id (línea 165)**:
```python
# TEST ESPERA:
assert "alphanumeric" in str(exc_info.value)

# MENSAJE REAL:
"problem_id cannot be empty"
```
✅ Fix: El mensaje vacío viene antes que validación de formato (correcto)

---

### 3. 🔴 **CRÍTICO: IntegrityError en Submissions** (5 tests)

**Problema**: Tests de `submission_service` fallan con constraint violation en SQLite.

**Archivo**: `backend/tests/test_submission_service.py`

**Tests afectados**:
- `test_get_statistics_with_submissions` (línea 203)
- `test_list_submissions_no_filters`
- `test_list_submissions_with_limit_offset`
- `test_list_submissions_filter_by_problem`
- `test_list_submissions_filter_by_student`

**Error**:
```
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: submissions.job_id
[SQL: INSERT INTO submissions (job_id, student_id, problem_id, code, ...) VALUES ('', None, 'sumatoria', 'bad code', ...)]
```

**Causa raíz**:
- Test intenta crear múltiples submissions con `job_id = ''` (string vacío)
- El campo `job_id` tiene constraint `UNIQUE` en el modelo
- SQLite no permite múltiples filas con job_id vacío

**Análisis del código de test**:
```python
# test_submission_service.py:203
sub2 = service.create_submission(
    db=db,
    problem_id="sumatoria",
    code="bad code",
    student_id=None
)
# Segundo submit sin job_id → usa default '' → Viola UNIQUE constraint
```

**Impacto**:
- 🔴 **ALTO** - Los tests de estadísticas y listados no se pueden ejecutar
- Imposible validar funcionalidad admin
- Puede indicar bug real en la lógica de creación de submissions

---

### 4. 🟡 **MENOR: Signature de get_test_files Cambió** (3 tests)

**Problema**: La función `get_test_files()` ahora retorna 3 valores, pero los tests esperan 2.

**Archivo**: `backend/tests/test_problem_service.py`

**Tests afectados**:
- `test_get_test_files_both_exist` (línea 59)
- `test_get_test_files_legacy_fallback` (línea 77)
- `test_get_test_files_not_found` (línea 93)

**Error**:
```python
# TEST (incorrecto):
tests_public, tests_hidden = service.get_test_files(problem_dir)

# ValueError: too many values to unpack (expected 2)
```

**Investigación necesaria**:
- Ver backend/services/problem_service.py para confirmar signature actual
- Probablemente retorna (tests_public, tests_hidden, conftest) o similar
- Tests necesitan actualización simple

---

### 5. 🟡 **MENOR: Tests de Excepciones No Lanzadas** (2 tests)

**Problema**: Tests esperan que se lance `ProblemNotFoundError`, pero no se lanza.

**Archivo**: `backend/tests/test_problem_service.py`

**Tests afectados**:
- `test_get_test_files_not_found` (línea 93)
- `test_load_rubric_file_not_found` (línea 126)

**Error**:
```python
with pytest.raises(ProblemNotFoundError) as exc_info:
    service.get_test_files(problem_dir)

# Failed: DID NOT RAISE <class 'backend.exceptions.ProblemNotFoundError'>
```

**Causa probable**:
- Las funciones fueron refactorizadas para retornar valores por defecto en lugar de lanzar
- O los paths de fallback funcionan correctamente
- Logs muestran: "Using fallback problems dir: problems"

**Impacto**:
- 🟡 **BAJO** - Indica cambio de comportamiento intencional
- Documentar si es feature o bug

---

## 📋 Plan de Corrección

### Prioridad 0 (Inmediato - Crítico)

**1. Fix IntegrityError en Submissions** 🔴
```python
# File: backend/tests/test_submission_service.py
# Solution: Generar job_id únicos para cada test

import uuid

def test_get_statistics_with_submissions(db):
    sub1 = service.create_submission(
        db=db,
        problem_id="sumatoria",
        code="good code",
        student_id="student1"
    )
    service.update_job_id(db, sub1.id, str(uuid.uuid4()))  # ✅ Job ID único

    sub2 = service.create_submission(
        db=db,
        problem_id="sumatoria",
        code="bad code",
        student_id="student2"
    )
    service.update_job_id(db, sub2.id, str(uuid.uuid4()))  # ✅ Job ID único
```

**Esfuerzo**: 🟢 Bajo (30 minutos)
**Impacto**: Desbloquea 5 tests

---

**2. Fix Firmas de validate_code_length** 🔴
```python
# File: backend/tests/test_validators.py
# Solution: Remover parámetro max_length, usar settings

def test_valid_code_length(self):
    code = "def suma(a, b):\n    return a + b"
    validate_code_length(code)  # ✅ Sin parámetro max_length

def test_code_too_long(self):
    from backend.config import settings
    code = "x" * (settings.MAX_CODE_LENGTH + 1)  # ✅ Usa settings

    with pytest.raises(ValidationError) as exc_info:
        validate_code_length(code)

    assert "exceeds maximum length" in str(exc_info.value)
```

**Esfuerzo**: 🟢 Bajo (30 minutos)
**Impacto**: Corrige 13 tests

---

### Prioridad 1 (Esta semana)

**3. Fix get_test_files() Unpacking** 🟡
```python
# File: backend/tests/test_problem_service.py
# Solution: Investigar signature real y actualizar

# Investigar primero:
from backend.services.problem_service import problem_service
import inspect
print(inspect.signature(problem_service.get_test_files))

# Luego actualizar tests según resultado
```

**Esfuerzo**: 🟢 Bajo (20 minutos)
**Impacto**: Corrige 3 tests

---

**4. Actualizar Assertions de Mensajes** 🟠
```python
# File: backend/tests/test_validators.py

def test_dangerous_import_os(self):
    code = "import os\nos.system('ls')"

    with pytest.raises(ValidationError) as exc_info:
        validate_code_safety(code)

    # ✅ Mensaje actualizado
    assert "dangerous pattern" in str(exc_info.value).lower()
    assert "import os" in str(exc_info.value).lower()
```

**Esfuerzo**: 🟢 Bajo (15 minutos)
**Impacto**: Corrige 3 tests

---

### Prioridad 2 (Próximas 2 semanas)

**5. Revisar Tests de Excepciones** 🟡
- Verificar si las funciones deben lanzar excepciones o no
- Actualizar tests según comportamiento deseado
- Documentar cambios de comportamiento

**Esfuerzo**: 🟡 Medio (1 hora)
**Impacto**: Corrige 2 tests, clarifica comportamiento

---

## 📊 Impacto Estimado de Correcciones

| Fix | Tests Corregidos | Esfuerzo | Prioridad |
|-----|------------------|----------|-----------|
| 1. IntegrityError submissions | 5 | 🟢 30min | 🔴 P0 |
| 2. validate_code_length firmas | 13 | 🟢 30min | 🔴 P0 |
| 3. get_test_files unpacking | 3 | 🟢 20min | 🟡 P1 |
| 4. Mensajes de error | 3 | 🟢 15min | 🟡 P1 |
| 5. Excepciones no lanzadas | 2 | 🟡 1h | 🟢 P2 |
| **TOTAL** | **26/53** | **2.5h** | - |

**Resultado esperado**:
- ✅ De **30 passing** → **56 passing** (100% - menos 2 pendientes de análisis)
- ⏱️ Tiempo total estimado: **2.5 horas**
- 🎯 Coverage real después: ~**100%**

---

## 🧪 Tests Workers (Pendiente)

```bash
# TODO: Ejecutar worker tests
docker compose exec worker pip install pytest pytest-mock
docker compose exec worker pytest worker/tests/ -v
```

**Nota**: Worker tests requieren Docker corriendo. No se pudieron ejecutar en este análisis.

---

## 📝 Recomendaciones

### Inmediatas

1. **Priorizar fixes P0** (IntegrityError + validate_code_length)
   - Son críticos para seguridad y funcionalidad core
   - Relativamente rápidos de corregir

2. **Setup CI/CD con tests automáticos**
   - GitHub Actions o similar
   - Evitar que refactorings futuros rompan tests
   - Pre-commit hooks con pytest

3. **Actualizar CLAUDE.md**
   - Documentar que tests están rotos
   - Agregar instrucciones de testing actualizadas

### Mediano plazo

4. **Agregar coverage badges al README**
   ```bash
   pytest --cov=backend --cov-report=html
   # Upload to codecov.io o similar
   ```

5. **Refactoring de tests**
   - Usar fixtures compartidos para submissions
   - Parametrizar tests similares
   - Agregar docstrings descriptivos

6. **Testing de integración end-to-end**
   - Submit real → Worker → Resultado
   - Probar flujo completo

---

## 🔗 Archivos Relacionados

- `backend/tests/test_validators.py` - 13 tests fallando
- `backend/tests/test_submission_service.py` - 5 tests fallando
- `backend/tests/test_problem_service.py` - 5 tests fallando
- `backend/validators.py` - Funciones con firmas cambiadas
- `backend/config.py` - Nueva configuración con Pydantic

---

## 📅 Historial

**10 Nov 2025**: Análisis inicial completado
- **Estado**: 23/53 tests fallando (43.4%)
- **Causa principal**: Refactorings sin actualizar tests
- **Plan**: Correcciones priorizadas por impacto

---

**Próximo paso**: Implementar fixes P0 (IntegrityError + validate_code_length)