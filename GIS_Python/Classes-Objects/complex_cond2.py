def test(a, b, c):
      if a and b:
	    print 'hi' 
      elif a and c:
	    print 'bonjour'
      elif a:
	    print 'hola'
      else:
	    print 'Select a language.'
	    
def main():
      a = True
      b = False
      c = False
      
      test(a, b, c)
      

if __name__== '__main__': 
      main()
