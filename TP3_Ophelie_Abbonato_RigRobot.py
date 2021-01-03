import maya.cmds as cmds

# Programme principal (main)
def NewCharacterCreation(n):
    
    newCharacter = Persos(n) # une instance de la classe Persos() avec le paramètre du nom
    newCharacter.CharacterCreation() # lance la création du perso
    newCharacter.rig() # rig du perso
    
    
def Interface(): #interface avec les slider et le bouton de creation

    #variables qui contienent les sliders
    
    global bodyHeight_
    global bodyDepth_
    global bodyW_
    global legSize_
    global legLenght_
    global headSize_
    global armLenght_
    global armsize_
    global nameF
   
    
    #fenetre
    cmds.window(title = "Generate a Character")
    cmds.columnLayout()
    
    #sliders de contrainte
    bodyHeight_ = cmds.floatSliderGrp( label = 'hauteur du corps', field=True, minValue=3.0, maxValue=160.0,value=120.0)
    bodyW_ = cmds.floatSliderGrp( label = 'largeur du corps', field=True, minValue=3.0, maxValue=160.0,value=40.0)
    bodyDepth_ = cmds.floatSliderGrp( label = 'epaisseur du corps', field=True, minValue=5.0, maxValue=60.0,value=20.0)
    legSize_ = cmds.floatSliderGrp( label = 'largeur des jambes', field=True, minValue=2.0, maxValue=50.0,value=20.0)
    legLenght_ = cmds.floatSliderGrp( label = 'longeur des jambes', field=True, minValue=3.0, maxValue=80.0,value=55.0)
    headSize_ = cmds.floatSliderGrp( label = 'taille de la tete', field=True, minValue=3.0, maxValue=60.0,value=30.0)
    armLenght_ = cmds.floatSliderGrp( label = 'taille des bras', field=True, minValue=3.0, maxValue=70.0,value=40.0)
    armsize_ = cmds.floatSliderGrp( label = 'longeur des bras', field=True, minValue=4.0, maxValue=30.0,value=15.0)
    
    nameF = cmds.textFieldGrp(text = "Name")
    
    
    #bouton de creation
    cmds.button(label = "Create Character", c = 'NewCharacterCreation(cmds.textFieldGrp(nameF,q=True,text = True))')
    #lance la fenetre
    cmds.showWindow()
    

#initialise l'interface
Interface()

