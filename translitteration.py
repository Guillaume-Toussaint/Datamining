import sys


cols_noms = ["AGER20","ANEMR","APAF","ASCEN","CATL","CMBL","COUPLE","CS1","DEIPL_15","ETUD","HLML","ILETUU","ILTUU","INAI","INFAM","MOCO"
            , "NBPI","NPERR","RECH","SANI","STOCD","SURF","TRANS"]

fichier_itemsets_traduits = open("res_decode.txt",'r')#open(sys.argv[1],'r')


out = open("itemsets_traduits.txt",'wt')
res = ""


for i in fichier_itemsets_traduits.readlines():
    print("ligne en cours : ",i)
    if i.strip()!="":##Cas une ligne sur 2
        itemset = i.split("#")[0].strip()
        #print("Itemset : ",itemset)
        for j in itemset.split(" "):
            #print(j,"  ",len(j))
            j = j.strip()
            index_col = int(j.split("-")[0].strip())
            #print("index : ",index_col)
            #print("type : ",type(index_col),"  len : ",len(j.split("-")[0].strip()))
        
            out.write(cols_noms[index_col]+'-'+j.split("-")[1]+" ")
        out.write("#"+i.split("#")[1]+"\n")
    out.flush()

fichier_itemsets_traduits.close()
out.close()
