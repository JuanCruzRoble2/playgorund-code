import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_promedio_decimales():
    """Test con decimales"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7.5\n8.5\n9.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "8.333333333333334"
    assert output == expected, f"Se esperaba '{expected}', se obtuvo '{output}'"

def test_promedio_iguales():
    """Test números iguales"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("15\n15\n15")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "15.0"
    assert output == expected, f"Se esperaba '{expected}', se obtuvo '{output}'"

