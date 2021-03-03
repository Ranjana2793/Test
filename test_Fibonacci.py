from Fibonacci import Fibonacci
from parameterized import parameterized, parameterized_class
def test_Fibonacci():
    assert Fibonacci(0)=="Please enter a positive integer"

def test_Fibonacci_with_1stterm():
   assert Fibonacci(1)==0

def test_Fibonacci_with_nterm():
    assert Fibonacci(2) == [0,1]
