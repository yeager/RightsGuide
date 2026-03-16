from rightsguide.i18n import _
"""Fördefinierad data för RightsGuide – frågor, svar och kategorier."""

CATEGORIES = [
    {
        "id": "lss",
        "title": "LSS – Stöd och service",
        "icon": "🏠",
        "description": "Lagen om stöd och service till vissa funktionshindrade",
        "color": "#3584e4",
        "qa": [
            {
                "q": "Vad är LSS?",
                "a": (
                    "LSS står för Lagen om stöd och service till vissa "
                    "funktionshindrade.\n\n"
                    "Det är en lag som ger dig rätt till särskilt stöd om du "
                    "har en funktionsnedsättning som gör att du behöver hjälp "
                    "i vardagen.\n\n"
                    "LSS ska ge dig möjlighet att leva som andra."
                ),
            },
            {
                "q": "Vem kan få LSS?",
                "a": (
                    "Du kan ha rätt till LSS om du tillhör en av tre grupper:\n\n"
                    "1️⃣ Du har en utvecklingsstörning, autism eller "
                    "autismliknande tillstånd.\n\n"
                    "2️⃣ Du har fått en hjärnskada som vuxen, till exempel "
                    "efter en olycka.\n\n"
                    "3️⃣ Du har en stor och varaktig fysisk eller psykisk "
                    "funktionsnedsättning som inte beror på normalt åldrande."
                ),
            },
            {
                "q": "Vilka insatser finns i LSS?",
                "a": (
                    "Det finns 10 insatser i LSS:\n\n"
                    "• Rådgivning och stöd\n"
                    "• Personlig assistans\n"
                    "• Ledsagarservice\n"
                    "• Kontaktperson\n"
                    "• Avlösarservice i hemmet\n"
                    "• Korttidsvistelse utanför hemmet\n"
                    "• Korttidstillsyn (för skolungdom över 12 år)\n"
                    "• Boende i familjehem eller bostad med särskild service "
                    "för barn och ungdomar\n"
                    "• Bostad med särskild service för vuxna\n"
                    "• Daglig verksamhet"
                ),
            },
            {
                "q": "Hur ansöker jag om LSS?",
                "a": (
                    "Så här gör du:\n\n"
                    "1. Kontakta din kommun och be att få prata med en "
                    "LSS-handläggare.\n\n"
                    "2. Du kan ansöka muntligt eller skriftligt.\n\n"
                    "3. Handläggaren utreder ditt behov.\n\n"
                    "4. Du får ett beslut – oftast inom tre månader.\n\n"
                    "💡 Tips: Du kan få hjälp av en god man, anhörig eller "
                    "annan person att ansöka."
                ),
            },
            {
                "q": "Kan jag överklaga ett beslut?",
                "a": (
                    "Ja! Om du får avslag kan du överklaga.\n\n"
                    "Du har 3 veckor på dig att överklaga från det att du "
                    "fick beslutet.\n\n"
                    "Skicka ditt överklagande till den myndighet som fattade "
                    "beslutet. De skickar det vidare till förvaltningsrätten.\n\n"
                    "💡 Tips: Be om hjälp att skriva överklagandet. Du kan "
                    "kontakta en funktionsrättsorganisation för stöd."
                ),
            },
        ],
    },
    {
        "id": "assistans",
        "title": "Personlig assistans",
        "icon": "🤝",
        "description": "Assistansersättning och personlig assistans",
        "color": "#33d17a",
        "qa": [
            {
                "q": "Vad är personlig assistans?",
                "a": (
                    "Personlig assistans innebär att du får hjälp av en eller "
                    "flera assistenter i din vardag.\n\n"
                    "Assistenten hjälper dig med saker som du inte klarar "
                    "själv på grund av din funktionsnedsättning.\n\n"
                    "Du bestämmer själv vem som ska vara din assistent och "
                    "hur hjälpen ska utföras."
                ),
            },
            {
                "q": "Vad är grundläggande behov?",
                "a": (
                    "Grundläggande behov är det som avgör om du har rätt "
                    "till assistans:\n\n"
                    "• Andning\n"
                    "• Personlig hygien\n"
                    "• Måltider\n"
                    "• Att klä av och på sig\n"
                    "• Att kommunicera med andra\n\n"
                    "Om du behöver hjälp med grundläggande behov i mer än "
                    "20 timmar per vecka kan du få assistansersättning "
                    "från Försäkringskassan."
                ),
            },
            {
                "q": "Vem betalar för assistansen?",
                "a": (
                    "Det beror på hur många timmar du behöver:\n\n"
                    "Under 20 timmar/vecka:\n"
                    "→ Kommunen betalar och beslutar.\n\n"
                    "Över 20 timmar/vecka:\n"
                    "→ Försäkringskassan betalar assistansersättning.\n"
                    "→ Kommunen betalar de första 20 timmarna.\n\n"
                    "Du betalar ingenting själv."
                ),
            },
            {
                "q": "Hur ansöker jag om assistans?",
                "a": (
                    "För kommunal assistans:\n"
                    "→ Kontakta din kommun (LSS-handläggare).\n\n"
                    "För assistansersättning:\n"
                    "→ Kontakta Försäkringskassan.\n"
                    "→ Telefon: 0771-524 524\n\n"
                    "Du behöver ett läkarintyg som beskriver din "
                    "funktionsnedsättning och dina behov.\n\n"
                    "💡 Tips: Många anlitar ett assistansbolag som hjälper "
                    "till med ansökan."
                ),
            },
            {
                "q": "Kan jag välja assistent själv?",
                "a": (
                    "Ja! Du har rätt att välja:\n\n"
                    "• Vem som ska vara din assistent\n"
                    "• Vilket assistansbolag du vill anlita\n"
                    "• Du kan också vara egen arbetsgivare\n"
                    "• Du kan anställa anhöriga som assistenter\n\n"
                    "Det viktigaste är att du har inflytande över din "
                    "egen assistans."
                ),
            },
        ],
    },
    {
        "id": "vard",
        "title": "Vård och omsorg",
        "icon": "🏥",
        "description": "Stöd från sjukvård och socialtjänst",
        "color": "#e66100",
        "qa": [
            {
                "q": "Vad är SoL?",
                "a": (
                    "SoL står för Socialtjänstlagen.\n\n"
                    "Det är en lag som ger alla rätt till stöd från "
                    "socialtjänsten om man behöver det.\n\n"
                    "Till skillnad från LSS behöver du inte tillhöra en "
                    "viss grupp – alla kan söka stöd enligt SoL.\n\n"
                    "Exempel på stöd: hemtjänst, boendestöd, ekonomiskt "
                    "bistånd (socialbidrag)."
                ),
            },
            {
                "q": "Vad är skillnaden mellan LSS och SoL?",
                "a": (
                    "LSS:\n"
                    "→ Bara för personer med vissa funktionsnedsättningar\n"
                    "→ Starkare rättigheter\n"
                    "→ Gratis (inga avgifter)\n"
                    "→ Ska ge \"goda levnadsvillkor\"\n\n"
                    "SoL:\n"
                    "→ Gäller alla som behöver stöd\n"
                    "→ Kommunen kan ta ut avgifter\n"
                    "→ Ska ge \"skälig levnadsnivå\"\n\n"
                    "💡 Tips: Om du har rätt till LSS brukar det vara "
                    "bättre att söka via LSS."
                ),
            },
            {
                "q": "Vad är habilitering?",
                "a": (
                    "Habilitering är stöd för dig som har en medfödd "
                    "eller tidigt förvärvad funktionsnedsättning.\n\n"
                    "Du kan få hjälp med:\n"
                    "• Träning och behandling\n"
                    "• Hjälpmedel\n"
                    "• Rådgivning\n"
                    "• Samtalsstöd\n\n"
                    "Kontakta din regions habiliteringscentrum för mer "
                    "information."
                ),
            },
            {
                "q": "Vad kostar sjukvård?",
                "a": (
                    "I Sverige finns ett högkostnadsskydd:\n\n"
                    "Läkarbesök:\n"
                    "→ Max 1 300 kr per 12 månader (frikort)\n\n"
                    "Medicin:\n"
                    "→ Max 2 850 kr per 12 månader\n\n"
                    "Barn och unga (under 18/20 år beroende på region) "
                    "har ofta gratis vård.\n\n"
                    "💡 Tips: Spara alla kvitton! Frikort utfärdas "
                    "automatiskt i de flesta regioner."
                ),
            },
            {
                "q": "Vart vänder jag mig för hjälp?",
                "a": (
                    "Här är viktiga kontakter:\n\n"
                    "🏛️ Din kommun – för LSS och socialtjänst\n\n"
                    "📞 Försäkringskassan – 0771-524 524\n"
                    "   (assistansersättning, sjukersättning)\n\n"
                    "📞 1177 Vårdguiden – för sjukvårdsfrågor\n\n"
                    "📞 Funktionsrätt Sverige – 08-546 404 00\n"
                    "   (stöd och rådgivning)\n\n"
                    "💡 Tips: Skriv ner dina frågor innan du ringer!"
                ),
            },
        ],
    },
    {
        "id": "ekonomi",
        "title": "Ekonomiskt stöd",
        "icon": "💰",
        "description": "Bidrag och ersättningar du kan ha rätt till",
        "color": "#9141ac",
        "qa": [
            {
                "q": "Vilka bidrag kan jag söka?",
                "a": (
                    "Här är de vanligaste bidragen:\n\n"
                    "• Aktivitetsersättning (18-29 år)\n"
                    "• Sjukersättning (30-65 år)\n"
                    "• Handikappersättning / merkostnadsersättning\n"
                    "• Bostadstillägg\n"
                    "• Bilstöd\n"
                    "• Assistansersättning\n\n"
                    "Alla dessa söks hos Försäkringskassan."
                ),
            },
            {
                "q": "Vad är aktivitetsersättning?",
                "a": (
                    "Aktivitetsersättning är för dig som är mellan "
                    "18 och 29 år.\n\n"
                    "Du kan få det om din arbetsförmåga är nedsatt med "
                    "minst en fjärdedel under minst ett år.\n\n"
                    "Det finns två typer:\n"
                    "• Vid nedsatt arbetsförmåga\n"
                    "• Vid förlängd skolgång\n\n"
                    "Kontakta Försäkringskassan för att ansöka."
                ),
            },
            {
                "q": "Vad är merkostnadsersättning?",
                "a": (
                    "Merkostnadsersättning är pengar för extra kostnader "
                    "som beror på din funktionsnedsättning.\n\n"
                    "Exempel på merkostnader:\n"
                    "• Hjälpmedel som du köpt själv\n"
                    "• Slitage på kläder och möbler\n"
                    "• Specialkost\n"
                    "• Resor till vård\n\n"
                    "Du söker hos Försäkringskassan. Du behöver kunna "
                    "visa vilka extra kostnader du har."
                ),
            },
            {
                "q": "Vad är bostadstillägg?",
                "a": (
                    "Bostadstillägg är ett tillägg till din ersättning "
                    "för att hjälpa dig betala hyran.\n\n"
                    "Du kan få bostadstillägg om du har:\n"
                    "• Aktivitetsersättning\n"
                    "• Sjukersättning\n\n"
                    "Hur mycket du får beror på din hyra och dina "
                    "inkomster.\n\n"
                    "💡 Tips: Sök bostadstillägg samtidigt som du söker "
                    "din ersättning!"
                ),
            },
            {
                "q": "Kan jag jobba och ha ersättning?",
                "a": (
                    "Ja, ofta kan du kombinera arbete och ersättning!\n\n"
                    "• Med aktivitetsersättning kan du prova att jobba "
                    "med \"vilande ersättning\".\n\n"
                    "• Du kan ha partiell sjukersättning (25%, 50% "
                    "eller 75%).\n\n"
                    "• Daglig verksamhet påverkar inte din ersättning.\n\n"
                    "💡 Tips: Prata med Försäkringskassan INNAN du börjar "
                    "jobba så att du vet vad som gäller."
                ),
            },
        ],
    },
]
