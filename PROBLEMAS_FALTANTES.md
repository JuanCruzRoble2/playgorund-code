# 📋 Problemas Faltantes por Unidad

**Fecha de análisis**: 10 de Noviembre, 2025

## 📊 Resumen Ejecutivo

- **Total unidades configuradas**: 40 unidades (8 materias × 5 unidades)
- **Total problemas existentes**: 31 problemas
- **Unidades con problemas**: 14 unidades
- **⚠️ Unidades SIN problemas**: 26 unidades (65% vacías)

## 🚨 Estado Crítico

El sistema tiene una **discrepancia crítica** entre la configuración de unidades y los problemas reales:

- Solo **14 de 40 unidades** tienen problemas asignados
- **26 unidades** mostrarán secciones vacías a los estudiantes
- Esto rompe la experiencia de usuario en la navegación jerárquica

---

## 📚 Detalle por Materia

### ✅ Programación 1 (Bien cubierta)

**Unidades con problemas**:
- `estructuras-secuenciales` - ✅ 10 problemas
- `estructuras-condicionales` - ✅ 9 problemas
- `funciones` - ✅ 1 problema (sumatoria)

**⚠️ Unidades sin problemas**:
- `estructuras-repetitivas` - ❌ 0 problemas
- `listas` - ❌ 0 problemas

**Prioridad**: Media (3/5 unidades cubiertas)

---

### ⚠️ Programación 2 (Sin problemas)

**⚠️ TODAS las unidades sin problemas**:
- `poo-basico` - ❌ 0 problemas
- `herencia` - ❌ 0 problemas
- `excepciones` - ❌ 0 problemas
- `archivos` - ❌ 0 problemas
- `estructuras-datos` - ❌ 0 problemas

**Prioridad**: Alta (materia completamente vacía)

---

### ⚠️ Programación 3 - Spring Boot (Sin problemas)

**Unidades con problemas**:
- `spring-web` - ✅ 1 problema (spring_hello_controller)

**⚠️ Unidades sin problemas**:
- `spring-fundamentos` - ❌ 0 problemas
- `spring-boot-basico` - ❌ 0 problemas
- `spring-data` - ❌ 0 problemas
- `spring-security` - ❌ 0 problemas

**Nota**: Spring Boot requiere infraestructura Java. Actualmente el runner solo soporta Python.

**Prioridad**: Baja (requiere cambio de infraestructura)

---

### ⚠️ Programación 4 - FastAPI (Parcialmente cubierta)

**Unidades con problemas**:
- `fastapi-fundamentos` - ✅ 1 problema (fastapi_hello_endpoint)

**⚠️ Unidades sin problemas**:
- `fastapi-validacion` - ❌ 0 problemas
- `fastapi-database` - ❌ 0 problemas
- `fastapi-security` - ❌ 0 problemas
- `fastapi-avanzado` - ❌ 0 problemas

**Prioridad**: Alta (materia compatible con infraestructura actual)

---

### ⚠️ Paradigmas de Programación (Parcialmente cubierta)

**Unidades con problemas**:
- `paradigma-oo` - ✅ 1 problema (paradigma_oo_java)
- `paradigma-logico` - ✅ 1 problema (paradigma_logico_prolog)
- `paradigma-funcional` - ✅ 1 problema (paradigma_funcional_haskell)

**⚠️ Unidades sin problemas**:
- `paradigma-imperativo` - ❌ 0 problemas
- `comparacion-paradigmas` - ❌ 0 problemas

**Nota**: Requiere soporte para Java, Prolog y Haskell en el runner.

**Prioridad**: Baja (requiere múltiples runners)

---

### ⚠️ Algoritmos y Estructuras de Datos (Sin problemas)

**⚠️ TODAS las unidades sin problemas**:
- `estructuras-datos-basicas` - ❌ 0 problemas
- `algoritmos-ordenamiento` - ❌ 0 problemas
- `algoritmos-busqueda` - ❌ 0 problemas
- `pilas-colas` - ❌ 0 problemas
- `recursion` - ❌ 0 problemas

**Nota**: Configurada para PSeInt, pero actualmente no hay runner PSeInt.

**Prioridad**: Media (requiere runner específico)

---

### ⚠️ Desarrollo Frontend (Parcialmente cubierta)

