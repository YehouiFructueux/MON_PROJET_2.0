

import json
import os 

ma_liste = []

debut = int()
fin = int()
salle = ""
salles_dispo = {
    "salle a" : "6 places",
    "salle b" : "12 places",
    "salle c" : "4 places"
}

def sauvegarder():
    with open("reservations.json", "w", encoding="utf-8") as fichier:
        json.dump(ma_liste, fichier, indent = 4, ensure_ascii = False)
    print("Sauvegarde effectuée.")

def charger():
    global ma_liste
    if os.path.exists("reservations.json"):
        with open("reservations.json", "r", encoding="utf-8") as fichier:
            ma_liste = json.load(fichier)         
           
            # __________LISTE__DES__SALLES__________


def salles_disponibles():
    global salles_dispo
    print()
    print("_-_-_-_SALLES DISPONIBLES_-_-_-_")
    print()
    print(salles_dispo)
    print()
    

def faire_une_reservation():
    global date_saisie
    print("-_-_-_-_-_-_-_FAIRE_UNE_RESERVATION_-_-_-_-_-_-_-_-")
    print()
    reservation = {}
    
#                     # ___________CHOISIR_UNE_SALLE__________        
  
    while True:
        salle = input("Choisissez votre salle: ").strip().lower()
        if salle.isdigit():
            print("Salle ne peut pas être un entier")
        elif salle == "":
            print("Vous devez choisir une salle")
        else:
            if salle in salles_dispo:
                reservation['salle'] = salle
                break
            else:
                print("salle inexistante")
                print()
                
#                  # __________DATE_________

    print()
    from datetime import datetime, date
    date_aujourdhui = date.today()
    while True:
        saisie = input("Entrez la date de votre réservation en suivant ce modèle (AAAA-MM-JJ): ").strip()
        try:
            date_saisie = datetime.strptime(saisie, "%Y-%m-%d").date()
            if date_saisie < date_aujourdhui:
                print("Erreur: La date ne peut pas être dans le passé")
            else:
                break
        except ValueError:
            print("Format incorrect. Utilisez le format AAAA-MM-JJ.")
    reservation['date'] = date_saisie.strftime("%Y-%m-%d")
    # print(f"Date enrégistrée: {reservation["date"]}")
    print()
    
#         # ____________DEBUT___________

       
    from datetime import datetime
    while True:
        try:
            saisie = input("Entrez l'heure de début en suivant ce modèle (HH:MM): ").strip()
            heure_saisie = datetime.strptime(saisie, "%H:%M").time()
            break
        except ValueError:
            print("Format incorrecte. Veuillez réessayer")       
    h = heure_saisie.hour
    m = heure_saisie.minute
    debut = h*60 + m
    reservation['debut'] = debut
    print()


#              # ____________FIN_________
            
    while True:
        try:
            saisie = input("Entrez l'heure de fin en suivant ce modèle (HH:MM): ").strip()
            heure_saisie = datetime.strptime(saisie, "%H:%M").time()
            h = heure_saisie.hour
            m = heure_saisie.minute
            fin = h * 60 + m

            if debut <= fin:
                print("L'heure de fin ne peut pas être identique à l'heure de début.")
                continue
            break
        except ValueError:
            print("Format incorrecte. Veuillez réessayer")

    reservation['fin'] = fin
    print()


#             # ________NOM_DU_RESPONSABLE_______


    while True:
        responsable = input("Nom du responsable: ").strip()
        if not responsable:
            print("Vous devez entrer un nom")
        elif responsable.isdigit():
            print("le nom ne peut pas contenir d'entier")
        else:
            break
    reservation['responsable'] = responsable
    print()

 #           # __________OBJET_________

    while True:
        objet = input("OBJET: ").strip()
        if not objet:
            print("Vous ne pouvez pas laisser l'espace vide")
        elif objet.isdigit():
            print("L'objet ne peut pas contenir d'entier")
        else:
            break
    reservation['objet'] = objet
    print()
    conflit = cas_de_conflit(salle, date_saisie, debut, fin)
    if not conflit:
        ma_liste.append(reservation)
        print("____ENREGISTREE____")
        print()
    else:
        print("Réservation non enregistré à cause du conflit")
        print()
    return salle, date_saisie, debut, fin, reservation

       #    _________CAS_DE_CONFLIT_______
       
