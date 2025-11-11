import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_25_celsius():
    """Test 25°C"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("25")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "77.0"
    assert output == expected, f"Se esperaba '{expected}', se obtuvo '{output}'"

def test_negativo():
    """Test temperatura negativa"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("-40")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "-40.0"
    assert output == expected, f"Se esperaba '{expected}', se obtuvo '{output}'"