**Unidades con problemas**:
- `html-fundamentos` - ✅ 1 problema (frontend_html_estructura)
- `css-estilos` - ✅ 1 problema (frontend_css_selector)
- `javascript-basico` - ✅ 1 problema (frontend_js_function)
- `typescript` - ✅ 1 problema (frontend_ts_tipos)

**⚠️ Unidades sin problemas**:
- `javascript-avanzado` - ❌ 0 problemas

**Prioridad**: Media (4/5 unidades cubiertas)

---

### ⚠️ Desarrollo Backend (Parcialmente cubierta)

**Unidades con problemas**:
- `python-fundamentos` - ✅ 1 problema (backend_python_dict)
- `fastapi-basico` - ✅ 1 problema (backend_fastapi_response)

**⚠️ Unidades sin problemas**:
- `bases-datos` - ❌ 0 problemas
- `autenticacion` - ❌ 0 problemas
- `deployment` - ❌ 0 problemas

**Prioridad**: Alta (materia compatible con infraestructura actual)

---

## 🎯 Plan de Acción Recomendado

### Prioridad 0 (Inmediato)

**Opción A: Reducir configuración de subjects_config.json**
- Eliminar o comentar las unidades sin problemas
- Actualizar frontend para no mostrar unidades vacías
- **Ventaja**: Solución inmediata, mejora UX
- **Desventaja**: Reduce alcance aparente del sistema

**Opción B: Crear problemas básicos para unidades críticas**
- Agregar 1-2 problemas por unidad en Programación 1, 4 y Backend
- Enfocarse en Python (compatible con runner actual)
- **Ventaja**: Mantiene alcance, mejora contenido
- **Desventaja**: Requiere tiempo de desarrollo

### Prioridad 1 (Corto plazo)

1. **Programación 1** - Agregar problemas para:
   - `estructuras-repetitivas` (while, for)
   - `listas` (append, slicing, comprensions)

2. **Programación 4** - Agregar problemas para:
   - `fastapi-validacion` (Pydantic models)
   - `fastapi-database` (SQLAlchemy CRUD)

3. **Backend** - Agregar problemas para:
   - `bases-datos` (SQL queries, ORM)
   - `autenticacion` (JWT, hashing)

### Prioridad 2 (Mediano plazo)

4. **Frontend** - Agregar problemas para:
   - `javascript-avanzado` (async/await, fetch)

5. **Programación 2** - Decidir si:
   - Cambiar a Python POO (compatible con runner actual)
   - O crear runner Java (más complejo)

### Prioridad 3 (Largo plazo)

6. **Paradigmas** - Requiere runners múltiples (Java, Prolog, Haskell)
7. **Algoritmos** - Requiere runner PSeInt o cambiar a Python
8. **Spring Boot** - Requiere runner Java con Spring Framework

---

## 🛠️ Recomendación Técnica

**Para resolver el problema inmediato**:

```bash
# Opción 1: Modificar subjects_config.json
# Comentar unidades sin problemas o agregar flag "has_problems": false

# Opción 2: Agregar filtro en backend
# Modificar /api/problems/hierarchy para ocultar unidades vacías
```

**Código sugerido** en `backend/app.py`:

```python
@app.get("/api/problems/hierarchy")
def get_problems_hierarchy() -> Dict[str, Any]:
    hierarchy = subject_service.get_hierarchy()
    problems_grouped = problem_service.group_by_subject_and_unit()

    # Filter out empty units
    for subject_id in list(hierarchy.keys()):
        for unit_id in list(hierarchy[subject_id].get("units", {}).keys()):
            problem_ids = problems_grouped.get(subject_id, {}).get(unit_id, [])

            # Hide units with no problems
            if len(problem_ids) == 0:
                del hierarchy[subject_id]["units"][unit_id]
            else:
                hierarchy[subject_id]["units"][unit_id]["problem_count"] = len(problem_ids)
                hierarchy[subject_id]["units"][unit_id]["problem_ids"] = problem_ids

        # Hide subjects with no units
        if not hierarchy[subject_id].get("units"):
            del hierarchy[subject_id]

    return {"hierarchy": hierarchy}
```

---

## 📝 Notas Adicionales

- El sistema actual solo soporta **Python 3.11** en el runner
- Para agregar soporte multi-lenguaje, se necesitan runners específicos
- La arquitectura actual (Docker sandbox) soporta múltiples lenguajes con modificaciones menores

---

**Documento generado automáticamente**
Para actualizar, ejecutar: `python scripts/analyze_problems.py`