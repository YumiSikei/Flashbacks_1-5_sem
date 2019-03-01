I11=int(input('I11: '))
I12=int(input('I12: '))
I21=int(input('I21: '))
I22=int(input('I22: '))

if I11<=-10e+2 or I11>=10e+2:
    print('{:13.6e}'.format(I11))
else:
    print('{:13.6f}'.format(I11))
if I12<=-10e+2 or I12>=10e+2:
    print('{:13.6e}'.format(I12))
else:
    print('{:13.6f}'.format(I12))
if I21<=-10e+2 or I21>=10e+2:
    print('{:13.6e}'.format(I21))
else:
    print('{:13.6f}'.format(I21))
if I22<=-10e+2 or I22>=10e+2:
    print('{:13.6e}'.format(I22))
else:
    print('{:13.6f}'.format(I22))
