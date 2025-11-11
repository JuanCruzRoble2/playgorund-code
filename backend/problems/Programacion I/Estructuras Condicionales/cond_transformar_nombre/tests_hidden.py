import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_nombre_completo_mayusculas():
    """Verifica opción 1 con nombre completo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Ana Maria Lopez\n1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "ANA MARIA LOPEZ", f"Se esperaba 'ANA MARIA LOPEZ', se obtuvo '{output}'"

def test_nombre_completo_minusculas():
    """Verifica opción 2 con nombre completo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("CARLOS RODRIGUEZ\n2")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "carlos rodriguez", f"Se esperaba 'carlos rodriguez', se obtuvo '{output}'"

def test_nombre_completo_title():
    """Verifica opción 3 con nombre completo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("jose garcia\n3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Jose Garcia", f"Se esperaba 'Jose Garcia', se obtuvo '{output}'"

def test_opcion_cero():
    """Verifica opción 0 (inválida)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("test\n0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Opción inválida", f"Se esperaba 'Opción inválida', se obtuvo '{output}'"

def test_opcion_negativa():
    """Verifica opción negativa (inválida)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("test\n-1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Opción inválida", f"Se esperaba 'Opción inválida', se obtuvo '{output}'"
