import streamlit as st
from bearcat_hud.core.bearcat_hud import BearcatHUD

st.set_page_config(page_title="Bearcat HUD", layout="wide")

st.title("🏈 Bearcat HUD")

hud = BearcatHUD()

st.sidebar.header("Select Options")
selected_game = st.sidebar.selectbox("Choose a game", hud.get_game_list())
selected_quarter = st.sidebar.selectbox("Choose a quarter", hud.get_quarters(selected_game))

st.header(f"Plays for {selected_game} - Quarter {selected_quarter}")
plays = hud.get_plays(selected_game, selected_quarter)
st.dataframe(plays)
