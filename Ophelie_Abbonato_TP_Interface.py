import maya.cmds as cmds

cmds.file(new=True,f=True)

#Les Colonnes

#Variables 'haut' :
    
hauteurCube = 0.5
largeurCube = 2.0
epaisseurCube = 2.0

#Variables 'colonne' :

radiusCylindre = 0.5
hauteurCylindre = 5.0

#Variables 'bas' :
    
hauteurSocle = 0.5
largeurSocle = 2.0
epaisseurSocle = 2.0



haut = cmds.polyCube(w = largeurCube ,d = epaisseurCube ,h = hauteurCube, name='haut')
cmds.move(0,hauteurSocle + hauteurCylindre + hauteurCube /2,0, 'haut')

colonne = cmds.polyCylinder(r = radiusCylindre, h = hauteurCylindre, name='colonne')
cmds.move(0,hauteurSocle + hauteurCylindre /2, 0)

bas = cmds.polyCube(w = largeurSocle, d = epaisseurSocle, h = hauteurSocle, name='bas')
cmds.move(0, hauteurSocle/2, 0, 'bas')
#Création d'une interface

cmds.window(title = " Temple 3.0 © ATI ")
cmds.columnLayout()
cmds.attrFieldSliderGrp(label = " Taille X du socle de la colonne ", min = 0.1, max=10.0, at='bas.sx' )
cmds.attrFieldSliderGrp(label = " Taille Y du socle de la colonne ", min = 0.1, max=10.0, at='bas.sy' )
cmds.attrFieldSliderGrp(label = " Taille z du socle de la colonne ", min = 0.1, max=10.0, at='bas.sz' )

cmds.attrFieldSliderGrp(label = " Taille X du haut de la colonne ", min = 0.1, max=10.0, at='haut.sx' )
cmds.attrFieldSliderGrp(label = " Taille Y du haut de la colonne ", min = 0.1, max=10.0, at='haut.sy' )
cmds.attrFieldSliderGrp(label = " Taille Z du haut de la colonne ", min = 0.1, max=10.0, at='haut.sz' )

cmds.attrFieldSliderGrp(label = "Taille X du cylindre de la colonne", min = 0.1, max=10.0, at='colonne.sx' )
cmds.attrFieldSliderGrp(label = "Taille Y du cylindre de la colonne", min = 0.1, max=10.0, at='colonne.sy' )
cmds.attrFieldSliderGrp(label = "Taille Z du cylindre de la colonne", min = 0.1, max=10.0, at='colonne.sz' )

#Variables nombre de colonnes (de 1 à 6) par rangs :
    
nbColonnades = 6
espaceEntreColonnes = 4

colonnade = cmds.group( 'colonne', 'haut', 'bas', name='colonnade' )

for i in range (nbColonnades):
    cmds.duplicate()
    cmds.move (espaceEntreColonnes * (i+1),0,0)
    
#Variables nombre de rangs (de 1 à 6) :
    
nbRangs = 6
espaceEntreRangs = 4
    
rang = cmds.group ( 'colonnade', 'colonnade1', 'colonnade2', 'colonnade3', 'colonnade4', 'colonnade5', 'colonnade6', name = 'rang' )

for i in range (nbRangs):
    cmds.duplicate()
    cmds.move (0,0,espaceEntreRangs * (i+1))       

#Les marches pour le RDC
#Variables 'RDCmarche1' :
    
hauteurMarche = 2.0
largeurMarche = 28.0
epaisseurMarche = 28.0

hauteurMarche1 = 2.0
largeurMarche1 = 29.0
epaisseurMarche1 = 29.0

hauteurMarche2 = 2.0
largeurMarche2 = 30.0
epaisseurMarche2 = 30.0

RDCmarche1 = cmds.polyCube(w = largeurMarche ,d = epaisseurMarche ,h = hauteurMarche, name='RDCmarche1')
cmds.move(11.967,(-hauteurMarche/2),11.967,'RDCmarche1')

RDCmarche2 = cmds.polyCube(w = largeurMarche1 ,d = epaisseurMarche1 ,h = hauteurMarche1, name='RDCmarche2')
cmds.move(11.967,(-hauteurMarche) + (-hauteurMarche1/2),11.967,'RDCmarche2')

RDCmarche3 = cmds.polyCube(w = largeurMarche2 ,d = epaisseurMarche2 ,h = hauteurMarche2, name='RDCmarche3')
cmds.move(11.967,(-hauteurMarche) + (-hauteurMarche1) + (-hauteurMarche2/2),11.967,'RDCmarche3')

#interface marches

cmds.attrFieldSliderGrp(label = " Taille X de la première marche ", min = 0.1, max=10.0, at='RDCmarche1.sx' )
cmds.attrFieldSliderGrp(label = " Taille Y de la première marche ", min = 0.1, max=10.0, at='RDCmarche1.sy' )
cmds.attrFieldSliderGrp(label = " Taille Z de la première marche ", min = 0.1, max=10.0, at='RDCmarche1.sz' )

