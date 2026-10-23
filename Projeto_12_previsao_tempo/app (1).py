import streamlit as st
from dados_api import previsao_temperatura

st.set_page_config(layout='wide')

cidades = {
    "Santana de Parnaíba": [-23.42831756832093, -46.930218054881905],
    "New York": [40.67776520260485, -73.95649461227816],
    "Atenas": [37.970512110369285, 23.727238282825045],
    "Fortaleza": [-3.7326789012030708, -38.531326564491025],
    "Berlim": [52.50735598800113, 13.412448253839397],
    "Copenhague": [55.67850892596702, 12.570287411918335],
    "Dubai": [25.20166125637402, 55.25133510459273],
    "Kuala Lumpur": [3.117971674953729, 101.6749865934935]
}

# ---------------------------------------- SIDEBAR

st.sidebar.title("Prevendo o Tempo")
st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a cidade", cidades.keys())
latitude , longitude = cidades[cidade]

# ---------------------------------------- BODY

st.title(f'Prevendo o Tempo em {cidade} para os próximos 7 dias')

st.markdown("---")

dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temperatura_media.iterrows():
    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Data",f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric("Temperatura média", f"{d['temperatura_media']:.2f}")

        with col3:
            if d['temperatura_media'] < 10:
                temp = "cold.png"

            elif d['temperatura_media'] < 18:
                temp = "cool.png"

            elif d['temperatura_media'] < 25:
                temp = "comfort.png"

            else:
                temp = "Warm.png"

            st.image(temp, width=40)

            
