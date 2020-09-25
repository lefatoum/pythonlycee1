spt = input("Entrez un âge:")
spt = int(spt)

if spt >= 12:
    print(f"Cet enfant de {spt} est en cadet. ")

elif spt > 9:
    print(f"Cet enfant de {spt} est minime.")

elif spt > 7:
    print(f"Cet enfant de {spt} est en pupille.")

else:
    print(f"Cte enfant de {spt} est en poussin ")
