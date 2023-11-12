import streamlit as st

st.set_page_config(page_title="Most Likely", page_icon=":point_right:")

st.markdown(
    """
        # Most Likely

        En fremragende leg at spille med folk, du ikke kender, eller lige har mødt... Fremragende for rejsende! Du skal være ret kreativ med dine spørgsmål, og vær ikke genert, når spørgsmålene til sidst bliver seksuelle... Jeg har aldrig spillet et spil, hvor det ikke er sket!

        Hvis du er nogen, der virker ret eventyrlysten/klodset/gal/festlig, ender du måske med at drikke meget i dette spil. Jeg håber, du har masser af alkohol klar, bare i tilfælde af.

        #### DET SKAL DU BRUGE:

        - Alkohol
        - Kreativitet
        - En beskidt tanke, hvis du vil have, at spillet skal være sjovt

    """
)

with st.expander("Regler"):
    st.markdown(
        """
            #### REGLERNE:

            1. Alle sidder i en cirkel med en drink eller tre, og en spiller stiller et "mest sandsynligt" spørgsmål. f.eks. "Hvem er mest sandsynligvis til at skade sig selv ved at spille bordtennis?" eller "Hvem er mest sandsynligvis til at komme i problemer med politiet for blotteri?"

            2. På tælling af 3 peger alle på den person, de tror, ville være mest tilbøjelig til at gøre, hvad der blev nævnt.

            3. Du skal tage 1 drink for hver person, der peger på dig. Så hvis 5 personer tror, at du er mest tilbøjelig til at komme i problemer med politiet for blotteri, skal du tage 5 drinks.

            En fantastisk leg at spille med folk, du lige har mødt, for at bryde isen, og vær ikke overrasket, hvis de "mest sandsynlige" spørgsmål bliver seksuelle... Det sker altid.

            #### REGLERNE I BIDESTØRRELSE:

            1. Alle sidder i en cirkel.
            2. Spillere skiftes til at stille et "mest sandsynligt" spørgsmål, f.eks. "Hvem er mest sandsynligvis til at brække deres tå?"
            3. På tælling af 3 peger alle på nogen, de tror er mest tilbøjelig til at gøre, hvad der blev nævnt.
            4. For hver person, der peger på dig, tager du 1 drink. Så hvis 7 personer tror, at du er mest tilbøjelig til at brække din tå, skal du tage 7 drinks.

    """
)
    
import streamlit as st
import random

statements = [
    "Most likely to get lost in their own hometown?",
    "Most likely to get caught skinny dipping?",
    "Most likely to get an embarrassing tattoo?",
    "Most likely to become a crazy cat lady?",
    "Most likely to eat something off the ground?",
    "Most likely to give their kid an unusual (*cough* ridiculous *cough*) name?",
    "Most likely to get arrested for urinating in public?",
    "Most likely to have a foot fetish?",
    "Most likely to let rip in public?",
    "Most likely to get arrested for being drunk and disorderly?",
    "Most likely to lock themselves out of the house?",
    "Most likely to stay in the bathroom the longest (we don't need to know what you're doing!)?",
    "Most likely to order a takeaway in the next 24 hours?",
    "Most likely to pull a sickie due to a hangover?",
    "Most likely to say something stupid on a first date?",
    "Most likely to own the most pets?",
    "Most likely to lose their phone on a night out?",
    "Most likely to stack it on a night out?",
    "Most likely to snore so badly their partner sleeps on the sofa?",
    "Most likely to have used fake I.D. to buy booze?"
]

# Use set to keep track of displayed statements
displayed_statements = set()

def get_random_statement():
    # Check if all statements have been displayed, reset if necessary
    if len(displayed_statements) == len(statements):
        displayed_statements.clear()
    
    # Get a random statement that hasn't been displayed yet
    statement = random.choice([s for s in statements if s not in displayed_statements])
    
    # Add the statement to the set of displayed statements
    displayed_statements.add(statement)
    
    return statement

# Button to display a random statement
if st.button("Nyt udsagn "):
    random_statement = get_random_statement()
    st.write(f"{random_statement}")
