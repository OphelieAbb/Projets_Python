import maya.cmds
cmds.polySphere()
cmds.currentTime(0)
cmds.setKeyframe(v=0,at='translateX')
cmds.currentTime(0)
cmds.setKeyframe(v=0,at='translateY')

cmds.currentTime(20)
cmds.setKeyframe(v=10,at='translateX')

cmds.currentTime(20)
cmds.setKeyframe(v=10,at='translateY')

cmds.currentTime(40)
cmds.setKeyframe(v=20,at='translateX')
cmds.currentTime(40)
cmds.setKeyframe(v=0,at='translateY')

cmds.currentTime(60)
cmds.setKeyframe(v=40,at='translateX')

cmds.currentTime(60)
cmds.setKeyframe(v=10,at='translateY')

