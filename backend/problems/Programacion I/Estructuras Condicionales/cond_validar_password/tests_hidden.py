import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_password_valida_10():
    """Verifica contraseña válida de 10 caracteres"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("mypass1234")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado una contraseña correcta", f"Se esperaba 'Ha ingresado una contraseña correcta', se obtuvo '{output}'"

def test_password_vacia():
    """Verifica contraseña vacía"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres", f"Se esperaba mensaje de error, se obtuvo '{output}'"

def test_password_limite_inferior():
    """Verifica límite inferior (7 caracteres)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("pass123")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres", f"Se esperaba mensaje de error, se obtuvo '{output}'"
