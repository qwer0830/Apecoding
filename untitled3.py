from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

a=input("你是誰??")

mc.postToChat('Hello'+a+',今天天氣真好')

mc.setBlocks(x,y,z,x+10,y+10,z+10,57)
mc.setBlocks(x+1,y+1,z+1,x+9,y+9,z+9,0)

mc.setBlocks(x+3,y+1,z,x+3,y+2,z,0)
mc.setBlocks(x+1,y+5,z+1,x+9,y+5,z+9,169)

