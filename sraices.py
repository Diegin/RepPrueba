import sympy as sp
# Metodo de Bisección 
def bisec(f,a,b,E): 
    x=sp.symbols('x');
    er=1; i=1; xo=1;
    if f.subs(x,a)*f.subs(x,b)>0:
        print('Intervalo Incorrecto')
    else:
        #print("{0:10s}\t {1:10s}\t {2:10s}\t {3:15s}\t {4:10s}".format('Iteracion','a','b','xn','Error'));
        while er>E:
            xf=(a+b)/2;    # Calculando la solucion
            # Calculando el error, tomando el cuenta la 1er iteracion
            if i==1:        
                er=1;
                print("{0:10d}\t {1:.12f}\t {2:.12f}\t {3:.12f}\t {4:.12f}".format(i,a,b,xf,er));
            else:
                er=abs((xf-xo)/xo)  
                # Se imprimen los resultados 
                print("{0:10d}\t {1:.12f}\t {2:.12f}\t {3:.12f}\t {4:.12f}".format(i,a,b,xf,er));
                # Si el error es menor a lo establecido, termina con el programa
            if er<E:
                print("\nLa solucion numérica es x =",xf, "con",i," iteraciones")
                break;
                # Reasignando "a" o "b" segun diga el algoritmo
            if f.subs(x,a)*f.subs(x,xf)<0:
                b=xf
            else:
                a=xf
            xo=xf;
            i=i+1;
        return xf        
    
            
# Metodo de Falsa Posicion
def fpos(f,a,b,E): 
    x=sp.symbols('x');
    er=1; i=1; xo=1;
    if f.subs(x,a)*f.subs(x,b)>0:
        print('Intervalo Incorrecto')
    else:
        #print("{0:10s}\t {1:10s}\t {2:10s}\t {3:15s}\t {4:10s}".format('Iteracion','a','b','xn','Error'));
        while er>E:
            xf=(a*f.subs(x,b)-b*f.subs(x,a))/(f.subs(x,b)-f.subs(x,a))  
            xf=float(xf)
            # Calculando la solucion
            # Calculando el error, tomando el cuenta la 1er iteracion
            if i==1:        
                er=1
                print("{0:10d}\t {1:.12f}\t {2:.12f}\t {3:.12f}\t {4:.12f}".format(i,a,b,xf,er))
            else:
                er=abs((xf-xo)/xo)  
                # Se imprimen los resultados 
                print("{0:10d}\t {1:.12f}\t {2:.12f}\t {3:.12f}\t {4:.12f}".format(i,a,b,xf,er))
                # Si el error es menor a lo establecido, termina con el programa
            if er<E:
                print("\n La solucion numerica es x =",xf, "con",i," iteraciones")
                break;
                #Reasignando "a" o "b" segun diga el algoritmo
            if f.subs(x,a)*f.subs(x,xf)<0:
                b=xf
            else:
                a=xf
            xo=xf;
            i=i+1;
        return xf

# Método de Newton
def newton(f,xo,E):
    x=sp.symbols('x');
    er=1; i=1;
    fp=sp.diff(f,x) 
    while er>E:
        xf=xo-(f.subs(x,xo))/(fp.subs(x,xo))
        xf=float(xf)
        # Calculando el error, tomando el cuenta la 1er iteracion
        if i==1:        
            print("{0:10d}\t {1:.12f}\t {2:.12f}".format(i,xf,er))
        else:
            er=abs((xf-xo)/xo)  
        # Se imprimen los resultados 
        print("{0:10d}\t {1:.12f}\t {2:.12f}".format(i,xf,er))
        # Si el error es menor a lo establecido, termina con el programa
        if er<E:
            print("\n La solucion numerica es x =",xf, "con",i," iteraciones")
            break
        # Aseguramos que se rompa por si no converge el método
        if i==15:
            break
        # Almacenando la última solución
        xo=xf;
        i=i+1;
    return xf

# Método de Secante
def secante(f,x0,x1,E):
    x=sp.symbols('x');
    er=1; i=1;
    while er>E:
        x2=x1-(f.subs(x,x1)*(x0-x1))/(f.subs(x,x0)-f.subs(x,x1))
        x2=float(x2)
        # Calculando el error, tomando el cuenta la 1er iteracion
        if i==1:        
            print("{0:10d}\t {1:.12f}\t {2:.12f}".format(i,x2,er))
        else:
            er=abs((x2-x1)/x1)  
        # Se imprimen los resultados 
        print("{0:10d}\t {1:.12f}\t {2:.12f}".format(i,x2,er))
        # Si el error es menor a lo establecido, termina con el programa
        if er<E:
            print("\n La solucion numerica es x =",x2, "con",i," iteraciones")
            break
        # Aseguramos que se rompa por si no converge el método
        if i==15:
            break
        # Almacenando la última solución
        x0=x1; x1=x2;
        i=i+1;
    return x2
