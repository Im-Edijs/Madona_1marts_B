def ievadi_vardu_un_ieraksti_faila():
    try:
        # Lietotāja vārda iegūšana
        lietotaja_vards = input("Ievadiet savu vārdu: ")

        # Faila nosaukums
        faila_nosaukums = "lietotajs.txt"

        # Faila atvēršana rakstīšanai
        with open(faila_nosaukums, 'w') as faila_rakstits:
            # Ieraksta lietotāja vārdu failā
            faila_rakstits.write(lietotaja_vards)

        print(f"Vārds '{lietotaja_vards}' veiksmīgi ierakstīts failā '{faila_nosaukums}'.")

    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' nav atrasts.")
    except PermissionError:
        print(f"Kļūda: Nav atļaujas rakstīt failā '{faila_nosaukums}'.")
    except Exception as e:
        print(f"Radās kļūda: {e}")