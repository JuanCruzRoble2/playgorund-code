# Problema: Verificar número par

## 🎯 Objetivo
Crear un programa que lea un número entero desde la entrada estándar y determine si es par. Si no es par (es impar), debe mostrar un mensaje solicitando un número par.

## 📥 Entrada
El programa recibirá **exactamente un valor** desde la entrada estándar:
- **Tipo de dato**: Número entero
- **Cómo leerlo**: Usar `input()` y convertir con `int()`
- **Ejemplos de valores válidos**: `4`, `7`, `0`, `-2`, `100`, `15`
- **Formato de lectura**: Una línea con el número

```python
numero = int(input())  # Lee y convierte a entero
```

**Concepto clave**: Un número es **par** si el resto de dividirlo entre 2 es igual a 0.
- Ejemplos pares: 0, 2, 4, 6, 8, 10, -2, -4
- Ejemplos impares: 1, 3, 5, 7, 9, -1, -3

## 📤 Salida Esperada
El programa debe imprimir **exactamente una línea** con uno de estos dos mensajes:

### ✅ Si el número es par (numero % 2 == 0):
```
Ha ingresado un número par
```

### ✅ Si el número es impar (numero % 2 != 0):
```
Por favor, ingrese un número par
```

**IMPORTANTE - Formato exacto**:
- ✅ Usar estas frases EXACTAS (mayúsculas y minúsculas como se muestra)
- ✅ "Ha ingresado" (con "H" mayúscula, "a" en "Ha" es minúscula)
- ✅ "Por favor" (con "P" mayúscula en "Por")
- ✅ Incluir los espacios y acentos correctos ("número" lleva tilde)
- ❌ NO imprimir mensajes adicionales como "Ingrese un número:", etc.
- ❌ NO cambiar la redacción de los mensajes

## 📋 Ejemplos de Ejecución

**Ejemplo 1 - Número par positivo**
```
Entrada: 4
Salida: Ha ingresado un número par
```
**Explicación**: 4 % 2 = 0, por lo tanto es par.

**Ejemplo 2 - Número impar**
```
Entrada: 7
Salida: Por favor, ingrese un número par
```
**Explicación**: 7 % 2 = 1 (no es 0), por lo tanto es impar.

**Ejemplo 3 - Cero es par**
```
Entrada: 0
Salida: Ha ingresado un número par
```
**Explicación**: 0 % 2 = 0, por lo tanto cero es par.

**Ejemplo 4 - Número par negativo**
```
Entrada: -6
Salida: Ha ingresado un número par
```
**Explicación**: -6 % 2 = 0, los números negativos también pueden ser pares.

**Ejemplo 5 - Número par grande**
```
Entrada: 100
Salida: Ha ingresado un número par
```
**Explicación**: 100 % 2 = 0, por lo tanto es par.

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. La función DEBE llamarse exactamente `main`
2. La función NO debe recibir parámetros
3. Debe incluir `if __name__ == "__main__": main()` al final (ya provisto)

### ✅ Lectura de datos:
1. Usar `input()` para leer la entrada
2. Convertir a entero con `int()`: `numero = int(input())`
3. NO imprimir prompts (mensajes que pidan datos)

### ✅ Lógica condicional:
1. Usar operador módulo `%` para obtener el resto
2. Comparar con `== 0` para verificar si es par
3. La condición es: `if numero % 2 == 0:`

### ✅ Salida de datos:
1. Usar `print()` con el mensaje exacto
2. Dos mensajes posibles según si es par o impar
3. Sin espacios extras, sin caracteres adicionales

## 💡 Pistas de Implementación

**Pista 1 - Operador módulo %**:
El operador `%` devuelve el resto de una división:
```python
10 % 2  # Resultado: 0 (10 dividido 2 da 5 con resto 0)
11 % 2  # Resultado: 1 (11 dividido 2 da 5 con resto 1)
0 % 2   # Resultado: 0 (0 dividido 2 da 0 con resto 0)
```

**Pista 2 - Estructura básica**:
```python
def main():
    numero = int(input())  # Lee y convierte a entero

    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
```

**Pista 3 - Prueba mental**:
Para verificar tu lógica, pregúntate:
- ¿4 % 2 es igual a 0? Sí → "Ha ingresado un número par" ✅
- ¿7 % 2 es igual a 0? No (es 1) → "Por favor, ingrese un número par" ✅

## ⚠️ Errores Comunes a Evitar

**Error 1: Olvidar el operador módulo %**
```python
# ❌ INCORRECTO - Usa división en lugar de módulo
if numero / 2 == 0:  # Esto no verifica si es par
    print("Ha ingresado un número par")
```
```python
# ✅ CORRECTO - Usa módulo %
if numero % 2 == 0:  # Verifica si el resto es 0
    print("Ha ingresado un número par")
```
**Por qué está mal**: La división `/` devuelve un decimal (ej: 5/2 = 2.5). El módulo `%` devuelve el resto (ej: 5%2 = 1).

**Error 2: Invertir la lógica (par vs impar)**
```python
# ❌ INCORRECTO - Lógica invertida
if numero % 2 == 0:
    print("Por favor, ingrese un número par")  # ¡Al revés!
else:
    print("Ha ingresado un número par")
```
```python
# ✅ CORRECTO - Lógica correcta
if numero % 2 == 0:
    print("Ha ingresado un número par")  # Cuando ES par
else:
    print("Por favor, ingrese un número par")  # Cuando NO es par
```
**Por qué está mal**: Si `numero % 2 == 0`, significa que SÍ es par, no que no lo es.

**Error 3: Mensajes con formato incorrecto**
```python
# ❌ INCORRECTO - Mensajes incorrectos
print("ha ingresado un numero par")  # Falta mayúscula y tilde
print("Ha ingresado un número Par")  # "Par" no debe ir en mayúscula
print("El número es par")  # Mensaje completamente diferente
```
```python
# ✅ CORRECTO - Mensajes exactos
print("Ha ingresado un número par")
print("Por favor, ingrese un número par")
```
**Por qué está mal**: Los mensajes deben ser exactamente como se especifica, incluyendo mayúsculas y tildes.

**Error 4: Comparar con 1 en lugar de 0**
```python
# ❌ INCORRECTO - Compara con 1
if numero % 2 == 1:  # Solo funciona para impares positivos
    print("Por favor, ingrese un número par")
```
```python
# ✅ CORRECTO - Compara con 0
if numero % 2 == 0:  # Verifica si es par
    print("Ha ingresado un número par")
else:  # Cualquier resto != 0 es impar
    print("Por favor, ingrese un número par")
```
**Por qué está mal**: Los números impares negativos dan resto -1, no 1. Es más seguro comparar si el resto es 0 (par) o no (impar).
