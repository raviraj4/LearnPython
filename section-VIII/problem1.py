import math
class line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        # (x1,y1)(x2,y2)
        # (1, 3) (2, 7)
    def distance(self):
        dist = math.sqrt(((self.coor2[0]-self.coor1[0])**2) + ((self.coor2[1]-self.coor1[1])**2))
        return dist
    def slope(self):
        numer = self.coor2[1] - self.coor1[1]
        denom = self.coor2[0] - self.coor1[0]
        slp = numer/denom
        return slp
    
class cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        self.pi = 22/7
            
    def volume(self):
        res = self.pi*((self.radius)**2)*self.height
        return res
    
    def surface_area(self):
        res = (2 * self.pi * self.radius * self.height ) + (2*self.pi*(self.radius**2)) 
        return res

l = line((3,2),(8,10))
dist = l.distance()
slope = l.slope()
print(dist,"\n",slope,"\n-----")
c = cylinder(2,3)
vol = c.volume()
sa = c.surface_area()
print(vol,"\n",sa,"\n-----")


        