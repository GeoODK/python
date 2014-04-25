# Jon Nordling
# 01/02/2013
# GEOG656
# Lab4 

import math

# Question (Super Class)
# This is the Geometry class. When a Geometry object is made
# The Geometry class will assign a unique identifier to the object
# The objects id can be called by the object.id
class Geometry:
    control_id = 0
    def __init__(self):
        Geometry.control_id += 1
        self.id = Geometry.control_id

# Question 2 (Sub class)
# This is a Point class that will create and point object when called.
# The Point class will have a unique id becasue it is a Geometry Object
# Also the Point class will have a x and a y cordinate

class Point(Geometry):
    # This is the initial funtion that will be called when the point calls is first defined
    def __init__(self,x_cord,y_cord):
        Geometry.__init__(self)
        self.x = x_cord
        self.y = y_cord

    # This function will over write the built in funtion
    # The function will return the x and y cordinate.
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    # This is a function that will compare two points and test
    # whether the x and y valuse are equal. The return true if they are
    # and false if they are not
    def equal(self,point2):
        if (self.x == point2.x) and (self.y == point2.y):
            return True
        else:
            return False

    # This is a id check function that will test if the ID
    # valuse of the two point objects are the same. Return true
    # if they are and Return false is not/
    def id_check(self,point2):
        if (self.id == point2.id):
            return True
        else:
            return False

    # This is a distance function that will calcualte the distance from one
    # point to the another. Then the function will return the distance valuse
    def distance_to(self,point2):
        x1 = self.x
        y1 = self.y
        x2 = point2.x
        y2 = point2.y
        distance = float(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
        return distance

# Question 3 
def test():
    p1 = Point(48.86200,2.34695) # Paris, France
    p2 = Point(50.09239,8.66890) # Frankfurt Germany
    p3 = Point(33.71463,73.06183) # Islamabad, Pakistan
    p4 = Point(31.54505,74.34068) # Lahore, Pakistan
    p5 = Point(38.80484,-77.04692) # Alexandria, VA

    p6 = Point(5,3)
    p7 = Point(2,7)
    

    print 'Check if points (X,Y) are equal to each other:'
    print 'p1=p2:', p1.equal(p2)
    print 'p2=p3:', p2.equal(p3)
    print 'p3=p4:', p3.equal(p4)
    print 'p4=p5:', p4.equal(p5)
    print ' '
    print 'Check if points ID\'s are equal to each other:'
    print 'p1=p2:', p1.id_check(p2)
    print 'p2=p3:', p2.id_check(p3)
    print 'p3=p4:', p3.id_check(p4)
    print 'p4=p5:', p4.id_check(p5)
    print ' '
    print 'Printing points p6 & p7'
    print p6
    print p7
    print ' '
    print 'Print Distance from p6 & p7'
    print p6.distance_to(p7)
    print ' '

if __name__ =="__main__":
    test()
