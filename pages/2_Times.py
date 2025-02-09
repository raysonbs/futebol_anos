import streamlit as st



st.set_page_config(
    page_title="Times",
    page_icon="🏃🏼",
    layout="wide"
)

# st.write('#Em Construção')

st.markdown('# Análise Times Por Temporada')


# df_liga_anos = st.session_state["data_ligas_anos"]

df_times_anos = st.session_state["data_times_anos"]

# st.write(df_liga_anos)
# st.write(df_times_anos)

# df_liga_anos = st.session_state["data_ligas_anos"]

# Coluna para se tornar o índice do DataFrame
# index_column = 'home_name'

# Redefine a coluna especificada como índice do DataFrame
# df_filtered = df_data.set_index(index_column)

# columns = ['status','home_name','home_image', "away_name",
#            'away_image','odds_ft_home','odds_ft_empate','odds_ft_away',"liga"]

# # df_filtered = df_data.set_index("status")

# st.dataframe(df_liga_anos[columns],
#              column_config={
#                  "home_image": st._column_config.ImageColumn(),
#                  "away_image":st._column_config.ImageColumn()
#              }
#             )


anos = df_times_anos['temporada_x'].unique().tolist()
anos.insert(0, "Todos")  # Adiciona a opção "Todos" no início da lista

temporada = st.sidebar.selectbox("Temporada",anos)

# Filtrar o DataFrame com base na seleção
if temporada == "Todos":
    df_filtrado_anos = df_times_anos
else:
    df_filtrado_anos = df_times_anos[df_times_anos['temporada_x'] == temporada]

# df_filtrado_anos = df_times_anos[df_times_anos['temporada_x'] == temporada]
# st.write(df_filtrado_anos)


columns = ["temporada_x", "home_name",'imagem_time','Total_G__Marcados','Total_Jogos_C',
           'Total_Jogos_05FT', '%Jogos05FT','Total_Jogos_15FT','%Jogos15FT',
           'Total_Jogos_25FT','%Jogos25FT','Total_Jogos_35FT','%Jogos35FT']


st.dataframe(df_filtrado_anos[columns],
            column_config={ 
                "imagem_time": st.column_config.ImageColumn('Escudo'),
             })