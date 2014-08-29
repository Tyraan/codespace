class Person:    
    population = 0
    def __init__(self, name):        
        self.name = name
        print ('Initializing %s)' % self.name)
        Person.population += 1        
        self.number=Person.population

class Counter:
    initnum=0
    def __init__(self):
        Counter.initnum+=1
        self.num=Counter.initnum
        


    
