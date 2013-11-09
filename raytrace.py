from math import sqrt

class Vector(object):
    __slots__=['x','y','z']
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return '<%.2f, %.2f, %.2f>' % (self.x, self.y, self.z)

    def __add__(self, v):
        return Vector(self.x + v.x,
                      self.y + v.y,
                      self.z + v.z)
    
    def __sub__(self, v):
        return Vector(self.x - v.x,
                      self.y - v.y,
                      self.z - v.z)

    def __mul__(self, s):
        return Vector(self.x * s,
                      self.y * s,
                      self.z * s)
    def __div__(self, s):
        return Vector(self.x / s,
                      self.y / s,
                      self.z / s)

    def __neg__(self):
        return Vector(-self.x,
                       -self.y,
                       -self.z)

    
    def magnitude(self):
        return sqrt(self.x * self.x +
                    self.y * self.y +
                    self.z * self.z)
    def normalize(self):
        return self / self.magnitude()

    def distance(self, other):
        return (self - other).magnitude()
    
    def dotprod(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def crossprod(self, v):
        return Vector(self.y * v.z - self.z * v.y,
                      self.z * v.x - self.x * v.z,
                      self.x * v.y - self.y * v.x)

    
def intersect_ray_sphere(pt, ray, scenter, sradius):
    # make ray a unit vector
    ray = ray / ray.magnitude()
    oc = pt - scenter
    d = ( (ray.dotprod(oc)) * (ray.dotprod(oc))
          - oc.dotprod(oc)
          + sradius * sradius )
    if d < 0:
        return None
    if d == 0:
        return -(ray.dotprod(oc))
    return min( -(ray.dotprod(oc)) + sqrt(d),
                -(ray.dotprod(oc)) - sqrt(d))
        
def ray_sphere_hit_point(pt, ray, scenter, sradius):
    solution = intersect_ray_sphere(pt, ray, scenter, sradius)
    if solution is None:
        return None
    return pt + ray * solution


print ray_sphere_hit_point(Vector(0,0,0),
                     Vector(1,0,0),
                     Vector(2,1,0),
                     1)

from Tkinter import Tk, Canvas, PhotoImage, mainloop
w = 400
h = 300
win = Tk()
can = Canvas(win, width=w, height=h, bg="#000000")
can.pack()
img = PhotoImage(width=w, height=h)
can.create_image((w/2, h/2), image=img, state="normal")

pt = Vector(0,0,0)
sphere_center = Vector(100, 0, 0)
sphere_radius = 70

max_dist = 100
def color(dist):
    r = 255 - int( min(dist, max_dist) / float(max_dist) * 255.0)
    return '#' + (hex(r)[2:] * 3)

for y in range(0, w):
    for z in range(0, h):
        sln = intersect_ray_sphere(pt,
                                   Vector(100, y - w/2, z - h/2),
                                   sphere_center,
                                   sphere_radius)
        img.put(sln and color(sln) or '#000000', (y, z))
    

mainloop()
