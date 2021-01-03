from maya.cmds import *

CR_bodyPartNames = ["Spine_", "Head_", "Arm_L_", "Leg_L_", "Arm_R_", "Leg_R_"]
CR_BonesNames = ["|Spine_1", "|Spine_2", "|Spine_3", "|Spine_4", "|Head_1", "|Head_2",
"|Arm_L_1", "|Arm_L_2", "|Arm_L_3", "|Arm_L_4", "|Arm_L_5",
"|Leg_L_1", "|Leg_L_2", "|Leg_L_3", "|Leg_L_4", "|Leg_L_5",
"|Arm_R_1", "|Arm_R_2", "|Arm_R_3", "|Arm_R_4", "|Arm_R_5",
"|Leg_R_1", "|Leg_R_2", "|Leg_R_3", "|Leg_R_4", "|Leg_R_5"]
    

'''===================================Warnings==================================='''
def CR_warningLocators() :
    if (len(ls(sl=1)) == 0):
        confirmDialog (title = "Error : Paroskrt_Rigging", message = "Can not create locators, need to select an object to rig")
    else :
        CR_bipedsShapeLocators()
'''===================================Warnings==================================='''


'''===================================Naming Function==================================='''
def CR_naming_coloring(i):    
    #si on lance cette fonction pour la premiere fois alors
    if (i==0):
        #nommer les objets
        CR_nameObject = 0 #variable qui selection le nom de son indice dans la liste des parties du corps CR_bodyPartNames
        CR_namePad = 1 #variable qui numerote les joints
    
    else :
        #s'incremente pour changer le nom des joints
        CR_nameObject += 1
        CR_namePad += 1
            
    
    #spine
    if (i>=0 and i<4) :
        CR_nameObject = 0
        #donne une couleur à l'objet
        CR_color = 17
    #head
    if (i>=4 and i<6) :
        CR_nameObject = 1
        if (i==4) :
            CR_namePad = 1
    #arm_l    
    if (i>=6 and i<11) :
        CR_nameObject = 2
        if (i==6) :
            CR_namePad = 1
            CR_color = 18
    #leg_l    
    if (i>=11 and i<16) :
        CR_nameObject = 3
        if (i==11) :
            CR_namePad = 1
            CR_color = 6
    #arm_r    
    if (i>=16 and i<21) :
        CR_nameObject = 4
        if (i==16) :
            CR_namePad = 1
            CR_color = 9
            
    #leg_r    
    if (i>=21 and i<26) :
        CR_nameObject = 5
        if (i==21) :
            CR_namePad = 1
            CR_color = 13
    
    
    CR_Name = (CR_bodyPartNames[CR_nameObject] + str(CR_namePad))
    #renvoie le nom de la partie du corps et son numero
    global CR_Name, CR_color
    global CR_nameObject, CR_namePad
'''===================================Naming Function==================================='''



'''===================================Locators and Controls size==================================='''
def CR_locatorsAndCtrlsSize() :
	#recupere le nom du group selectionne
	CR_mainGroup = ls(sl=1, shortNames=1)
	
	#recupere la valeur de taille des locators et controls 
	CR_scaleValue = floatFieldGrp(CR_locCtrlsSize_FFG, q=1, value1=1)

	for i in range (26):
		#selectionne le bon nom
		CR_naming_coloring(i)
		
		#scale le locator
		CR_path = "|" + str(CR_mainGroup[0]) + "|Locators_grp|Global_ctrl"
		if (objExists(CR_path + CR_BonesNames[i] + "_loc|")):
			scale (CR_scaleValue,CR_scaleValue,CR_scaleValue ,CR_path + CR_BonesNames[i] + "_loc|")
		
		#scale du controleur
		CR_path = "|" + str(CR_mainGroup) + "|RIG|Global_ctrl"
		if (objExists(CR_path + CR_BonesNames[i] + "_ctrl|")):
			scale (CR_scaleValue,CR_scaleValue,CR_scaleValue ,CR_path + CR_BonesNames[i] + "_ctrl|") 
'''===================================Locators and Controls size==================================='''




