from graphics.rectangle import*
from graphics.circle import*
from graphics.threeDgraphics.cuboid import*
from graphics.threeDgraphics.sphere import*

l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
print("Area is",rectArea(l, b))
print("Perimeter is",rectPeri(l, b))

r=int(input("enter the radius:"))
print("Area is ",cirArea(r))
print("Perimeter is",cirPeri(r))
 
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
h=int(input("ente rthe height"))
print("Area is",cubArea(l, h, b))
print("perimeter is",cubPeri(l, b, h))

r=int(input("enter the radius:"))
print("Area is",spArea(r))
print("Perimeter is ",spPeri(r))

