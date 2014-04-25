class Duck:
    def __init__(self, color='white'):
        self.color = color
    
    def getColor(self):
        return self.color


def main():
    donald = Duck('blue')
    print donald.getColor()
    
    roy = Duck()
    print roy.getColor()    

if __name__ == "__main__": 
    main()