# Problema: Transformar nombre

## 🎯 Objetivo
Crear un programa que lea un nombre y una opción numérica desde la entrada estándar, y transforme el nombre según la opción: convertir a mayúsculas, minúsculas o formato título. Si la opción es inválida, debe imprimir un mensaje de error.

## 📥 Entrada
El programa recibirá **DOS líneas**:

**Línea 1: nombre**
- String (cadena de texto)
- Ejemplos válidos: `pedro`, `MARIA`, `juan`, `José García`

**Línea 2: opción**
- Número entero
- Valores válidos: `1`, `2`, `3`
- Valores inválidos: Cualquier otro número (ej: `0`, `4`, `5`, `-1`)

**IMPORTANTE**: Primero se lee el nombre con `input()`, luego la opción con `int(input())`.

## 📤 Salida Esperada
El programa debe **imprimir** el resultado según la opción:

| Opción | Transformación | Método de Python | Ejemplo |
|--------|----------------|------------------|---------|
| 1 | MAYÚSCULAS | `nombre.upper()` | `pedro` → `PEDRO` |
| 2 | minúsculas | `nombre.lower()` | `MARIA` → `maria` |
| 3 | Formato Título | `nombre.title()` | `juan` → `Juan` |
| Otro | Error | - | `Opción inválida` |

**IMPORTANTE - Formato exacto**:
- ✅ Opción 1: Todas las letras en MAYÚSCULAS
- ✅ Opción 2: Todas las letras en minúsculas
- ✅ Opción 3: Primera letra de cada palabra en mayúscula, resto en minúsculas
- ✅ Opción inválida: Imprimir exactamente `Opción inválida` (con tilde en "Opción")
- ✅ Usar `print()` para mostrar el resultado
- ❌ NO agregar texto adicional

## 📋 Ejemplos de Ejecución

**Ejemplo 1 - Opción 1 (MAYÚSCULAS)**
```
Entrada: pedro
Entrada: 1
Salida: PEDRO
```
**Explicación**: Opción 1 convierte todo a mayúsculas usando `upper()`.

**Ejemplo 2 - Opción 2 (minúsculas)**
```
Entrada: MARIA
Entrada: 2
Salida: maria
```
**Explicación**: Opción 2 convierte todo a minúsculas usando `lower()`.

**Ejemplo 3 - Opción 3 (Título)**
```
Entrada: juan
Entrada: 3
Salida: Juan
```
**Explicación**: Opción 3 formatea como título usando `title()` (primera letra mayúscula).

**Ejemplo 4 - Opción inválida**
```
Entrada: ana
Entrada: 5
Salida: Opción inválida
```
**Explicación**: 5 no es una opción válida (solo 1, 2 o 3), se imprime mensaje de error.

**Ejemplo 5 - Título con múltiples palabras**
```
Entrada: josé garcía
Entrada: 3
Salida: José García
```
**Explicación**: `title()` pone en mayúscula la primera letra de cada palabra.

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura del programa**:
   - ✅ Crear una función llamada exactamente `main()` (sin parámetros)
   - ✅ Toda la lógica debe estar dentro de `main()`
   - ✅ Al final del archivo, incluir: `if __name__ == "__main__": main()`

2. **Lectura de datos**:
   - ✅ Primera línea: leer el nombre con `input()`
   - ✅ Segunda línea: leer la opción con `int(input())`
   - ❌ NO solicitar datos con mensajes como "Ingrese el nombre:"

3. **Métodos de string a usar**:
   - **Opción 1**: `nombre.upper()` - Convierte a MAYÚSCULAS
   - **Opción 2**: `nombre.lower()` - Convierte a minúsculas
   - **Opción 3**: `nombre.title()` - Primera letra de cada palabra en mayúscula

4. **Lógica condicional**:
   - ✅ Usar estructura `if-elif-elif-else`
   - ✅ Verificar `opcion == 1`, `opcion == 2`, `opcion == 3`
   - ✅ El `else` maneja cualquier otra opción (inválida)

