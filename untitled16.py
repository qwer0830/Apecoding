from mcpi.minecraft import Minecraft
mc=Minecraft.create()

myID=mc.getPlayerEntityId("Ultraman07")

while True:
    x,y,z=mc.player.getPos()
    a=mc.getBlock(x,y-1,z)
    print(a)
    
    if a == 57:
        mc.postToTitle(myID,"i can't start")
    elif a == 166:
        mc.postToTitle(myID,"start?!")
        
    if a == 169:
        mc.executeCommand("kill @e")
    if a == 41:
        mc.executeCommand("spawnpoint Ultraman07")
    if a == 133:
        mc.postToTitle(myID,"finish!")
        break
