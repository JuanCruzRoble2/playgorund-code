import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_limite_muy_leve_leve_inferior():
    """Verifica límite entre Muy leve y Leve (2.9)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("2.9")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy leve", f"Se esperaba 'Muy leve', se obtuvo '{output}'"

def test_limite_muy_leve_leve_superior():
    """Verifica límite entre Muy leve y Leve (3.0)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("3.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Leve", f"Se esperaba 'Leve', se obtuvo '{output}'"

def test_limite_fuerte_muy_fuerte_superior():
    """Verifica límite entre Fuerte y Muy Fuerte (6.0)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("6.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy Fuerte", f"Se esperaba 'Muy Fuerte', se obtuvo '{output}'"

def test_limite_muy_fuerte_extremo_inferior():
    """Verifica límite entre Muy Fuerte y Extremo (6.99)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("6.99")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy Fuerte", f"Se esperaba 'Muy Fuerte', se obtuvo '{output}'"

def test_limite_muy_fuerte_extremo_superior():
    """Verifica límite entre Muy Fuerte y Extremo (7.0)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Extremo", f"Se esperaba 'Extremo', se obtuvo '{output}'"

def test_magnitud_muy_alta():
    """Verifica magnitud muy alta (9.5)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("9.5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Extremo", f"Se esperaba 'Extremo', se obtuvo '{output}'"
