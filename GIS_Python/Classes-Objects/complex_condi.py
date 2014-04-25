def test(a, b, c):

      if a:
	    if b:
		  print 'hi' 
	    elif c:
		  print 'bonjour'
	    else:
		  print 'hola'
      else:
	    print 'Select a language.'
	    
def main():
      a = True
      b = False
      c = False
      print id(b), id(c)
     
      test(a, b, c)
      

if __name__== '__main__': 
      main()
