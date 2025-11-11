# Problema: Validar contraseña

## 🎯 Objetivo
Crear un programa que lea una contraseña desde la entrada estándar y valide si tiene una longitud aceptable (entre 8 y 14 caracteres, inclusivo). Si la longitud es válida, imprime un mensaje de éxito; si no, imprime un mensaje de error específico.

## 📥 Entrada
El programa recibirá **UNA línea** con:
- Un string (cadena de texto) que representa la contraseña
- Ejemplos válidos: `abc12345`, `password123456`, `MiClave#2024`

**IMPORTANTE**: Debes leer la contraseña con `input()`.

**Regla de validación**: Una contraseña es válida si tiene **entre 8 y 14 caracteres** (incluyendo 8 y 14).
- ✅ Válido: 8, 9, 10, 11, 12, 13, 14 caracteres
- ❌ Inválido: Menos de 8 o más de 14 caracteres

## 📤 Salida Esperada
El programa debe **imprimir** uno de estos mensajes:

### ✅ Si longitud entre 8 y 14 (8 ≤ len(password) ≤ 14):
```
Ha ingresado una contraseña correcta
```

### ✅ Si longitud menor a 8 o mayor a 14:
```
Por favor, ingrese una contraseña de entre 8 y 14 caracteres
```

**IMPORTANTE - Formato exacto**:
- ✅ Usar estas frases EXACTAS (mayúsculas, minúsculas, tildes, espacios)
- ✅ "Ha ingresado" (con "H" mayúscula)
- ✅ "Por favor, ingrese" (con "P" mayúscula, coma después de "favor")
- ✅ Incluir tilde en "contraseña"
- ✅ Usar `print()` para mostrar el resultado
- ❌ NO cambiar la redacción

## 📋 Ejemplos de Ejecución

**Ejemplo 1 - Exactamente 8 caracteres (válido)**
```
Entrada: abc12345
Salida: Ha ingresado una contraseña correcta
```
**Explicación**: 8 caracteres está en el rango válido [8, 14].

**Ejemplo 2 - Exactamente 14 caracteres (válido)**
```
Entrada: password123456
Salida: Ha ingresado una contraseña correcta
```
**Explicación**: 14 caracteres es el máximo permitido, todavía válido.

**Ejemplo 3 - Menos de 8 caracteres (inválido)**
```
Entrada: abc123
Salida: Por favor, ingrese una contraseña de entre 8 y 14 caracteres
```
**Explicación**: 6 caracteres es menor que 8, no válido.

**Ejemplo 4 - Más de 14 caracteres (inválido)**
```
Entrada: password12345678
Salida: Por favor, ingrese una contraseña de entre 8 y 14 caracteres
```
**Explicación**: 16 caracteres es mayor que 14, no válido.

**Ejemplo 5 - Longitud intermedia (válido)**
```
Entrada: MiClave#2024
Salida: Ha ingresado una contraseña correcta
```
**Explicación**: 12 caracteres está dentro del rango [8, 14].

**Ejemplo 6 - Contraseña muy corta (inválido)**
```
Entrada: 123
Salida: Por favor, ingrese una contraseña de entre 8 y 14 caracteres
```
**Explicación**: 3 caracteres es mucho menor que 8, no válido.

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura del programa**:
   - ✅ Crear una función llamada exactamente `main()` (sin parámetros)
   - ✅ Toda la lógica debe estar dentro de `main()`
   - ✅ Al final del archivo, incluir: `if __name__ == "__main__": main()`

2. **Lectura de datos**:
   - ✅ Usar `input()` para leer la entrada
   - ❌ NO solicitar datos con mensajes como "Ingrese la contraseña:"

3. **Función len()**:
   - ✅ `len(password)` devuelve el número de caracteres en el string
   - ✅ Cuenta todos los caracteres: letras, números, símbolos, espacios

