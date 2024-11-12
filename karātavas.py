# Gerda Brosko 12.b, darbs- Karātavas
#Mērķis: izveidot karātavu spēli Python programmēšanas valodā, apgūstot Python pamata funkcijas un loģiku.1
#Svarīgākie punkti:
#Nejauša vārda atlase: Izveidot vārdu sarakstu un atlasīt nejaušu vārdu spēlei, izmantojot random.choice() funkciju.
#Spēles datu saglabāšana: Izveidot divus sarakstus vai kopas (uzminēts_pareizi un uzminēts_nepareizi), lai saglabātu pareizos un nepareizos minējumus.
#Minējumu pārvaldība: Dot spēlētājam noteiktu minējumu skaitu (piemēram, 6), kas samazinās ar katru kļūdu. Nodrošināt, lai spēlētājs var ievadīt tikai vienu burtu, pārbaudot, vai ievadītais simbols ir burts un nav atkārtots.
#Pareizo un nepareizo minējumu attēlojums: Parādīt vārda pašreizējo norādi, aizvietojot pareizi minētos burtus, bet neatklātos attēlot ar _. Nepareizu minējumu gadījumā pakāpeniski attēlot "cilvēciņa" zīmējumu, kas simbolizē karātavas.
#Uzvaras un zaudējuma nosacījumi: Nodrošināt uzvaru, ja spēlētājs uzmin visus vārda burtus pirms mēģinājumi beidzas, un zaudējumu, ja mēģinājumi iztērēti pirms viss vārds uzminēts.
#Spēles atkārtošanas iespēja: Pēc uzvaras vai zaudējuma piedāvāt iespēju spēlēt vēlreiz vai izbeigt spēli.
#Lietotāja pieredze: Nodrošināt skaidrus paziņojumus par pareizajiem un nepareizajiem minējumiem un atlikušajiem mēģinājumiem, lai spēlētājam būtu skaidrs, cik burti vēl jāuzmin un cik kļūdu drīkst pieļaut.

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
    
    print("Uzspēlējam karātavas!")
    
    # Spēles cikls turpinās līdz uzvarai vai zaudējumam
    while mēģinājumi > 0:
        parādīt_cilvēciņu(len(uzminēts_nepareizi))  # Parāda cilvēciņu atkarībā no kļūdu skaita
        parādīt_norādi(vārds, uzminēts_pareizi)  # Parāda pašreizējo vārda stāvokli

        # Spēlētāja minējums
        minējums = input("Mini burtu ! ").lower()

        if len(minējums) != 1 or not minējums.isalpha():
            print("Lūdzu, ievadi vienu burtu!")
            continue

        if minējums in uzminēts_pareizi or minējums in uzminēts_nepareizi:
            print("Šis burts jau ir minēts. Mēģini vēlreiz.")
            continue

        # Pārbauda, vai minējums ir pareizs
        if minējums in vārds:
            uzminēts_pareizi.add(minējums)
            print(f"Pareizi, minētais burts '{minējums}' ir vārdā.")
        else:
            uzminēts_nepareizi.add(minējums)
            mēģinājumi -= 1
            print(f"Nepareizi, minētais burts '{minējums}' nav vārdā. Tev atliek {mēģinājumi} mēģinājumi.")

        # Pārbauda, vai spēlētājs ir uzminējis visu vārdu
        if set(vārds) == uzminēts_pareizi:
            print("Malacis, tu atminēji!")
            parādīt_norādi(vārds, uzminēts_pareizi)
            break

    else:
        print("Spēles beigas! (Iztērēji visus mēģinājumus.)")
        print(f"Pareizais vārds bija: {vārds}")

# Funkcija, kas dod iespēju spēlēt vēlreiz
def spēlēt_atkal():
    while True:
        atbilde = input("Vai vēlaties mēģināt vēlreiz? (jā/nē): ").lower()
        if atbilde == "jā":
            return True
        elif atbilde == "nē":
            return False
        else:
            print("Lūdzu, ievadi 'jā' vai 'nē'.")

# Galvenā programma
def galvenā_funkcija():
    while True:
        karātavu_spēle()  # Izsauc spēles funkciju
        if not spēlēt_atkal():
            print("Laba spēle! Līdz nākamajai reizei!")
            break

if __name__ == "__main__":
    galvenā_funkcija()

