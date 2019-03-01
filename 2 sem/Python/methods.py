def newtons_method(x0,f,f_der,eps):
	while True:
		x1 = x0 - (f(x0)/f_der(x0))
		if abs(x1-x0) < eps:
			return x1
		x0 = x1

def newtons_simplified(x0,f,f_der,eps):
	x1 = x0 - (f(x0)/f_der(x0))
	while True:
		xn = x1 - (f(x1)/f_der(x0))
		if abs(xn-x1) < eps:
			return xn
		x1 = xn

def false_position(a,b,f,f_der,eps):
	while True:
		x1 = a - (f(a)*(b-a)/(f(b)-f(a)))
		if abs(x1-a) < eps:
			return x1
		a = x1

# выбрать коэффициент к, знак определять по знаку первой производной
def iterations(x0,f,f_der,k,eps):
	while True:
		x1 = x0 - k*f(x0)	
		if abs(x1-x0) < eps:
			return x1
		x0 = x1  

def secant(x0,x1,f,f_der,eps):
	x1 = x0+eps
	while True:
		xn = x1 - (f(x1)*(x1-x0)/(f(x1)-f(x0)))
		if abs(xn-x1) < eps:
			return xn
		x0 = x1
		x1 = xn


def chord(a,b,f,f_der,eps):
	while True:
	    xn = b - (f(b)*(b-a)/(f(b)-f(a)))
	    if abs(xn-b) < eps:
	    	return xn
	    b = xn
	

def Steffensen(x0,f,f_der,eps):
	while True:
		x1 = x0 - (f(x0)/(f(x0+f(x0))-f(x0)))*f(x0)
		if abs(x1-x0) < eps:
			return x1
		x0 = x1

def mixed(a,b,f,f_der,eps):
	x1 = a-(b-a)*f(a)/(f(b)-f(a))
	xt = b-f(b)/f_der(b)
	while True:
		xn = x1-(xt-x1)*f(x1)/(f(xt)-f(x1))
		if abs(xn-x1) < eps:
			return xn
		xt = xt-f(xt)/f_der(xt)
		x1 = xn

def ridder(a,b,f,eps):
	x2 = (b+a)/2
	eq = (f(x2)+f(a)*sqrt(f(x2)*f(x2)-f(b)*f(a)))/f(x2)
	while True:
		xn = (b*f(x2)*eq-x2*f(b)*eq)/(f(b)*eq-f(x2)*eq)
		# xn = x2 + f(a)*f(b)*(b-a)/sqrt((f(x2)*f(x2)-f(a)*f(b))/f(x2))
		if abs(xn-x3) < eps:
			return xn
		b = x2
		x2 = xn

def brent(a,b,f,eps):
	c = (a+b)/2
	while True:
		xn = -f(a)*(-f(b))*x2/((f(x2)-f(a))*(f(x2)-f(b)))
			  + (f(b)*f(b)*a/((f(a)-f(b))*(f(a)-f(b))) 
			  + (-f(a)*(-f(c))*b)/((f(b)-f(a))*(f(b)-f(a)))
		if abs(xn-c) < eps:
			return xn
		a = b
		b = c
		c = xn