def cas_de_conflit(salle, date_saisie, debut, fin):
    conflit = False
    from datetime import datetime
    
    for liste in ma_liste:
        date_liste = datetime.strptime(liste['date'], "%Y-%m-%d").date()
        if liste['salle'].lower() == salle.lower() and date_liste == date_saisie:
            if debut < liste['fin'] and liste['debut'] < fin:
                conflit = True

    if conflit == True:
        print("Risque de conflit. Veuillez choisir une autre horaire")
        print()
    return conflit

def detection_de_conflit():
    print()
    print("-------DETECTION_DE_CONFLIT--------")
    print()
    salle = input("Choisissez votre salle: ").strip()
    date_saisie = input("Entrez la date (AAAA-MM-JJ): ").strip()
    debut = input("Entrez l'heure de début (HH:MM): ").strip()
    fin = input("Entrez l'heure de fin (HH:MM): ").strip()
    from datetime import datetime
    date_saisie = datetime.strptime(date_saisie, "%Y-%m-%d").date()
    heure_debut = datetime.strptime(debut, "%H:%M").time()
    debut = heure_debut.hour * 60 + heure_debut.minute
    heure_fin = datetime.strptime(fin, "%H:%M").time()
    fin = heure_fin.hour * 60 + heure_fin.minute
    
    cas_de_conflit(salle, date_saisie, debut, fin)

                    #__________PLANNING__________
                    