5. **Salida de datos**:
   - ✅ Usar `print()` para mostrar el resultado
   - ✅ Para opciones 1, 2, 3: imprimir el nombre transformado
   - ✅ Para otras opciones: imprimir exactamente `Opción inválida`

## 💡 Pistas de Implementación

**Pista 1 - Estructura completa**:
```python
def main():
    nombre = input()  # Lee el nombre
    opcion = int(input())  # Lee la opción

    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    elif opcion == 3:
        print(nombre.title())
    else:
        print("Opción inválida")
```

**Pista 2 - Métodos de string**:
Los métodos de string se llaman con el formato `variable.metodo()`:
```python
nombre = "Pedro"
nombre.upper()  # "PEDRO"
nombre.lower()  # "pedro"
nombre.title()  # "Pedro"
```

**Pista 3 - Diferencia entre title() y capitalize()**:
- `title()`: Primera letra de CADA palabra en mayúscula → `"josé garcía"` → `"José García"`
- `capitalize()`: Solo primera letra del string → `"josé garcía"` → `"José garcía"`

Para este ejercicio, usa `title()`.

## ⚠️ Errores Comunes a Evitar

**Error 1: Usar print() en lugar de return**
```python
# ❌ INCORRECTO - Usa print
def transformar_nombre(nombre, opcion):
    if opcion == 1:
        print(nombre.upper())  # ¡No retorna!
```
```python
# ✅ CORRECTO - Usa return
def transformar_nombre(nombre, opcion):
    if opcion == 1:
        return nombre.upper()
```
**Por qué está mal**: La función debe retornar el valor, no imprimirlo.

**Error 2: Olvidar el método de string (paréntesis)**
```python
# ❌ INCORRECTO - Falta ()
return nombre.upper  # Retorna el método, no el resultado
```
```python
# ✅ CORRECTO - Con paréntesis
return nombre.upper()  # Ejecuta el método y retorna resultado
```
**Por qué está mal**: Sin `()`, estás retornando el método en sí, no el resultado de ejecutarlo.

**Error 3: Mensaje de error incorrecto**
```python
# ❌ INCORRECTO - Mensajes incorrectos
return "Opcion invalida"     # Falta tilde
return "opción inválida"     # Falta mayúscula en "Opción"
return "Error"               # Mensaje completamente diferente
return "Ingrese 1, 2 o 3"    # Mensaje diferente
```
```python
# ✅ CORRECTO - Mensaje exacto
return "Opción inválida"  # Con tilde, mayúscula correcta
```
**Por qué está mal**: El mensaje debe ser exactamente como se especifica.

**Error 4: Usar capitalize() en lugar de title()**
```python
# ❌ INCORRECTO - Usa capitalize
if opcion == 3:
    return nombre.capitalize()  # Solo primera letra del string
    # "josé garcía" → "José garcía" (incorrecto)
```
```python
# ✅ CORRECTO - Usa title
if opcion == 3:
    return nombre.title()  # Primera letra de cada palabra
    # "josé garcía" → "José García" (correcto)
```
**Por qué está mal**: El ejercicio pide formato título, que es primera letra de cada palabra en mayúscula.

**Error 5: No manejar opciones inválidas**
```python
# ❌ INCORRECTO - Falta el caso else
def transformar_nombre(nombre, opcion):
    if opcion == 1:
        return nombre.upper()
    elif opcion == 2:
        return nombre.lower()
    elif opcion == 3:
        return nombre.title()
    # ¿Qué pasa si opcion es 5? ¡No retorna nada!
```
```python
# ✅ CORRECTO - Incluye else
def transformar_nombre(nombre, opcion):
    if opcion == 1:
        return nombre.upper()
    elif opcion == 2:
        return nombre.lower()
    elif opcion == 3:
        return nombre.title()
    else:
        return "Opción inválida"  # Maneja opciones inválidas
```
**Por qué está mal**: Siempre debe haber un caso que maneje valores inesperados.
