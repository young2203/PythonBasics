#!/usr/bin/env python
# Create a new static FE analysis job for Calculix based on a Salome mesh
#  mesh preparation steps:
#   to avoid having undesired shells / beams in the model, create two groups 
#   called X_edge and X_surfs in Salome. All elements of groups starting with
#   X_ will be deleted by the converter"
 
# J.Cugnoni, CAELinux.com, 2014
from Tkinter import *
from tkCommonDialog import *
from tkMessageBox import *
from tkFileDialog import *
import os
import commands
import subprocess
import os.path
import sys

envsource="/opt/CalculiX_2.6.1/setenv.sh"
ccx_bin="/usr/loca/bin/ccx"
cgx_bin="/usr/local/bin/cgx"
paraview_bin="/opt/paraviewopenfoam3120/bin/paraview"
unv2abaqus="/opt/caelinux/unv2abaqus.py"
editor="/usr/bin/gnome-text-editor"

tplSurfHeader="""
read %s
"""
tplSurfBody="""
comp %s down
send %s abq surf
"""
tplSurfFooter="""
exit
"""

inpTemplate="""
*MATERIAL,NAME=STEEL
*ELASTIC
210e3, 0.3
*DENSITY
7850e-12
*STEP
*STATIC
10
*BOUNDARY
Group1,1,3,0.
*CLOAD
Group2,0.1,0.1,0.1
*NODE FILE
U,S,E
*END STEP

"""

scriptListGrps='grep "\*NSET.*,.*NSET=" %s | cut -d"=" -f2'


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
        self.meshlbl=Label(self,text="Salome UNV Mesh: ")
        self.meshname=Entry(self,width=40)
        self.meshlbl.grid(row=irow,column=1)
        self.meshname.grid(row=irow,column=2)
        self.meshbtn=Button(self,text="...",command=self.selectMesh)
        self.meshbtn.grid(row=irow,column=3)
        # template file
        #irow=irow+1
        #self.tpllbl=Label(self,text="Template File: ")
        #self.tplname=Entry(self,width=40)
        #self.tpllbl.grid(row=irow,column=1)
        #self.tplname.grid(row=irow,column=2)
        #self.tplbtn=Button(self,text="...",command=self.selectTpl)
        #self.tplbtn.grid(row=irow,column=3)
        # buttons
        irow=irow+1
        self.readbtn=Button(self,text="Convert",command=self.convert)
        self.readbtn.grid(row=irow,column=1)
        self.editbtn=Button(self,text="Edit",command=self.edit_inp)
        self.editbtn.grid(row=irow,column=2)
        self.cgxbtn=Button(self,text="CGX Pre-pro",command=self.cgx)
        self.cgxbtn.grid(row=irow,column=3)
        irow=irow+1
        self.solvebtn=Button(self,text="Solve",command=self.solve)
        self.solvebtn.grid(row=irow,column=1)
        self.postbtn=Button(self,text="PostPro",command=self.postpro)
        self.postbtn.grid(row=irow,column=2)
                
    def __init__(self,master=None):        
        self.vars={"prjname":"","basedirname":"","meshname":"","tplname":""}
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def selectBaseDir(self):
        titl="Select a base directory:"
        self.setText(self.basedirname,askdirectory(title=titl))

    def selectMesh(self):
        self.setText(self.meshname,askopenfilename(title="Select a UNV mesh file",filetypes=(("UNV file ","*.unv"),)))
        
    #def selectTpl(self):
    #    tpldir=os.path.join(os.path.dirname(sys.argv[0]),"Templates")
    #    self.setText(self.tplname,askopenfilename(initialdir=tpldir,title="Select a Template INP file",filetypes=(("INP file ","*.inp"),)))

    def getvars(self):
        self.vars["prjname"]=self.prjname.get()
        self.vars["basedirname"]=self.basedirname.get()
        self.vars["meshname"]=self.meshname.get()
        #self.vars["tplname"]=self.tplname.get()
        
    def setText(self,obj,txt):
        obj.delete(0,65535)
        obj.insert(0,txt)

    def copyfile(self,filein,fileout):
        fd1=open(filein,"r")
        fd2=open(fileout,"w")
        fd2.write(fd1.read())
        fd1.close()
        fd2.close()        

    def convert(self):
        # retrieve variables
        self.getvars()
        bdir=self.vars["basedirname"].strip()
        prjname=self.vars["prjname"].strip()
        meshname=self.vars["meshname"].strip()
        #tplname=self.vars["tplname"].strip()
        prjdir=os.path.join(bdir,prjname)
        if os.path.exists(prjdir):
            showerror(title="Error",message="Error, project name allready exists in base directory")
        else:
            # project directory
            print("Make project directory")
            os.makedirs(prjdir)
	    os.chdir(prjdir)
            # file names
            prefix=os.path.join(prjdir,prjname)
            inpfile=os.path.join(prjdir,prjname + ".inp")
            unvfile=os.path.join(prjdir,prjname + ".unv")
            #surfscript=os.path.join(prjdir,prjname + "post.fbd")
            #tplfile==os.path.join(prjdir,prjname + ".tpl.inp")
            # copy files
            print("Copy files")
            self.copyfile(meshname,unvfile) 
            #self.copyfile(tplname,tplfile)
            # convert mesh
            print("Convert UNV mesh to CCX")
            cmdline="%s %s %s N"%(unv2abaqus,unvfile,prefix)
            print(cmdline)
            os.system(cmdline)
            # append MATERIALS and STEP section
            os.system("echo '%s' >>%s"%(inpTemplate,inpfile))
            # show message and exit
            showinfo(title="Success",message=("Operation finished, please read output in terminal. Output file: %s" % inpfile))
            #self.doquit()

    def edit_inp(self):
        self.getvars()
        bdir=self.vars["basedirname"].strip()
        prjname=self.vars["prjname"].strip()
        meshname=self.vars["meshname"].strip()
        prjdir=os.path.join(bdir,prjname)
        prefix=os.path.join(prjdir,prjname)
        inpfile=os.path.join(prjdir,prjname + ".inp")
        subprocess.Popen([editor,inpfile])

    def cgx(self):
        self.getvars()
        bdir=self.vars["basedirname"].strip()
        prjname=self.vars["prjname"].strip()
        meshname=self.vars["meshname"].strip()
        prjdir=os.path.join(bdir,prjname)
        prefix=os.path.join(prjdir,prjname)
        inpfile=os.path.join(prjdir,prjname + ".inp")        
        subprocess.Popen([cgx_bin,"-c",inpfile])

    def solve(self):
        self.getvars()
        bdir=self.vars["basedirname"].strip()
        prjname=self.vars["prjname"].strip()
        meshname=self.vars["meshname"].strip()
        prjdir=os.path.join(bdir,prjname)
        prefix=os.path.join(prjdir,prjname)
        inpfile=os.path.join(prjdir,prjname + ".inp")
        os.system("cd %s; source %s; %s %s"%(prjdir,envsource,ccx_bin,prefix))   

    def postpro(self):
        self.getvars()
        bdir=self.vars["basedirname"].strip()
        prjname=self.vars["prjname"].strip()
        meshname=self.vars["meshname"].strip()
        prjdir=os.path.join(bdir,prjname)
        prefix=os.path.join(prjdir,prjname)
        inpfile=os.path.join(prjdir,prjname + ".inp")        
        subprocess.Popen([paraview_bin])

# main
app=CreateJobApp()
top=app.master
top.wm_title("Create New Calculix Analysis")
app.mainloop()

