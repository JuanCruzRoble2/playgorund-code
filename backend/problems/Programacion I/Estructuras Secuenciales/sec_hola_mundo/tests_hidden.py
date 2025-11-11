import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_mayuscula_inicial():
    """Verifica que la H sea mayúscula"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    assert output.startswith("Hola"), f"El mensaje debe comenzar con 'Hola' (H mayúscula)"
    assert output == "Hola Mundo!", f"Se esperaba 'Hola Mundo!', se obtuvo '{output}'"

def test_signo_exclamacion():
    """Verifica que termine con signo de exclamación"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    assert output.endswith("!"), f"El mensaje debe terminar con '!'"
    assert output == "Hola Mundo!", f"Se esperaba 'Hola Mundo!', se obtuvo '{output}'"

def test_formato_exacto():
    """Verifica formato exacto sin espacios extras"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    assert output == "Hola Mundo!", f"El formato debe ser exacto: 'Hola Mundo!'"
    assert " " in output, "Debe haber un espacio entre 'Hola' y 'Mundo'"
    assert output.count(" ") == 1, "Debe haber exactamente un espacio"