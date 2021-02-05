from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
x,y,z=mc.player.getPos()

color=random.randrange(0,16)
mc.setBlock9(x,y,z,35,color)