'''===================================Functions==================================='''
'''========================== PART I =========================='''
def CR_bipedsShapeLocators():
	global CR_BonesNames
	#recuperer le nom du mesh
	CR_currentSelection = ls (sl=1)
	
	#MainGroup
	CR_mainGroup = group (empty = 1, name = CR_currentSelection[0] + "_grp")
	#cree un groupe pour ranger les meshes
	CR_geoGrp = group (empty = 1, name = "GEO")
	#faire un controleur global
	CR_Global_ctrl = circle (radius = 7, nr = (0,1,0), name = "Global_ctrl")
	#faire un groupe pour les locators qui sera le futur groupe RIG
	CR_locatorsGrp = group (name = "Locators_grp")
	
	
	#ranger tout les meshes dans un groupe GEO
	for i in range (len(CR_currentSelection)):
		parent (CR_currentSelection[i], CR_geoGrp)
	parent (CR_locatorsGrp, CR_geoGrp, CR_mainGroup) #ranger le tout dans un gros group du nom de l'objet
	
	
	
	#creer tous les locators de reference
	spaceLocator( p=(-8.413081449e-06, 9.6, -0.7131352644), name = "Spine_1_loc")
	spaceLocator( p=(-7.97154734e-06, 11.08496541, -0.4725232722), name = "Spine_2_loc")
	spaceLocator( p=(-7.971550481e-06, 13.28719076, -0.7774189785), name = "Spine_3_loc")
	spaceLocator( p=(-7.971553703e-06, 14.94566643, -0.7250401233), name = "Spine_4_loc")
	spaceLocator( p=(0.01324357063, 15.82535393, -0.2936910902), name = "Head_1_loc")
	spaceLocator( p=(0.002143653087, 17.90617149, 0.05847858918), name = "Head_2_loc")
	
	spaceLocator( p=(0.9237635557, 14.57662661, 0.3013605926), name = "Arm_L_1_loc")
	spaceLocator( p=(1.846322061, 14.46532677, -0.5575719114), name = "Arm_L_2_loc")
	spaceLocator( p=(4.615022089, 14.46532677, -0.5575719114), name = "Arm_L_3_loc")
	spaceLocator( p=(7.358602841, 14.46532677, -0.5575719114), name = "Arm_L_4_loc")
	spaceLocator( p=(9.705151099, 14.46532677, -0.5575719114), name = "Arm_L_5_loc")
	
	spaceLocator( p=(0.9633714138, 9.318605965, -0.03547440495), name = "Leg_L_1_loc")
	spaceLocator( p=(0.9992516642, 5.475920042, 0.1909012911), name = "Leg_L_2_loc")
	spaceLocator( p=(0.824461909, 0.849936647, -0.4949280491), name = "Leg_L_3_loc")
	spaceLocator( p=(0.8737618201, 0.3316621097, 0.3333020308), name = "Leg_L_4_loc")
	spaceLocator( p=(0.9865090203, 0.08531223974, 1.485409048), name = "Leg_L_5_loc")
	
	spaceLocator( p=(-0.9237635557, 14.57662661, 0.3013605926), name = "Arm_R_1_loc")
	spaceLocator( p=(-1.846322061, 14.46532677, -0.5575719114), name = "Arm_R_2_loc")
	spaceLocator( p=(-4.615022089, 14.46532677, -0.5575719114), name = "Arm_R_3_loc")
	spaceLocator( p=(-7.358602841, 14.46532677, -0.5575719114), name = "Arm_R_4_loc")
	spaceLocator( p=(-9.705151099, 14.46532677, -0.5575719114), name = "Arm_R_5_loc")
	
	spaceLocator( p=(-0.963388, 9.31861, -0.0354744), name = "Leg_R_1_loc")
	spaceLocator( p=(-0.999268, 5.47592, 0.190901), name = "Leg_R_2_loc")
	spaceLocator( p=(-0.824479, 0.849937, -0.494928), name = "Leg_R_3_loc")
	spaceLocator( p=(-0.873779, 0.331662, 0.333302), name = "Leg_R_4_loc")
	spaceLocator( p=(-0.986526, 0.0853122, 1.48541), name = "Leg_R_5_loc")
	
	#path
	CR_path = str(CR_mainGroup) + "|" + str(CR_locatorsGrp) + "|Global_ctrl"
	#recentrer le pivot
	for i in range (len (CR_BonesNames)) :
	    parent (CR_BonesNames[i] + "_loc|", CR_path)
	    xform (cp = 1)
	
	#retour des variables
	select (str(CR_mainGroup) + "|" + str(CR_locatorsGrp) + "|Global_ctrl|")
	global CR_currentSelection, CR_mainGroup, CR_locatorsGrp, CR_Global_ctrl, CR_path
	
	CR_colorLocators()
    



