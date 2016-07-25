from logging import getLogger

def aDecorator(func):
    def _func(*args, **kwargs):
        print 'I am excecuting before method call %s!' % func.func_name
        _ret = func(*args, **kwargs)
        print 'I am executing after method call %s!' % func.func_name
        return _ret
    return _func

@aDecorator
def myMultiplyFunction(arg1, arg2):
    print 'Multiplying %r and %r: %r!' % (arg1, arg2, arg1*arg2)
    return arg1*arg2

@aDecorator
def myDivideFunction(arg1, arg2):
    print 'Dividing %r and %r: %r!' % (arg1, arg2, arg1/arg2)
    return arg1/arg2
