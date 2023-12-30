from csv import reader
from operator import itemgetter

def main():
    file = leggi_file("player_stats.csv")
    attaccantiPiuForti = attaccanti_piu_forti(file)
    centroCampistiPiuForti = centrocampisti_piu_forti(file)
    print("I tre attaccanti più forti sono: ")
    print("Nome \t\t Squadra \t\t Efficacia")
    for giocatore in attaccantiPiuForti:
        print(f"{giocatore['nomeGiocatore']:25} {giocatore['team']:25} {giocatore['efficacia']:25}")
    print()
    print("I tre centrocampisti più forti sono: ")
    print("Nome \t\t Squadra \t\t Efficacia")
    for giocatore in centroCampistiPiuForti:
        print(f"{giocatore['nomeGiocatore']:25} {giocatore['team']:25} {giocatore['efficacia']:25}")


"""
@function leggi_file: Funzione che legge un file e crea il dizionario con i calciatori
@param filename: nome/percorso del file da cui estrarre i dati
"""
def leggi_file(filename):
    try:
        inFile = open(filename, "r", encoding="utf-8")
        try:
            lista = []
            lettore = reader(inFile)
            prima = True
            for line in lettore:
                if prima:
                    prima = False
                else:
                    nomeGiocatore = line[0]
                    team = line[2]
                    posizione = line[1]
                    minutiGiocati = int(line[4])
                    if posizione == "FW":
                        goals = int(line[5])
                        assist = int(line[6])
                        fuoriGiochi = int(line[7])
                        if minutiGiocati != 0:
                            efficaciaAttaccante = (goals + assist - fuoriGiochi)/minutiGiocati
                        else:
                            efficaciaAttaccante = 0
                        record = {
                            "nomeGiocatore": nomeGiocatore,
                            "team": team,
                            "efficacia": efficaciaAttaccante,
                            "ruolo": posizione,
                        }
                        lista.append(record)
                    elif posizione == "MF":
                        palleIntercettate = int(line[8])
                        palleRecuperate = int(line[12])
                        crossFatti = int(line[7])
                        assist = int(line[6])
                        if crossFatti != 0 and minutiGiocati != 0:
                            efficaciaCentrocampista = (palleIntercettate + palleRecuperate + (assist / crossFatti))/minutiGiocati
                        else:
                            efficaciaCentrocampista = 0
                        record = {
                            "nomeGiocatore": nomeGiocatore,
                            "team": team,
                            "efficacia": efficaciaCentrocampista,
                            "ruolo": posizione,
                        }
                        lista.append(record)
            return lista
        except Exception as message2:
            exit(str(message2))
    except FileNotFoundError as message:
        exit(str(message))

"""
@function attaccanti_piu_forti: stampa i 3 attaccanti più forti
@params elenco: elenco dei giocatori
"""
def attaccanti_piu_forti(elenco):
    lista = []
    elencoOrdinato = sorted(elenco, key=itemgetter('efficacia'), reverse= True)
    contatore = 0
    for giocatore in elencoOrdinato:
        if contatore < 3 and giocatore["ruolo"] == "FW":
            lista.append(giocatore)
            contatore+=1
    return lista
"""
@function centrocampisti_piu_forti: stampa i 3 centrocampisti più forti
@params elenco: elenco dei giocatori
"""
def centrocampisti_piu_forti(elenco):
    lista = []
    elencoOrdinato = sorted(elenco, key=itemgetter('efficacia'), reverse= True)
    contatore = 0
    for giocatore in elencoOrdinato:
        if contatore < 3 and giocatore["ruolo"] == "MF":
            lista.append(giocatore)
            contatore+=1
    return lista
main()