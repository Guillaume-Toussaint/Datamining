import sys


cols_noms = ["AGER20","ANEMR","APAF","ASCEN","CATL","CMBL","COUPLE","CS1","DIPL_15","ETUD","HLML","ILETUU","ILTUU","INAI","INFAM","MOCO"
            , "NBPI","NPERR","RECH","SANI","STOCD","SURF","TRANS"]

#fichier_itemsets_traduits = open("res_decode.txt",'r')#open(sys.argv[1],'r')



nameinput = "res_decode.txt"
fichier_itemsets_traduits = None
if len(sys.argv)>1:
    fichier_itemsets_traduits = open(sys.argv[1],'r')
else:
    fichier_itemsets_traduits = open(nameinput,'r')






namefile = "itemsets-regles_exploitables.txt"
out = None
if len(sys.argv)>2:
    out = open(sys.argv[2],'wt')
else:
    out = open(namefile,'wt')



for i in fichier_itemsets_traduits.readlines():
    #print("ligne en cours : ",i)
    if i.strip()!="":##Cas une ligne sur 2
        itemset = i.split("#")[0].strip()
        #print("Itemset : ",itemset)
        association_rules = False
        if "==>" in itemset:
            print("association rule")
            association_rules = True
        for k in itemset.split(" ==> "):
            for j in k.split(" "):
                #print(j,"  ",len(j))
                j = j.strip()
                index_col = int(j.split("-")[0].strip())
                #print("index : ",index_col)
                #print("type : ",type(index_col),"  len : ",len(j.split("-")[0].strip()))

                out.write(cols_noms[index_col]+'-'+j.split("-")[1]+" ")

            if association_rules:
                out.write("==> ")
                association_rules = False

        out.write("#"+i.split("#")[1])
        if len(i.split("#"))>2:#Confiance en plus dans le fichier txt
            out.write("#"+i.split("#")[2])
        out.write("\n")
    out.flush()

fichier_itemsets_traduits.close()
out.close()
