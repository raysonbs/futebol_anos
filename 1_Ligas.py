import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
import time

st.set_page_config(
    page_title="Ligas",
    page_icon="🏃🏼",
    layout="wide"
)

st.markdown('# Análise de Ligas Por Temporada')

# Função para carregar os dados do banco de dados
def load_data():
    # Informações de conexão e caminho do certificado
    username = 'root'
    password = 'FomFAYykiMbEFBR15ahPbuPcPiaN1lq2'
    host = '3il9oh.stackhero-network.com'
    port = 6454
    database = 'BD_Anos_Consolidados'

    # Configurações SSL
    ssl_args = {
        'ssl': {
            'ca': 'C:\\Users\\RAYSON\\isrgrootx1.pem'  # Certifique-se de que o caminho é válido
        }
    }

    # Criar a engine de conexão com o banco de dados
    engine = create_engine(
        f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}',
        connect_args=ssl_args
    )
    
    df_liga_anos = pd.read_sql_table('t_ligas_anos', con=engine)
    df_times_anos = pd.read_sql_table('t_times_anos', con=engine)

    return df_liga_anos, df_times_anos

# Inicializar a sessão para armazenamento de dados
if "last_loaded" not in st.session_state:
    st.session_state["last_loaded"] = 0  # Inicializa com 0 ou outro valor conveniente

# Checar se os DataFrames estão na sessão e se precisam ser atualizados
if "data_ligas_anos" not in st.session_state or time.time() - st.session_state["last_loaded"] > 600:
    df_liga_anos, df_times_anos = load_data()
    st.session_state["data_ligas_anos"] = df_liga_anos
    st.session_state["data_times_anos"] = df_times_anos
    st.session_state["last_loaded"] = time.time()

# Acesso e exibição do DataFrame df_ligas_anos
if "data_ligas_anos" in st.session_state:
    df_ligas_anos = st.session_state["data_ligas_anos"]
    # st.write("Dados das Ligas por Ano:")
    # st.write(df_ligas_anos)
else: 
    st.error("Os dados das ligas não foram carregados.")

# Acesso e exibição do DataFrame df_times_anos
if "data_times_anos" in st.session_state:
    df_times_anos = st.session_state["data_times_anos"]
    # st.write("Dados dos Times por Ano:")
    # st.write(df_times_anos)
else: 
    st.error("Os dados dos times não foram carregados.")
    

anos = df_ligas_anos['temporada'].unique().tolist()
anos.insert(0, "Todos")  # Adiciona a opção "Todos" no início da lista


temporada = st.sidebar.selectbox("Temporada",anos)


# Filtrar o DataFrame com base na seleção
if temporada == "Todos":
    df_filtrado_anos = df_ligas_anos
else:
    df_filtrado_anos = df_ligas_anos[df_ligas_anos['temporada'] == temporada]

# df_filtrado_anos = df_times_anos[df_times_anos['temporada_x'] == temporada]
# st.write(df_filtrado_anos)

st.dataframe(df_filtrado_anos,
            column_config={ 
                "image_league": st.column_config.ImageColumn('Escudo'),
             })