def CR_colorLocators():
	for i in range(26):
		#renvoie une couleur pour chaque locator
		CR_naming_coloring(i)
		#colorise tous les locators
		setAttr (CR_path + CR_BonesNames[i] + "_loc|" + ".overrideEnabled", 1)
		setAttr (CR_path + CR_BonesNames[i] + "_loc|" + ".overrideColor", CR_color)
	
	#coloriser le controlleur global
	setAttr (str(CR_mainGroup) + "|" + str(CR_locatorsGrp) + "|Global_ctrl|" + ".overrideEnabled", 1)
	setAttr (str(CR_mainGroup) + "|" + str(CR_locatorsGrp) + "|Global_ctrl|" + ".overrideColor", 17)
	
	#select the main group
	select(str(CR_mainGroup))








'''========================== PART II =========================='''

def CR_bipedsRig():
    #recupere le nom du group selectionne
    CR_mainGroup = ls(sl=1, shortNames=1)
    global CR_mainGroup
    #cree un l'interieur un group SETUP ou ranger le rig
    CR_Setup_grp = group (empty=1, name = "SETUP")
    parent (CR_Setup_grp,CR_mainGroup)
    
    for i in range (26):
        #nomme bien les joints
        CR_naming_coloring(i)
        
        #chemin des locators sur lesquels se poser
        CR_path = "|" + str(CR_mainGroup[0]) + "|" + str(CR_locatorsGrp) + "|Global_ctrl"
        #pose un joint à chaque locator
        CR_createdJoint = joint (p=(pointPosition ((CR_path + CR_BonesNames[i] + "_loc|"), w=1)), name = (CR_bodyPartNames[CR_nameObject] + str(CR_namePad) + "_jnt"))
        
        #verifie si le nom des joints a change, auqeul cas il deparente les joints
        if (i==6 or i==11 or i==16 or i==21):
            parent (CR_createdJoint, ("|" + str(CR_mainGroup[0]) + "|SETUP"))
        
    #renvoir vers une fonction qui oriente les joints
    CR_orientJoints()



def CR_orientJoints():
    CR_path = "|" + str(CR_mainGroup[0]) + "|SETUP"
    #oriente les joints des bras
    select (CR_path + "|Arm_L_1_jnt|", CR_path + "|Arm_R_1_jnt|")
    joint (e=1,  oj = "yzx", secondaryAxisOrient = "xdown", ch=1, zso=1)
    #oriente les joints des jambes et du corps
    select (CR_path + "|Leg_L_1_jnt|", CR_path + "|Leg_R_1_jnt|", CR_path + "|Spine_1_jnt|")
    joint (e=1,  oj = "yxz", secondaryAxisOrient = "xup", ch=1, zso=1)
    
    #parente le rig final
    parent (CR_path + "|Arm_L_1_jnt|", CR_path + "|Arm_R_1_jnt|", CR_path + "|Spine_1_jnt|Spine_2_jnt|Spine_3_jnt|Spine_4_jnt|")
    parent (CR_path + "|Leg_L_1_jnt|", CR_path + "|Leg_R_1_jnt|", CR_path + "|Spine_1_jnt|")
    
    CR_CreateCtrlForEveryJoint()




def CR_CreateCtrlForEveryJoint():
    
    CR_path = str(CR_mainGroup[0]) + "|" + str(CR_locatorsGrp) + "|Global_ctrl"
    
    
    for i in range(25):
        #defini le nom du controlleur
        CR_naming_coloring(i)
        CR_ctrlName = (CR_Name + "_ctrl")
    
        #cree un controller
        CR_createdController = circle(radius = 1, nr = (0,1,0), name = CR_ctrlName)
        	
        #recuperer la position du joint correspondant
        CR_locatorPosition = pointPosition ((CR_path + CR_BonesNames[i] + "_loc|"), w=1)
        #deplacer le controle par rapport à son joint
        move (CR_locatorPosition[0], CR_locatorPosition[1], CR_locatorPosition[2]) 
        
        #orienter le controlleur vers le joint suivant
        select (CR_path + CR_BonesNames[i+1] + "_loc|", replace=1)
        select (CR_createdController, add=1)
        aimConstraint (offset=(0, 0, 0), weight=1, aimVector=(0, 1, 0), upVector=(0, 0, 1), worldUpType="vector", worldUpVector = (0, 1, 0))
        #supprimer la contrainte
        delete(CR_ctrlName + "_aimConstraint1")
        
        xform (cp=1)
        #ranger tous les controllers dans le groupe de rig, enfants du controller global
        select (CR_createdController, CR_path, replace=1)
        Parent ()
    
    
    delete (CR_path + "|Leg_L_5_ctrl|", CR_path + "|Arm_R_5_ctrl|", CR_path + "|Head_2_ctrl|", CR_path + "|Arm_L_5_ctrl|")
    
    CR_colorControllers()




