# =============================================================================
#                           Importações
# =============================================================================

import re
import os
import numpy as np
from numpy import radians
from numpy import degrees

# =============================================================================
#                       Variáveis Globais
# =============================================================================

F=[1,1,2]
fac=np.math.factorial
mat=np.linalg

# =============================================================================
#                       Inicialização
# =============================================================================
class Iniciar():
    def __init__(self, n):
        self.n = n
        
# =============================================================================
#                       Sequência de Fibonacci
# =============================================================================

class Fibonacci(Iniciar):

    def Fib(self):
        n=self.n
        if n>1:
            for i in range(2, n):
                m=F[i]
                F[i]=F[i-1]+F[i-2]
                F.append(m)
            del(F[n])
            return F
        else:
            return [F[n]]
    
    def fib(self):
        n=self.n
        if n>1:
            for i in range(2, n):
                m=F[i]
                F[i]=F[i-1]+F[i-2]
                F.append(m)
            del(F[n])
            return F[n-1]
        else:
            return F[n]

# =============================================================================
#                       Trigonometria
# =============================================================================

class Trigonometria(Iniciar):
   
    def sin(self):
        x=(self.n)
        y=np.sin(radians(x))
        if x%90==0:
            z=int(y)
            return float(z)
        else:
            return  y 
    
    def cos(self):
        x=self.n
        y=np.cos(radians(x))
        if x%90==0:
            z=int(y)
            return float(z)
        else:
            return y
    
    def tg(self):
        x=self.n
        y=np.tan(radians(x))
        if x%45==0:
            z=int(y)
            if y>0:
                return float(z)+1
            else:
                return float(z)
        else:
            return y
    
    def cotg(self):
        x=self.n
        y=1/np.tan(radians(x))
        return(y)
        
    def sec(self):
        x=self.n
        y=1/np.cos(radians(x))
        return y
        
    def cossec(self):
        x=self.n
        y=1/np.sin(radians(x))
        return y
    
    def asin(self):
        x=self.n
        y=np.arcsin(x)
        return degrees(y)
    
    def acos(self):
        x=self.n
        y=np.arccos(x)
        return degrees(y)
    
    def atg(self):
        x=self.n
        y=np.arctan(x)
        return degrees(y)
    
    def acotg(self):
        x=self.n
        y=1/x
        z=np.arctan(y)
        return degrees(z)
    
# =============================================================================
#               Fatorial de um número inteiro           
# =============================================================================

class Fatorial(Iniciar):
        
    def Fac(self):
        
        x = self.n
        
        if x>-1:
                      
            y = fac(x)
            return y

        else:
            return ('digite um valor positivo')
        
# =============================================================================
#               Análise combinatória        
# =============================================================================
class Combinar():
    
    def __init__(self, p, n):
        
        self.p=p
        self.n=n
        
    def Arranjo(self):
        
        p=self.p
        n=self.n
        y=fac(p)/fac(p-n)
        return y
    
    def Combina(self):
        
        p=self.p
        n=self.n
        #fac=np.math.factorial
        y=fac(p)/(fac(n)*fac(p-n))
        return y
      
# =============================================================================
#               Logaritmo
# =============================================================================

class Logaritmo(Iniciar):
    
    def ln(self):
        n=self.n
        x=np.log(n)
        return x

    def log10(self):
        n=self.n
        x=np.log10(n)
        return x

    def log2(self):
        n=self.n
        x=np.log2(n)
        return x
    
# =============================================================================
#               Raíses de um polinomio 
# =============================================================================

class Solver(Iniciar):

    def solve(self):
        n=self.n
        p = np.poly1d(n)
        r=np.roots(p)
        return r.tolist()
    
# =============================================================================
#                   Matrizes
# =============================================================================
    
class Matriz(Iniciar):
    
    def Inv(self):
        n=self.n
        y=mat.inv(n)
        return y
    
    def Det(self):
        n=self.n
        y=mat.det(n)
        return y
    
    
    
    
    