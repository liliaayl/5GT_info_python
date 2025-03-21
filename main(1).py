print("Bonjour")
import datetime
now=datetime.datetime.now()
annee_now=now.year

nom1=input("Quel est ton nom ?")
annee1=input("En quelle année es-tu né ?")

nom2=input("Quel est le nom de ton voisin ?")
annee2=input("En quelle année est-il née ?")

annee1=int (annee1)
age1=now.year-annee1

annee2=int (annee2)
age2=now.year-annee2

print(nom1,"a",age1,"ans")
print(nom2,"a",age2,"ans")

if age1>age2:
  print(nom1,"est plus agé que",nom2)
elif age1<age2:
  print(nom2,"est plus agé que",nom1)
elif age1==age2:
  print(nom1,"et",nom2,"ont le même age.")
else:
  print("T'es bête ou quoi ??")
