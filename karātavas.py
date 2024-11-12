# Gerda Brosko 12.b, darbs- Karātavas

import random

# Vārdu saraksts, no kura tiek izvēlēts nejaušs vārds
vārdu_saraksts = [
    'suns', 'kaķis', 'zivs', 'lapa', 'zils', 'zaļš', 'sarkans', 
    'gulēt', 'ēst', 'mašīnas', 'skola', 'lekt', 'lietussargs', 
    'tukums', 'liepāja', 'ventspils', 'krāslava', 'dejot', 'dziedāt'
]

# Karātavu zīmējums atkarībā no nepareizo minējumu skaita
cilvēciņa_zīmējums = {
    0: (" o ", "   ", "   "),
    1: (" o ", " | ", "   "),
    2: (" o ", "/| ", "   "),
    3: (" o ", "/|\\", "   "),
    4: (" o ", "/|\\", "/  "),
    5: (" o ", "/|\\", "/ \\")
}

# Funkcija, lai attēlotu cilvēciņu atkarībā no nepareizo minējumu skaita
def parādīt_cilvēciņu(nepareizās_minējumi):
    print("**")
    for rinda in cilvēciņa_zīmējums.get(nepareizās_minējumi, []):
        print(rinda)
    print("**")
        
# Funkcija, lai parādītu pašreizējo norādi uzminētajiem burtiem
def parādīt_norādi(vārds, uzminēts_pareizi):
    norāde = [burts if burts in uzminēts_pareizi else "_" for burts in vārds]
    print(" ".join(norāde))

# Galvenā spēles funkcija
def karātavu_spēle():
    vārds = random.choice(vārdu_saraksts)  # Nejauša vārda izvēle
    uzminēts_pareizi = set()  # Burti, kas minēti pareizi
    uzminēts_nepareizi = set()  # Burti, kas minēti nepareizi
    mēģinājumi = 6  # Spēlētājam ir 6 mēģinājumi
    
    print("Laipni lūgti karātavu spēlē!")
    
    # Spēles cikls turpinās līdz uzvarai vai zaudējumam
    while mēģinājumi > 0:
        parādīt_cilvēciņu(len(uzminēts_nepareizi))  # Parāda cilvēciņu atkarībā no kļūdu skaita
        parādīt_norādi(vārds, uzminēts_pareizi)  # Parāda pašreizējo vārda stāvokli

        # Spēlētāja minējums
        minējums = input("Miniet burtu: ").lower()

        if len(minējums) != 1 or not minējums.isalpha():
            print("Lūdzu, ievadiet tikai vienu burtu.")
            continue

        if minējums in uzminēts_pareizi or minējums in uzminēts_nepareizi:
            print("Šis burts jau ir minēts. Mēģiniet vēlreiz.")
            continue

        # Pārbauda, vai minējums ir pareizs
        if minējums in vārds:
            uzminēts_pareizi.add(minējums)
            print(f"Labi! Burts '{minējums}' ir vārdā.")
        else:
            uzminēts_nepareizi.add(minējums)
            mēģinājumi -= 1
            print(f"Nav pareizi! Burts '{minējums}' nav vārdā. Atliek {mēģinājumi} mēģinājumi.")

        # Pārbauda, vai spēlētājs ir uzminējis visu vārdu
        if set(vārds) == uzminēts_pareizi:
            print("Apsveicu! Jūs uzminējāt vārdu!")
            parādīt_norādi(vārds, uzminēts_pareizi)
            break

    else:
        print("Spēle beigusies! Jūs iztērējāt visus mēģinājumus.")
        print(f"Pareizais vārds bija: {vārds}")

# Funkcija, kas dod iespēju spēlēt vēlreiz
def spēlēt_atkal():
    while True:
        atbilde = input("Vai vēlaties spēlēt vēlreiz? (jā/nē): ").lower()
        if atbilde == "jā":
            return True
        elif atbilde == "nē":
            return False
        else:
            print("Lūdzu, ievadiet 'jā' vai 'nē'.")

# Galvenā programma
def galvenā_funkcija():
    while True:
        karātavu_spēle()  # Izsauc spēles funkciju
        if not spēlēt_atkal():
            print("Paldies, ka spēlējāt! Uz redzēšanos!")
            break

if __name__ == "__main__":
    galvenā_funkcija()

