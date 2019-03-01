#method for the solution of integrals
def integral(x):
    value_function = x*x
    return value_function

def Booles_rule(a,b,n):
    step = (b - a) /4
    array = [0] * 5
    error_term = (-1*8 * step**7 * integral(0.000001)**8 / 945)
    for i in range(len(array)):
        array[i] = integral(a + i * step)
    answer = (2*step*(7*array[0]+32*array[1]+12*array[2]+32*array[3]+7*array[4])/45)
    answer += error_term
    return answer

def left(a,b,n):
    h=(b-a)/n
    start=a
    answer=0
    while start<b:
        present_value=integral(start)
        answer+=present_value
        start+=h
    return h*answer
def right(a,b,n):
    h=(b-a)/n
    start=a+h
    answer=0
    while start <= b:
        present_value=integral(start)
        answer+=present_value
        start+=h
    return h*answer
def middle(a,b,n):
    h=(b-a)/n
    start=a+h
    answer=0
    while start <= b:
        present_value=integral(start-h/2)
        answer+=present_value
       # print('\t',answer)
        start+=h
    return h*answer
def trapezoidal_rule(a,b,n):
    step=(b-a)/n
    start=a+step
    answer=(integral(a)+integral(b))/2
    while(start < b):
        present_value=integral(start)
        start+=step
        answer+=present_value
    answer*=step
    return answer
def parabol(a,b,n):
    h=(b-a)/n
    start=a+h
    k=0
    answer=integral(a)+integral(b)
    while start < b:
        k+=1
        if k%2==0:
            answer+=2*integral(start)
        else:
            answer+=4*integral(start)
        start+=h
    return h*answer/3
def tri_vosem(a,b,n):
    h=(b-a)/3/n
    m=3*n-1
    answer=integral(a)+integral(b)
    for i in range (1,m+1) :
        x=a+h*i
        if i%3==0:
            answer+=2*integral(x)
        else: answer+=3*integral(x)
    return 3/8*answer*h
def tri_vosem2(a,b,n):
    h=(b-a)/3
    start=a+h
    k=1
    answer=integral(a)+integral(b)
    while start < b:
        if k%3==0: answer += 2*integral(start)
        else: answer += 3*integral(start)
        k+=1
        start+=h
    return answer*3*h/8
     
def weddle_rule(a,b,n):
    h=(b-a)/6
    array=[0]*7
    for i in range(len(array)):
        array[i]=integral(a+i*h)
    answer=float(3/10*h*(array[0]+5*array[1]+array[2]+6*array[3]+array[4]+5*array[5]+array[6]))
    return answer
            
a,b = map(int,input('Введите ограничение интегрирование a,b: ').split())
n=int(input('Введите кол-во разбиений: '))
print('{:5f}'.format(trapezoidal_rule(a,b,n)))
print('{:5f}'.format(middle(a,b,n)))
print('{:5f}'.format(right(a,b,n)))
print('{:5f}'.format(left(a,b,n)))
print('{:5f}'.format(Booles_rule(a,b,n)))
print('{:5f}'.format(parabol(a,b,n)))
print('{:5f}'.format(tri_vosem2(a,b,n)),'!')
print('{:5f}'.format(weddle_rule(a,b,n)),)
print('{:5f}'.format(tri_vosem(a,b,n)),'!')
