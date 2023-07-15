def fun1(*args):
    print(args)
    print(args[1])
    
    
fun1(10,23,4,532)


def fun1(*args,**kwargs):
    print(kwargs)
    print(kwargs['var1'])
    
fun1(1,2,3,var1=10,var2=20)
