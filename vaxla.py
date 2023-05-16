#exchange
#in: belopp som sla växlas valör på en sedel eller mynt
#out: antal sedlar.mynt man får ut i valör
def exchange(belopp, sedel):
    return int(belopp) // sedel

#get_exchange_dict
#in: inbetalt belopp, priset på varan
#out: dictionary inhåller antal mynt-sedlar i varje valör

def get_exchange_dict(inbetalning, priset)