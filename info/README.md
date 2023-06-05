# Project Python trojan framework
### De Smedt Laurens 2ITCSC2

### requirements staan in het mapje info
## Werking:

- Als de gebruiker op een gevaarlijke link klikt dan wordt er een bestand op de computer van de gebruiker gezet.
- Vervolgens zal het script gerund worden. De download file zal geen verdachte dingen bevatten
    - Main programma 
    - Connectie naar een github repo
    - Een default config 
    - Default module die systeem info zal opslaan
    - Default check tijd
    - Deze informatie zal opgeslagen worden en verzonden worden naar een github repo je moet wel ingelogd zijn omdat momenteel de token moeilijk doet
 - Na een tijd die aanpasbaar is zal de main een git clone uitvoeren en de nieuwe modules inladen die door een hacker zijn online gezet. 
 - Hij zal dan deze modules uit voeren en ook verkregen bestanden opslaan en versturen naar Github (evenutueel ook bestanden verwijderen nadat de module is uitgevoerd) 



### Te werk gaan : 
- Eerst proberen om een bestand van een github repo te halen
    - Niet gelukt wegens premissie errors dus linux rocky
- Vervolgens een test module te laten werken 
- Die een bestand zal maken in het mapje logs 
- En vervolgens de bestanden zal versturen naar de repo