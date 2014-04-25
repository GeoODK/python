class Person(object):
    def __init__(self):
        self = self
    
def main():
    jon = Person()
    jon.name= 'jon'
    print jon.name
main()
