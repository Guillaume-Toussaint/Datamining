#
#Fichier tiré du TP de Data Mining
#On se sert de ce fichier post traitement pour ensuite le translittérer dans un fichier lisible

 #Usage
# python DecodeAfterSPMF.py fich-a-decoder fich-resultat
#
import sys
import pickle


def decode(a):
    list=a.split(' ')
    s=""

    for i in list:
        if i!='' and int(i) in invdico.keys():
            s=s+invdico[int(i)]+' '
    return s

p=len(sys.argv)

if p==3:
    f_out=sys.argv[2]
else:
    f_out="res_decode.txt"
res=open(f_out,'w')


# Construction du dictionnaire
dic = open('invdico.dbm', 'rb')
invdico = pickle.load(dic)
print(invdico)

results= sys.argv[1]
f = open(results,'r')

for l in f.readlines():
    r=l.split("#")
 #   print r
    aa=r[0].split('==> ') # on decoupe comme s'il s'agit d'une regle
    if len(aa)==1:
        rdec=decode(aa[0])
        res.write(rdec+'# '+'# '.join(r[1:])+'\n')
    elif len(aa)==2:
        rdec0=decode(aa[0])
        rdec1=decode(aa[1])
        res.write(rdec0 +'==> '+ rdec1 +'# '+'# '.join(r[1:])+'\n')
    else:
        print('Format de ligne incorrect')
res.close()
