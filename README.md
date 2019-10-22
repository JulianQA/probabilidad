# Probability
In the first file 'probabilidad.py', you can calculate the probability that a particle is in a particular position within a system. It also calculates the probability of moving from one vector to another.
#  How does it work?
First, you must download the .py file whose name is 'probabilidad.py'. It's a library implemented in Python, which works based on functions, each of these receives the necessary parameters to execute the desired operation and return the result of each operation, 
then you can see some examples:
```python
def proba(vec,pos): #receive the vector and position
    nor = norma(vec)
    arr = vec[pos]
    p = arr[0][0]**2 + arr[0][1]**2
    res = p/(nor)**2
    return res #returns the probability that you are in the position you gave
def trans(vec1,vec2): #receive two vectors
    arr = multiplicacion_matrices(mat_adjunta(vec2),vec1)
    aba = norma(vec1)*norma(vec2)
    izq = arr[0][0][0] / aba
    der = arr[0][0][1] / aba
    res = izq + der
    return res # returns the probability of moving from the first vector to the second
```
+ if you need to try any function, before using the library unittest, you must do the following:
```python
print(function_name_of_test(the_parameters_that_the_function receives))
```
# Test
If you need to test your results, you must download the .py file called 'Test.py'. The files 'probabilidad.py' and 'Test.py' must be in the same folder so that it can be executed correctly. Example of how it should be done:
```python
import unittest
import partilinea
class TestmyFunctions(unittest.TestCase):
    def testpro(self):
        a = [[(-3,-1)],[(0,-2)],[(0,1)],[(2,0)]] #the value you will enter
        b = 2 #the value you will enter
        esperado = 0.05263157894736841 #the value you expect
        res = partilinea.proba(a,b) #the value that the function throws
        self.assertEqual(esperado,res)
    def testtrans(self):
        a = [[(1,0)],[(0,-1)]] #the value you will enter
        b = [[(0,1)],[(1,0)]] #the value you will enter
        esperado = -0.9999999999999998 #the value you expect
        res = partilinea.trans(a,b) #the value that the function throws
        self.assertEqual(esperado,res)
if __name__ == '__main__':
    unittest.main()
#############################
    
    In the Python console you should see:
    ..............................
    Ran 3 tests in (your time)s

    OK
    ..............................
    else, should correct the error
```
# Made by
+ Julián Quintero.
+ Systems Engineer.
+ Escuela Colombiana de Ingeniería Julio Garavito.
