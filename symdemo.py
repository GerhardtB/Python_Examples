import sympy as sym
x=sym.symbols("x")
t=sym.symbols("t")
# substitution with numerical value
expr=x**2+2*x-1
print(expr.subs(x,1))
# substitution with an algabraic expression
print(expr.subs(x,2*t/3-1/t))
# use expand() to expand the function
print(sym.expand(expr.subs(x,2*t/3-1/t)))
#integration example
print(1.0/sym.sqrt(1.0+x**2),x)
print("integrated: "+str(sym.integrate(1.0/sym.sqrt(1.0+x**2),x)))
#differentiation example
print("differentiate "+str(1+sym.sin(x)**2))
print(sym.diff(1+sym.sin(x)**2))
#ODE example
y=sym.Function("y")
print("solve the ODE: "+str(sym.Eq(y(t).diff(t,t)-y(t))))
print(sym.dsolve(sym.Eq(y(t).diff(t,t)-y(t),sym.exp(t)),y(t)))
