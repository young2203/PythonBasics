#!/usr/bin/env python
# Create a new FE analysis job from a template
# J.Cugnoni, CAELinux.com, 2005-2013
from Tkinter import *
from tkCommonDialog import *
from tkMessageBox import *
from tkFileDialog import *
import os
import os.path
import sys

astk_bin_path="/opt/aster113/bin/astk"

templateASTK="""
etude,fich,3,FR F
opt_val,rep_dex _VIDE
etude,fich,3,UL 8
etude,fich,2,type mess
etude,fich,4,donnee 0
option,nbmaxnook 1
etude,fich,2,resultat 1
nom_fich_export _VIDE
option,rep_dex 0
etude,fich,4,compress 0
etude oui
debug 0
opt_val,cpresok RESNOOK
forlib_delete non
etude,fich,4,serv Local
etude,fich,3,donnee 0
serv_fich_export -1
surcharge,nbfic 0
etude,fich,6,FR F
path_etude [__prjdir__]
option,rep_outils 0
etude,fich,6,UL 80
etude,fich,3,resultat 1
option,cpresok 1
etude,fich,5,compress 0
etude,fich,1,FR F
etude,fich,1,serv Local
consult_supprimer non
memoire 512
etude,fich,1,UL 20
onglet_actif etude
asquit non
etude,fich,2,donnee 0
option,classe 1
etude,fich,4,type erre
consult_a_corriger non
ident non
etude,fich,4,resultat 1
etude,fich,6,compress 0
etude,fich,1,donnee 1
rex non
etude,fich,1,type libr
etude,fich,1,nom ./[__prjname__]mesh.med
suivi_interactif 1
path_sources _VIDE
pre_eda non
etude,fich,4,FR F
forlib_create non
etude,fich,4,UL 9
etude,fich,3,nom ./[__prjname__].resu
serv_tests -1
etude,fich,6,serv Local
etude,fich,5,nom ./[__prjname__].base
make_etude run
option,depart 1
nom_profil [__astkfile__]
args _VIDE
etude,fich,5,resultat 1
etude,fich,0,donnee 1
opt_val,mem_aster _VIDE
etude,fich,3,serv Local
etude,fich,0,compress 0
option,mem_aster 1
asdeno non
serv_surcharge -1
serv_sources -1
surcharge non
etude,fich,6,type rmed
etude,fich,0,serv Local
M_1 oui
serv_etude -1
M_2 non
etude,fich,6,resultat 1
etude,fich,2,FR F
opt_val,rep_outils _VIDE
M_3 non
etude,fich,2,UL 6
path_surcharge _VIDE
consult non
M_4 non
asno non
etude,fich,3,type resu
etude,fich,1,compress 0
opt_val,ncpus 1
emis_sans non
serveur localhost
opt_val,classe _VIDE
opt_val,dbgjeveux _VIDE
option,ncpus 1
etude,fich,0,type comm
opt_val,facmtps 1
etude,fich,0,resultat 0
opt_val,rep_mat _VIDE
special _VIDE
tests,nbfic 0
temps 240
option,dbgjeveux 0
etude,fich,5,FR R
etude,fich,5,serv Local
asrest non
batch 0
etude,fich,5,UL 0
etude,fich,2,compress 0
option,facmtps 1
serv_profil -1
etude,fich,6,donnee 0
etude,fich,0,FR F
option,rep_mat 0
etude,fich,0,UL 1
etude,fich,2,serv Local
etude,fich,0,nom ./[__prjname__].comm
asverif non
etude,fich,2,nom ./[__prjname__].mess
opt_val,depart _VIDE
etude,fich,1,resultat 0
sources,nbfic 0
etude,fich,5,donnee 0
etude,fich,4,nom ./[__prjname__].erre
tests non
noeud localhost
etude,fich,5,type base
etude,fich,3,compress 0
emis_prof non
etude,fich,6,nom ./[__prjname__]res.med
etude,nbfic 7
agla non
opt_val,nbmaxnook 5
version STA11.3
path_tests _VIDE
nom_profil %s
path_etude %s
etude,fich,0,nom ./%s.comm
etude,fich,1,nom ./%smesh.med
etude,fich,2,nom ./%s.mess
etude,fich,3,nom ./%s.resu
etude,fich,4,nom ./%s.erre
etude,fich,5,nom ./%s.base
etude,fich,6,nom ./%sres.med
"""

