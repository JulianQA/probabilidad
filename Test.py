import unittest
import partilinea
class TestmyFunctions(unittest.TestCase):
    def testpro(self):
        a = [[(-3,-1)],[(0,-2)],[(0,1)],[(2,0)]]
        b = 2
        esperado = 0.05263157894736841
        res = partilinea.proba(a,b)
        self.assertEqual(esperado,res)
    def testtrans(self):
        a = [[(1,0)],[(0,-1)]]
        b = [[(0,1)],[(1,0)]]
        esperado = -0.9999999999999998
        res = partilinea.trans(a,b)
        self.assertEqual(esperado,res)
if __name__ == '__main__':
    unittest.main()
        
