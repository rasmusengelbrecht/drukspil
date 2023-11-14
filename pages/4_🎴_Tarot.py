import streamlit as st
import pandas as pd
import json
import numpy as np # linear algebra
import os
import random
import PIL
import datetime
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tarot", page_icon=":flower_playing_cards:")

st.markdown(
    """
        # Tarot

        Se hvad skæbnen bringer. **Træk dine kort her :point_down:**
    """
)

@st.cache_data
def load_data(filename): 
    data = json.load(open(filename))
    return data

#data=load_data('/workspaces/data/tarot-images.json') 
data=load_data('/workspaces/data/tarot-images.json')
df = pd.json_normalize(data['cards'])

#st.write(df)

df['fortune_telling_1'] = df['fortune_telling'].str[0]
df['fortune_telling_2'] = df['fortune_telling'].str[1]
df['fortune_telling_3'] = df['fortune_telling'].str[2]
df = df.fillna('')

if st.button("Se din skæbne 🔮"):  

		reading = df.sample(n = 3).reset_index(drop=True)  
		
		today = datetime.date.today()
		date = today.strftime("%d-%B-%Y")
				
		# identify images
		name_img_past = reading['img'].iloc[0]
		name_img_present = reading['img'].iloc[1]
		name_img_future = reading['img'].iloc[2]

		# open images
		img_past = PIL.Image.open(f'/workspaces/data/{name_img_past}')
		img_present = PIL.Image.open(f'/workspaces/data/{name_img_present}')
		img_future = PIL.Image.open(f'/workspaces/data/{name_img_future}')

		# plot images
		fig, (past, present, future) = plt.subplots(1, 3, figsize=(5, 3), facecolor='#0e1117')
		fig.suptitle('Din skæbne bringer:', fontsize=10, color='white')
		past.imshow(img_past)
		past.axis('off')
		past.set_title(reading['name'].iloc[0], fontsize=7, color='white')
		present.imshow(img_present)
		present.axis('off')
		present.set_title(reading['name'].iloc[1], fontsize=7, color='white')
		future.imshow(img_future)
		future.axis('off')
		future.set_title(reading['name'].iloc[2], fontsize=7, color='white')
		plt.show()
		st.pyplot(fig)
		
		# Outcomes
		st.text('Min kære, her er hvad fortiden, nutiden og fremtiden bringer dig:')
		st.text('')
		st.subheader('I din fortid : ')
		st.text(reading['fortune_telling_1'].iloc[0])
		st.text(reading['fortune_telling_2'].iloc[0])
		st.text(reading['fortune_telling_3'].iloc[0])
		st.text('')
		st.subheader('I nutiden: ')
		st.text(reading['fortune_telling_1'].iloc[1])
		st.text(reading['fortune_telling_2'].iloc[1])
		st.text(reading['fortune_telling_3'].iloc[1])
		st.text('')
		st.subheader('I fremtiden: ')
		st.text(reading['fortune_telling_1'].iloc[2])
		st.text(reading['fortune_telling_2'].iloc[2])
		st.text(reading['fortune_telling_3'].iloc[2])