def voir_le_planning():
    print()
    print("-_-_-_-_-_-_-_PLANNING_-_-_-_-_-_-_-_-")
    print()
    
    while True:
        salle = input("Choisissez votre salle: ").strip()

        if not salle:
            print("Vous devez choisir une salle")
        elif salle.isdigit():
            print("La salle ne peut pas être un entier")
        elif salle:
            break
        if salle in salles_dispo:
            break
        else:
            print("Salle inexistante")
            
    from datetime import datetime

    while True:
        saisie = input("Entrez la date (AAAA-MM-JJ): ").strip()
        try:
            date_saisie = datetime.strptime(saisie, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Format incorrect. Utilisez le format AAAA-MM-JJ.")
    compteur = 0
    for liste in ma_liste:
        date_liste = datetime.strptime(liste['date'], "%Y-%m-%d").date()

        if liste['salle'] == salle and date_liste == date_saisie:
            compteur += 1
            print(liste)
        else:
            continue
    if compteur == 0:
        print("INEXISTANT")

                        #__________CRENAUX_LIBRES_______
    
def afficher_creneaux_libres():
    print()
    while True:
        salle = input("Pour quelle salle voulez-vous voir le creneau libre: ").strip()
        if not salle:
            print("Vous ne pouvez pas laisser l'espace vide")
        elif salle.isdigit():
            print("Ce champ n'est pas reservé aux entiers")
        else:
            break
    
    print()
    from datetime import datetime, date
    while True:
        saisie = input("Entrez la date de la réservation en suivant ce modèle (AAAA-MM-JJ): ").strip()
        try:
            date_saisie = datetime.strptime(saisie, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Format incorrect. Utilisez le format AAAA-MM-JJ.")
            
    reservations = []
    
    for reservation in ma_liste:
        date_reservation = datetime.strptime(reservation['date'], "%Y-%m-%d").date()
        if date_reservation == date_saisie and reservation['salle'].lower() == salle.lower():
            reservations.append(reservation)

    if not reservations:
        print("Aucune réservation. La salle est libre de 08h00 à 18h00.")
        return

    reservations.sort(key=lambda x: x["debut"])

    ouverture = 480 
    fermeture = 1080
    debut_creneau = ouverture

    print(f"Créneaux libres pour {salle} le {date_saisie} :")

    for reservation in reservations:
        if debut_creneau < reservation['debut']:
            
            print(f"{debut_creneau / 60}h à {reservation['debut'] / 60}h")
        debut_creneau = reservation['fin']
        
    if debut_creneau < fermeture:
        print(f"{debut_creneau / 60}h à {fermeture / 60}h")
print()

                        # _________annuler_une_reservation________
                         
def annuler_une_reservation():
    while True:
            salle = input("Entrez la salle de la reservation: ").strip()
            if not salle:
                print("Vous ne pouvez pas laisser l'espace vide")
            elif salle.isdigit():
                print("Ce champ n'est pas reservé aux entiers")
            else:
                break
    
    print()
    from datetime import datetime, date
    while True:
        saisie = input("Entrez la date de votre réservation en suivant ce modèle (AAAA-MM-JJ): ").strip()
        try:
            date_saisie = datetime.strptime(saisie, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Format incorrect. Utilisez le format AAAA-MM-JJ.")
    

    from datetime import datetime
    while True:
        try:
            saisie = input("Entrez l'heure de début en suivant ce modèle (HH:MM): ").strip()
            heure_saisie = datetime.strptime(saisie, "%H:%M").time()
            break
        except ValueError:
            print("Format incorrecte. Veuillez réessayer")       
    h = heure_saisie.hour
    m = heure_saisie.minute
    debut = h*60 + m
    print()
                
    while True:
        try:
            saisie = input("Entrez l'heure de fin en suivant ce modèle (HH:MM): ").strip()
            heure_saisie = datetime.strptime(saisie, "%H:%M").time()
            h = heure_saisie.hour
            m = heure_saisie.minute
            fin = h * 60 + m

            if debut <= fin:
                print("L'heure de fin ne peut pas être identique à l'heure de début.")
                continue
            break
        except ValueError:
            print("Format incorrecte. Veuillez réessayer")
    
    print()
        
    trouve = False
    for reservation in ma_liste:
        date_reservation = datetime.strptime(reservation['date'], "%Y-%m-%d").date()
        if reservation['salle'] == salle and date_reservation == date_saisie and reservation['debut'] == debut and reservation['fin'] == fin:
            trouve = True
            print(reservation)
            a_supprimer = reservation
            while True:
                choix = input("Voulez-vous vraiment annuler cette reservation ? (oui/non) : ").strip().lower()
                if choix == "oui":
                    ma_liste.remove(a_supprimer)
                    print("Votre réservation a été annulée")
                    break
                elif choix == "non":
                    print("Votre reservation est conservée")
                    break
                else:
                    print("Veuillez repondre par oui ou non")
            break
    if not trouve:
        print("RESERVATION INTROUVABLE")    
    

                        # __________MENU__________
if __name__=="__main__":
    
    charger()
                
    choix = int()
    print("_-_-_-_MENU_-_-_-_")
    print()
    while choix != 8:
        print("1. Liste des salles")
        print("2. Réserver une salle")
        print("3. Détection de conflit")
        print("4. Planning")
        print("5. Voir les créneaux libres")
        print("6. Annuler")
        print("7. Sauvegarde")
        print("8. Quitter")
        print("9. Affichage de la liste")
        print()
        while True:
            try:
                choix = int(input("Faîtes votre choix: "))
                if choix:
                    break
            except ValueError:
                print("Vous devez faire un choix")
            break
        if choix <= 0 or choix > 8:
            print("Choix incorrecte")
            print()
        if choix == 1:
            salles_disponibles()
        if choix == 2:
            faire_une_reservation()
        if choix == 3:
            detection_de_conflit()
        if choix == 4:
            voir_le_planning()
        if choix == 5:
            afficher_creneaux_libres()
        if choix == 6:
            annuler_une_reservation()
        if choix == 7:
            sauvegarder()
        if choix == 8:
            print("____Vous__avez__quitté__le__programme____")
        if choix == 9:
            print(ma_liste)
            print()