def CR_colorControllers():
	CR_path = str(CR_mainGroup[0]) + "|" + str(CR_locatorsGrp) + "|Global_ctrl"
	
	for i in range(26):
		#renvoie une couleur pour chaque controleur
		CR_naming_coloring(i)
		
		#colorise si le controlleur existe
		if (objExists(CR_path + CR_BonesNames[i] + "_ctrl|")):
			#colorise tous les controleur
			setAttr (CR_path + CR_BonesNames[i] + "_ctrl|" + ".overrideEnabled", 1)
			setAttr (CR_path + CR_BonesNames[i] + "_ctrl|" + ".overrideColor", CR_color)

	CR_DeleteAllLocators()
		
		


def CR_DeleteAllLocators():
    CR_path = str(CR_mainGroup[0]) + "|" + str(CR_locatorsGrp) + "|Global_ctrl"

    for i in range (26) :
		delete (CR_path + CR_BonesNames[i] + "_loc|")
    
    rename (str(CR_mainGroup[0]) + "|" + str(CR_locatorsGrp), "RIG")
    
    #select the main group
    select(str(CR_mainGroup[0]))








'''========================== PART III =========================='''
def CR_OrganizeCtrlsInHierachy():
    #recupere le nom du group selectionne
    CR_mainGroup = ls(sl=1, shortNames=1)
    CR_path = str(CR_mainGroup[0]) + "|RIG|Global_ctrl|"
    global CR_mainGroup, CR_path
    
    #organize controllers in hierarchy
    CR_SelectAndParentCtrls(0,5)
    CR_SelectAndParentCtrls(6,10)
    CR_SelectAndParentCtrls(11,15)
    CR_SelectAndParentCtrls(16,20)
    CR_SelectAndParentCtrls(21,25)
    
    #parente les controles entre eux
    parent (CR_path + "|Arm_L_1_ctrl|", CR_path + "|Arm_R_1_ctrl|", CR_path + "|Spine_1_ctrl|Spine_2_ctrl|Spine_3_ctrl|Spine_4_ctrl|")
    parent (CR_path + "|Leg_L_1_ctrl|", CR_path + "|Leg_R_1_ctrl|", CR_path + "|Spine_1_ctrl|")
    
    constraintCtrlsToJoints()




def CR_SelectAndParentCtrls(CR_start,CR_End) :
    select(clear=1)
    #selectione tous les controles d'un meme groupe
    for i in range(CR_start,CR_End) :
        CR_naming_coloring(i) #defini ce qu'il faut selectionner
        select (CR_path + CR_Name + "_ctrl", add=1)
    
    CR_currentSelection = ls(sl=1)

    #parente tous les controleurs selectionnes
    for i in range (1, len(CR_currentSelection)):
        select (CR_currentSelection[len(CR_currentSelection) - i], r=1) #selectionne le dernier element de la liste
        select (CR_currentSelection[len(CR_currentSelection) - i-1], add=1) #selectionne l'avant dernier element
        parent()




def constraintCtrlsToJoints():
    #selectionne tous les controllers
    CR_path = str(CR_mainGroup[0]) + "|RIG|Global_ctrl"
    select(CR_path + "|Spine_1_ctrl")
    SelectHierarchy()
    
    #selectionne tous les controlleurs
    CR_path = "|" + str(CR_mainGroup[0]) + "|SETUP"
    select(CR_path + "|Spine_1_jnt", add=1)
    SelectHierarchy()
    
    #deselectionne les joints aux extremites
    select(CR_path + "|Spine_1_jnt|Spine_2_jnt|Spine_3_jnt|Spine_4_jnt|Head_1_jnt|Head_2_jnt", d=1) #tete
    select(CR_path + "|Spine_1_jnt|Spine_2_jnt|Spine_3_jnt|Spine_4_jnt|Arm_L_1_jnt|Arm_L_2_jnt|Arm_L_3_jnt|Arm_L_4_jnt|Arm_L_5_jnt", d=1) #bras gauche
    select(CR_path + "|Spine_1_jnt|Leg_L_1_jnt|Leg_L_2_jnt|Leg_L_3_jnt|Leg_L_4_jnt|Leg_L_5_jnt", d=1) #jambe gauche
    select(CR_path + "|Spine_1_jnt|Spine_2_jnt|Spine_3_jnt|Spine_4_jnt|Arm_R_1_jnt|Arm_R_2_jnt|Arm_R_3_jnt|Arm_R_4_jnt|Arm_R_5_jnt", d=1) #bras droit
    select(CR_path + "|Spine_1_jnt|Leg_R_1_jnt|Leg_R_2_jnt|Leg_R_3_jnt|Leg_R_4_jnt|Leg_R_5_jnt", d=1) #jambe droite
    
    	
    CR_currentSelection = ls(sl=1, transforms=1)

    #les contraindre aux joints
    for i in range(len(CR_currentSelection)/2):
        #selectionne le controlleur
        select(CR_currentSelection[i], r=1)
        
        #le reinitialiser
        makeIdentity(apply=1, t=1, r=1, s=1, n=0, pn=1)
    	DeleteHistory()
    	
        #selectionne le joint correspondant
        select(CR_currentSelection[len(CR_currentSelection)/2 + i], add=1)
        ParentConstraint(maintainOffset = 1)






