def memo(fn):
    cache = {}
    miss = object()   
    def wrapper(*args):
        result = cache.get(args, miss)
        
        if result is miss:
            result = fn(*args)
            cache[args] = result
            print('result is miss')
        print('wrapper return %s'%(result,))
        return result

    return wrapper


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@memo
def add(n):
    if n<3:
        return n
    return fib(n-1)+fib(n-3)
