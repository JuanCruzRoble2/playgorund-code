# Problema: Mayor de dos números

## 🎯 Objetivo
Crear un programa que lea dos números desde la entrada estándar y muestre el número mayor de los dos. Si ambos números son iguales, puede mostrar cualquiera de ellos.

## 📥 Entrada
El programa recibirá **exactamente dos valores** desde la entrada estándar:
- **Tipo de dato**: Números decimales (flotantes)
- **Cómo leerlos**: Usar `input()` y convertir con `float()` para cada uno
- **Formato**: Cada número en una línea separada
- **Ejemplos de valores válidos**: `5.0`, `10`, `-3.5`, `0`, `7.8`

```python
a = float(input())  # Lee el primer número
b = float(input())  # Lee el segundo número
```

**IMPORTANTE**: Se usa `float()` en lugar de `int()` porque los números pueden tener decimales.

## 📤 Salida Esperada
El programa debe imprimir **exactamente una línea** con el número mayor:
- Si `a > b`, imprimir el valor de `a`
- Si `b > a`, imprimir el valor de `b`
- Si `a == b`, imprimir cualquiera de los dos (son iguales)

**IMPORTANTE - Formato exacto**:
- ✅ Imprimir solo el número, sin texto adicional
- ✅ Python imprimirá automáticamente el formato del número (ej: `10.0` o `10`)
- ❌ NO imprimir mensajes como "El mayor es:", "Resultado:", etc.
- ❌ NO agregar espacios extras o caracteres adicionales

## 📋 Ejemplos de Ejecución

**Ejemplo 1 - Primer número mayor**
```
Entrada: 5
Entrada: 10
Salida: 10
```
**Explicación**: Como 10 > 5, se imprime 10.

**Ejemplo 2 - Segundo número mayor**
```
Entrada: 20
Entrada: 15
Salida: 20
```
**Explicación**: Como 20 > 15, se imprime 20.

**Ejemplo 3 - Números iguales**
```
Entrada: 7
Entrada: 7
Salida: 7
```
**Explicación**: Como ambos son iguales (7 == 7), se puede imprimir cualquiera (en este caso 7).

**Ejemplo 4 - Números decimales**
```
Entrada: 3.5
Entrada: 2.8
Salida: 3.5
```
**Explicación**: Como 3.5 > 2.8, se imprime 3.5.

**Ejemplo 5 - Números negativos**
```
Entrada: -5
Entrada: -10
Salida: -5
```
**Explicación**: Como -5 > -10 (menos negativo es mayor), se imprime -5.

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. La función DEBE llamarse exactamente `main`
2. La función NO debe recibir parámetros
3. Debe incluir `if __name__ == "__main__": main()` al final (ya provisto)

### ✅ Lectura de datos:
1. Leer el primer número: `a = float(input())`
2. Leer el segundo número: `b = float(input())`
3. NO imprimir prompts (mensajes que pidan datos)
4. Usar `float()` para soportar decimales

### ✅ Lógica condicional:
1. Comparar usando `>` o `>=`
2. Puedes usar `if-else` o `if-elif-else`
3. Manejar el caso donde `a == b` (son iguales)

### ✅ Salida de datos:
1. Usar `print()` con el número mayor
2. Imprimir SOLO el número, sin texto adicional
3. Sin espacios extras, sin caracteres adicionales

## 💡 Pistas de Implementación

**Pista 1 - Estructura básica con if-else**:
```python
def main():
    a = float(input())
    b = float(input())

    if a > b:
        print(a)
    else:
        print(b)  # Si b >= a, imprime b
```
Esta solución funciona porque si `a` no es mayor que `b`, entonces `b` debe ser mayor o igual a `a`.

**Pista 2 - Estructura con if-elif-else**:
```python
def main():
    a = float(input())
    b = float(input())

    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print(a)  # Son iguales, imprimir cualquiera
```

**Pista 3 - Usando la función max() (avanzado)**:
Python tiene una función incorporada `max()` que devuelve el mayor de dos o más valores:
```python
def main():
    a = float(input())
    b = float(input())
    print(max(a, b))
```

## ⚠️ Errores Comunes a Evitar

**Error 1: Usar int() en lugar de float()**
```python
# ❌ INCORRECTO - No maneja decimales
a = int(input())  # Falla si el input es "3.5"
b = int(input())
```
```python
# ✅ CORRECTO - Maneja enteros y decimales
a = float(input())  # Funciona con "3", "3.5", "-10", etc.
b = float(input())
```
**Por qué está mal**: `int()` falla si se ingresa un número decimal. `float()` acepta tanto enteros como decimales.

**Error 2: Imprimir mensajes adicionales**
```python
# ❌ INCORRECTO - Texto adicional
if a > b:
    print("El mayor es:", a)
else:
    print("El mayor es:", b)
```
```python
# ✅ CORRECTO - Solo el número
if a > b:
    print(a)
else:
    print(b)
```
**Por qué está mal**: Solo debe imprimirse el número, sin etiquetas ni texto adicional.

**Error 3: No manejar el caso de igualdad**
```python
# ❌ INCORRECTO - Falta el caso a == b
if a > b:
    print(a)
elif b > a:
    print(b)
# ¿Qué pasa si a == b? No imprime nada
```
```python
# ✅ CORRECTO - Todos los casos cubiertos
if a > b:
    print(a)
else:
    print(b)  # Cubre b > a y a == b
```
**Por qué está mal**: Si no cubres todos los casos, el programa podría no imprimir nada cuando los números son iguales.

**Error 4: Comparación con >= en ambas ramas**
```python
# ❌ INCORRECTO - Lógica redundante
if a >= b:
    print(a)
if b >= a:  # Esto podría ejecutarse también
    print(b)
```
```python
# ✅ CORRECTO - Usa if-else
if a >= b:
    print(a)
else:
    print(b)
```
**Por qué está mal**: Sin `else`, ambas condiciones podrían ser verdaderas (cuando `a == b`), imprimiendo dos números en lugar de uno.
