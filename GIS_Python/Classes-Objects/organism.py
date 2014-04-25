class Organism:
    '''A thing that lives in a tide pool.'''
    
    def __init__(self, name, x, y):
        '''A living thing that is at location (x,y) in the tide pool.'''
        
        self.name = name
        self.x = x
        self.y = y
 
    def __str__(self):
        '''Return a string representation of this Organism.'''
        
        return '(%s, [%s, %s])' % (self.name, self.x, self.y)
    
    def can_eat(self, food):
        '''Report whether this Organism can eat the given food.
        Since we don't know anything about what a generic organism
        eats, this always returns False.'''

        return False
    
    def move(self):
        '''Ask the organism to move.  By default, this does nothing,
        since we don't know anything about how fast or how far a
        generic organism would move.'''

        return


class Arthropod(Organism):
    '''An arthropod that has a fixed number of legs.'''
    
    def __init__(self, name, x, y, legs):
        '''An arthropod with the given number of legs that exists at location
        (x, y) in the tide pool.'''
        
        Organism.__init__(self, name, x, y)
        self.legs = legs
    
    def __str__(self):
        '''Return a string representation of this Arthropod.'''
        
        return '(%s, %s, [%s, %s])' % (self.name, self.legs, self.x, self.y)



def main():
    o1 = Organism("test", 10, 10)
    o2 = Arthropod("a", 100, 200, 10)
    print o1
    print o2
    

if __name__ == "__main__": main()