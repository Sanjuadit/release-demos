import streamlit as st
# import pokebase as pb
import pandas as pd
import numpy as np
from PIL import Image
import time
import random

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("Improved cache spinner demo", "🌀", layout="wide")
icon("🌀")
cache_load = 15

st.title("Improved cache spinner demo", anchor=False)
st.info("""If you've used `st.cache_data` or `st.cache_resource`, you've probably noticed the spinner displayed in your UI in the event of a "cache miss" when your cached function runs. We've made **visual improvements** to this spinner – it is now overlayed on top of existing UI elements, preventing jumpiness and visual glitches.""")
# st.write("""If you've used `st.cache_data` or `st.cache_resource`, you've probably noticed the spinner displayed in your UI in the event of a "cache miss" when your cached function runs.""")
# st.write("We've made some **visual improvements** to this spinner – it is now overlayed on top of existing UI elements, preventing jumpiness and visual glitches.")
# Enhanced caching spinner prevents UI jumpiness by overlaying, not pushing down, elements.")
# st.write("Learn more about caching in [<PLACEHOLDER_OUR_DOCS>](https://docs.streamlit.io/).")
st.divider()

def clear_cache():
    st.cache_data.clear()

corgi = Image.open("1.28/pages/kevin.jpg")
otter = Image.open("1.28/pages/sea_otter.png")
duck = Image.open("1.28/pages/duck.jpeg")
penguin = Image.open("1.28/pages/penguin.jpeg")
st.button("Show me the spinners", on_click=clear_cache)

col1, col2, = st.columns(2)

@st.cache_data
def render_df():
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    time.sleep(cache_load)
    return df

@st.cache_data
def render_chart():
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    time.sleep(cache_load)
    return df

with col1:
    st.header("Old spinner")
    with st.spinner("Notice how the spinner pushes the image down ⬇️"):
        time.sleep(3)
    st.image(corgi)
with col2:
    st.header("New and improved spinner")
    @st.cache_data
    def render_kevin():
        time.sleep(cache_load)
        return corgi
    st.image(retrieve_corgi_image())
    # st.caption("🚗 Corgi on a Roadtrip")
# tell user what happens when they select the ruler below
# st.info("Use the slider to simulate different cache load times. It'll help you see how the enhanced caching spinner behaves.", icon="ℹ️")
# cache_load = st.slider("Choose cache function load time:", 0, 30, 10)

st.divider()

# with st.sidebar:
#     @st.cache_data
#     def fetch_pokemon():
#         time.sleep(cache_load)
#         random_id = random.randint(1, 251)
#         pokemon = pb.pokemon(random_id)
#         pokemon_name = pokemon.name
#         sprite = pb.SpriteResource('pokemon', random_id, official_artwork=True)
#         return pokemon_name.capitalize(), sprite.url
#     st.subheader("⚠️ Vital Sidebar Content")
#     st.info("The spinner overlays below to prevent UI jumpiness.", icon="🌀")
#     st.divider()
#     st.write("**Cached Pokemon** :fire:")
#     pokemon_name, sprite = fetch_pokemon()
#     st.image(sprite, width=150)
#     st.caption(f"**{pokemon_name}**")




st.subheader("Cache spinners:")
st.info("Notice how the spinner overlays other elements, keeping UI sleek and avoiding jumps.", icon="🔄")
st.write("Rendering a dataframe...")
st.dataframe(render_df())
st.divider()
st.info("A bar chart, also cached. Again, watch for the non-intrusive spinner.", icon="📊")
st.write("Rendering a chart...")
st.bar_chart(render_chart())
st.divider()

st.info("Choose your aquatic pet and see the cached image load smoothly.", icon="🖼️")
st.write("Rendering some images...")
animal = st.radio("Select your aquatic pet:", ["Otter", "Duck", "Penguin"], horizontal=True)

col1, col2 = st.columns(2)

with col1:
    @st.cache_data
    def retrieve_corgi_image():
        time.sleep(cache_load)
        return corgi

    st.write("**Cached Corgi Cuteness...**")
    st.image(render_kevin())
    st.caption("🚗 Corgi on a Roadtrip")

with col2:
    st.write("**`st.spinner` Cuteness** 🌊")
    if animal == "Duck":
        picture = duck
        caption = "🦆 Baby Duckling"
    elif animal == "Penguin":
        picture = penguin
        caption = "🐧 Little Penguin"
    else:    
        picture = otter
        caption = "🦦 Fluffy Otter"

    with st.spinner("Loading Spinner..."):
        time.sleep(3)
        st.image(picture, use_column_width=True)
        st.caption(caption)
st.divider()

