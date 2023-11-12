import streamlit as st
import random

st.set_page_config(page_title="Hvem Her", page_icon=":point_right:")

st.markdown(
    """
        # Hvem Her?

        Peg på den deltager som passer bedst til udsagnet, den med flest stemmer, drikker det antal slurke som vedkommende har modtaget stemmer. **Prøv et udsagn her :point_down:**
    """
)

statements = [
    "Hvem her er mest tilbøjelig til at fare vild i deres eget hjemby?",
    "Hvem her er mest tilbøjelig til at blive taget i at bade nøgen?",
    "Hvem her er mest tilbøjelig til at få en pinlig tatovering?",
    "Hvem her er mest tilbøjelig til at blive en skør katte dame?",
    "Hvem her er mest tilbøjelig til at spise noget fra jorden?",
    "Hvem her er mest tilbøjelig til at give deres barn et usædvanligt (*host* latterligt *host*) navn?",
    "Hvem her er mest tilbøjelig til at blive anholdt for at tisse offentligt?",
    "Hvem her er mest tilbøjelig til at have en fod fetish?",
    "Hvem her er mest tilbøjelig til at slippe en prut offentligt?",
    "Hvem her er mest tilbøjelig til at blive anholdt for at være fuld og uordenlig?",
    "Hvem her er mest tilbøjelig til at låse sig selv ude af huset?",
    "Hvem her er mest tilbøjelig til at blive i badeværelset længst tid (vi behøver ikke at vide, hvad du laver!)?",
    "Hvem her er mest tilbøjelig til at bestille takeout inden for de næste 24 timer?",
    "Hvem her er mest tilbøjelig til at tage en fridag på grund af tømmermænd?",
    "Hvem her er mest tilbøjelig til at sige noget dumt på første date?",
    "Hvem her er mest tilbøjelig til at eje flest kæledyr?",
    "Hvem her er mest tilbøjelig til at miste deres telefon på en bytur?",
    "Hvem her er mest tilbøjelig til at falde om på en bytur?",
    "Hvem her er mest tilbøjelig til at snorke så meget, at deres partner sover på sofaen?",
    "Hvem her er mest tilbøjelig til at have brugt en falsk ID for at købe alkohol?",
    "Hvem her er mest tilbøjelig til at date to fyre på én gang?",
    "Hvem her er mest tilbøjelig til at gå i seng med nogen på første date?",
    "Hvem her er mest tilbøjelig til at glemme navnet på en person, de har været sammen med?",
    "Hvem her er mest tilbøjelig til at have et engangsliggende?",
    "Hvem her er mest tilbøjelig til at blive taget i at kysse med nogen offentligt?",
    "Hvem her er mest tilbøjelig til at falde i søvn under sex?",
    "Hvem her er mest tilbøjelig til at prøve en trekant?",
    "Hvem her er mest tilbøjelig til at have noget kørende med deres chef?",
    "Hvem her er mest tilbøjelig til at blive taget i at være sammen med deres eks?",
    "Hvem her er mest tilbøjelig til at bygge et sex-dungeon?",
    "Hvem her er mest tilbøjelig til at tage det første skridt?",
    "Hvem her er mest tilbøjelig til at gå i seng med en kollega?",
    "Hvem her er mest tilbøjelig til at besøge en stripklub?",
    "Hvem her er mest tilbøjelig til at være into BDSM?",
    "Hvem her er mest tilbøjelig til at onanere et offentligt sted?",
    "Hvem her er mest tilbøjelig til at lave en sexvideo?",
    "Hvem her er mest tilbøjelig til ikke at bruge beskyttelse?",
    "Hvem her er mest tilbøjelig til at blive taget i at se porno?",
    "Hvem her er mest tilbøjelig til at snyde deres partner?",
    "Hvem her er mest tilbøjelig til at stønne højst under sex?",
    "Hvem her er mest tilbøjelig til at blive en TikTok-stjerne?",
    "Hvem her er mest tilbøjelig til at blive millionær?",
    "Hvem her er mest tilbøjelig til at have flest børn?",
    "Hvem her er mest tilbøjelig til at slå en verdensrekord?",
    "Hvem her er mest tilbøjelig til at ende i fængsel?",
    "Hvem her er mest tilbøjelig til at blive politiker?",
    "Hvem her er mest tilbøjelig til at melde sig til hæren?",
    "Hvem her er mest tilbøjelig til at tage ud i rummet?",
    "Hvem her er mest tilbøjelig til at opsige deres job og rejse jorden rundt?",
    "Hvem her er mest tilbøjelig til at blive berømt?",
    "Hvem her er mest tilbøjelig til at leve længst?",
    "Hvem her er mest tilbøjelig til at ødelægge en jobsamtale?",
    "Hvem her er mest tilbøjelig til at få en PhD?",
    "Hvem her er mest tilbøjelig til at gifte sig ind i den kongelige familie?",
    "Hvem her er mest tilbøjelig til at optræde i en reality-tv-show?",
    "Hvem her er mest tilbøjelig til at skrive en bog?",
    "Hvem her er mest tilbøjelig til at blive komiker?",
    "Hvem her er mest tilbøjelig til at gå bankerot?",
    "Hvem her er mest tilbøjelig til at trække sig tidligt tilbage?",
    "Hvem her er mest tilbøjelig til at blive gift mere end én gang?",
    "Hvem her er mest tilbøjelig til at slippe afsted med mord?",
    "Hvem her er mest tilbøjelig til at være den favoriserede søskende?",
    "Hvem her er mest tilbøjelig til at skuffe deres venner for at flirte med en fremmed?",
    "Hvem her er mest tilbøjelig til at dø først, hvis I var med i en gyserfilm?",
    "Hvem her er mest tilbøjelig til at blamere en ven offentligt?",
    "Hvem her er mest tilbøjelig til at blamere sig selv offentligt?",
    "Hvem her er mest tilbøjelig til at komme med en sarkastisk kommentar?",
    "Hvem her er mest tilbøjelig til at vinde i et løb?",
    "Hvem her er mest tilbøjelig til at røbe en hemmelighed?",
    "Hvem her er mest tilbøjelig til at trække sig tilbage på landet?",
    "Hvem her er mest tilbøjelig til at trække sig tilbage i en by?",
    "Hvem her er mest tilbøjelig til at bruge mest på tøj?",
    "Hvem her er mest tilbøjelig til at give penge til velgørenhed?",
    "Hvem her er mest tilbøjelig til at lave frivilligt arbejde?",
    "Hvem her er mest tilbøjelig til at forsvinde fra vennekredsen?",
    "Hvem her er mest tilbøjelig til at stjæle i en butik?",
    "Hvem her er mest tilbøjelig til at skide i naturen?",
    "Hvem her er mest tilbøjelig til at give skylden for noget på en anden?",
    "Hvem her er mest tilbøjelig til at lyve på deres CV?",
    "Hvem her er mest tilbøjelig til at gå en uge uden at tage et bad?",
    "Hvem her er mest tilbøjelig til at flirte med bartenderen for at få en gratis drink?",
    "Hvem her er mest tilbøjelig til at blive spurgt om deres nummer?",
    "Hvem her er mest tilbøjelig til at have en stripper til deres polterabend?",
    "Hvem her er mest tilbøjelig til at drikke for meget?",
    "Hvem her er mest tilbøjelig til at danse på bordet?",
    "Hvem her er mest tilbøjelig til at vågne op med en tatovering?",
    "Hvem her er mest tilbøjelig til at flirte med en dørmand?",
    "Hvem her er mest tilbøjelig til at være den første ved karaoke?",
    "Hvem her er mest tilbøjelig til at være den sidste person stående?",
    "Hvem her er mest tilbøjelig til at fare vild på en bytur?",
    "Hvem her er mest tilbøjelig til at holde polterabend på Ibiza?",
    "Hvem her er mest tilbøjelig til at vinde i lerdueskydning?",
    "Hvem her er mest tilbøjelig til at være dygtig til pole-dancing?",
    "Hvem her er mest tilbøjelig til at vinde i gokart?",
    "Hvem her er mest tilbøjelig til at være den første på dansegulvet?",
    "Hvem her er mest tilbøjelig til at få en drink købt til dem?",
    "Hvem her er mest tilbøjelig til at vågne op uden tømmermænd?",
    "Hvem her er mest tilbøjelig til at melde sig til Paradise Hotel?"
]

