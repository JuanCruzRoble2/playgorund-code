# Problema: Clasificación de terremoto

## 🎯 Objetivo
Crear un programa que lea una magnitud de terremoto desde la entrada estándar y clasifique según la escala de Richter, imprimiendo una categoría que indica el nivel de intensidad del sismo.

## 📥 Entrada
El programa recibirá **UNA línea** con:
- Un número decimal que representa la magnitud en la escala de Richter
- Ejemplos válidos: `2.5`, `3.7`, `4.8`, `5.5`, `6.3`, `8.0`, `9.5`
- Rango esperado: Generalmente entre 0 y 10 (la escala de Richter es logarítmica)

**IMPORTANTE**: Debes leer la magnitud como número decimal usando `float(input())`.

## 📤 Salida Esperada
El programa debe imprimir **EXACTAMENTE** una de estas clasificaciones:

| Rango de Magnitud | Clasificación |
|-------------------|---------------|
| magnitud < 3 | `Muy leve` |
| 3 ≤ magnitud < 4 | `Leve` |
| 4 ≤ magnitud < 5 | `Moderado` |
| 5 ≤ magnitud < 6 | `Fuerte` |
| 6 ≤ magnitud < 7 | `Muy Fuerte` |
| magnitud ≥ 7 | `Extremo` |

**IMPORTANTE - Formato exacto**:
- ✅ Respetar mayúsculas y minúsculas exactamente como se muestra
- ✅ "Muy Fuerte" lleva espacio y ambas palabras con mayúscula inicial
- ✅ "Muy leve" tiene solo la M mayúscula
- ✅ Usar `print()` para mostrar el resultado
- ❌ NO agregar texto adicional

## 📋 Ejemplos de Ejecución

**Ejemplo 1 - Muy leve**
```
Entrada: 2.5
Salida: Muy leve
```
**Explicación**: 2.5 < 3, por lo tanto es "Muy leve".

**Ejemplo 2 - Leve**
```
Entrada: 3.7
Salida: Leve
```
**Explicación**: 3 ≤ 3.7 < 4, por lo tanto es "Leve".

**Ejemplo 3 - Moderado**
```
Entrada: 4.8
Salida: Moderado
```
**Explicación**: 4 ≤ 4.8 < 5, por lo tanto es "Moderado".

**Ejemplo 4 - Fuerte**
```
Entrada: 5.5
Salida: Fuerte
```
**Explicación**: 5 ≤ 5.5 < 6, por lo tanto es "Fuerte".

**Ejemplo 5 - Muy Fuerte**
```
Entrada: 6.3
Salida: Muy Fuerte
```
**Explicación**: 6 ≤ 6.3 < 7, por lo tanto es "Muy Fuerte".

**Ejemplo 6 - Extremo**
```
Entrada: 8.0
Salida: Extremo
```
**Explicación**: 8.0 ≥ 7, por lo tanto es "Extremo".

**Ejemplo 7 - Caso borde: Exactamente 3**
```
Entrada: 3.0
Salida: Leve
```
**Explicación**: 3.0 cumple con 3 ≤ magnitud < 4, por lo tanto es "Leve".

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura del programa**:
   - ✅ Crear una función llamada exactamente `main()` (sin parámetros)
   - ✅ Toda la lógica debe estar dentro de `main()`
   - ✅ Al final del archivo, incluir: `if __name__ == "__main__": main()`

2. **Lectura de datos**:
   - ✅ Usar `input()` para leer la entrada
   - ✅ Convertir a decimal con `float()`
   - ❌ NO solicitar datos con mensajes como "Ingrese la magnitud:"

3. **Lógica condicional**:
   - ✅ Usar estructura `if-elif-elif-...-else`
   - ✅ Evaluar rangos en orden (menor a mayor)
   - ✅ Usar operadores de comparación: `<`, `>=`
   - ✅ Asegurar que todos los rangos estén cubiertos (6 casos)

