

VOTOS_CAD_X = 0
VOTOS_CAD_Y= 0
VOTOS_CAD_Z = 0
VOTOS_BRANCOS = 0
VOTOS_NULOS = 0

while True:

    print()
    print(f"TOTAL CANDIDATO X: {VOTOS_CAD_X}")
    print(f"TOTAL CANDIDATO Y: {VOTOS_CAD_Y}")
    print(f"TOTAL CANDIDATO Z: {VOTOS_CAD_Z}")
    print(f"TOTAL VOTOS BRANCOS: {VOTOS_BRANCOS}")
    print(f"TOTAL VOTOS NULOS: {VOTOS_NULOS}")
    print()

    try:
        print(f"Candidato_X - 889")
        print(f"Candidato_Y - 847")
        print(f"Candidato_Z - 515")
        print("Branco - 0")
        print()
        voto = int(input("Em quem você gostaria de votar?"))

        if voto == 889:
            VOTOS_CAD_X += 1
        elif voto == 847:
            VOTOS_CAD_Y += 1
        elif voto == 515:
            VOTOS_CAD_Z += 1
        elif voto == 0:
            VOTOS_BRANCOS += 1
        else:
            VOTOS_NULOS += 1

    except:
        print("Voto inválido, tente novamente.")


    encerrar = input("Gostaria de encerrar a votação? Responda com S ou N: ")
    if encerrar == "S":
        if VOTOS_CAD_X > VOTOS_CAD_Y and VOTOS_CAD_X > VOTOS_CAD_Z:
            print()
            print(f"O Candidato X recebeu: {VOTOS_CAD_X} votos.")
            print(f"Candidato Y recebeu: {VOTOS_CAD_Y} votos.")
            print(f"Candidato Z recebeu: {VOTOS_CAD_Z} votos.")
            print(f"Votos Brancos: {VOTOS_BRANCOS} votos.")
            print(f"Votos Nulos: {VOTOS_NULOS} votos.")
            print()
            print(f"O Candidato X venceu as eleições com: {VOTOS_CAD_X} votos!")
            print()
        elif VOTOS_CAD_Y > VOTOS_CAD_X and VOTOS_CAD_Y > VOTOS_CAD_Z:
            print()
            print(f"Candidato X recebeu: {VOTOS_CAD_X} votos.")
            print(f"Candidato Y recebeu: {VOTOS_CAD_X} votos.")
            print(f"Candidato Z recebeu: {VOTOS_CAD_Z} votos.")
            print(f"Votos Brancos: {VOTOS_BRANCOS} votos.")
            print(f"Votos Nulos: {VOTOS_NULOS} votos.")
            print()
            print(f"O Candidato Y venceu as eleições com: {VOTOS_CAD_Y} votos!")
            print()
        elif VOTOS_CAD_Z > VOTOS_CAD_X and VOTOS_CAD_Z > VOTOS_CAD_X:
            print()
            print(f"Candidato X recebeu: {VOTOS_CAD_X} votos.")
            print(f"Candidato Y recebeu: {VOTOS_CAD_X} votos.")
            print(f"Candidato Z recebeu: {VOTOS_CAD_Z} votos.")
            print(f"Votos Brancos: {VOTOS_BRANCOS} votos.")
            print(f"Votos Nulos: {VOTOS_NULOS} votos.")
            print()
            print(f"O Candidato Z venceu as eleições com: {VOTOS_CAD_Z} votos!")
            print()
        else:
            print("Nenhum candidato venceu as eleições!")

        break

    if encerrar == 'N':
        continue




