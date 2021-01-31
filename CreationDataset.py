


data = open("GrandEst",'r') ## Le dataset doit s'appeler GrandEst et se trovuer dans le répertoire courant.


#Noms des colonnes que nous allons garder
cols_noms = ["AGER20","ANEMR","APAF","ASCEN","CATL","CMBL","COUPLE","CS1","DIPL_15","ETUD","HLML","ILETUU","ILTUU","INAI","INFAM","MOCO"
            , "NBPI","NPERR","RECH","SANI","STOCD","SURF","TRANS"] #### Noms ds colonnes qui intéressent

cols = data.readline()



cols_indice = dict()

noms = cols.split(";")

k=0 #Constitution d'un tableau avec les indices des colonnes que l'on conserve pour créer le nouveau dataset
for n in noms:
    if n in cols_noms:
        cols_indice[n] = k
    k+=1


print(cols_indice) # Colonnes et indices de celles-ci


##On créée le dataset que l'on va utiliser par la suite
outfile = open("data.txt",'wt')
for d in data:
    ligne = d.split(";")
    #print(ligne)
    to_print = ""
    for v in cols_indice.values():
        to_print+=ligne[v]+","
        #print(to_print)
    to_print = to_print[:-1]
    #print(to_print)
    outfile.write(to_print+"\n")
    outfile.flush()
outfile.close()
