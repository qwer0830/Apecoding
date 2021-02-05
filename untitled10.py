from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
x,y,z=mc.player.getPos()


y-=1


for i in range(10):
    color=random.randrange(0,16)
    mc.setBlocks(x+i,y,z,x+9,y,z+9,35,color)
    for j in range(10):
        mc.setBlocks(x,y,z+j,x+9,y,z+9,35,color)