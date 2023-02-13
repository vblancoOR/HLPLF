import numpy as np
import random
import itertools

# =============================================================================
# Generates nxn random matrices with probabilities in list P= [0.1, 0.2, 0.3])
# maxit instances are generated.
# the matrices are stored in files filesP/ProbGroupsNn_it.txt"
# =============================================================================
# P= [0.1, 0.2, 0.3, 0.4, 0.5]

def ProbGenerationGroups(n: int, maxit: int):
    
    A=list(itertools.product(range(n),range(n)))

    E=[]
    for a in A:
        if a[0]<a[1]:
            E.append(a)
    for it in range(maxit):        
        rd=np.random.randint(3, size=len(E))
    
        file="filesP/ProbGroupsN%d_%d.txt"%(n,it+1)

        p=np.zeros((n,n))
        for k in range(n):
            p[k,k]=0.05
            
            
        for i in range(len(E)):
            if rd[i]==0:
                p[E[i][0],E[i][1]]=0.1
            if rd[i]==1:
                p[E[i][0],E[i][1]]=0.2
            if rd[i]==2:
                p[E[i][0],E[i][1]]=0.3
        
                
            
            p[E[i][1],E[i][0]]=p[E[i][0],E[i][1]]
            
            
            
        np.savetxt(file,p,fmt='%.4f')
 
    
 # =============================================================================
 # Generates nxn random matrices with xame probabilities in list P
 # =============================================================================
#P=[0.1, 0.2, 0.3]        
 
def ProbGenerationSame(n: int, P: list):
    
    for pp in P:
        file="filesP/ProbsSameN%dP%.1f.txt"%(n,pp)
        p=pp*np.ones((n,n))
            
                
                
                
        np.savetxt(file,p,fmt='%.4f')
        
        
# =============================================================================
# Generates nxn random matrices with probabilities up to those in list "P" (we use P= [0.1, 0.2, 0.3, 0.4, 0.5])
# in our experiments, "maxit" random instances for each probability in P.
# the matrices are stored in files filesP/ProbNnPp_it.txt"
# =============================================================================
# P= [0.1, 0.2, 0.3, 0.4, 0.5]
        
def ProbGenerationRandom(n: int, maxit: int, P: list):
    
    for p0 in P:
        for it in range(maxit):
            file="filesP/ProbN%dP%.1f_%d.txt"%(n,p0,it+1)
    
            p=p0*np.random.rand(n,n)#0.3*np.ones((n,n))
            
            minp=np.min(p)
            
            
            np.fill_diagonal(p, minp*np.random.rand(n))
            
            psym=(p+p.T)/2
            
            
            
            np.savetxt(file,psym,fmt='%.4f')    