4. **Comparaciones de rangos**:
   - `magnitud < 3` → "Muy leve"
   - `magnitud < 4` → "Leve" (ya sabemos que >= 3)
   - `magnitud < 5` → "Moderado"
   - `magnitud < 6` → "Fuerte"
   - `magnitud < 7` → "Muy Fuerte"
   - `else` → "Extremo" (magnitud >= 7)

5. **Salida de datos**:
   - ✅ Usar `print()` para mostrar el resultado
   - ✅ Formato exacto según la tabla (respetar mayúsculas/minúsculas)

## 💡 Pistas de Implementación

**Pista 1 - Estructura completa con if-elif-else**:
```python
def main():
    magnitud = float(input())  # Lee la magnitud

    if magnitud < 3:
        print("Muy leve")
    elif magnitud < 4:
        print("Leve")
    elif magnitud < 5:
        print("Moderado")
    elif magnitud < 6:
        print("Fuerte")
    elif magnitud < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")
```
**Nota**: Esta estructura aprovecha que cada `elif` solo se evalúa si los anteriores fueron `False`.

**Pista 2 - Orden de evaluación**:
Es importante evaluar en orden de menor a mayor:
- Empieza por magnitud < 3 (el rango más bajo)
- Continúa con < 4, < 5, < 6, < 7
- Termina con `else` para magnitud >= 7

## ⚠️ Errores Comunes a Evitar

**Error 1: No leer la entrada con input()**
```python
# ❌ INCORRECTO - Valor hardcodeado
def main():
    magnitud = 5.5  # No lee la entrada
    if magnitud < 3:
        print("Muy leve")
```
```python
# ✅ CORRECTO - Lee con input()
def main():
    magnitud = float(input())  # Lee desde entrada estándar
    if magnitud < 3:
        print("Muy leve")
```
**Por qué está mal**: El programa debe leer desde la entrada estándar.

**Error 2: Condiciones incorrectas o incompletas**
```python
# ❌ INCORRECTO - Rangos mal definidos
magnitud = float(input())
if magnitud < 3:
    print("Muy leve")
elif magnitud < 3 and magnitud < 4:  # ¡Condición imposible!
    print("Leve")
```
```python
# ✅ CORRECTO - Rangos bien definidos
magnitud = float(input())
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:  # Ya sabemos que magnitud >= 3
    print("Leve")
```
**Por qué está mal**: Si `magnitud < 3` es False, entonces `magnitud >= 3`, por lo que la segunda condición es redundante.

**Error 3: Formato de salida incorrecto**
```python
# ❌ INCORRECTO - Mayúsculas/minúsculas incorrectas
print("muy leve")      # Falta mayúscula en "Muy"
print("MUY FUERTE")    # Todo en mayúsculas
print("Muy fuerte")    # "fuerte" debe tener "F" mayúscula
```
```python
# ✅ CORRECTO - Formato exacto
print("Muy leve")
print("Muy Fuerte")
```
**Por qué está mal**: Los strings deben coincidir exactamente con la especificación.

**Error 4: Mayúsculas incorrectas**
```python
# ❌ INCORRECTO - Formato incorrecto
return "muy leve"       # Falta mayúscula en "Muy"
return "MUY FUERTE"     # Todo en mayúsculas
return "Muy fuerte"     # "fuerte" debe tener "F" mayúscula
```
```python
# ✅ CORRECTO - Formato exacto
return "Muy leve"
return "Muy Fuerte"
```
**Por qué está mal**: Los strings deben coincidir exactamente con la especificación, incluyendo mayúsculas.

**Error 5: Olvidar el caso else**
```python
# ❌ INCORRECTO - Falta el caso >= 7
if magnitud < 3:
    return "Muy leve"
# ... más condiciones ...
elif magnitud < 7:
    return "Muy Fuerte"
# ¿Qué pasa si magnitud >= 7? ¡No retorna nada!
```
```python
# ✅ CORRECTO - Cubre todos los casos
if magnitud < 3:
    return "Muy leve"
# ... más condiciones ...
elif magnitud < 7:
    return "Muy Fuerte"
else:
    return "Extremo"  # Cubre magnitud >= 7
```
**Por qué está mal**: Siempre debe haber un caso que cubra todos los valores posibles.
