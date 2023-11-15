import streamlit as st
import random
import time

st.set_page_config(page_title="Træmand", page_icon=":deciduous_tree:")

st.markdown(
    """
        # Træmand

        Spillerne trækker på skift et "kort", og følger anvisningerne for kortet. **Træk et kort her :point_down:**
    """
)

cards = [
    "🍻 Fælles skål 🍻",
    "🍻🎲 Uddel 2 slurke til en anden spiller",
    "🌳 Træmanden drikker 3 slurke 🌳",
    "👈🍻 Personen til venstre skal drikke 2 slurke",
    "🍻👉 Personen til højre skal drikke 2 slurke",
    "😫🍻 Du skal selv drikke 2 slurke 🍻😫"
]

# Function to get a random card
def get_random_card():
    return random.choice(cards)

col1, col2, col3 = st.columns(3)

# Button to display a random card
if col2.button("Nyt kort :new:"):
    random_card = get_random_card()
    st.info(f"{random_card}")


with st.expander("Regler"):
    st.markdown(
        """
            #### REGLERNE:

            1. Sæt jer rundt om et bord, hvor I skiftes til at slå med terningen. Den første som slår 3, må udnævne en træmand.
            
            2. Den næste spiller, som slår tre, bliver den nye træmand. 
            
            3. Hvis træmanden slår en 3’er, må vedkommende give stafetten videre til en af de andre spillere.
            
            4. Slår deltagerne 1,2,4,5 eller 6 gælder følgende regler:

                - 1: Fælles skål

                - 2: Uddel 2 slurke til en anden spiller
                
                - 3: Træmanden drikker 3 slurke
                
                - 4: Personen til venstre skal drikke 2 slurke
                
                - 5: Personen til højre skal drikke 2 slurke
                
                - 6: Du skal selv drikke 2 slurke

    """
)

