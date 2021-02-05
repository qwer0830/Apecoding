from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x=99
y=256
z=66


Position=mc.player.getTilePos()
x=Position.x
y=Position.y
z=Position.z

time.sleep(10)
mc.player.setTilePos(x,y,z)