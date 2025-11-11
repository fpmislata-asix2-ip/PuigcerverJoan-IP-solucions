vots = []
nom_delegat = input("Introdueix el nom del delegat: ")
while nom_delegat != "END":
    vots.append(nom_delegat)
    nom_delegat = input("Introdueix el nom del delegat: ")

print(vots)
vots_per_candidat = {}
for vot in vots:
    if vot in vots_per_candidat:
        vots_per_candidat[vot] += 1
    else:
        vots_per_candidat[vot] = 1
        
print(vots_per_candidat)

# Calcular el nombre de vots màxim => list_utils.max
# Per a cada candidat -> vots:
#     Comprovar si el nombre de vots és el màxim:
#     Si ho és:
#          Guardar el nombre de vots

# max_vots = max(vots_per_candidat.values())
values = list(vots_per_candidat.values())
max_vots = values[0]
for nombre_vots in values:
    if nombre_vots > max_vots:
        max_vots = nombre_vots

print(max_vots)

# Calcular els candidats que tenen el nombre de vots màxim
# Per a cada candidat -> vots:
#     Si vots és el màxim
#          Guardar el candidat en una llista
delegats = []
for nom, vots in vots_per_candidat.items():
    if vots == max_vots:
        delegats.append(nom)

print(delegats)