# Function to get a random statement that hasn't been displayed yet
def get_random_statement():
    # Retrieve or initialize the displayed statements for the current session
    displayed_statements = st.session_state.get("displayed_statements", [])

    # Check if all statements have been displayed
    if len(displayed_statements) == len(statements):
        return None  # Return None to indicate no more statements

    # Get a random statement that hasn't been displayed yet
    statement = random.choice([s for s in statements if s not in displayed_statements])

    # Add the statement to the set of displayed statements
    displayed_statements.append(statement)

    # Update the displayed statements in the session state
    st.session_state.displayed_statements = displayed_statements

    return statement

col1, col2, col3 = st.columns(3)

# Button to display a random statement
if col2.button("Nyt udsagn :new:"):
    random_statement = get_random_statement()

    if random_statement is not None:
        st.info(f"{random_statement}")
    else:
        st.info("Ikke flere udsagn tilbage")


with st.expander("Regler"):
    st.markdown(
        """
            #### REGLERNE:

            1. Alle sidder i en cirkel med en drink eller tre, og en spiller stiller et "mest sandsynligt" spørgsmål. f.eks. "Hvem er mest tilbøjelig til at skade sig selv ved at spille bordtennis?" eller "Hvem er mest tilbøjelig til at komme i problemer med politiet for blotteri?"

            2. På tælling af 3 peger alle på den person, de tror, ville være mest tilbøjelig til at gøre, hvad der blev nævnt.

            3. Du skal tage 1 slurk for hver person, der peger på dig. Så hvis 5 personer tror, at du er mest tilbøjelig til at komme i problemer med politiet for blotteri, skal du tage 5 slurke.

    """
)
    