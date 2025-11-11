import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_vocal_o_minuscula():
    """Verifica vocal 'o' minúscula"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("perro")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "perro!", f"Se esperaba 'perro!', se obtuvo '{output}'"

def test_vocal_i_minuscula():
    """Verifica vocal 'i' minúscula"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("kiwi")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "kiwi!", f"Se esperaba 'kiwi!', se obtuvo '{output}'"

def test_vocal_A_mayuscula():
    """Verifica vocal 'A' mayúscula"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("CASA")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "CASA!", f"Se esperaba 'CASA!', se obtuvo '{output}'"

def test_consonante_r():
    """Verifica string que termina en 'r'"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("amor")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "amor", f"Se esperaba 'amor', se obtuvo '{output}'"

def test_consonante_l():
    """Verifica string que termina en 'l'"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("sol")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "sol", f"Se esperaba 'sol', se obtuvo '{output}'"