class Persos():
    """classe de personnages"""
    # name = ""
    # mainGroup = ""
        
    # Le constructeur de la classe __init__ qui est lancé automatiquement
    def __init__(self,n):
        
        self.name = n # le nom du perso
        self.mainGroup = cmds.group(empty=True, name=n) # Le groupe du perso
        
        
        
        self.bodyHeight = cmds.floatSliderGrp(bodyHeight_, q = True, v = True)
        self.bodyDepth = cmds.floatSliderGrp(bodyDepth_, q = True, v = True)
        self.bodyW = cmds.floatSliderGrp(bodyW_, q = True, v = True)
        self.legSize = cmds.floatSliderGrp(legSize_, q = True, v = True)
        self.legLenght = cmds.floatSliderGrp(legLenght_, q = True, v = True)
        self.headSize = cmds.floatSliderGrp(headSize_, q = True, v = True)
        self.armSize = cmds.floatSliderGrp(armsize_, q = True, v = True)
        self.armLenght = cmds.floatSliderGrp(armLenght_, q = True, v = True)
        
    def rig(self) :	
      
        cmds.group(em=True, n='Rig' )
        cmds.joint( p= (0.171124,-43.991319,0))
        cmds.joint( p= (0.171124,-21.637474,0))
        cmds.joint('joint1',e=True,zso=True,oj='xyz',sao='yup')
        
        
        cmds.joint( p= (0.171124,8.977573 ,0))
        cmds.joint('joint2',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (0.171124,34.733089,0))
        cmds.joint('joint3',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (0.171124,57.086934,0))
        cmds.joint('joint4',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (0.171124,77.011012,0))
        cmds.joint('joint5',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (8.168084,46.565763,0))
        cmds.joint('joint7',e=True,zso=True,oj='xyz',sao='yup')
        cmds.parent('joint7','joint4')
        
        cmds.joint( p= (-8.168084,46.040793,0))
        cmds.parent('joint8','joint4')
        
        cmds.joint( p= (-20.167369,43.581907,0))
        
        cmds.joint( p= (-19.793546,43.581907,0))
        cmds.joint( p= (-60.166378,43.581907,0))
        cmds.joint('joint9',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (-100.165388,43.581907,0))
        cmds.joint('joint10',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (-115.118288,43.581907,0))
        cmds.joint('joint11',e=True,zso=True,oj='xyz',sao='yup')

        cmds.select(clear=True)
        cmds.joint( p= (20.097474,44.088276,0))
        cmds.joint( p= (59.887389,44.474585,0))
        cmds.joint('joint14',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (100.449924,44.474585,0))
        cmds.joint('joint15',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (114.743389,44.474585,0))
        cmds.joint('joint16',e=True,zso=True,oj='xyz',sao='yup')
        cmds.parent('joint14','joint7')
        
        cmds.select(clear=True)
        cmds.joint( p= (-17.206283,-61.004095,0))
        cmds.joint( p= (-20.334698,-115.229957,0))
        cmds.joint('joint18',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (-19.813296,-171.020027,0))
        cmds.joint('joint19',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (-19.813296,-225.997318,0))
        cmds.joint('joint20',e=True,zso=True,oj='xyz',sao='yup')
        cmds.parent('joint18','joint1')
        
        cmds.select(clear=True)
        cmds.joint( p= (15.815459,-60.351589,0))
        cmds.joint( p= (20.855821,-116.154906,0))
        cmds.joint('joint22',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (20.272872,-170.369114,0))
        cmds.joint('joint23',e=True,zso=True,oj='xyz',sao='yup')
        
        cmds.joint( p= (20.272872,-225.166271,0))
        cmds.joint('joint24',e=True,zso=True,oj='xyz',sao='yup')
        cmds.parent('joint22','joint1')

        cmds.ikHandle(sj='joint10', ee='joint12',name='Bras_G_IK')
        cmds.ikHandle(sj='joint14', ee='joint16',name='Bras_D_IK')
        cmds.ikHandle(sj='joint22', ee='joint24',name='Jambe_G_IK')
        cmds.ikHandle(sj='joint18', ee='joint20',name='Jambe_D_IK')
        cmds.ikHandle(sj='joint1', ee='joint14',name='Colonne_IK')
        
        cmds.bindSkin(self.name, 'joint1')
        
        cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), sw=360, r=1,name='Poignet_G_CTRL')
        cmds.move(-100.16539,43.581905,1.17984e-07)
        cmds.rotate(0,0,90)
        cmds.scale(15,15,15)
        cmds.makeIdentity(apply=True)
        cmds.parentConstraint('Poignet_G_CTRL','Bras_G_IK')
        
        cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), sw=360, r=1,name='Poignet_D_CTRL')
        cmds.move(100.449921,44.474586,0)
        cmds.rotate(0,0,90)
        cmds.scale(15,15,15)
        cmds.makeIdentity(apply=True)
        cmds.parentConstraint('Poignet_D_CTRL','Bras_D_IK')
        
        cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), sw=360, r=1,name='Jambe_D_CTRL')
        cmds.move(-19.813295,-171.02002,0)
        cmds.scale(20,20,20)
        cmds.makeIdentity(apply=True)
        cmds.parentConstraint('Jambe_D_CTRL','Jambe_D_IK')
        
        cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), sw=360, r=1, name='Jambe_G_CTRL')
        cmds.move(20.272873,-170.36911,0)
        cmds.scale(20,20,20)
        cmds.makeIdentity(apply=True)
        cmds.parentConstraint('Jambe_G_CTRL','Jambe_G_IK')
        
        
    def CharacterCreation(self) : #fonction principale
        self.Body()
        self.Head()
        self.Legs()
        self.Arms()
        # On parente les différentes parties au Groupe
        cmds.parent(self.Corps, self.mainGroup)
        cmds.parent(self.Head, self.mainGroup)
        cmds.parent(self.Cuisse_l, self.mainGroup)
        cmds.parent(self.Tibia_l, self.mainGroup)
        cmds.parent(self.Pied_l, self.mainGroup)
        cmds.parent(self.Cuisse_r, self.mainGroup)
        cmds.parent(self.Tibia_r, self.mainGroup)
        cmds.parent(self.Pied_r, self.mainGroup)
        cmds.parent(self.AvantBras_l, self.mainGroup)
        cmds.parent(self.Bras_l, self.mainGroup)
        cmds.parent(self.Main_l, self.mainGroup)
        cmds.parent(self.AvantBras_r, self.mainGroup)
        cmds.parent(self.Bras_r, self.mainGroup)
        cmds.parent(self.Main_r, self.mainGroup)
        

    def Head(self): #creation de la tÃªte
        self.Head = cmds.polyCube(w=self.headSize,d=self.headSize,h=self.headSize,name='Head')
        cmds.move(0,self.bodyHeight/2+self.headSize/2,0)
        
        
    def Body(self): #creation du corps
        self.Corps = cmds.polyCube(w=self.bodyW,d=self.bodyDepth,h=self.bodyHeight,name='Corps')
    
    
    def Legs(self): #creation des jambes
        self.Cuisse_l = cmds.polyCube(w=self.legSize,d=self.legSize,h=self.legLenght,name='Cuisse_l')
        cmds.move(self.bodyW/2,-self.bodyHeight/2-self.legLenght/2,0)
        self.Tibia_l = cmds.polyCube(w=self.legSize,d=self.legSize,h=self.legLenght,name='Tibia_l')
        cmds.move(self.bodyW/2,-self.bodyHeight/2-self.legLenght*1.5,0)
        self.Pied_l = cmds.polyCube(w=self.legSize,d=self.legSize,h=self.legLenght,name='Pied_l')
        cmds.move(self.bodyW/2,-self.bodyHeight/2-self.legLenght*2.5,0)
        
        
        self.Cuisse_r = cmds.polyCube(w=self.legSize,d=self.legSize,h=self.legLenght,name='Cuisse_r')
        cmds.move(-self.bodyW/2,-self.bodyHeight/2-self.legLenght/2,0)
        self.Tibia_r = cmds.polyCube(w=self.legSize,d=self.legSize,h=self.legLenght,name='Tibia_r')
        cmds.move(-self.bodyW/2,-self.bodyHeight/2-self.legLenght*1.5,0)
        self.Pied_r = cmds.polyCube(w=self.legSize,d=self.legSize,h=self.legLenght,name='Pied_r')
        cmds.move(-self.bodyW/2,-self.bodyHeight/2-self.legLenght*2.5,0)
        
    def Arms(self): #creation des bras
    
        #Gauche
        self.AvantBras_l = cmds.polyCube(w=self.armSize,d=self.armSize,h=self.armLenght,name='AvantBras_l')
        cmds.move(self.bodyW/2+self.armLenght/2,self.bodyHeight/2-self.armSize,0)
        cmds.rotate(0,0,90)
        self.Bras_l = cmds.polyCube(w=self.armSize,d=self.armSize,h=self.armLenght,name='Bras_l')
        cmds.move(self.bodyW/2+self.armLenght+self.armLenght/2,self.bodyHeight/2-self.armSize,0)
        cmds.rotate(0,0,90)
        self.Main_l = cmds.polyCube(w=self.armSize,d=self.armSize,h=self.armSize,name='Main_l')
        cmds.move(self.bodyW/2+self.armLenght*2+self.armSize/2,self.bodyHeight/2-self.armSize,0)
        cmds.rotate(0,0,90)
        
        #Droite
        self.AvantBras_r = cmds.polyCube(w=self.armSize,d=self.armSize,h=self.armLenght,name='AvantBras_r')
        cmds.move(-self.bodyW/2-self.armLenght/2,self.bodyHeight/2-self.armSize,0)
        cmds.rotate(0,0,-90)
        self.Bras_r = cmds.polyCube(w=self.armSize,d=self.armSize,h=self.armLenght,name='Bras_r')
        cmds.move(-self.bodyW/2-self.armLenght-self.armLenght/2,self.bodyHeight/2-self.armSize,0)
        cmds.rotate(0,0,-90)
        self.Main_r = cmds.polyCube(w=self.armSize,d=self.armSize,h=self.armSize,name='Main_r')
        cmds.move(-self.bodyW/2-self.armLenght*2-self.armSize/2,self.bodyHeight/2-self.armSize,0)
        cmds.rotate(0,0,-90)
        
        