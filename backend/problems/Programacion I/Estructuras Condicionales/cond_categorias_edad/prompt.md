# Problema: Categorías de edad

## 🎯 Objetivo
Crear una función que reciba una edad y retorne la categoría correspondiente según rangos de edad definidos: Niño/a, Adolescente, Adulto/a joven, o Adulto/a.

## 📥 Entrada
La función recibirá **un parámetro**:
- **Nombre del parámetro**: `edad`
- **Tipo de dato**: Número entero (int)
- **Ejemplos de valores válidos**: `8`, `15`, `25`, `40`, `12`, `17`, `30`

```python
def categoria_edad(edad):
    # edad es un número entero
    # Debes retornar un string con la categoría
```

## 📤 Salida Esperada
La función debe **retornar** (NO imprimir) un string según el rango de edad:

| Rango de Edad | Categoría Retornada |
|---------------|---------------------|
| edad < 12 | `"Niño/a"` |
| 12 ≤ edad < 18 | `"Adolescente"` |
| 18 ≤ edad < 30 | `"Adulto/a joven"` |
| edad ≥ 30 | `"Adulto/a"` |

**IMPORTANTE - Formato exacto**:
- ✅ Usar `return`, NO `print()`
- ✅ Strings exactos: `"Niño/a"`, `"Adolescente"`, `"Adulto/a joven"`, `"Adulto/a"`
- ✅ Respetar mayúsculas y minúsculas exactamente
- ✅ Incluir la barra `/` en "Niño/a", "Adulto/a joven", "Adulto/a"
- ✅ No incluir espacios extras
- ❌ NO cambiar la redacción

## 📋 Ejemplos de Ejecución

**Ejemplo 1 - Niño/a**
```python
categoria_edad(8)
# 8 < 12
# Retorna: "Niño/a"
```
**Explicación**: 8 es menor que 12, por lo tanto pertenece a la categoría "Niño/a".

**Ejemplo 2 - Adolescente**
```python
categoria_edad(15)
# 12 ≤ 15 < 18
# Retorna: "Adolescente"
```
**Explicación**: 15 está en el rango [12, 18), por lo tanto es "Adolescente".

**Ejemplo 3 - Adulto/a joven**
```python
categoria_edad(25)
# 18 ≤ 25 < 30
# Retorna: "Adulto/a joven"
```
**Explicación**: 25 está en el rango [18, 30), por lo tanto es "Adulto/a joven".

**Ejemplo 4 - Adulto/a**
```python
categoria_edad(40)
# 40 ≥ 30
# Retorna: "Adulto/a"
```
**Explicación**: 40 es mayor o igual a 30, por lo tanto es "Adulto/a".

**Ejemplo 5 - Caso borde: Exactamente 12 (inicio de Adolescente)**
```python
categoria_edad(12)
# 12 ≤ 12 < 18
# Retorna: "Adolescente"
```
**Explicación**: 12 marca el inicio del rango de Adolescente (inclusivo).

**Ejemplo 6 - Caso borde: Exactamente 11 (final de Niño/a)**
```python
categoria_edad(11)
# 11 < 12
# Retorna: "Niño/a"
```
**Explicación**: 11 es el último valor que califica como "Niño/a".

**Ejemplo 7 - Caso borde: Exactamente 18 (inicio de Adulto/a joven)**
```python
categoria_edad(18)
# 18 ≤ 18 < 30
# Retorna: "Adulto/a joven"
```
**Explicación**: 18 marca el inicio del rango de "Adulto/a joven" (inclusivo).

**Ejemplo 8 - Caso borde: Exactamente 30 (inicio de Adulto/a)**
```python
categoria_edad(30)
# 30 ≥ 30
# Retorna: "Adulto/a"
```
**Explicación**: 30 marca el inicio del rango de "Adulto/a" (inclusivo).

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura de la función**:
   - ✅ La función DEBE llamarse exactamente `categoria_edad`
   - ✅ DEBE recibir un parámetro llamado `edad`
   - ✅ DEBE retornar un string (usar `return`, NO `print()`)

2. **Lógica condicional**:
   - ✅ Usar estructura `if-elif-elif-else` (4 casos)
   - ✅ Evaluar rangos en orden:
     - `if edad < 12:` → "Niño/a"
     - `elif edad < 18:` → "Adolescente" (ya sabemos que edad ≥ 12)
     - `elif edad < 30:` → "Adulto/a joven" (ya sabemos que edad ≥ 18)
     - `else:` → "Adulto/a" (edad ≥ 30)

