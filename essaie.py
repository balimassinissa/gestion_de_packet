def distribute_belts(belts):
    categories = [125, 120, 115, 110, 105, 100]
    total_belts = sum(belts)
    num_packs = total_belts // 10

    # Initialisation des paquets
    packs = [[0] * len(categories) for _ in range(num_packs)]

    # Répartition initiale
    for i, count in enumerate(belts):
        j, reste = divmod(count, num_packs)
        
        for k in range(reste):
            packs[k][i] = j + 1
        for k in range(reste, num_packs):
            packs[k][i] = j
    
    # Ajuster les paquets pour garantir exactement 10 ceintures par paquet
    for pack in packs:
        while sum(pack) != 10:
            for i in range(len(categories)):
                if sum(pack) < 10 and belts[i] > 0:
                    pack[i] += 1
                    belts[i] -= 1
                elif sum(pack) > 10 and pack[i] > 0:
                    pack[i] -= 1
                    belts[i] += 1

    return packs

# Exemple d'utilisation
if __name__ == "__main__":
    belts = [5,10, 10, 5, 5, 6]  # Ceintures de 120, 115, 110, 105, 100 respectivement
    print("SUM:", sum(belts))
    try:
        distribution = distribute_belts(belts)
        print("Distribution des paquets:")
        for i, pack in enumerate(distribution):
            print(f"Paquet {i+1}: {pack}")
    except ValueError as e:
        print(e)
