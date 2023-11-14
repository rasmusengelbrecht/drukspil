import streamlit as st
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page 

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Overblik",
        page_icon=":beers:",
    )

    st.write("# Velkommen til Drukspil! :beers:")

    st.markdown(
        """
        Drukspil er en gratis platform med danske drukspil du kan bruge fra mobilen, lige når du har brug for dem.
        
        **Vælg et spil i menuen** for at komme i gang!

        ### Vores spil:
    """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        hvem = st.button("👉 Spil Hvem Her..")
        if hvem:
            switch_page("hvem her")    

        vandfald = st.button("💧 Spil Vandfald")
        if vandfald:
            switch_page("vandfald")    

    with col2:
        opus = st.button("🎲 Spil Opus")
        if opus:
            switch_page("opus")    

        træmand = st.button("🌳 Spil Træmand")
        if træmand:
            switch_page("træmand")

    with col3:
        tarot = st.button("🎴 Spil Tarot")
        if tarot:
            switch_page("tarot")    


if __name__ == "__main__":
    run()