3. **Valor de retorno**:
   - ✅ Retornar strings exactos con mayúsculas/minúsculas correctas
   - ✅ Incluir barra `/` en las categorías que la requieren
   - ✅ "Adulto/a joven" debe tener espacio entre "Adulto/a" y "joven"

## 💡 Pistas de Implementación

**Pista 1 - Estructura completa**:
```python
def categoria_edad(edad):
    if edad < 12:
        return "Niño/a"
    elif edad < 18:
        return "Adolescente"
    elif edad < 30:
        return "Adulto/a joven"
    else:
        return "Adulto/a"
```

**Pista 2 - Orden de evaluación**:
Es importante evaluar en orden de menor a mayor:
- Primero `edad < 12` (el rango más bajo)
- Luego `edad < 18` (sabiendo que ya edad ≥ 12)
- Luego `edad < 30` (sabiendo que ya edad ≥ 18)
- Finalmente `else` para edad ≥ 30

Esto evita condiciones redundantes como `edad >= 12 and edad < 18`.

**Pista 3 - Casos borde**:
Los límites son **inclusivos por la izquierda**:
- 11 → "Niño/a" (< 12)
- 12 → "Adolescente" (≥ 12 y < 18)
- 17 → "Adolescente" (< 18)
- 18 → "Adulto/a joven" (≥ 18 y < 30)
- 29 → "Adulto/a joven" (< 30)
- 30 → "Adulto/a" (≥ 30)

## ⚠️ Errores Comunes a Evitar

**Error 1: Usar print() en lugar de return**
```python
# ❌ INCORRECTO - Usa print
def categoria_edad(edad):
    if edad < 12:
        print("Niño/a")  # ¡No retorna!
```
```python
# ✅ CORRECTO - Usa return
def categoria_edad(edad):
    if edad < 12:
        return "Niño/a"
```
**Por qué está mal**: La función debe retornar el valor, no imprimirlo. Los tests llaman `categoria_edad(8) == "Niño/a"`, esperando un valor de retorno.

**Error 2: Condiciones redundantes**
```python
# ❌ INCORRECTO - Condiciones redundantes
if edad < 12:
    return "Niño/a"
elif edad >= 12 and edad < 18:  # Redundante
    return "Adolescente"
```
```python
# ✅ CORRECTO - Condiciones simplificadas
if edad < 12:
    return "Niño/a"
elif edad < 18:  # Ya sabemos que edad >= 12
    return "Adolescente"
```
**Por qué está mal**: Si llegamos al `elif`, ya sabemos que `edad < 12` fue False, por lo tanto `edad >= 12`. No es necesario verificarlo de nuevo.

**Error 3: Formato incorrecto de strings**
```python
# ❌ INCORRECTO - Formatos incorrectos
return "Niño"            # Falta "/a"
return "Nino/a"          # Falta tilde en "ñ"
return "adolescente"     # Falta mayúscula inicial
return "Adulto joven"    # Falta "/a"
return "Adulto/ajoven"   # Falta espacio
```
```python
# ✅ CORRECTO - Formatos exactos
return "Niño/a"
return "Adolescente"
return "Adulto/a joven"
return "Adulto/a"
```
**Por qué está mal**: Los strings deben coincidir exactamente con la especificación, incluyendo mayúsculas, tildes, barras y espacios.

**Error 4: Rangos mal definidos**
```python
# ❌ INCORRECTO - Límites incorrectos
if edad <= 12:          # 12 debería ser Adolescente, no Niño/a
    return "Niño/a"
elif edad < 18:
    return "Adolescente"
```
```python
# ✅ CORRECTO - Límites correctos
if edad < 12:           # < 12 para Niño/a
    return "Niño/a"
elif edad < 18:         # 12-17 para Adolescente
    return "Adolescente"
```
**Por qué está mal**: Los límites deben ser exactos según la tabla. 12 años marca el inicio de "Adolescente", no el final de "Niño/a".

**Error 5: Olvidar el caso else**
```python
# ❌ INCORRECTO - Falta el caso >= 30
def categoria_edad(edad):
    if edad < 12:
        return "Niño/a"
    elif edad < 18:
        return "Adolescente"
    elif edad < 30:
        return "Adulto/a joven"
    # ¿Qué pasa si edad >= 30? ¡No retorna nada!
```
```python
# ✅ CORRECTO - Incluye else
def categoria_edad(edad):
    if edad < 12:
        return "Niño/a"
    elif edad < 18:
        return "Adolescente"
    elif edad < 30:
        return "Adulto/a joven"
    else:
        return "Adulto/a"  # Cubre edad >= 30
```
**Por qué está mal**: Siempre debe haber un caso que cubra todos los valores posibles. Sin `else`, la función retornaría `None` para edades ≥ 30.
