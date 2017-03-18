import os
from subprocess import check_output as co

def run(size):
    os.system("mkdir try_%f 1>/dev/null 2>&1"%size)
    os.system("cp POTCAR KPOINTS INCAR try_%f/"%size)
    os.system("cat POSCAR | sed s/size/%(s)f/g > try_%(s)f/POSCAR"%{"s":size})
    os.system("cd try_%f;mpirun -n 22 vasp 1>/dev/null 2>&1"%size)
    return float(co("cd try_%f;grep TOTEN OUTCAR | tail -n 1"%size,shell=True).split()[-2])

def find(a,A,b,B):
    if b-a < 0.01:
        return
    print a,b,A,B
    m = (2.*a + b)/3
    n = (2.*b + a)/3
    M = run(m)
    N = run(n)
    if M < N:
        find(a,A,n,N)
    else:
        find(m,M,b,B)

def main(a,b):
    A=run(a)
    B=run(b)
    find(a,A,b,B)


if __name__ == "__main__":
    main(2,8)
