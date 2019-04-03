from classPoint import Point

class Triangle:
    def __init__(self, p1, p2, p3):
        test1 = True if p1 - p2 < p3 and p3 < p1 + p2 else False
        test2 = True if p2 - p3 < p1 and p1 < p2 + p3 else False
        test3 = True if p3 - p1 < p2 and p2 < p3 + p1 else False
        
        if test1 and test2 and test3:
            self._distanceA = p1
            self._distanceB = p2
            self._distanceC = p3
    
    def equilateral(self): return True if self._distanceA == self._distanceB and self._distanceA == self._distanceC else False
    def isosceles(self):
        test1 = True if self._distanceA == self._distanceB and self._distanceA != self._distanceC else False
        test2 = True if self._distanceA == self._distanceC and self._distanceA != self._distanceB else False
        test3 = True if self._distanceB == self._distanceC and self._distanceB != self._distanceA else False
        
        return test1 or test2 or test3
    def scalene(self):
        test1 = True if self._distanceA != self._distanceB else False
        test2 = True if self._distanceA != self._distanceC else False
        test3 = True if self._distanceC != self._distanceB else False
        
        return test1 and test2 and test3

    def perimeter(self): return self._distanceA + self._distanceB + self._distanceC

point1 = Point(1, 1)
point2 = Point(2, 1)
point3 = Point(2, 2)

distance1 = point1.distancePoints(point2)
distance2 = point2.distancePoints(point3)
distance3 = point3.distancePoints(point1)

obj1 = Triangle(distance1, distance2, distance3)
print(obj1.isosceles())