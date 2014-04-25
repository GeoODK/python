# classes.py by Elle
# This is an exercise file from Geog656
class Animal:
    
    def __init__(self, legs = 4):
        self.legs = legs
        print self.legs

    def talk(self):
        print "I can talk"
    
    def walk(self):
        print "I can walk"
    
    def clothes(self):
        print "I have a nice clothes"

class Duck(Animal):
    
    def __init__(self, color='white') :
        Animal.__init__(self, 2)
        self.color = color
    
    def getColor(self):
        return self.color
    
    def quack(self):
        print('Quaaack!')

    def walk(self):
        Animal.walk(self)
        print('Walks like a duck.')


class Dog(Animal):
    
    def clothes(self):
        print "I have a white fur"    

def main():
    donald = Duck()
    print donald.getColor()    
    donald.quack()
    donald.walk()
    donald.talk()
    
    gufi = Dog()
    gufi.talk()
    gufi.walk()
    gufi.clothes()

if __name__ =="__main__": main()
