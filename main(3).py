import random

nombre1=random.randint(-100,100)
nombre2=random.randint(-100,100)

somme= nombre1 + nombre2
question="Que vaut la somme de "+str(nombre1)+" et "+str(nombre2)+" ?"
reponse=input(question)
reponse=int(reponse)

if reponse==somme :
  print("Vous etes bon")
elif reponse!=somme :
 print("c'est faux!")
 print("Recommence")

else:
  print("Une situation innatendue est survenue.")