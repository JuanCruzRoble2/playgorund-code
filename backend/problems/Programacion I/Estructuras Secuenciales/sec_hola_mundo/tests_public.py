import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_mensaje_correcto():
    """Verifica que el mensaje sea exactamente 'Hola Mundo!'"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    assert output == "Hola Mundo!", f"Se esperaba 'Hola Mundo!', se obtuvo '{output}'"

def test_sin_entrada():
    """Verifica que no se solicite entrada del usuario"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("")
    sys.stdout = StringIO()

    try:
        student.main()
        output = sys.stdout.getvalue().strip()
    except EOFError:
        output = None
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

    assert output is not None, "No debes usar input() en este ejercicio"
    assert output == "Hola Mundo!", f"Se esperaba 'Hola Mundo!', se obtuvo '{output}'"