class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
def meth():
    print ('Calling method')

class MyMeta(type):
    @classmethod
    def __prepare__(cls,name,baseClasses):
        return {'meth':meth}
    def __new__(clas,name,baseClasses,classdict):
        return type.__new__(cls,name,baseClasses,classdict)

class Test(metaclass = MyMeta):
    def __init__(self):
        pass
    attr = 'an attribute'