class CreateJobApp(Frame):
    def createWidgets(self):
        irow=0
        # prjname
        irow=irow+1
        self.prjlbl=Label(self,text="Project Name: ")
        self.prjname=Entry(self,width=40)
        self.prjlbl.grid(row=irow,column=1)
        self.prjname.grid(row=irow,column=2)
        # basedir
        irow=irow+1
        self.basedirlbl=Label(self,text="Base directory: ")
        self.basedirname=Entry(self,width=40)
        self.basedirlbl.grid(row=irow,column=1)
        self.basedirname.grid(row=irow,column=2)
        self.basedirbtn=Button(self,text="...",command=self.selectBaseDir)
        self.basedirbtn.grid(row=irow,column=3)
        # MED mesh file
        irow=irow+1
        self.meshlbl=Label(self,text="MED Mesh File: ")
        self.meshname=Entry(self,width=40)
        self.meshlbl.grid(row=irow,column=1)
        self.meshname.grid(row=irow,column=2)
        self.meshbtn=Button(self,text="...",command=self.selectMesh)
        self.meshbtn.grid(row=irow,column=3)
        # template file
        irow=irow+1
        self.tpllbl=Label(self,text="Template File: ")
        self.tplname=Entry(self,width=40)
        self.tpllbl.grid(row=irow,column=1)
        self.tplname.grid(row=irow,column=2)
        self.tplbtn=Button(self,text="...",command=self.selectTpl)
        self.tplbtn.grid(row=irow,column=3)
        # buttons
        irow=irow+1
        self.okbtn=Button(self,text="GO",command=self.validate)
        self.okbtn.grid(row=irow,column=1)
                
    def __init__(self,master=None):        
        self.vars={"prjname":"","basedirname":"","meshname":"","tplname":""}
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def selectBaseDir(self):
        titl="Select a base directory:"
        self.setText(self.basedirname,askdirectory(title=titl))

    def selectMesh(self):
        self.setText(self.meshname,askopenfilename(title="Select a MED mesh file",filetypes=(("MED file ","*.med"),)))
        
    def selectTpl(self):
        tpldir=os.path.join(os.path.dirname(sys.argv[0]),"Templates")
        self.setText(self.tplname,askopenfilename(initialdir=tpldir,title="Select a Template COMM file",filetypes=(("COMM file ","*.comm"),)))

    def getvars(self):
        self.vars["prjname"]=self.prjname.get()
        self.vars["basedirname"]=self.basedirname.get()
        self.vars["meshname"]=self.meshname.get()
        self.vars["tplname"]=self.tplname.get()
        
    def setText(self,obj,txt):
        obj.delete(0,65535)
        obj.insert(0,txt)

    def copyfile(self,filein,fileout):
        fd1=open(filein,"r")
        fd2=open(fileout,"w")
        fd2.write(fd1.read())
        fd1.close()
        fd2.close()        

    def validate(self):
        # retrieve variables
        self.getvars()
        bdir=self.vars["basedirname"].strip()
        prjname=self.vars["prjname"].strip()
        meshname=self.vars["meshname"].strip()
        tplname=self.vars["tplname"].strip()
        prjdir=os.path.join(bdir,prjname)
        if os.path.exists(prjdir):
            showerror(title="Error",message="Error, project name allready exists in base directory")
        else:
            # project directory
            os.makedirs(prjdir)
            # file names
            commfile=os.path.join(prjdir,prjname + ".comm")
            messfile=os.path.join(prjdir,prjname + ".mess")
            errefile=os.path.join(prjdir,prjname + ".erre")
            resufile=os.path.join(prjdir,prjname + ".resu")
            mmedfile=os.path.join(prjdir,prjname + "mesh.med")
            rmedfile=os.path.join(prjdir,prjname + "res.med")
            basefile=os.path.join(prjdir,prjname + ".base")
            astkfile=os.path.join(prjdir,prjname + ".astk")
            # copy files
            self.copyfile(meshname,mmedfile)
            self.copyfile(tplname,commfile)
            # create ASTK profile
            fd=open(astkfile,"w")
            fd.write(templateASTK % ((astkfile,prjdir,) + (prjname,)*7))
            fd.close()
            # show message and exit
            showinfo(title="Success",message=("New FE analysis project %s created sucessfully. We open it now with ASTK to continue your analysis." % astkfile))
            os.system("%s --profil %s &"%(astk_bin_path,astkfile))
            #self.doquit()

# main
app=CreateJobApp()
top=app.master
top.wm_title("Create New Aster Job")
app.mainloop()

