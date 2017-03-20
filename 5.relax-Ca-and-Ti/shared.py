#%!/usr/bin/env python
#

import os
import shutil

class find_me_parser():
    def get_poscar(self):
        with open(os.path.join(self.prefix,"POSCAR"),"r") as pos_file:
            self.pos=pos_file.read()
        self.to_replace=self.pos
    def __init__(self,prefix):
        self.prefix = prefix
        self.get_poscar()
    def get_energy_vasp(self,var,tag):
        this_name=os.path.join(self.prefix,"try_%s"%tag)
        self.copy_data(this_name,var)
        os.system("cd %s;vasp_without_mpi 1>output"%this_name)
        ans = self.analyze(os.path.join(this_name,"OUTCAR"))
        return ans
    def copy_data(self,this_name,var):
        shutil.rmtree(this_name,ignore_errors=True)
        os.makedirs(this_name)
        shutil.copy(os.path.join(self.prefix,"INCAR"),os.path.join(this_name,"INCAR"))
        shutil.copy(os.path.join(self.prefix,"POTCAR"),os.path.join(this_name,"POTCAR"))
        shutil.copy(os.path.join(self.prefix,"KPOINTS"),os.path.join(this_name,"KPOINT"))
        with open(os.path.join(this_name,"POSCAR"),"w") as this_pos_file:
            this_pos_file.write(self.get_this_pos(var))
    def get_this_pos(self,var):
        this_pos=self.to_replace
        this_pos += "%f %f %f\n"%(var[0],var[1],var[2])
        this_pos += "%f %f %f\n"%(var[3]+0.5,var[4]+0.5,var[5]+0.5)
        this_pos += "0.5 0.0 0.0\n0.0 0.5 0.0\n0.0 0.0 0.5\n"
        return this_pos
    def ana(self,text):
        p = text.split("\n")[2:2+2]
        return map(
                float,
                sum(
                    map(
                        lambda x:x.split()[:3],
                        p
                        ),
                    []
                    )
                )
    def analyze(self,file_name):
        with open(file_name,"r") as to_ana_file:
            to_ana=to_ana_file.read()
            temp = 0
            ans = []
            while True:
                start=to_ana.find("POSITION",temp)
                if start == -1:
                    if temp==0:
                        return []
                    break
                temp=start+1
                end=to_ana.find("entropy",start)
                this_t=to_ana[start:end]
                ans.append([self.ana(this_t)])
        en=float(this_t[this_t.find("TOTEN"):].split()[2])
        for i in ans:
            i.append(en)
        return ans
    get_energy=get_energy_vasp
