from list_utils import read_list

def mutiple_sublist(l, mult):
    sublist = []
    for e in l:
        if e % mult == 0:
            sublist.append(e)
    return sublist

if __name__ == "__main__":
    # Introducció dades
    l = read_list()
    mult = int(input("Introdueix un nombre per trobar els seus múltiples: "))

    # Lògica
    l_mult = mutiple_sublist(l, mult)

    # Mostrar dades
    print(f"Els múltiples de {mult} són: {l_mult}")