'''========================== PART IV =========================='''
def BindSkin():
	sel = ls(sl = True)#Selectionne tes listes de tes éléments quand tu sélectionnes le mesh 
	if (len(sel) == 0):#Situ n'a pas select le mesh alors tu auras le message endessous
		confirmDialog(title = "Empty Selection", message = "You have to select the main group", button = ['Ok'])    
	else:
	
	
		'''partie que j'ai ajoute pour que le script marche quel que soit le groupe qu'on selectionne'''
		#recupere le nom du group selectionne
		CR_mainGroup = ls(sl=1, shortNames=1)
		
		#selectionner tout dans le groupe de geometrie
		select (str(CR_mainGroup[0]) + "|GEO")
		SelectHierarchy() #selectionne egalement les shapes des meshes, c'est pour ca qu'on met le flag transforms dans le ls pour n'avoir que le node de tranform
		#deselectionne le groupe geo
		select(str(CR_mainGroup[0]) + "|GEO", d=1)
		'''partie que j'ai ajoute pour que le script marche quel que soit le groupe qu'on selectionne'''
		
		
		sel = ls(sl = True, transforms=1)#Selectionne tes listes de tes éléments quand tu sélectionnes le mesh
		for i in range(0, len(sel)): 
		    skinCluster(sel[i], (str(CR_mainGroup[0]) + "|SETUP|Spine_1_jnt"), bm = 3, sm = 1, dr = 0.1, name = "Mesh"+str(i))
		    geomBind('Mesh'+str(i), bm = 3, gvp = [256, 1])#gvp resolution   
'''===================================Functions==================================='''



'''===================================Interface==================================='''
window()
columnLayout()

rowColumnLayout(nc = 2)
button (label = "Locators", c = "CR_warningLocators()", annotation = "This is gonna create locators in order to rig the selected meshes. The main group is gonna be call after the fisrt selected object")
text (label = "    Create locators in order to rig the selected meshes")
button (label = "Rig", c = "CR_bipedsRig()", annotation = "Select the main group in order to create joints and controllers")
text (label = "    Select the main group. Creates joints and controllers")
setParent ('..')


rowLayout(nc=3)
button (label = "  +  ", c="floatFieldGrp(CR_locCtrlsSize_FFG, e=1, value1 =(floatFieldGrp(CR_locCtrlsSize_FFG, q=1, value1=1) + 0.1))" + "\nCR_locatorsAndCtrlsSize()") #ajoute 0.1 au scale
button (label = "  -  ", c="floatFieldGrp(CR_locCtrlsSize_FFG, e=1, value1 =(floatFieldGrp(CR_locCtrlsSize_FFG, q=1, value1=1) - 0.1))" + "\nCR_locatorsAndCtrlsSize()") #enleve 0.1 au scale
CR_locCtrlsSize_FFG = floatFieldGrp (extraLabel="Ctrls Default Size", value1 = 1, cc = "CR_locatorsAndCtrlsSize()")
setParent ('..')


rowColumnLayout(nc = 2)
button (label = "Constraint", c = "CR_OrganizeCtrlsInHierachy()", annotation = "Select the main group in order to link the controllers to the joints")
text (label = "    Select the main group. Links controllers to joints")
button (label = "BindSkin", c = "BindSkin()", annotation = "Select the main group in order to skin the mesh(es)")
text (label = "    Select the main group. Skins the mesh(es)")
showWindow()

