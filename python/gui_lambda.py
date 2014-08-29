#以下是用 lambda i=i:i，lambda :i, lambda i:i ,以及lambda a=i:i 的四个函数。
def odd():
	f=[]
	for i in 'abcdefg':
	    f.append((lambda:i))
	return f
def no_odd():
	f=[]
	for i in 'abcdefg':
		f.append((lambda i:i))
	return f
    
def f_odd():
    f=[]
    for i in 'abcdefg':
        f.append((lambda i=i:i))
    return f

def a_odd():
    f=[]
    for i in 'abcdefg':
        f.append((lambda a=i:i))
    return f

#这是一个简单的for循环
def for_iter(obj):
    for i in obj:
        print (i(),end='')


# 用 for_iter 循环 odd()，no_odd(), f_odd(),a_odd()  分别会生成不同的结果 ，
# 请问为什么 。 如果把 四个函数中 的lambda换成 普通函数，应该各是什么样子呢？
