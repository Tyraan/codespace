__author__ = 'Tyraan'
from math import sqrt
from math import sqrt
import operator as op
class Vector:
  # TODO: Finish the Vector class.
    def __init__(self,lst):
        self.lst=lst
        self.length = len(lst)

    def check_length(f):
        def wrapper(self,other):
            if len(self) !=len(other):
                raise ValueError()
            return f(self,other)
        return wrapper

    @check_length
    def add(self,vector):
        return Vector([i+j for i,j in zip(self.lst,vector.lst)])


    @check_length
    def subtract(self,vector):
        if self.length== vector.length:
            return Vector([i-j for i,j in zip(self.lst,vector.lst)])
        else:
            raise Exception
    @check_length
    def dot(self,vector):
        if self.length == vector.length:
            return sum(i*j for i,j in zip(self.lst,vector.lst))
        else:
            raise Exception('Only vectors of the same coordinates can arthmatic operation.')

    def __str__(self):
        return str(tuple(self.lst))

    def norm(self):
        return sqrt(sum( i**2 for i in self.lst ))




    
    
    
        
