# Usage
# python DecodeAfterSPMF.py fich-a-decoder fich-resultat
#
import sys
import pickle


def decode(a):
#    print invdico
    list=a.split(' ')
    s=""
 #   print list
    for i in list:
 #       print "xxx"+i+"xxxx"
        if i!='' and int(i) in invdico.keys():
 #           print "oui"
            s=s+invdico[int(i)]+' '
 #   print "s"
 #   print s
    return s

p=len(sys.argv)
#print p

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
        print('!!!!! ligne non conforme')
res.close()
    
    
