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

def test_muy_leve():
    """Verifica clasificación Muy leve (magnitud < 3)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("2.5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy leve", f"Se esperaba 'Muy leve', se obtuvo '{output}'"

def test_leve():
    """Verifica clasificación Leve (3 ≤ magnitud < 4)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("3.7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Leve", f"Se esperaba 'Leve', se obtuvo '{output}'"

def test_moderado():
    """Verifica clasificación Moderado (4 ≤ magnitud < 5)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("4.8")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Moderado", f"Se esperaba 'Moderado', se obtuvo '{output}'"

def test_fuerte():
    """Verifica clasificación Fuerte (5 ≤ magnitud < 6)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5.5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Fuerte", f"Se esperaba 'Fuerte', se obtuvo '{output}'"

def test_muy_fuerte():
    """Verifica clasificación Muy Fuerte (6 ≤ magnitud < 7)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("6.3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy Fuerte", f"Se esperaba 'Muy Fuerte', se obtuvo '{output}'"

def test_extremo():
    """Verifica clasificación Extremo (magnitud ≥ 7)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("8.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Extremo", f"Se esperaba 'Extremo', se obtuvo '{output}'"
