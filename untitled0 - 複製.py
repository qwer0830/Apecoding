from mcpi.minecraft import Minecraft
mc=Minecraft.create()

for i in range(20):
    x,y,z=mc.player.getPos()
    x+=1
    mc.setBlock(x,y-1,z+3,57)
    mc.setBlock(x+1,y-1,z+3,57)
    mc.setBlock(x+2,y-1,z+3,57)
    mc.setBlock(x+3,y-1,z+3,57)
    mc.setBlock(x+4,y-1,z+3,57)
    mc.setBlock(x+5,y-1,z+3,57)
    mc.setBlock(x+6,y-1,z+3,57)
    
    mc.setBlock(x,y-1,z+4,57)
    mc.setBlock(x+1,y-1,z+4,57)
    mc.setBlock(x+2,y-1,z+4,57)
    mc.setBlock(x+3,y-1,z+4,57)
    mc.setBlock(x+4,y-1,z+4,57)
    mc.setBlock(x+5,y-1,z+4,57)
    mc.setBlock(x+6,y-1,z+4,57)
    
    mc.setBlocks(x+6,y,z,x+16,y+10,z+10,57)
    mc.setBlocks(x+7,y+1,z+1,x+15,y+9,z+9,0)

    mc.setBlocks(x+6,y+1,z+3,x+6,y+2,z+4,0)
    mc.setBlocks(x+7,y+5,z+1,x+15,y+5,z+9,169)
