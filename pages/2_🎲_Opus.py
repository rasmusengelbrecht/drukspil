import streamlit as st
import random
import time

st.set_page_config(page_title="Opus", page_icon=":game_die:")

st.markdown(
    """
        # Opus

        Spillerne trækker på skift et "kort", og følger anvisningerne for kortet. **Træk et kort her :point_down:**
    """
)

with st.expander("Start musikken"):
    st.video("https://www.youtube.com/watch?v=jv18kaukcfk&ab_channel=An1ka101")

def roll_dice():
    return random.randint(1, 6)

col1, col2, col3 = st.columns(3)

# Button to roll the dice
if col2.button("Rul terningen"):
    time.sleep(2)
    result = roll_dice()
    if result == 6:
        st.success(f"Juhuu! 🎉 Du slog {result} - Send den videre")
    else:
        st.error(f"Øv.. Du slog {result} 😔 Prøv igen!")


with st.expander("Regler"):
    st.markdown(
        """
            #### REGLERNE:

            1. Alle sidder i en cirkel med en drink eller tre, og en spiller stiller et "mest sandsynligt" spørgsmål. f.eks. "Hvem er mest tilbøjelig til at skade sig selv ved at spille bordtennis?" eller "Hvem er mest tilbøjelig til at komme i problemer med politiet for blotteri?"

            2. På tælling af 3 peger alle på den person, de tror, ville være mest tilbøjelig til at gøre, hvad der blev nævnt.

            3. Du skal tage 1 slurk for hver person, der peger på dig. Så hvis 5 personer tror, at du er mest tilbøjelig til at komme i problemer med politiet for blotteri, skal du tage 5 slurke.

    """
)

