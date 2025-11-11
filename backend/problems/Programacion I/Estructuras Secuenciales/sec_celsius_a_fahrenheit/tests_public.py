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

def test_0_celsius():
    """Test 0°C = 32°F"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "32.0"
    assert output == expected, f"Se esperaba '{expected}', se obtuvo '{output}'"

def test_100_celsius():
    """Test 100°C = 212°F"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("100")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "212.0"
    assert output == expected, f"Se esperaba '{expected}', se obtuvo '{output}'"

