import streamlit as st
from streamlit.logger import get_logger

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
        
        **👈 Vælg et spil i menuen** for at komme i gang!

        ### Værd at vide
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
    """
    )


if __name__ == "__main__":
    run()
