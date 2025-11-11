# Problema: String termina en vocal

## 🎯 Objetivo
Crear un programa que lea un string desde la entrada estándar y verifique si termina en vocal. Si termina en vocal (a, e, i, o, u, A, E, I, O, U), debe imprimir el string con un signo de exclamación `!` al final. Si no termina en vocal, debe imprimir el string sin modificar.

## 📥 Entrada
El programa recibirá **UNA línea** con:
- Un string (cadena de texto)
- Ejemplos válidos: `casa`, `papel`, `Chile`, `HOLA`, `amor`

**IMPORTANTE**: Debes leer el texto con `input()`.

**Concepto clave**: Vocales son: a, e, i, o, u (minúsculas) y A, E, I, O, U (mayúsculas).

## 📤 Salida Esperada
El programa debe imprimir **EXACTAMENTE**:

### ✅ Si termina en vocal:
Imprimir el string con `!` al final:
```
Entrada: casa
Salida: casa!
```
```
Entrada: Chile
Salida: Chile!
```

### ✅ Si NO termina en vocal:
Imprimir el string original sin modificar:
```
Entrada: papel
Salida: papel
```
```
Entrada: amor
Salida: amor
```

**IMPORTANTE**:
- ✅ Usar `print()` para mostrar el resultado
- ✅ Verificar vocales en MAYÚSCULAS y minúsculas
- ✅ El signo de exclamación va PEGADO al texto: `casa!` (no `casa !`)
- ❌ NO agregar texto adicional

## 📋 Ejemplos de Ejecución

**Ejemplo 1 - Termina en vocal minúscula**
```
Entrada: casa
Salida: casa!
```
**Explicación**: "casa" termina en 'a' (vocal), se agrega '!' → "casa!"

**Ejemplo 2 - NO termina en vocal**
```
Entrada: papel
Salida: papel
```
**Explicación**: "papel" termina en 'l' (consonante), se imprime sin cambios.

**Ejemplo 3 - Termina en vocal mayúscula**
```
Entrada: Chile
Salida: Chile!
```
**Explicación**: "Chile" termina en 'e' (vocal), se agrega '!' → "Chile!"

**Ejemplo 4 - Consonante al final**
```
Entrada: amor
Salida: amor
```
**Explicación**: "amor" termina en 'r' (consonante), se imprime sin cambios.

**Ejemplo 5 - Vocal mayúscula al final**
```
Entrada: HOLA
Salida: HOLA!
```
**Explicación**: "HOLA" termina en 'A' (vocal mayúscula), se agrega '!' → "HOLA!"

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura del programa**:
   - ✅ Crear una función llamada exactamente `main()` (sin parámetros)
   - ✅ Toda la lógica debe estar dentro de `main()`
   - ✅ Al final del archivo, incluir: `if __name__ == "__main__": main()`

2. **Lectura de datos**:
   - ✅ Usar `input()` para leer el string
   - ❌ NO solicitar datos con mensajes como "Ingrese texto:"

3. **Acceso al último carácter**:
   - ✅ Usar indexación negativa: `texto[-1]`
   - Esto obtiene el último carácter sin importar el largo del string

4. **Lógica condicional**:
   - ✅ Verificar si el último carácter es vocal usando `in`
   - ✅ Considerar TODAS las vocales: `'aeiouAEIOU'`
   - ✅ Usar concatenación `+` para agregar el `!`

5. **Salida de datos**:
   - ✅ Usar `print()` para mostrar el resultado
   - ✅ Si termina en vocal: imprimir `texto + "!"`
   - ✅ Si NO termina en vocal: imprimir `texto`

## 💡 Pistas de Implementación

**Pista 1 - Estructura básica**:
```python
def main():
    texto = input()  # Lee el string
    ultimo = texto[-1]  # Obtiene último carácter

    if ultimo in 'aeiouAEIOU':
        print(texto + "!")
    else:
        print(texto)
```

**Pista 2 - Operador `in` para vocales**:
El operador `in` verifica si un carácter está en un string:
```python
'a' in 'aeiouAEIOU'  # True (es vocal)
'z' in 'aeiouAEIOU'  # False (no es vocal)
'E' in 'aeiouAEIOU'  # True (vocal mayúscula)
```

**Pista 3 - Concatenación de strings**:
Para agregar el `!` al final:
```python
texto = "casa"
resultado = texto + "!"  # "casa!"
```

## ⚠️ Errores Comunes a Evitar

**Error 1: No leer el texto con input()**
```python
# ❌ INCORRECTO - No lee la entrada
def main():
    texto = "casa"  # Hardcodeado
    if texto[-1] in 'aeiouAEIOU':
        print(texto + "!")
```
```python
# ✅ CORRECTO - Lee con input()
def main():
    texto = input()  # Lee desde entrada estándar
    if texto[-1] in 'aeiouAEIOU':
        print(texto + "!")
```
**Por qué está mal**: El programa debe leer desde la entrada estándar, no tener valores hardcodeados.

**Error 2: Olvidar vocales mayúsculas**
```python
# ❌ INCORRECTO - Solo verifica minúsculas
texto = input()
if texto[-1] in 'aeiou':  # No detecta 'A', 'E', 'I', 'O', 'U'
    print(texto + "!")
```
```python
# ✅ CORRECTO - Incluye mayúsculas y minúsculas
texto = input()
if texto[-1] in 'aeiouAEIOU':  # Detecta todas las vocales
    print(texto + "!")
```
**Por qué está mal**: El problema pide considerar vocales en mayúsculas y minúsculas.

**Error 3: Agregar espacio antes del signo**
```python
# ❌ INCORRECTO - Espacio antes del !
print(texto + " !")  # "casa !" (incorrecto)
```
```python
# ✅ CORRECTO - Sin espacio
print(texto + "!")  # "casa!" (correcto)
```
**Por qué está mal**: El signo debe ir pegado al texto, sin espacios.

**Error 4: No imprimir en el caso else**
```python
# ❌ INCORRECTO - No imprime cuando no es vocal
def main():
    texto = input()
    if texto[-1] in 'aeiouAEIOU':
        print(texto + "!")
    # ¡No imprime nada si no es vocal!
```
```python
# ✅ CORRECTO - Print en ambos casos
def main():
    texto = input()
    if texto[-1] in 'aeiouAEIOU':
        print(texto + "!")
    else:
        print(texto)  # Imprime original
```
**Por qué está mal**: El programa SIEMPRE debe imprimir algo, incluso cuando el texto no termina en vocal.
