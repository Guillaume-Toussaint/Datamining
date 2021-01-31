# Data minig - Notice d'utilisation du projet
#### Guillaume Toussaint - Morgane Coltel - Christian Barbesant



## Prérequis

- Un outil capable de lire les notebooks python (ex : jupyter)
- Une installation de python3
- Une installation du JRE


## Jeu de données

Nous avons décidé pour ce projet de simplifier le jeu de données Grand Est pour qu'il corresponde à l'utilisation que l'on souhaite en faire.
Pour cela, nous avons réalisé un notebook python qui permet cette transformation, et qui peut servir à effectuer divers traitements sur le jeu de données.

Pour transformer le jeu de données en jeu de données réduit, il suffit d'exécuter les blocs de code présents dans le notebook **en ayant le fichier de données Grand Est dans le répertoire dans lequel se trouve le notebook**. En conséquence, le fichier passe d'unt taille de 400 Mo à seulement 72 Mo.

## Encodage pour SPMF

Pour transformer ce jeu de données en un fichier exploitable par SPMF, nous avons utilisé le programme fourni durant l'un des TP de ce cours.
Pour l'utiliser, il suffit d'exécuter la commande suivante dans un terminal :
`python EncodeForSpmf.py data.txt pour_spmf.txt` sur Windows
`python3 EncodeForSpmf.py data.txt pour_spmf.txt` sur Linux

Faire ceci nous donne un jeu de données plus important, car le programme transforme les attributs multivalués du jeu de donénes de départ en plusieurs colonnes de valeurs booléennes.
En effet, le jeu de données passe à une taille de 92Mo.

## Utilisation par SPMF

Le jeu de données nouvellement créé et transformé est désormais exploitable par SPMF.
On peut désormais l'utiliser sur SPMF, notamment via l'algorithme FPGrowth.
Dans un premier temps, on sélectionne l'agorithme FPGrowth_itemsets. On définit un support, et on choisit d'inscrire les résultats dans un fichier de sortie qui sera noté <X> dans la suite de ce document.

## Décoder les résultats de SPMF

Une fois l'utilisation de SPMF terminée, on exécute une des commande suivante dans un terminal :

`python DecodeAfterSpmf.py <X> ` sur Windows
`python3 DecodeAfterSpmf.py <X>` sur Linux
DecodeAfterSpmf.py est là aussi un fichier récupéré d'un des TP de ce cours.

Ce programme crée un fichier res_decode.txt qui contient les itemsets ou règles d'associations issues du fichiers SPMF dans le format <Numéro de l'attribut>-<valeur de l'attribut>.
Ainsi, nous savons quelle valeur sur quelle colonne fait partie de l'itemset ou de la règle d'association.

à côté de ces informations, nous retrouvons également le support absolu du pattern, et, dans le cas des règles d'association, la confiance calculée.

## Translittération des fichiers décodés

Pour que les résultats de l'exploration de données soient plus lisibles, on utilise le programme translitteration.py de la manière suivante :

`python DecodeAfterSpmf.py res_decode.txt <Y>` sur Windows
`python3 DecodeAfterSpmf.py res_decode.txt <Y>` sur Linux
Avec <Y> le nom du fichier texte de sortie. S'il n'est pas précisé, un fichier par défaut "itemsets-regles_exploitables.txt" est créé.

Ce fichier contient les mêmes informations que le fichier créé après exécution du programme DecodeAfterSpmf.py, mais dont les numéros de colonnes sont rempalcés par leurs sigles, de sorte à ce que les règles d'association et itemsets trouvés soient facilement compréhensible par un lecteur.