cmds.attrFieldSliderGrp(label = " Taille X de la deuxième marche ", min = 0.1, max=10.0, at='RDCmarche2.sx' )
cmds.attrFieldSliderGrp(label = " Taille Y de la deuxième marche ", min = 0.1, max=10.0, at='RDCmarche2.sy' )
cmds.attrFieldSliderGrp(label = " Taille Z de la deuxième marche ", min = 0.1, max=10.0, at='RDCmarche2.sz' )

cmds.attrFieldSliderGrp(label = " Taille X de la troisième marche ", min = 0.1, max=10.0, at='RDCmarche3.sx' )
cmds.attrFieldSliderGrp(label = " Taille Y de la troisième marche ", min = 0.1, max=10.0, at='RDCmarche3.sy' )
cmds.attrFieldSliderGrp(label = " Taille Z de la troisième marche ", min = 0.1, max=10.0, at='RDCmarche3.sz' )

#Frise du dessus

hauteuFriseGrecqueBordures = 0.5
largeurFriseGrecqueBordures = 30.0
epaisseurFriseGrecqueBordures = 30.0 

hauteuFriseGrecqueInterieur = 1.0
largeurFriseGrecqueInterieur = 28.0
epaisseurFriseGrecqueInterieur = 28.0 

hauteuFriseGrecqueBordures1 = 0.5
largeurFriseGrecqueBordures1 = 30.0
epaisseurFriseGrecqueBordures1 = 30.0 

frise1 = cmds.polyCube(w = largeurFriseGrecqueBordures ,d = epaisseurFriseGrecqueBordures ,h = hauteuFriseGrecqueBordures, name='frise1')
cmds.move(11.967,hauteurSocle + hauteurCylindre + hauteurCube + hauteuFriseGrecqueBordures/2,11.967,'frise1')

frise2 = cmds.polyCube(w = largeurFriseGrecqueInterieur ,d = epaisseurFriseGrecqueInterieur ,h = hauteuFriseGrecqueInterieur, name='frise2')
cmds.move(11.967,hauteurSocle + hauteurCylindre + hauteurCube + hauteuFriseGrecqueBordures + hauteuFriseGrecqueInterieur/2,11.967,'frise2')

frise3 = cmds.polyCube(w = largeurFriseGrecqueBordures1 ,d = epaisseurFriseGrecqueBordures1 ,h = hauteuFriseGrecqueBordures1, name='frise3')
cmds.move(11.967,hauteurSocle + hauteurCylindre + hauteurCube + hauteuFriseGrecqueBordures + hauteuFriseGrecqueInterieur + 
hauteuFriseGrecqueBordures1/2,11.967,'frise3')

#interface frise

cmds.attrFieldSliderGrp(label = " Taille X de la première frise ", min = 0.1, max=10.0, at='frise1.sx' )
cmds.attrFieldSliderGrp(label = " Taille Y de la première frise ", min = 0.1, max=10.0, at='frise1.sy' )
cmds.attrFieldSliderGrp(label = " Taille Z de la première frise ", min = 0.1, max=10.0, at='frise1.sz' )

cmds.attrFieldSliderGrp(label = " Taille X de la deuxième frise ", min = 0.1, max=10.0, at='frise2.sx' )
cmds.attrFieldSliderGrp(label = " Taille Y de la deuxième frise ", min = 0.1, max=10.0, at='frise2.sy' )
cmds.attrFieldSliderGrp(label = " Taille Z de la deuxième frise ", min = 0.1, max=10.0, at='frise2.sz' )

cmds.attrFieldSliderGrp(label = " Taille X de la troisième frise ", min = 0.1, max=10.0, at='frise3.sx' )
cmds.attrFieldSliderGrp(label = " Taille Y de la troisième frise ", min = 0.1, max=10.0, at='frise3.sy' )
cmds.attrFieldSliderGrp(label = " Taille Z de la troisième frise ", min = 0.1, max=10.0, at='frise3.sz' )


#Création du toit
#Variables pour le toit

penteToit = 2.0
hauteurToit = 1.0

toit = cmds.polyCube(width = largeurMarche, depth = epaisseurMarche, height = hauteurToit, subdivisionsDepth=2, name='toit')
cmds.move(11.967 ,hauteurSocle + hauteurCylindre + hauteurCube + hauteuFriseGrecqueBordures + hauteuFriseGrecqueInterieur + 
hauteuFriseGrecqueBordures1 + hauteurToit/2,11.967,'toit')

#Création de la pente du toit
cmds.polyMoveVertex('toit.vtx[4]', ty = penteToit)
cmds.polyMoveVertex('toit.vtx[5]', ty = penteToit)

cmds.attrFieldSliderGrp(label = "Taille X du toit", min = 0.1, max=10.0, at='toit.sx' )
cmds.attrFieldSliderGrp(label = "Taille Y du toit", min = 0.1, max=10.0, at='toit.sy' )
cmds.attrFieldSliderGrp(label = "Taille Z du toit", min = 0.1, max=10.0, at='toit.sz' )

cmds.showWindow()