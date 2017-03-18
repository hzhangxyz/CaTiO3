import os
from subprocess import check_output as co

def run(size):
    os.system("mkdir %f 1>/dev/null 2>&1"%size)
    os.system("cp POTCAR KPOINTS INCAR %f/"%size)
    os.system("cat POSCAR | sed s/size/%(s)f/g > %(s)f/POSCAR"%{"s":size})
    os.system("cd %f;mpirun -n 22 vasp"%size)
    return float(co("cd %f;grep TOTEN OUTCAR | tail -n 1"%size,shell=True).split()[-2])

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
