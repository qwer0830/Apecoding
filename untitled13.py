from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange

answar=randrange(0,16)
myID=mc.getPlayerEntityId("Ultraman07")

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        
        if data>answar:
            mc.postToChat('wrong answar')
        elif data<answar:
            mc.postToChat('...蛤?')
        else:
            mc.setBlock(hit.pos,57)
            mc.postToTitle(myID,"HA↗HA↗HA↗HA↗HA↗")
            break