4. **Lógica condicional**:
   - ✅ Verificar si la longitud está en el rango [8, 14]
   - ✅ Usar operador `and` para combinar condiciones: `len(password) >= 8 and len(password) <= 14`
   - ✅ Alternativamente: `8 <= len(password) <= 14` (Python permite comparaciones encadenadas)

5. **Salida de datos**:
   - ✅ Usar `print()` para mostrar el resultado
   - ✅ Si válido: imprimir mensaje de éxito
   - ✅ Si inválido: imprimir mensaje de error con instrucciones

## 💡 Pistas de Implementación

**Pista 1 - Estructura básica con and**:
```python
def main():
    password = input()  # Lee la contraseña
    longitud = len(password)

    if longitud >= 8 and longitud <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
```

**Pista 2 - Versión compacta con comparación encadenada**:
```python
def main():
    password = input()

    if 8 <= len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
```
Python permite escribir `8 <= len(password) <= 14` en lugar de `len(password) >= 8 and len(password) <= 14`.

**Pista 3 - Función len()**:
La función `len()` devuelve un número entero:
```python
len("abc")        # 3
len("password")   # 8
len("")           # 0 (string vacío)
len("123 456")    # 7 (cuenta el espacio)
```

## ⚠️ Errores Comunes a Evitar

**Error 1: Usar return en lugar de print**
```python
# ❌ INCORRECTO - Usa return
def main():
    password = input()
    if 8 <= len(password) <= 14:
        return "Ha ingresado una contraseña correcta"  # ¡No imprime!
```
```python
# ✅ CORRECTO - Usa print
def main():
    password = input()
    if 8 <= len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
```
**Por qué está mal**: La función debe imprimir el valor, no retornarlo.

**Error 2: Usar < o > en lugar de <= o >=**
```python
# ❌ INCORRECTO - Excluye 8 y 14
password = input()
if len(password) > 8 and len(password) < 14:  # Solo 9-13
    print("Ha ingresado una contraseña correcta")
```
```python
# ✅ CORRECTO - Incluye 8 y 14
password = input()
if len(password) >= 8 and len(password) <= 14:  # 8-14
    print("Ha ingresado una contraseña correcta")
```
**Por qué está mal**: El problema dice "entre 8 y 14 caracteres (incluyendo 8 y 14)", por lo tanto debes usar `>=` y `<=`.

**Error 3: Usar or en lugar de and**
```python
# ❌ INCORRECTO - Usa or (lógica incorrecta)
password = input()
if len(password) >= 8 or len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
    # ¡Esto es SIEMPRE True! Cualquier número es >= 8 O <= 14
```
```python
# ✅ CORRECTO - Usa and
password = input()
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
```
**Por qué está mal**: Necesitas que AMBAS condiciones sean verdaderas (mayor o igual a 8 Y menor o igual a 14).

**Error 4: Mensajes con formato incorrecto**
```python
# ❌ INCORRECTO - Mensajes incorrectos
print("ha ingresado una contraseña correcta")  # Falta mayúscula
print("Ha ingresado una contrasena correcta")  # Falta tilde en "ñ"
print("Contraseña correcta")                   # Mensaje diferente
print("Por favor ingrese una contraseña...")   # Falta coma después de "favor"
```
```python
# ✅ CORRECTO - Mensajes exactos
print("Ha ingresado una contraseña correcta")
print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
```
**Por qué está mal**: Los mensajes deben coincidir exactamente con la especificación.

**Error 5: Invertir la lógica**
```python
# ❌ INCORRECTO - Lógica invertida
password = input()
if len(password) < 8 or len(password) > 14:
    print("Ha ingresado una contraseña correcta")  # ¡Al revés!
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
```
```python
# ✅ CORRECTO - Lógica correcta
password = input()
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")  # Cuando ES válida
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
```
**Por qué está mal**: El mensaje de éxito debe mostrarse cuando la contraseña ES válida, no cuando no lo es.
