# Problema: Aprobado o Desaprobado

## 🎯 Objetivo

Implementar un programa que reciba una nota numérica y evalúe si el estudiante aprobó (nota ≥ 6) o desaprobó (nota < 6).

## 📥 Entrada

El programa recibirá **UNA línea** con:
- Un número decimal o entero que representa la nota del estudiante
- Ejemplos válidos: `7`, `6.5`, `4`, `10`

**IMPORTANTE**: Debes leer la nota como número (usa `float(input())` o `int(input())`).

## 📤 Salida Esperada

El programa debe imprimir **EXACTAMENTE** una de estas dos palabras (respeta mayúsculas):
- `Aprobado` - si la nota es mayor o igual a 6
- `Desaprobado` - si la nota es menor a 6

**IMPORTANTE**:
- ✅ Imprime SOLO la palabra, sin puntos, sin comillas, sin texto adicional
- ✅ La primera letra DEBE ser mayúscula y el resto minúsculas
- ❌ NO imprimas: "El alumno está Aprobado" o "Aprobado." o "APROBADO"

## 📋 Ejemplos de Ejecución

**Ejemplo 1:**
```
Entrada: 7
Salida: Aprobado
```
Explicación: 7 ≥ 6, por lo tanto está aprobado.

**Ejemplo 2:**
```
Entrada: 6
Salida: Aprobado
```
Explicación: 6 = 6 (justo en el límite), por lo tanto está aprobado.

**Ejemplo 3:**
```
Entrada: 4
Salida: Desaprobado
```
Explicación: 4 < 6, por lo tanto está desaprobado.

**Ejemplo 4:**
```
Entrada: 5.9
Salida: Desaprobado
```
Explicación: 5.9 < 6, por lo tanto está desaprobado (aunque esté cerca).

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura del programa**:
   - ✅ Crear una función llamada exactamente `main()` (sin parámetros)
   - ✅ Toda la lógica debe estar dentro de `main()`
   - ✅ Al final del archivo, incluir: `if __name__ == "__main__": main()`

2. **Lectura de datos**:
   - ✅ Usar `input()` para leer la entrada del usuario
   - ✅ Convertir a número con `int()` o `float()`
   - ❌ NO solicitar datos con mensajes como "Ingrese la nota:"

3. **Comparación**:
   - ✅ Usar el operador de comparación `>=` para verificar si nota >= 6
   - ✅ Usar `if-else` para las dos posibles salidas

4. **Salida de datos**:
   - ✅ Usar `print()` para mostrar el resultado
   - ✅ Formato exacto: `Aprobado` o `Desaprobado` (sin texto adicional)

## 💡 Pistas de Implementación

1. La estructura básica es:
   ```python
   def main():
       nota = float(input())  # Leer la nota
       # Tu código de comparación aquí
       # print() del resultado
   ```

2. Recuerda que el operador `>=` significa "mayor o igual que"

3. El condicional `if-else` te permite manejar dos casos mutuamente excluyentes

## ⚠️ Errores Comunes a Evitar

❌ **Error 1**: Pedir datos con mensajes
```python
nota = float(input("Ingrese la nota: "))  # ¡MAL!
```

❌ **Error 2**: Formato de salida incorrecto
```python
print("El resultado es: Aprobado")  # ¡MAL!
print("aprobado")  # ¡MAL! (minúscula)
```

❌ **Error 3**: No convertir a número
```python
nota = input()  # ¡MAL! queda como texto
if nota >= 6:   # ¡ERROR! no puedes comparar texto con número
```

✅ **Código correcto**:
```python
nota = float(input())
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
```
