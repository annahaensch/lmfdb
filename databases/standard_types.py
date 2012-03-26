from type_generation import String, Array, Dict, Int, Anything, Float

def PolynomialAsString(convention):
    class ParametrizedPolynomialAsString(String):
        def sage(self):
            return convention(self)
        
        def latex(self, letter = convention.variable_name()):
            return self.sage().change_variable_name(letter)._latex_()
        
    return ParametrizedPolynomialAsString

class PermutationAsList(Array(Int)):
    def cycle_string(self):
        from sage.combinat.permutation import Permutation
        return Permutation(self).cycle_string()

class TooLargeInt(String):
    pass
    
class LabelString(String):
    pass
    
FiniteSequence = Array
FiniteSet = Array


class GAP_GroupLabel(LabelString):
    pass
    
def PrimeIndexedSequence(x):
    return Array(x)

def AlgebraicNumberPolynomialString(pol_as_string_convention):
    class ParametrizedAlgebraicNumberPolynomialString(String):
        pass
    return ParametrizedAlgebraicNumberPolynomialString

class AlgebraicNumberString_Root(String):
    z = lambda n: e^(pi*I/n)
    def eval(self):
        tmp = self.replace("^","**")
        return eval(tmp,{"__builtins__":None},{"z":AlgebraicNumberString_Root.z})