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


anos = df_times_anos['temporada_x'].unique().tolist()
anos.insert(0, "Todos")  # Adiciona a opção "Todos" no início da lista


temporada = st.sidebar.selectbox("Temporada",anos)


# Filtrar o DataFrame com base na seleção
if temporada == "Todos":
    df_filtrado_anos = df_times_anos
    times = df_times_anos["home_name"].unique().tolist()
    times.insert(0, "Todos")
    times = st.sidebar.selectbox("Times_Seleção", times)
    if times == "Todos":
        # df_filtrado_anos
        pass
    else:
        df_filtrado_anos = df_times_anos[df_times_anos['home_name'] == times]
    #     df_filtrado_anos = df_ligas_anos[df_ligas_anos['temporada'] == temporada and df_liga_anos[df_liga_anos['liga'] == ligas]]
else:
    df_filtrado_anos = df_times_anos[df_times_anos['temporada_x'] == temporada]

    times = df_times_anos["home_name"].unique()
    # # ligas.insert(0, "Todos")
    times = st.sidebar.selectbox("Liga_Seleção", times)
    df_filtrado_anos = df_filtrado_anos[df_filtrado_anos['home_name'] == times]

columns = ["temporada_x", "home_name",'imagem_time','Total_G__Marcados','Total_Jogos_C',
           'Total_Jogos_05FT', '%Jogos05FT','Total_Jogos_15FT','%Jogos15FT',
           'Total_Jogos_25FT','%Jogos25FT','Total_Jogos_35FT','%Jogos35FT']

st.dataframe(df_filtrado_anos[columns],
    column_config={ 
    "imagem_time": st.column_config.ImageColumn('Escudo'),
    })
 