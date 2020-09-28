from realpoint import *
p1=point(3, [1, 2, 3])
print(p1)
p2=point(3, [6, 7, 8])
p2.mirror(-1)
print(p2)
print("p1 distance from p2=", p1.dist(p2))


