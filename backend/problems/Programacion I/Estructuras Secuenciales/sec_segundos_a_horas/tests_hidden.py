import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_1800_segundos():
    """Test 1800 segundos (0.5 horas)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1800")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "1800 segundos equivalen a 0.5 horas"
    assert output == expected, f"Se esperaba '{expected}', se obtuvo '{output}'"

def test_0_segundos():
    """Test 0 segundos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "0 segundos equivalen a 0.0 horas"
    assert output == expected, f"Se esperaba '{expected}', se obtuvo '{output}'"

