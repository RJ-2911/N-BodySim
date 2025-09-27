from vpython import vector, sphere, rate, cross, norm, mag
from random import random

G = 1
M = 1
R = 1
rsoft = 0.03
w = vector(0,0.05,0)
n = 0
N = 10
stars = []

while n<N:
  rt = R*vector(2*random()-1,2*random()-1,2*random()-1)
  stars = stars + [sphere(pos=rt,radius=R/30,make_trail=False,retain=100)]
  n = n + 1

for star in stars:
  star.m = M/N
  star.p = star.m*cross(w,vector(star.pos.x,0,star.pos.z))
  star.F = vector(0,0,0)

t = 0
dt = 0.01

while t<10:
  rate(100)
  for star in stars:
    star.F = vector(0,0,0)
  for i in range(len(stars)):
    for j in range(len(stars)):
      if i!=j:
        rji = stars[i].pos - stars[j].pos
        stars[i].F = stars[i].F - G*stars[i].m*stars[j].m*norm(rji)/(mag(rji)**2+rsoft**2)
        
  for star in stars:
    star.p = star.p + star.F*dt
    star.pos = star.pos + star.p*dt/star.m
  t = t + dt