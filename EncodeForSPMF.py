#
# Usage : python <File-to-encode> <encoded-file>
# Usage : python <File-to-encode> (ecriture dans out.txt)
#
#

import sys
import pickle

p=len(sys.argv)
print(p)

if p==3:
    f_out=sys.argv[2]
else:
    f_out="out.txt"

# Construction du dictionnaire
dico={}
invdico={}
indice=1
f=open(sys.argv[1],'r')
f.readline() # On enlève la première ligne de header
for line in f.readlines():
    line=line.rstrip()
    #print(line)
    for i,e in enumerate(line.split(',')):
        a=str(i)+"-"+e
        if a not in dico.keys():
            print(a)
            dico[a]=indice
            invdico[indice]=a
            indice +=1
f.close()

print(dico)

# construction du fichier de donnees
out=open(f_out,'w')
f=open(sys.argv[1],'r')
for line in f.readlines():
    line=line.rstrip()
    l=[]
 #   print line
    for i,e in enumerate(line.split(',')):
        a=str(i)+"-"+e
        l.append(dico[a])
    l.sort()
    l2=[str(i) for i in l]
    
    
#    input("xxx :")
#    out.write
    #out.write("{"+",".join(l2)+"}")
    out.write(" ".join(l2))
    out.write("\n")
f.close()

fichier=open('invdico.dbm', 'wb')
pickle.dump(invdico,fichier)
