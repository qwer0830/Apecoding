from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random

color=random.randrange(0,4)
def PlantTree(x,y,z):
    mc.setBlocks(x+1,y+2,z,x+3,y+5,z+2,18,color)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,17)


x,y,z=mc.player.getPos()

for i in range(10):
    for j in range(10):
        for k in range(10):
            
            PlantTree(x+i*j,j+j*k,z+i*k)