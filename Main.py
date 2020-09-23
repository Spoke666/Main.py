# =============================================================================
#                    Executador da calculadora  
# =============================================================================

from Class import *


os.system('clear') or None
print('\n Bem Vindo ao Kalpy 0.0.9 !!! \n \n Digite a função em seguida o número. \n \n Digite "h" para obter ajuda. \n \n Escreva "sair" para sair...')

while True:

    a=input('-> ') 
    b=re.sub('[-,.0-9]','',a)       # Função base
    c=re.sub('[^-.0-9]','',a)      # Números retorno
    
    # print(a)
    # print(b)
    # print(c)
        
    try:
        
# =============================================================================
#                           Sair
# =============================================================================
        
        if a=='sair':
            print('sair')
            os.system('clear') or None
            break
      
# =============================================================================
#                           Ajuda  
# =============================================================================
        
        if a=='h':            
            h=open('Help.txt','r')
            h1=h.read()
            print(h1)
            h.close()
# =============================================================================
#                       Executador Fibonacci
# =============================================================================
        
        n=1000000     # limita o número de interações
        
        if b=='Fib()':
            if int(float(c))>n:
                print('Não quebre seu computador pfv!!!')
                     
            elif int(c)>0:
                
                fib=Fibonacci(int(c))
                print(a+' = ', fib.Fib())
                            
            else:
                print('Operação Inválida')
                
        if b=='fib()':
            
            if int(float(c))>n:
                print('Não quebre seu computador pfv!!!')
                          
            elif int(c)>0:
                fib=Fibonacci(int(c))
                print(a+' = ', fib.fib())
                            
            else:
                print('Operação Inválida')
                
# =============================================================================
#                      Executador Trigonometrico
# =============================================================================

        if b=='sin()':
            trig=Trigonometria(float(c))
            print(trig.sin())
        
        if b=='cos()':
            trig=Trigonometria(float(c))
            print(trig.cos())
                
        if b=='tg()':
            trig=Trigonometria(float(c))
            print(trig.tg())

        if b=='cotg()':
            trig=Trigonometria(float(c))
            print(trig.cotg())
                
        if b=='sec()':
            trig=Trigonometria(float(c))
            print(trig.sec())
                
        if b=='cossec()':
            trig=Trigonometria(float(c))
            print(trig.cossec())
                
        if b=='asin()':
            trig=Trigonometria(float(c))
            print(trig.asin())

        if b=='acos()':
            trig=Trigonometria(float(c))
            print(trig.acos())

        if b=='atg()':
            trig = Trigonometria(float(c))
            print(trig.atg())
            
        if b=='acotg()':
            trig = Trigonometria(float(c))
            print(trig.acotg())

# =============================================================================
#                       Executador Fatorial
# =============================================================================
        
        if b=='fac()':
            if int(c)>=0:
                fac = Fatorial(int(c))
                print(fac.Fac()) 
            else:
                print('Operação Inválida')
        
# =============================================================================
#                       Executador Combinatório
# =============================================================================
        
        if b=='A()':
            c=a[1:]
            d=list(eval(c))
            p,n=d[0],d[1]
            comb=Combinar(p,n)
            print(comb.Arranjo())

        if b=='C()':
            c=a[1:]
            d=list(eval(c))
            p,n=d[0],d[1]
            comb=Combinar(p,n)
            print(comb.Combina())

# =============================================================================
#                       Executador Logarítimo
# =============================================================================
        
        if b=='ln()':
            
            if float(c)>=0:
                log=Logaritmo(float(c))
                print(log.ln())
                
            else:
                print('Operação Inválida')

        if b=='log()':
            
            if float(c)>=0:
                log=Logaritmo(float(c))
                print(log.log10())
                
            else:
                print('Operação Inválida')                

        if b=='logd()':
            
            if float(c)>=0:
                log=Logaritmo(float(c))
                print(log.log2())

            else:
                print('Operação Inválida')

# =============================================================================
#                       Executador Polinomial
# =============================================================================
            
        if b=='solve()':
            c=a[5:]
            d=list(eval(c))
            s=Solver(d)
            p=np.poly1d(d)
            print(p,'= 0  ->  x =', s.solve())
            
# =============================================================================
#                       Executador Matricial      
# =============================================================================
 
        if a[:3]=='Inv':
            c=a[4:(len(a)-1)]
            d=np.array(list(eval(c)))
            M=Matriz(d)
            print(M.Inv())
            
        if a[:3]=='Det':
            c=a[4:(len(a)-1)]
            d=np.array(list(eval(c)))
            M=Matriz(d)
            print(M.Det())
        
# =============================================================================
#                      Executador Cálculos Básicos       
# =============================================================================
        try:            # Quem diria que um try dentro de outro resolve bug kkk
            try:      
                print(eval(a))
                
# =============================================================================
#                           Retorna Errors no código         
# =============================================================================               
                
            except ZeroDivisionError:
                print('inf')
        except ValueError:
            print('Error1')
        except SyntaxError:
            print('Error2')
        except:
            pass            
        
    except:
        pass  