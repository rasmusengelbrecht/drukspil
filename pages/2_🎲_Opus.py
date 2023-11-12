import streamlit as st
import requests

st.set_page_config(page_title="Opus", page_icon=":game_die:")

st.markdown(
    """
        # Opus

        Spillerne trækker på skift et "kort", og følger anvisningerne for kortet. **Træk et kort her :point_down:**
    """
)

@st.cache_data
def read_file_from_url(url):
    headers = {
        "User-Agent": "StreamlitDocs/1.5.0 (https://docs.streamlit.io; hello@streamlit.io)"
    }
    return requests.get(url, headers=headers).content


file_bytes = read_file_from_url(
    "https://github.com/rasmusengelbrecht/drukspil/blob/568f4a189ac08e23d75f89a534f97d18e65fae5c/.devcontainer/opus.ogg"
)

st.audio(file_bytes, format="audio/ogg")


with st.expander("Regler"):
    st.markdown(
        """
            #### REGLERNE:

            1. Alle sidder i en cirkel med en drink eller tre, og en spiller stiller et "mest sandsynligt" spørgsmål. f.eks. "Hvem er mest tilbøjelig til at skade sig selv ved at spille bordtennis?" eller "Hvem er mest tilbøjelig til at komme i problemer med politiet for blotteri?"

            2. På tælling af 3 peger alle på den person, de tror, ville være mest tilbøjelig til at gøre, hvad der blev nævnt.

            3. Du skal tage 1 slurk for hver person, der peger på dig. Så hvis 5 personer tror, at du er mest tilbøjelig til at komme i problemer med politiet for blotteri, skal du tage 5 slurke.

    """
)

