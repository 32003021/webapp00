"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd

#Titulo
st.title("AUTOCUST")

#SubTitulo
st.subheader('Quem se organiza economiza')

#Introdução
st.markdown('Nas ultimas décadas temos observado uma grande instabilidade politica, jurídica e econômica no país, esse fatores de instabilidade trouxeram uma alta oscilação de preços. No mundo dos automóveis não é diferente, as taxas vem se tornando cada vez mais elevadas e o preços dos combustíveis sofreu uma grande alta.')
st.markdown('A AutoCust vem para ajudar os donos de carros a entender todos os custos com o combustível do seu veiculo e economizar muito. Vamos entender a composição dos combustíveis, comparar a rentabilidade entre gasolina e o etanol, alertar os clientes sobre o pagamento do IPVA, licenciamento e outras  datas importantes.')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Menu Principal',
    ('Cadastro', 'Calculadora de Preços', 'Historico de Preços', 'Calendario')
)

if add_selectbox == 'Cadastro':
    st.write("oi")
    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )

    #Mapa de Campinas
    map_data = pd.DataFrame(
        np.random.randn(500, 2) / [50, 50] + [-22.90556, -47.06083],
        columns=['lat', 'lon'])
    st.map(map_data)

elif add_selectbox == 'Calculadora de Preços':
    st.write("tudo bem")
elif add_selectbox == 'Historico de Preços':
    st.write("amo a luana")
else:
    st.write("bjs")



  
