def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome fun')
        any_function()
    return wrapper_function

def fun1():
    print('this is fun 1')

@ decorator_function
def fun2():
    print('this is fun2 ')

fun1=decorator_function(fun1)
fun2()