import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np 
import math
import matplotlib.pyplot as plt
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure          # isso cria gráficos Bokeh
from streamlit_bokeh import streamlit_bokeh  # insere o gráfico no Streamlit

st.set_page_config(
    page_title="Fórmula Econômica",
    page_icon="logo.square.png",
    layout="wide"
)

#tela inicial 
def opcoes_menu():  #DESENVOLVIDO
    col1, col2 = st.columns([1, 8])  # ajuste os pesos conforme necessário

    with col1:
        st.image("logo.square.png", width=90)  # ou 70, se preferir

    with col2:
        st.image("logo.rectangle.png", width=230)

    
    st.header('_Os melhores simuladores e cálculos econômicos estão aqui!_', divider = 'orange')
    #vou criar uma barra lateral para entrarem em contato, informações complementares e deixar o site bonito!
    with st.sidebar:
        col1, col2 = st.columns([3, 6])
        with col1:
            st.image("logo.square.png", width=100)  # ou 70, se preferir
        with col2:
            st.markdown("## :orange[Fórmula] :orange[Econômica]")

        st.write()
        if st.button('Sobre'):
            st.session_state.tela = 'sobre'
        st.link_button('Entre em Contato',"https://wa.me/5533998488760?text=Ol%C3%A1%21%20Vim%20pelo%20seu%20site%20F%C3%B3rmula%20Econ%C3%B4mica.%20Gostaria%20de%20mais%20informa%C3%A7%C3%B5es%21")
        st.markdown("---")
        st.caption("Versão 1.0 • 2025")
        st.caption("© Fórmula Econômica - Todos os direitos reservados")
    opcao = st.selectbox("Escolha um Simulador:", 
                         ["Macroeconômico", "Microeconômico", "Financeiro", "Estatístico", "Conversor de Moeda"])

    if st.button("Avançar"): #este botão é para quando vc utilizar o selectbox, definir qual vc utilizará e não ir de primeira, é tipo um botão de certeza
        if opcao == "Macroeconômico":
            st.session_state.tela = 'macro'    #entra dentre de outra tela esse st.session_state.tela sabe? ai cada tela é nomeada!
        elif opcao == "Microeconômico":
            st.session_state.tela = 'micro'
        elif opcao == "Financeiro":
            st.session_state.tela = 'fin'
        elif opcao == "Estatístico":
            st.session_state.tela = 'est'
        elif opcao == "Conversor de Moeda":
            st.session_state.tela = 'conv'

#menu macroeconômico
def tela_macro(): #DESENVOLVIDO
    st.title('Simulador Macroeconômico')
    st.subheader('Simule e analise os principais indicadores da economia', divider = 'orange')
    #para nao dar rerun
    if "opcoes_macro" not in st.session_state:
        st.session_state.opcoes_macro = None
    if "opcoes2_macro" not in st.session_state:
        st.session_state.opcoes2_macro = None
    if "opcoes3_macro" not in st.session_state:
        st.session_state.opcoes3_macro = None
    if "col_mc_1ok" not in st.session_state:
        st.session_state.col_mc_1ok = False
    if "col_mc_2ok" not in st.session_state:
        st.session_state.col_mc_2ok = False
    
    col1_mac, col2_mac = st.columns(2)
    with col1_mac:
        st.write('I')
        lista_macro = ['Macro I', 'Macro II', 'Macro III']
        st.session_state.opcoes_macro = st.selectbox('Escolha o tópico:', lista_macro)
        if st.button('OK', key = 'col1macro'):
            st.session_state.col_mc_1ok = True
        if st.button("Voltar ao Menu", key = "btn_menu_mac"):
            st.session_state.tela = 'menu'
    with col2_mac:
        st.write('II.')
        if st.session_state.col_mc_1ok == True:
            if st.session_state.opcoes_macro == 'Macro I':
                lista_macro_2 = ["PIB pelas 3 óticas", "Índice de Preços e Quantidade", "PIB Agregado e Crescimento"]
                st.session_state.opcoes2_macro = st.selectbox('Escolha a matéria:', lista_macro_2)
                if st.button('Avançar', key = 'macro_I_button'):
                    st.session_state.col_mc_2ok = True
            else:
                st.warning('A desenvolvedora ainda está aprendendo esta matéria!')
    st.markdown('---')
    if st.session_state.col_mc_1ok and st.session_state.col_mc_2ok:
        #tela
        match st.session_state.opcoes_macro:
            case 'Macro I':
                match st.session_state.opcoes2_macro:
                    case 'PIB pelas 3 óticas':
                        st.write('oi')
                    case 'Índice de Preços e Quantidade':
                        st.header('Simulador de Índices de Preços e Quantidade')
                        st.info('Use a tabela abaixo para criar uma economia fictícia e calcular os principais indicadores macroeconômicos')
                        # primeiro a pessoa precisa me informar quantos bens quer na economia
                        st.subheader('1. Configure sua economia')
                        st.session_state.num_bens = st.slider('Quantos bens você quer analisar na sua economia?', 2, 20, 3)
                        #com base na quantidade de bens, crio um dataframe 
                        #primeiro preciso de pandas...
                        #preciso meio que inicializar essa matriz q é o dataframe, então vou utilizar for
                        lista_inicial = [] #lista vazia
                        for periodo in [0, 1]: #para periodo em 0 e 1
                            for i in range (1, st.session_state.num_bens + 1): # i representa a linha
                                lista_inicial.append(
                                    {
                                        'PERÍODO': periodo,
                                        'BEM': f'Bem{i}',
                                        'PREÇO': 0.0,
                                        'QUANTIDADE': 0
                                    }
                                )

                        df_inicial = pd.DataFrame(lista_inicial)
                        #agora o usuário vai preencher a tabela
                        st.subheader('2. Preencha os dados da sua economia')
                        st.write("Insira os preços e quantidades para o período base (0) e o período atual (1).")
                        df_editado = st.data_editor( #comando para sair da biblioteca do panda e ir pro streamlit
                            df_inicial, #dataframe que criamos
                            num_rows = "dynamic", #parametro para fazer o usuario remover e adicionar bens
                            key = "data_editor_indices" #só uma chave para essa funcionalidade ser unica. caso eu criar outro dataframe futuramente pode dar erro
                        )

                        #depois do usuário preencher, oferecemos opções de calculo.
                        st.subheader("3. Escolha quais índices calcular:")
                        resultado_macro_indices = ['Índice de Preços de Laspeyres (IPCA)','Índice de Preços de Paasche (Deflator do PIB)','Índice de Preços de Fischer','Índice de Quantidade de Laspeyres','Índice de Quantidade de Paasche','Índice de Quantidade de Fischer']
                        indices_selecionados = st.multiselect('Quais resultados deseja visualizar?', resultado_macro_indices)
                        #Botão "Calcular Índices".
                        if st.button('Calcular índices', type= 'primary', key= 'stbtnci'):
                            try:
                                #tratamento de erro
                                #separar os dataframes por periodos
                                base = df_editado[df_editado['PERÍODO'] == 0].reset_index(drop=True) #estrutura de dicionario
                                atual = df_editado[df_editado['PERÍODO'] == 1].reset_index(drop=True)
                                # pra garantir que temos o mesmo número de bens em ambos os períodos
                                if len(base) != len(atual):
                                    st.error("Erro: O número de bens no Período 0 é diferente do Período 1. Por favor, ajuste a tabela.")
                                    return #Para a execução aqui
                                # Extrair as colunas como arrays numpy para cálculos rápidos
                                P0 = base['PREÇO (P)'].values
                                Q0 = base['QUANTIDADE (Q)'].values
                                P1 = atual['PREÇO (P)'].values
                                Q1 = atual['QUANTIDADE (Q)'].values

                                resultados = {}
                                # Cálculos de Preços
                                resultados['Índice de Preços de Laspeyres (IPCA)'] = ((P1 * Q0).sum() / (P0 * Q0).sum()) * 100
                                resultados['Índice de Preços de Paasche (Deflator do PIB)'] = ((P1 * Q1).sum() / (P0 * Q1).sum()) * 100
                                resultados['Índice de Preços de Fischer'] = np.sqrt(resultados['Índice de Preços de Laspeyres (IPCA)'] * resultados['Índice de Preços de Paasche (Deflator do PIB)'])

                                # Cálculos de Quantidade
                                resultados['Índice de Quantidade de Laspeyres'] = ((P0 * Q1).sum() / (P0 * Q0).sum()) * 100
                                resultados['Índice de Quantidade de Paasche'] = ((P1 * Q1).sum() / (P1 * Q0).sum()) * 100
                                resultados['Índice de Quantidade de Fischer'] = np.sqrt(resultados['Índice de Quantidade de Laspeyres'] * resultados['Índice de Quantidade de Paasche'])

                                st.subheader("Resultados")
                                
                                #cria colunas para exibir os resultados de forma organizada, via GEMINI
                                cols = st.columns(len(indices_selecionados))
                                col_idx = 0
                                for indice in indices_selecionados:
                                    with cols[col_idx]:
                                        st.metric(label=indice, value=f"{resultados[indice]:.2f}")
                                    col_idx += 1
                            #tratamento de erro
                            except ZeroDivisionError:
                                st.error("Erro: Divisão por zero. Verifique se todos os preços e quantidades no período base são maiores que zero.")
                            except Exception as e:
                                st.error(f"Ocorreu um erro inesperado: {e}")
                    case 'PIB Agregado e Crescimento':
                        #O QUE DESEJA CALCULAR?
                        opcoes_pib_agreg = ['PIB Real', 'PIB Nominal', 'Deflator do PIB']
                            #DEPENDENDO DA ESCOLHA PEDE OS OUTROS VALORES, AS FÓRMULAS LÁ
                            #SAIDA
                            #DEPOIS DA SAÍDA: DESEJA CALCULAR TAXA DE CRESCIMENTO ECONÔMICO? PEDE OS DADOS DE UM SEGUNDO ANO PARA COMPARAR OS PIBS REAIS E CALCULAR VARIAÇÃO PERCENTUAL






   

@st.cache_data(ttl=86400)  # cache diário (86400 segundos = 24 horas)     #via chat gpt

# Função para obter taxas de câmbio atualizadas via API (via chat gpt ajuda)
def obter_taxas(): #DESENVOLVIDO com api e gpt
    try:
        url = "https://api.frankfurter.app/latest?from=USD"
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        # Frankfurter retorna um dicionário de taxas direto
        taxas = {"USD": 1.0}  # base USD
        for moeda, valor in dados['rates'].items():
            taxas[moeda] = float(valor)

        return taxas

    except Exception as e:
        st.error(f"Erro ao buscar taxas: {e}")
        return {"USD": 1.0}  # Fallback básico

# Simuladores simples
def tela_micro():  #EM DESENVOLVIMENTO --- pretendo integrar MATPLOTLIB para simular os gráficos
    st.title('Simulador Microeconômico')
    st.subheader('_Simule aqui suas principais necessidades microeconômicas_', divider = 'orange')
    col1, col2 = st.columns(2)
    if "col_1ok_micro" not in st.session_state:
        st.session_state.col_1ok_micro = False
    if "col_2ok_micro" not in st.session_state:
        st.session_state.col_2ok_micro = False
    if "opcoes_micro" not in st.session_state:
        st.session_state.opcoes_micro = None
    if "opcoes_2_micro" not in st.session_state:
        st.session_state.opcoes_2_micro = None
    if "calcular_plot" not in st.session_state:
        st.session_state.calcular_plot = False
    if "opcoes_ci" not in st.session_state:
        st.session_state.opcoes_ci = None
    if "col_1ok_ci" not in st.session_state:
        st.session_state.col_1ok_ci = False
    if "col_2ok_ci" not in st.session_state:
        st.session_state.col_2ok_ci = False
    if "opcoes_1_ci" not in st.session_state:
        st.session_state.opcoes_1_ci = None
    if "opcoes_2_ci" not in st.session_state:
        st.session_state.opcoes_2_ci = None
    if "acb" not in st.session_state:
        st.session_state.acb = None
    if "bcb" not in st.session_state:
        st.session_state.bcb = None
    if "ucb" not in st.session_state:
        st.session_state.ucb = None
    if "aro" not in st.session_state:
        st.session_state.aro = None
    if "bro" not in st.session_state:
        st.session_state.bro = None
    if "rro" not in st.session_state:
        st.session_state.rro = None
    if "q1" not in st.session_state:
        st.session_state.q1 = None
    if "q2" not in st.session_state:
        st.session_state.q2 = None

    
    
    #---------------------COLUNA 1 ----------------------------------------
    with col1:
        st.write('I.')
        LISTA_MICRO = ['Micro I', 'Micro II', 'Micro III']
        st.session_state.opcoes_micro = st.selectbox("Selecione a matéria: ", LISTA_MICRO)
        if st.button('OK', key = "btn_micro"):
            st.session_state.col_1ok_micro = True
        if st.button("Voltar ao Menu", key = "btn_menu"):
            st.session_state.tela = 'menu'
    #----------------------COLUNA 2 ---------------------------------------
    with col2:
        st.write('II.')
        if st.session_state.col_1ok_micro == True:
            if st.session_state.opcoes_micro == 'Micro I':
                LISTA_MICROI = ["Linha de Restrição Orçamentária", "Curva de indiferença", "Equilíbrio do Consumidor", "Maximização de Utilidade", "Elasticidades"]
                st.session_state.opcoes_2_micro = st.selectbox("Selecione o tópico:", LISTA_MICROI)
                if st.button('Avançar', key = 'btn_avanc_micro'):
                    st.session_state.col_2ok_micro = True
            if st.session_state.opcoes_micro == 'Micro II':
                st.warning("A desenvolvedora ainda está aprendendo essa matéria! Volte daqui uns meses para possível atualização!")
            if st.session_state.opcoes_micro == 'Micro III':
                st.warning("A desenvolvedora ainda está aprendendo essa matéria! Volte daqui uns meses para possível atualização!")

    #------------------------------- TELA ---------------------------------
    if (st.session_state.col_2ok_micro and st.session_state.col_1ok_micro):
        match st.session_state.opcoes_micro:
            case 'Micro I':
                st.warning("A desenvolvedora ainda está atualizando essa matéria! Aguarde novas funcionalidades")
                st.markdown("---")
                match st.session_state.opcoes_2_micro:
                    case "Linha de Restrição Orçamentária":
                        st.subheader("Linha de Restrição Orçamentária")
                        # Inicializar variáveis no session_state (para evitar erro)
                        if "q1" not in st.session_state:
                            st.session_state.q1 = []
                        if "q2" not in st.session_state:
                            st.session_state.q2 = []
                        if "calcular_plot" not in st.session_state:
                            st.session_state.calcular_plot = False
                        #dividir mais duas colunas aqui
                        col1_lrc, col2_lrc = st.columns(2)
                        with col1_lrc:
                            # Sliders de entrada
                            a = st.slider("Preço do bem A (a)", 1, 1000, 40, 1)
                            b = st.slider("Preço do bem B (b)", 1, 1000, 20, 1)
                            R = st.slider("Renda (R)", 1, 2000, 200, 1)
                            st.session_state.aro = a
                            st.session_state.bro = b
                            st.session_state.rro = R 
                            if st.button("Calcular", key = "btn_micro_lro"):
                            # Fórmulas: q2 = (R/p2) - (p1/p2)*q1
                                q1_max = R / a
                                q2_max = R / b
                                q1 = np.linspace(0, q1_max, 200)
                                q2 = (R / b) - ((a / b) * q1)
                                q2 = np.clip(q2, 0, None)  # Garante não-negativo
                                 # Salvar no session_state
                                st.session_state.q1 = q1
                                st.session_state.q2 = q2
                                st.session_state.q1_max = q1_max
                                st.session_state.q2_max = q2_max
                                st.session_state.calcular_plot = True
                        with col2_lrc:
                            if st.session_state.calcular_plot:
                                source = ColumnDataSource(data=dict(q1=st.session_state.q1, q2=st.session_state.q2))
                                                # Criar gráfico Bokeh
                                ro_p = figure(
                                    title=f"Linha de Restrição Orçamentária (R={int(st.session_state.rro)})",
                                    x_axis_label="Bem A",
                                    y_axis_label="Bem B",
                                    width=700,
                                    height=500,
                                    tools="pan,wheel_zoom,reset,save"
                                )

                                # Linha da restrição
                                ro_p.line("q1", "q2", source=source, line_width=3, color="navy",
                                        legend_label=f"R={int(st.session_state.rro)}")

                                # Hover para mostrar coordenadas
                                hover = HoverTool(tooltips=[("Bem A", "@q1{0.00}"), ("Bem B", "@q2{0.00}")], mode="mouse")
                                ro_p.add_tools(hover)

                                # Ajuste de ranges para caber os interceptos
                                ro_p.x_range.start = 0
                                ro_p.x_range.end = st.session_state.q1_max * 1.05
                                ro_p.y_range.start = 0
                                ro_p.y_range.end = st.session_state.q2_max * 1.05

                                # Renderizar no Streamlit
                                streamlit_bokeh(ro_p, use_container_width=True, theme="streamlit", key="restricao_orcamentaria")
                    case "Curva de indiferença":
                        st.subheader("Curva de indiferença")
                        st.warning("Curva que representa todas as combinações de cestas de mercado que geram o mesmo nível de satisfação para um consumidor. (Robert S. Pindyck,  Daniel L. Rubinfeld,  Eleutério Prado,  Thelma Guimarães, Microeconomia)")
                        col1_ci, col2_ci = st.columns(2)
                        with col1_ci:
                            st.write("")
                            lista_ci = ["Cobb-Douglas: U(x,y)=x^a* y^b", "Perfeitos substitutos: U(x,y)=ax+by"]
                            st.session_state.opcoes_ci = st.selectbox("Escolha sua função de Utilidade:", lista_ci)
                            match st.session_state.opcoes_ci:
                                case "Cobb-Douglas: U(x,y)=x^a* y^b":
                                    a = st.slider("Expoente do bem X (a)", 0.1, 1.0, 0.5, 0.01)
                                    b = st.slider("Expoente do bem Y (b)", 0.1, 1.0, 0.5, 0.01)
                                    U = st.slider("Nível de Utilidade (U)", 1, 2000, 25, 1)
                                    st.session_state.acb = a
                                    st.session_state.bcb = b
                                    st.session_state.ucb = U
                                    # Dados
                                    x = np.linspace(1, 50, 300)
                                    y = (U / (x**a))**(1/b)

                                    # Criar gráfico Bokeh
                                    p = figure(title=f"Curva de Indiferença U={U}",
                                            x_axis_label="Bem X",
                                            y_axis_label="Bem Y",
                                            width=700, height=500,
                                            tools="pan,wheel_zoom,reset,save")

                                    p.line(x, y, line_width=2, color="navy", legend_label=f"U={U}")
                                    p.add_tools(HoverTool(tooltips=[("X", "$x"), ("Y", "$y")]))

                                    if st.button("Criar gráfico", key = "btn_ci_cd"):
                                        st.session_state.col_1ok_ci = True
                                        st.session_state.opcoes_1_ci = True

                                    
                                case "Perfeitos substitutos: U(x,y)=ax+by":
                                    a = st.slider("Coeficiente do bem X (a)", 0.1, 200.0, 1.0, 0.1)
                                    b = st.slider("Coeficiente do bem Y (b)", 0.1, 200.0, 1.0, 0.1)
                                    U = st.slider("Nível de Utilidade (U)", 1, 500, 20, 1)

                                    st.session_state.a_ps = a
                                    st.session_state.b_ps = b
                                    st.session_state.u_ps = U
                                    # Dados
                                    x = np.linspace(0, 50, 300)
                                    y = (U - a * x) / b
                                    y = np.where(y >= 0, y, np.nan)  # evita valores negativos no gráfico

                                    # Criar gráfico Bokeh
                                    p = figure(
                                        title=f"Curva de Indiferença (U={U})",
                                        x_axis_label="Bem X",
                                        y_axis_label="Bem Y",
                                        width=700, height=500,
                                        tools="pan,wheel_zoom,reset,save"
                                    )

                                    p.line(x, y, line_width=2, color="navy", legend_label=f"U={U}")
                                    p.add_tools(HoverTool(tooltips=[("X", "$x"), ("Y", "$y")]))

                                    if st.button("Criar gráfico", key="btn_ci_ps"):
                                        st.session_state.col_1ok_ci = True
                                        st.session_state.opcoes_2_ci = True
                        with col2_ci:
                            st.write("Aqui ficará o gráfico")
                            if st.session_state.col_1ok_ci== True:
                                if st.session_state.opcoes_1_ci == True: #caso for opção 1
                                    streamlit_bokeh(p, use_container_width=True, theme="streamlit", key="indiferencacd")
                                if st.session_state.opcoes_2_ci == True: #opção 2
                                    streamlit_bokeh(p, use_container_width=True, theme="streamlit", key="indiferencasp")
            case 'Micro II':
                st.write("")
            case 'Micro III':
                st.write("")
                

def tela_fin(): # EM DESENVOLVIMENTO
    st.title('Simulador Financeiro')
    st.subheader('_Todos os cálculos de Matemática Financeira aqui!_', divider='orange')

    #para não dar rerun
    if "col_1ok" not in st.session_state:
        st.session_state.col_1ok = False
    if "col_2ok" not in st.session_state:
        st.session_state.col_2ok = False
    if "opcoes" not in st.session_state:
        st.session_state.opcoes = None
    if "opcoes2" not in st.session_state:
        st.session_state.opcoes2 = None
    if "opcoes3" not in st.session_state:
        st.session_state.opcoes3 = None
    if "capital" not in st.session_state:
        st.session_state.capital = 0.0
    if "juros" not in st.session_state:
        st.session_state.juros = 0.0
    if "prazo" not in st.session_state:
        st.session_state.prazo = 0.0
    if "montante" not in st.session_state:
        st.session_state.montante = 0.0


    col1, col2 = st.columns(2)  #divide em duas colunas

# ---------------COLUNA 1 ----------------------
    with col1:  
        st.write("I.")
        lista_fin = ['Juros Simples', 'Descontos Simples','Juros Compostos','Taxa Real de Juros', 'Equivalência de Capitais', 'Sequências Uniformes e Não Uniformes', 'Amortização']
        st.session_state.opcoes = st.selectbox("Escolha o tópico I:", lista_fin)
        if st.button("Avançar", key = "btn_col1"):
            st.session_state.col_1ok = True
        if st.button("Voltar ao Menu", key = "btn_menu"):
            st.session_state.tela = 'menu'
  
#----------------COLUNA 2-----------------------
    with col2:
        st.write("II.")
        if st.session_state.col_1ok:
            match st.session_state.opcoes:
                case 'Juros Simples':
                    LISTA_TOPICOII = ['Juros Simples', 'Taxas Equivalentes', 'Juro Exato x Juro Comercial', 'Valor Atual e Nominal']
                    st.session_state.opcoes2 = st.selectbox("Escolha o tópico II: ", LISTA_TOPICOII)
                    if st.button("Pronto", key="btn_col2"):
                        st.session_state.col_2ok = True
                case 'Descontos Simples':
                    LISTA_TOPICOII = ['Desconto comercial', 'Taxa de desconto X Taxa de juros']
                    st.session_state.opcoes2 = st.selectbox("Escolha o tópico II: ", LISTA_TOPICOII)
                    if st.button("Pronto", key="btn_col2"):
                        st.session_state.col_2ok = True
            
                case 'Juros Compostos':
                    LISTA_TOPICOII = ['Juros Compostos', 'Períodos Não Inteiros', 'Taxas Equivalentes', 'CDB e RCB', 'Valor atual', 'Valor nominal', 'Compra a vista x Compra a Prazo', 'Taxa Acumulada', 'Taxa Over Selic']
                    st.session_state.opcoes2 = st.selectbox("Escolha o tópico II: ", LISTA_TOPICOII)
                    if st.button("Pronto", key="btn_col2"):
                        st.session_state.col_2ok = True
            '''
                case 'Taxa Real de Juros':
                    LISTA_TOPICOII = ['Índice de preços', 'Taxa Acumulada', 'IPCA', 'Taxa Real de Juros']
                    st.session_state.opcoes2 = st.selectbox("Escolha o tópico II: ", LISTA_TOPICOII)
                    if st.button("Pronto", key="btn_col2"):
                        st.session_state.col_2ok = True
                case'Equivalência de Capitais':
                    LISTA_TOPICOII = ['Equivalência de dois valores monetários', 'Valor atual de um conjunto de capitais', 'Valores equivalentes', 'Taxa interna de retorno']
                    st.session_state.opcoes2 = st.selectbox("Escolha o tópico II: ", LISTA_TOPICOII)
                    if st.button("Pronto", key="btn_col2"):
                        st.session_state.col_2ok = True
                case 'Sequências Uniformes e Não Uniformes':
                    LISTA_TOPICOII = ['Sequência Uniforme', 'Montante de Sequência Uniforme', 'Sequência em Gradiente', 'Sequência em Progressão Aritmética', 'Sequência em Progressão Geométrica', 'Renda Perpétua']
                    st.session_state.opcoes2 = st.selectbox("Escolha o tópico II: ", LISTA_TOPICOII)
                    if st.button("Pronto", key="btn_col2"):
                        st.session_state.col_2ok = True
                case 'Amortização':
                    LISTA_TOPICOII = ['SAC', 'PRICE', 'Saldo devedor no Sistema Francês', 'Sistema Americano']
                    st.session_state.opcoes2 = st.selectbox("Escolha o tópico II: ", LISTA_TOPICOII)
                    if st.button("Pronto", key="btn_col2"):
                        st.session_state.col_2ok = True
            '''
#------------- FORA DA COLUNA ------------------------------------
    st.markdown("---")
    if (st.session_state.col_1ok and st.session_state.col_2ok):
        match st.session_state.opcoes:
            case 'Juros Simples':
                match st.session_state.opcoes2:
                    case 'Juros Simples':
                        st.subheader("Determine a variável a ser calculada:")
                        lista_js_js = ['Montante', 'Capital', 'Taxa de Juros', 'Prazo']
                        # Adicionei uma key única para o selectbox para segurança
                        opcao_selecionada = st.selectbox(" ", lista_js_js, key="js_opcao_selecionada")
                        st.markdown("---")
                        match opcao_selecionada:
                            case 'Montante':
                                # ENTRADAS
                                st.write("Insira os dados para calcular o Montante:")
                                # Adicionei sufixos para tornar as chaves únicas
                                capital_input = st.number_input("Capital:", min_value=0.0, format="%.2f", key="montante_input_capital1")
                                prazo_input = st.number_input("Prazo:", min_value=0.0, format="%.2f", key="montante_input_prazo1")
                                juros_input = st.number_input("Taxa de Juros (%):", min_value=0.0, format="%.2f", key="montante_input_juros1")
                                st.warning("O período da taxa deve ser compatível com o prazo!")

                                if st.button("Calcular", key="montante_btn_calcular"):
                                    if (capital_input == 0 or prazo_input == 0 or juros_input == 0):
                                        st.error('Por favor insira um valor válido e diferente de zero!')
                                    else:
                                        # PROCESSAMENTO
                                        montante_calculado = capital_input * (1 + (juros_input / 100) * prazo_input)
                                        with st.expander("Resultado", expanded=True):
                                            # SAIDA
                                            st.metric(label='Montante', value=f"R$ {montante_calculado:,.2f}")

                            case 'Capital':
                                # ENTRADAS
                                st.write("Insira os dados para calcular o Capital:")
                                montante_input = st.number_input("Montante:", min_value=0.0, format="%.2f", key="capital_input_montante2")
                                juros_input = st.number_input("Taxa de Juros (%):", min_value=0.0, format="%.2f", key="capital_input_juros2")
                                prazo_input = st.number_input("Prazo:", min_value=0.0, format="%.2f", key="capital_input_prazo2")
                                st.warning("O período da taxa deve ser compatível com o prazo!")

                                if st.button("Calcular", key="capital_btn_calcular"):
                                    if (montante_input == 0 or prazo_input == 0 or juros_input == 0):
                                        st.error('Por favor insira um valor válido e diferente de zero!')
                                    else:
                                        # PROCESSAMENTO
                                        capital_calculado = montante_input / (1 + (juros_input / 100) * prazo_input)
                                        with st.expander("Resultado", expanded=True):
                                            # SAIDA
                                            st.metric(label='Capital', value=f"R$ {capital_calculado:,.2f}")

                            case 'Taxa de Juros':
                                # ENTRADAS
                                st.write("Insira os dados para calcular a Taxa de Juros:")
                                montante_input = st.number_input("Montante:", min_value=0.0, format="%.2f", key="juros_input_montante3")
                                capital_input = st.number_input("Capital:", min_value=0.0, format="%.2f", key="juros_input_capital3")
                                prazo_input = st.number_input("Prazo:", min_value=0.0, format="%.2f", key="juros_input_prazo3")
                                st.warning("O período da taxa será compatível com o prazo!")

                                if st.button("Calcular", key="juros_btn_calcular"):
                                    if (capital_input == 0 or prazo_input == 0 or montante_input == 0):
                                        st.error('Por favor insira um valor válido e diferente de zero!')
                                    else:
                                        # PROCESSAMENTO (Fórmula corrigida para retornar a taxa em %)
                                        juros_calculado = (((montante_input / capital_input) - 1) / prazo_input) * 100
                                        with st.expander("Resultado", expanded=True):
                                            # SAIDA
                                            st.metric(label='Taxa de Juros', value=f"{juros_calculado:,.2f}%")

                            case 'Prazo':
                                # ENTRADAS
                                st.write("Insira os dados para calcular o Prazo:")
                                montante_input = st.number_input("Montante:", min_value=0.0, format="%.2f", key="prazo_input_montante4")
                                capital_input = st.number_input("Capital:", min_value=0.0, format="%.2f", key="prazo_input_capital4")
                                juros_input = st.number_input("Taxa de Juros (%):", min_value=0.0, format="%.2f", key="prazo_input_juros4")
                                st.warning("O prazo será compatível com o período da taxa!")
                                
                                if st.button("Calcular", key="prazo_btn_calcular"):
                                    if (capital_input == 0 or montante_input == 0 or juros_input == 0):
                                        st.error('Por favor insira um valor válido e diferente de zero!')
                                    else:
                                        # PROCESSAMENTO (Fórmula corrigida para usar a taxa como decimal)
                                        taxa_decimal = juros_input / 100
                                        prazo_calculado = ((montante_input / capital_input) - 1) / taxa_decimal
                                        with st.expander("Resultado", expanded=True):
                                            # SAIDA
                                            st.metric(label='Prazo', value=f"{prazo_calculado:,.2f}")      
                    case 'Taxas Equivalentes':
                        st.subheader("Determine a variável a ser calculada:")
                        st.warning("No caso de Juros Simples, sabe-se que o prazo deve ser expresso na mesma unidade que a taxa. Então é preciso converter estas taxas para que sejam equivalentes.")
                        dict_taxas = {
                            "ao dia": 1/360,
                            "ao mês": 30/360,
                            "ao bimestre": 60/360,
                            "ao trimestre": 90/360,
                            "ao quadrimestre": 120/360,
                            "ao semestre": 180/360,
                            "ao ano": 1
                        }
                        #session.state para nao dar RERUN
                        if "tipo_conversao" not in st.session_state:
                            st.session_state.tipo_conversao = False
                        if "mostrar_inputs" not in st.session_state:
                            st.session_state.mostrar_inputs = False
                        if "calcular_taxas" not in st.session_state:
                            st.session_state.calcular_taxas = None
                        if "calcular_prazo" not in st.session_state:
                            st.session_state.calcular_prazo = None

                        #ENTRADA
                        st.session_state.tipo_conversao = st.selectbox("O que você deseja converter?", ["Taxa de Juros", "Prazo"])           
                        if st.button("Avançar", key = "btn_taxa_equivalente"):
                            st.session_state.mostrar_inputs = True

                        st.markdown("---")
                        if st.session_state.mostrar_inputs:
                            if st.session_state.tipo_conversao == "Taxa de Juros":
                                st.warning("Utilize esta ferramenta quando quiser converter o período da taxa para outro")
                                juros = st.number_input("Digite a taxa de juros (%):", min_value = 0.0)
                                periodo_origem = st.selectbox("Período de origem:",list(dict_taxas.keys()))
                                periodo_destino = st.selectbox("Converter para:",list(dict_taxas.keys()))
                                if juros == 0:
                                    st.error('Por favor insira um valor maior que zero para a taxa de juros!')
                                else:
                                    if st.button("Calcular", key = "btn_taxa_equivalente_juros"):
                                        st.session_state.calcular_taxas = (juros *  ((dict_taxas[periodo_destino])/dict_taxas[periodo_origem]))

                                    if st.session_state.calcular_taxas is not None:
                                        st.markdown("---")
                                        with st.expander("Resultado"):
                                            st.metric("Taxa Equivalente", f"{st.session_state.calcular_taxas:.4f}% {periodo_destino}")

                            elif st.session_state.tipo_conversao == "Prazo":
                                st.warning("Utilize esta ferramenta quando se sabe a taxa inicial, sabe a taxa final, mas não sabe qual período ela se transformou!")
                                juros = st.number_input("Digite a taxa de juros inicial (%)", min_value=0.0)
                                juros_fim = st.number_input("Digite a taxa de juros final (%)", min_value=0.0)
                                periodo_origem = st.selectbox("Digite o período de origem:", list(dict_taxas.keys()), key="p_origem")
                                
                                if st.button("Calcular Prazo Equivalente", key="btn_taxa_equivalente_prazo"):
                                    #tratamento de erro:
                                    if juros== 0 or juros_fim == 0:
                                        st.error("Por favor insira valores maiores que 0 para os juros!")
                                    else:
                                        # 1. calcular prazo em anos
                                        prazo_anos = (juros / juros_fim) * dict_taxas[periodo_origem]

                                        # 2. arredondar se próximo de 1 ano
                                        if abs(prazo_anos - 1) < 0.01:
                                            prazo_formatado = "1 ano"
                                        else:
                                            # converter para dias para exibir valor exato
                                            prazo_dias = prazo_anos * 360
                                            prazo_formatado = f"{prazo_dias:.0f} dias ({prazo_anos:.2f} anos)"
                                        
                                        st.session_state.calcular_prazo = prazo_formatado

                                if st.session_state.calcular_prazo is not None:
                                    st.markdown("---")
                                    with st.expander("Resultado"):
                                        st.metric("Prazo Equivalente", st.session_state.calcular_prazo)
                    case 'Juro Exato x Juro Comercial':
                        st.markdown("---")
                        st.subheader("Definição de Juro Exato x Juro Comercial")
                        st.warning(
                            "Os juros exatos consideram o ano civil (365 dias) e cada mês com o número real de dias. "
                            "Os juros comerciais consideram o ano comercial (360 dias) e cada mês com 30 dias."
                        )

                        # Dicionário de períodos (fração do ano)
                        dict_taxas = {
                            "ao dia": 1/360,
                            "ao mês": 30/360,
                            "ao bimestre": 60/360,
                            "ao trimestre": 90/360,
                            "ao quadrimestre": 120/360,
                            "ao semestre": 180/360,
                            "ao ano": 1
                        }

                        # Inicialização segura do session_state
                        if "juros" not in st.session_state:
                            st.session_state.juros = 0.0
                        if "capital" not in st.session_state:
                            st.session_state.capital = 0.0
                        if "prazo" not in st.session_state:
                            st.session_state.prazo = 0.0
                        if "tempo_juros" not in st.session_state or st.session_state.tempo_juros not in dict_taxas:
                            st.session_state.tempo_juros = "ao mês"
                        if "tempo_prazo" not in st.session_state or st.session_state.tempo_prazo not in dict_taxas:
                            st.session_state.tempo_prazo = "ao mês"

                        # Entradas
                        juros_input = st.number_input("Taxa de Juros (%):", min_value=0.0,value=st.session_state.juros,key="input_juros_je")
                        tempo_juros = st.selectbox("Selecione o período da Taxa de Juros (%)",list(dict_taxas.keys()),key="tempo_juros_je")
                        capital_input = st.number_input("Capital:",min_value=0.0,value=st.session_state.capital,key="input_capital_je")
                        prazo_input = st.number_input("Prazo:",min_value=0.0,value=st.session_state.prazo,key="input_prazo_je")
                        tempo_prazo = st.selectbox("Selecione o período de aplicação:",list(dict_taxas.keys()),key="tempo_prazo_je")
                        st.warning("O período da taxa deve ser compatível com o prazo!")

                        # Validação de zero
                        if capital_input == 0 or juros_input == 0 or prazo_input == 0:
                            st.error("Por favor, insira valores diferentes de zero!")
                        else:
                            st.session_state.capital = capital_input
                            st.session_state.juros = juros_input
                            st.session_state.prazo = prazo_input

                            if st.button("Calcular", key = "btn_calcular_juro_exato"):
                                # 1. Converter a taxa para uma taxa ANUAL.
                                taxa_anual = (st.session_state.juros / 100) / dict_taxas[tempo_juros]

                                # 2. Converter o prazo para DIAS (usando a base comercial de 360 dias).
                                dias = st.session_state.prazo * (dict_taxas[tempo_prazo] * 360)

                                # 3. Calcular os juros usando a taxa anual e o prazo em dias.
                                juros_comercial = st.session_state.capital * taxa_anual * (dias / 360)
                                juros_exato = st.session_state.capital * taxa_anual * (dias / 365)
                                
                                # Armazenando no session_state
                                st.session_state.juros_comercial = juros_comercial
                                st.session_state.juros_exato = juros_exato

                                # Exibição dos resultados
                                with st.expander("Juro Comercial"):
                                    st.metric(
                                        label="Juros Comercial",
                                        value=f"R${st.session_state.juros_comercial:,.2f}"
                                    )

                                with st.expander("Juro Exato"):
                                    st.metric(
                                        label="Juros Exato",
                                        value=f"R${st.session_state.juros_exato:,.2f}"
                                    )
                    case 'Valor Atual e Nominal':
                        st.subheader("Valor Atual e Nominal")
                        lista_vavn = ["Valor nominal", "Valor atual", "Taxa de juros", "Prazo"]
                        st.session_state.opcao_vavn = st.selectbox("Selecione a opção que deseja calcular:", lista_vavn)
                        match st.session_state.opcao_vavn:
                            case 'Valor nominal':
                                #VN=VA×(1+i×n)
                                st.write("Insira os dados:")
                                juros_vn_input = st.number_input("Taxa de juros (%):", min_value=0.0, value=st.session_state.get('juros2', 0.0), key="input_juros2")
                                valor_atual_input = st.number_input("Valor atual:", min_value=0.0, value=st.session_state.get('valor atual',0.0), key="input_valor_atual1")
                                prazo2_input = st.number_input("Prazo:", min_value=0.0, value=st.session_state.get('prazo2', 0.0), key="input_prazo2")     
                                if (juros_vn_input == 0 or prazo2_input == 0 or valor_atual_input == 0):
                                    st.error('Por favor insira um valor válido e diferente de zero!')
                                else:                           
                                    juros_decimal = juros_vn_input/100
                                    st.session_state.juros = juros_vn_input
                                    st.session_state.valor_atual = valor_atual_input
                                    st.session_state.prazo2 = prazo2_input
                                    if st.button("Calcular", key = "btn_vnjs"):
                                        #PROCESSAMENTO 
                                        
                                        st.session_state.valor_nominal_calculado = valor_atual_input * (1 + (juros_decimal * prazo2_input))
                                        with st.expander("Resultado"):
                                            #SAIDA
                                            st.metric(label = 'Valor Nominal', value = f"R${st.session_state.valor_nominal_calculado:,.2f}")
                            case 'Valor atual':
                                #VA = VN / ( 1 + in)
                                st.write("Insira os dados:")
                                juros_va_input = st.number_input("Taxa de juros (%):", min_value=0.0, value=st.session_state.get('juros2', 0.0), key="input_juros1")
                                valor_nominal_input = st.number_input("Valor nominal:", min_value=0.0, value=st.session_state.get('valor nominal', 0.0), key="input_valor_nominal1")
                                prazo2_input = st.number_input("Prazo:", min_value=0.0, value=st.session_state.get('prazo2', 0.0), key="input_prazo1")     
                                if (juros_va_input == 0 or prazo2_input == 0 or valor_nominal_input == 0):
                                    st.error('Por favor insira um valor válido e diferente de zero!')
                                else:                           
                                    juros_decimal = juros_va_input / 100
                                    st.session_state.juros2 = juros_va_input
                                    st.session_state.valor_nominal = valor_nominal_input
                                    st.session_state.prazo2 = prazo2_input
                                    if st.button("Calcular", key = "btn_vajs"):
                                        #PROCESSAMENTO 
                                        st.session_state.valor_atual_calculado = valor_nominal_input / (1 + (juros_decimal * prazo2_input))                
                                        with st.expander("Resultado"):
                                            #SAIDA
                                            st.metric(label = 'Valor Atual', value = f"R${st.session_state.valor_atual_calculado:,.2f}")
                            case 'Taxa de juros':
                                st.write("Insira os dados:")
                                valor_atual_input = st.number_input("Valor atual:", min_value=0.0, value=st.session_state.get('valor atual',0.0), key="input_valor_atual2")
                                valor_nominal_input = st.number_input("Valor nominal:", min_value=0.0, value=st.session_state.get('valor nominal', 0.0), key="input_valor_nominal2")
                                prazo2_input = st.number_input("Prazo:", min_value=0.0, value=st.session_state.get('prazo', 0.0), key="input_prazo3")     
                                if (valor_atual_input == 0 or prazo2_input == 0 or valor_nominal_input == 0):
                                    st.error('Por favor insira um valor válido e diferente de zero!')
                                else:                           
                                    st.session_state.valor_atual = valor_atual_input
                                    st.session_state.valor_nominal = valor_nominal_input
                                    st.session_state.prazo2 = prazo2_input
                                    if st.button("Calcular", key = "btn_vnvajs"):
                                        #PROCESSAMENTO 
                                        st.session_state.taxa_calculada = (((valor_nominal_input / valor_atual_input) - 1) / prazo2_input) * 100           
                                        with st.expander("Resultado"):
                                            #SAIDA
                                            st.metric(label = 'Juros', value = f"{st.session_state.juros:,.2f}% ao período")
                            case 'Prazo':
                                st.write("Insira os dados:")
                                valor_atual_input = st.number_input("Valor atual:", min_value=0.0, value=st.session_state.get('valor atual',0.0), key="input_valor_atual4")
                                valor_nominal_input = st.number_input("Valor nominal:", min_value=0.0, value=st.session_state.get('valor nominal', 0.0), key="input_valor_nominal4")
                                juros2_input = st.number_input("Taxa de juros (%):", min_value=0.0, value=st.session_state.get('juros2', 0.0), key="input_juros4")     
                                if (valor_atual_input == 0 or juros2_input == 0 or valor_nominal_input == 0):
                                    st.error('Por favor insira um valor válido e diferente de zero!')
                                else:                           
                                    st.session_state.valor_atual = valor_atual_input
                                    st.session_state.valor_nominal = valor_nominal_input
                                    st.session_state.juros2 = juros2_input
                                    if st.button("Calcular", key = "btn_vnvajs"):
                                        #PROCESSAMENTO 
                                        st.session_state.prazo_calculado = ((valor_nominal_input / valor_atual_input) - 1) / juros_decimal                        
                                        with st.expander("Resultado"):
                                            #SAIDA
                                            st.metric(label = 'Prazo', value = f"{st.session_state.prazo_calculado:,.2f}")
            case 'Descontos Simples':
                match st.session_state.opcoes2:
                    case 'Desconto comercial':
                        lista_desconto = ['Desconto', 'Valor líquido/descontado', 'Taxa Efetiva de Juros']
                        #D = Ndn
                        #Vd = N − D
                        st.session_state.opcoes3 = st.selectbox('Escolha o que deseja calcular:', lista_desconto)
                        match st.session_state.opcoes3:
                            case 'Desconto':
                                st.subheader('Desconto')
                                st.markdown("---")
                                st.warning("Fórmula: D = Ndn")
                                capital_input = st.number_input("Capital:", min_value=0.00, value=st.session_state.get('capital', 0.0), key="input_capital")
                                prazo_input = st.number_input("Prazo:", min_value=0.00, value=st.session_state.get('prazo', 0.0), key="input_prazo")
                                taxa_desconto_input = st.number_input("Taxa de desconto:", min_value=0.00, value=st.session_state.get('juros',0.0), key="input_desconto_taxa")
                                st.warning('O prazo deve estar no mesmo período que a taxa de juros.')
                                
                                if (capital_input == 0 or prazo_input == 0 or taxa_desconto_input == 0):
                                    st.error('Por favor insira um valor válido e diferente de zero!')
                                else:
                                    st.session_state.capital = capital_input
                                    st.session_state.prazo = prazo_input
                                    st.session_state.taxa_desconto = taxa_desconto_input
                                if st.button("Calcular", key = "desconto"):
                                    st.session_state.desconto = (capital_input * prazo_input * taxa_desconto_input/100)
                                    with st.expander("Resultado"):
                                        st.metric(label = 'Desconto', value = f"R$ {st.session_state.desconto:,.2f}") 
                            case 'Valor líquido/descontado':
                                st.subheader('Valor líquido / descontado')
                                st.markdown("---")
                                st.warning("Fórmula: Vd = N - Ndn ")
                                capital_input = st.number_input("Capital:", min_value=0.00, value=st.session_state.get('capital', 0.0), key="input_capital")
                                prazo_input = st.number_input("Prazo:", min_value=0.00, value=st.session_state.get('prazo', 0.0), key="input_prazo")
                                taxa_desconto_input = st.number_input("Taxa de desconto:", min_value=0.00, value=st.session_state.get('juros',0.0), key="input_desconto_taxa")
                                st.warning('O prazo deve estar no mesmo período que a taxa de juros.')
                                
                                if (capital_input == 0 or prazo_input == 0 or taxa_desconto_input == 0):
                                    st.error('Por favor insira um valor válido e diferente de zero!')
                                else:
                                    st.session_state.capital = capital_input
                                    st.session_state.prazo = prazo_input
                                    st.session_state.taxa_desconto = taxa_desconto_input
                                if st.button("Calcular", key = "desconto"):
                                    st.session_state.valor_desconto = capital_input - (capital_input * prazo_input * taxa_desconto_input/100)
                                    with st.expander("Resultado"):
                                        st.metric(label = 'Valor Descontado', value = f"R$ {st.session_state.valor_desconto:,.2f}")
                            case 'Taxa Efetiva de Juros':
                                st.subheader('Taxa efetiva de juros')
                                st.markdown("---")
                                capital_input = st.number_input("Capital:", min_value=0.00, value=st.session_state.get('capital', 0.0), key="input_capital")
                                valor_desconto_input = st.number_input("Valor descontado:", min_value=0.00, value=st.session_state.get('valor desconto', 0.0), key="input_valor_desconto")
                                                               
                                if (capital_input == 0 or valor_desconto_input == 0):
                                    st.error('Por favor insira um valor válido e diferente de zero!')
                                else:
                                    st.session_state.capital = capital_input
                                    st.session_state.valor_desconto = valor_desconto_input
                                if st.button("Calcular", key = "taxa_efetiva"):
                                    st.session_state.taxa_efetiva = (((capital_input /valor_desconto_input) - 1) * 100)
                                    with st.expander("Resultado"):
                                        st.metric(label = 'Taxa efetiva de juros', value = f"{st.session_state.taxa_efetiva:,.2f}% a.p.")
                    case 'Taxa de desconto X Taxa de juros':
                        st.subheader('Taxa de desconto x Taxa de juros')
                        st.markdown("---")
                        lista_desconto_taxa = ['taxa de desconto', 'taxa mensal de juros simples']
                        st.session_state.opcao4 = st.selectbox("Escolha qual variável achar", lista_desconto_taxa)
                        if st.session_state.opcao4 == 'taxa de desconto': 
                            st.warning("Fórmula: d = i/(1 + in)")
                            taxa_mensal_input = st.number_input("Taxa Mensal/Efetiva de Juros Simples:", min_value=0.00, value=st.session_state.get('taxa_mensal_efetiva', 0.0), key="input_tem")
                            prazo_input = st.number_input("Prazo", min_value=0.00, value=st.session_state.get('prazo', 0.0), key="input_prazo")                              
                            if (prazo_input == 0 or taxa_mensal_input == 0):
                                st.error('Por favor insira um valor válido e diferente de zero!')
                            else:
                                st.session_state.taxa_mensal_efetiva = taxa_mensal_input
                                st.session_state.prazo = prazo_input
                            if st.button("Calcular", key = "taxa_desconto"):
                                st.session_state.taxa_desconto = taxa_mensal_input / (1 + taxa_mensal_input * prazo_input)
                                with st.expander("Resultado"):
                                    st.metric(label = 'Taxa de desconto', value = f"{st.session_state.taxa_desconto:,.2f}% a.p.")        
                        if st.session_state.opcao4 == 'taxa mensal de juros simples':
                            st.warning("Fórmula: i = d / ( 1 - dn)")
                            taxa_desconto_input = st.number_input("Taxa de desconto:", min_value=0.00, value=st.session_state.get('desconto', 0.0), key="input_taxa_desconto")
                            prazo_input = st.number_input("Prazo", min_value=0.00, value=st.session_state.get('prazo', 0.0), key="input_prazo")                              
                            if (prazo_input == 0 or taxa_desconto_input == 0):
                                st.error('Por favor insira um valor válido e diferente de zero!')
                            else:
                                st.session_state.taxa_desconto = taxa_desconto_input
                                st.session_state.prazo = prazo_input
                            if st.button("Calcular", key = "taxa_mensal"):
                                st.session_state.taxa_mensal = taxa_desconto_input / (1 - taxa_desconto_input * prazo_input)
                                with st.expander("Resultado"):
                                    st.metric(label = 'Taxa de juros efetiva', value = f"{st.session_state.taxa_mensal:,.2f}% a.p.") 
            case 'Juros Compostos':
                match st.session_state.opcoes2:
                    case 'Juros Compostos':
                        st.subheader("Determine a variável a ser calculada:")
                        lista_jc_jc = ['Montante', 'Capital', 'Taxa de Juros', 'Prazo']
                        # Adicionei uma key única para o selectbox para segurança
                        opcao_selecionada = st.selectbox(" ", lista_jc_jc, key="jc_opcao_selecionada")
                        st.markdown("---")
                        match opcao_selecionada:
                            case 'Montante':
                                # ENTRADAS
                                st.write("Insira os dados para calcular o Montante:")
                                # Adicionei sufixos para tornar as chaves únicas
                                capital_input = st.number_input("Capital:", min_value=0.0, format="%.2f", key="montante_input_capital1_jc")
                                prazo_input = st.number_input("Prazo:", min_value=0.0, format="%.2f", key="montante_input_prazo1_jc")
                                juros_input = st.number_input("Taxa de Juros (%):", min_value=0.0, format="%.2f", key="montante_input_juros1_jc")
                                st.warning("O período da taxa deve ser compatível com o prazo!")

                                if st.button("Calcular", key="montante_btn_calcular_jc"):
                                    if (capital_input == 0 or prazo_input == 0 or juros_input == 0):
                                        st.error('Por favor insira um valor válido e diferente de zero!')
                                    else:
                                        # PROCESSAMENTO
                                        montante_calculado = capital_input * ((1 + (juros_input / 100))**prazo_input)
                                        with st.expander("Resultado", expanded=True):
                                            # SAIDA
                                            st.metric(label='Montante', value=f"R$ {montante_calculado:,.2f}")

                            case 'Capital':
                                # ENTRADAS
                                st.write("Insira os dados para calcular o Capital:")
                                montante_input = st.number_input("Montante:", min_value=0.0, format="%.2f", key="capital_input_montante2_jc")
                                juros_input = st.number_input("Taxa de Juros (%):", min_value=0.0, format="%.2f", key="capital_input_juros2_jc")
                                prazo_input = st.number_input("Prazo:", min_value=0.0, format="%.2f", key="capital_input_prazo2_jc")
                                st.warning("O período da taxa deve ser compatível com o prazo!")

                                if st.button("Calcular", key="capital_btn_calcular_jc"):
                                    if (montante_input == 0 or prazo_input == 0 or juros_input == 0):
                                        st.error('Por favor insira um valor válido e diferente de zero!')
                                    else:
                                        # PROCESSAMENTO
                                        capital_calculado = montante_input / ((1 + (juros_input / 100)) ** prazo_input)
                                        with st.expander("Resultado", expanded=True):
                                            # SAIDA
                                            st.metric(label='Capital', value=f"R$ {capital_calculado:,.2f}")

                            case 'Taxa de Juros':
                                # ENTRADAS
                                st.write("Insira os dados para calcular a Taxa de Juros:")
                                montante_input = st.number_input("Montante:", min_value=0.0, format="%.2f", key="juros_input_montante3")
                                capital_input = st.number_input("Capital:", min_value=0.0, format="%.2f", key="juros_input_capital3")
                                prazo_input = st.number_input("Prazo:", min_value=0.0, format="%.2f", key="juros_input_prazo3")
                                st.warning("O período da taxa será compatível com o prazo!")

                                if st.button("Calcular", key="juros_btn_calcular"):
                                    if (capital_input == 0 or prazo_input == 0 or montante_input == 0):
                                        st.error('Por favor insira um valor válido e diferente de zero!')
                                    else:
                                        # PROCESSAMENTO (Fórmula corrigida para retornar a taxa em %)
                                        juros_calculado = (((montante_input / capital_input)** prazo_input) - 1) * 100
                                        with st.expander("Resultado", expanded=True):
                                            # SAIDA
                                            st.metric(label='Taxa de Juros', value=f"{juros_calculado:,.2f}%")

                            case 'Prazo':
                                # ENTRADAS
                                st.write("Insira os dados para calcular o Prazo:")
                                montante_input = st.number_input("Montante:", min_value=0.0, format="%.2f", key="prazo_input_montante4_jc")
                                capital_input = st.number_input("Capital:", min_value=0.0, format="%.2f", key="prazo_input_capital4_jc")
                                juros_input = st.number_input("Taxa de Juros (%):", min_value=0.0, format="%.2f", key="prazo_input_juros4_jc")
                                st.warning("O prazo será compatível com o período da taxa!")
                                
                                if st.button("Calcular", key="prazo_btn_calcular_jc"):
                                    if (capital_input == 0 or montante_input == 0 or juros_input == 0):
                                        st.error('Por favor insira um valor válido e diferente de zero!')
                                    else:
                                        # PROCESSAMENTO (Fórmula corrigida para usar a taxa como decimal)
                                        taxa_decimal = juros_input / 100
                                        prazo_calculado = (math.log(montante_input / capital_input))/ (math.log(1 + taxa_decimal))
                                        with st.expander("Resultado", expanded=True):
                                            # SAIDA
                                            st.metric(label='Prazo', value=f"{prazo_calculado:,.2f}")
                    case 'Períodos Não Inteiros':
                        st.subheader('Período Não Inteiro')
                    case 'Taxas Equivalentes':
                        st.subheader('Taxas equivalentes')
                    case 'CDB e RCB':
                        st.subheader("CDB e RCB")
                    


            #case 'Taxa Real de Juros':                      

def tela_est():  #DESENVOLVIDO
    st.title('Simulador Estatístico')
    st.subheader('Insira seus dados e selecione as análises desejadas', divider='orange')
    #inputs aqui
    st.markdown("#### 1. Insira sua amostra de dados") 
    df = pd.DataFrame({
        "X": [500.0, None, None],
        "Y": [None, None, None]})
    st.warning("_A coluna Y é opcional. Se não for usar, deixe em branco._")
    edited_df = st.data_editor(df, num_rows="dynamic")

    lista_est = ['Somatório', 
                 'Produtório', 
                 'Média Aritmética',
                 'Média Ponderada',
                 'Mediana', 
                 'Amplitude', 
                 'Variância', 
                 'Desvio Padrão', 
                 'Coeficiente de Variação', 
                 'Quartis', 
                 'Coeficiente de Correlação de Pearson (r)', 
                 'Frequência Absoluta', 
                 'Frequência Relativa']
    st.markdown("#### 2. Selecione os cálculos")
    opcoes = st.multiselect("Escolha uma ou mais análises estatísticas para calcular:", lista_est)
    
    if st.button('Calcular'):
        #limpeza
        col_x = pd.to_numeric(edited_df["X"], errors="coerce").dropna()
        col_y = pd.to_numeric(edited_df["Y"], errors="coerce").dropna()  #pedi ajuda pro chat gpt ajudar a limpar
        if col_x.empty:
            st.error("⚠️ Você precisa preencher ao menos um número válido na coluna X.")
            return
        st.markdown("### Resultados:")
        if "Somatório" in opcoes:
            with st.expander("Somatórios:"):
                st.metric(f"Somatório X:", f"{col_x.sum():.2f}")
                st.metric(f"Somatório X²:", f"{(col_x**2).sum():.2f}")
                if not col_y.empty:
                    st.metric(f"Somatório Y:", f"{col_y.sum():.2f}")
                    st.metric(f"Somatório Y²:", f"{(col_y**2).sum():.2f}")
                    st.metric(f"Somatório XY:", f"{(col_y * col_x).sum():.2f}")
        if "Produtório" in opcoes:
            with st.expander("Produtórios:"):
                st.metric(f"Produtório X:", f"{math.prod(col_x):.2f}")
                st.metric(f"Produtório X²:", f"{math.prod(col_x**2):.2f}")
                if not col_y.empty:
                    st.metric(f"Produtório Y:", f"{math.prod(col_y):.2f}")
                    st.metric(f"Produtório Y²:", f"{math.prod(col_y**2):.2f}")
                    st.metric(f"Produtório de XY:", f"{math.prod(col_x * col_y):.2f}")
        if "Média Aritmética" in opcoes:
            with st.expander("Médias Aritméticas:"):
                n_x = len(col_x)
                st.metric(f"Média Aritmética de X:", f"{col_x.mean():.2f}")
                if not col_y.empty:
                    n_y = len(col_y)
                    st.metric(f"Média Aritmética de Y:", f"{col_y.mean():.2f}")
                    st.metric(f"Média Aritmética de X + Y:", f"{((col_y.sum() + col_x.sum())/(n_y + n_x)):.2f}")
        if "Média Ponderada" in opcoes:
            with st.expander('Média Ponderada'):
                if col_y.empty:
                    st.error("Utiliza-se X como valor e Y como peso")
                if not col_y.empty:
                    st.metric(f"Média Ponderada de X com peso Y:", f"{(((col_y * col_x).sum())/(col_y).sum()):.2f}")
        if "Mediana" in opcoes:
            with st.expander("Medianas"):
                st.metric(f"Mediana X:", f"{col_x.median():.2f}")
                if not col_y.empty:
                    st.metric(f"Mediana Y:", f"{col_y.median():.2f}")
        if "Amplitude" in opcoes:
            with st.expander("Amplitude"):
                amplitudex = col_x.max() - col_x.min()
                st.metric(f"Amplitude de X:", f"{amplitudex:.2f}")
                if not col_y.empty:
                    amplitudey = col_y.max() - col_y.min()
                    st.metric(f"Amplitude de Y:", f"{amplitudey:.2f}")
        if "Variância" in opcoes:
             with st.expander("Variâncias"):
                st.metric(f"Variância Amostral de X:", f"{col_x.var():.2f}")
                st.metric(f"Variância Populacional de X:", f"{col_x.var(ddof=0):.2f}")
                if not col_y.empty:
                    st.metric(f"Variância Amostral de Y", f"{col_y.var():.2f}")
                    st.metric(f"Variância Populacional de Y", f"{col_y.var(ddof=0):.2f}")
        if 'Desvio Padrão' in opcoes:
            with st.expander("Desvio Padrão:"):
                st.metric("Desvio Padrão Amostral de X", f"{col_x.std():.2f}")
                st.metric("Desvio Padrão Populacional de X", f"{col_x.std(ddof=0):.2f}")
                if not col_y.empty:
                    st.metric("Desvio Padrão Amostral de Y", f"{col_y.std():.2f}")
                    st.metric("Desvio Padrão Populacional de Y", f"{col_y.std(ddof=0):.2f}")
        if "Coeficiente de Variação" in opcoes:
            with st.expander("Coeficientes de Variação (%)"):  #desvio padrão dividido pela media * 100
                cv_x = (col_x.std() / col_x.mean()) * 100
                st.metric(f"CV de X", f"{cv_x:.2f}%")
                if not col_y.empty and col_y.mean() != 0:   #nao pode ter divisão por zero
                    cv_y = (col_y.std() / col_y.mean()) * 100
                    st.metric(f"CV de Y", f"{cv_y:.2f}%")
        if "Quartis" in opcoes:
            with st.expander("Quartis"):
                st.metric(f"Primeiro Quartil(Q1) de X", f"{col_x.quantile(0.25):.2f}")
                st.metric(f"Segundo Quartil(Q2)/Mediana de X", f"{col_x.quantile(0.50):.2f}")
                st.metric(f"Terceiro Quartil(Q3) de X", f"{col_x.quantile(0.75):.2f}")
                st.metric(f"Amplitude Interquartil (IQR = Q3 - Q1) de X", f"{(col_x.quantile(0.75) - col_x.quantile(0.25)) :.2f}")
                if not col_y.empty:
                    st.metric(f"Primeiro Quartil(Q1) de Y", f"{col_y.quantile(0.25):.2f}")
                    st.metric(f"Segundo Quartil(Q2)/Mediana de Y", f"{col_y.quantile(0.50):.2f}")
                    st.metric(f"Terceiro Quartil(Q3) de Y", f"{col_y.quantile(0.75):.2f}")
                    st.metric(f"Amplitude Interquartil (IQR = Q3 - Q1) de Y", value=f"{(col_y.quantile(0.75) - col_y.quantile(0.25)) :.2f}")
        if "Coeficiente de Correlação de Pearson (r)" in opcoes:
            with st.expander("Coeficiente de Correlação de Pearson (r)"):
                if col_y.empty:
                    st.warning("Por favor preencha os dados da coluna Y para obter o R!")
                if not col_y.empty:
                    st.metric(f"(r):", (col_x.corr(col_y)) )
        if "Frequência Absoluta" in opcoes:
            with st.expander("Frequência Absoluta"):
                st.write("Contagem de cada valor de X:")
                freq_abs_x = col_x.value_counts().reset_index()
                freq_abs_x.columns = ['Valor', 'Frequência'] #era isso que eu pedi ajuda pro chat gpt, em relação a como mudar o nome das colunas
                st.dataframe(freq_abs_x, use_container_width=True) 
                #st.dataframe(col_x.value_counts().reset_index())   #eu tinha feito assim, mas pedi ajuda pro chat gpt sobre como deixar a tabela mais bonita, então considerei o codigo bonito
                if not col_y.empty:
                    st.write("Contagem de cada valor de Y:")
                    freq_abs_x = col_x.value_counts().reset_index()
                    freq_abs_x.columns = ['Valor', 'Frequência']
                    st.dataframe(freq_abs_x, use_container_width=True)
        if "Frequência Relativa" in opcoes:
            with st.expander("Frequência relativa"):
                st.write("Porcentagem de cada valor em X:")
                #usa normalize=True para obter a proporção
                freq_rel_x = col_x.value_counts(normalize=True).reset_index()
                freq_rel_x.columns = ['Valor', 'Frequência (%)']
                #multiplica por 100 e formata para exibição
                freq_rel_x['Frequência (%)'] *= 100
                st.dataframe(freq_rel_x.style.format({'Frequência (%)': '{:.2f}%'}),use_container_width=True)
                if not col_y.empty:
                    st.write("Porcentagem de cada valor em Y:")
                    freq_rel_y = col_y.value_counts(normalize=True).reset_index()
                    freq_rel_y.columns = ['Valor', 'Frequência (%)']
                    freq_rel_y['Frequência (%)'] *= 100
                    st.dataframe(freq_rel_y.style.format({'Frequência (%)': '{:.2f}%'}), use_container_width=True)

    st.markdown("---")

    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_conv():   #DESENVOLVIDO
    st.title('Conversor de Moeda💲')
    st.subheader('Converta para mais de 13 moedas!')
    taxas_em_usd = obter_taxas()
    if len(taxas_em_usd) <= 1:
        st.warning("Não foi possível obter as taxas de câmbio. Tente novamente mais tarde.")
        return
    #armazenando as moedas #via chat gpt
    # moedas suportadas pela nova API (pegas em https://www.frankfurter.app/docs/#section/Supported-currencies)
    nomes_moedas = {
        "USD": "Dólar (USD)",
        "EUR": "Euro (EUR)",
        "BRL": "Real (BRL)",
        "GBP": "Libra Esterlina (GBP)",
        "JPY": "Iene Japonês (JPY)",
        "AUD": "Dólar Australiano (AUD)",
        "CAD": "Dólar Canadense (CAD)",
        "CHF": "Franco Suíço (CHF)",
        "CNY": "Yuan Chinês (CNY)",
        "MXN": "Peso Mexicano (MXN)",
        "NOK": "Coroa Norueguesa (NOK)",
        "INR": "Rupia Indiana (INR)",
        "KRW": "Won Sul-Coreano (KRW)",
        "HKD": "Dólar de Hong Kong (HKD)",
        "SGD": "Dólar de Singapura (SGD)",
    }

    moedas = list(nomes_moedas.values())
    siglas = list(nomes_moedas.keys())

    #inputs
    valor1 = st.number_input("Valor:")
    opcaomoeda1 = st.selectbox("Converter de:", moedas)
    opcaomoeda2 = st.selectbox("Para:", moedas)
    
    #divide em duas colunas o frame
    col1, col2 = st.columns(2)

     # Carrega taxas atualizadas
    taxas_em_usd = obter_taxas()
    resultado = None

    with col1:
        if st.button("Voltar"):
            st.session_state.tela = 'menu'
    with col2:
        if st.button("▶️Converter"):
            try: #tratamento de erro né, vamos mexer com divisão, vai dar erro se for zero
                # Converte o valor para USD e depois para a moeda destino
                sigla1 = siglas[moedas.index(opcaomoeda1)]
                sigla2 = siglas[moedas.index(opcaomoeda2)]
                valor_em_usd = valor1 / taxas_em_usd[sigla1]
                resultado = valor_em_usd * taxas_em_usd[sigla2]
                st.success(f'{valor1:.2f} {sigla1} ≈ {resultado:.2f} {sigla2}')
            except ZeroDivisionError:
                st.error("Erro: Divisão por zero nas taxas.")
            except Exception as e:
                st.error(f"Erro inesperado: {e}")   

def tela_sobre(): #DESENVOLVIDO
    st.header(':orange[Sobre o Projeto]')
    with st.expander('Comentário da desenvolvedora'):
        st.write('🔹 O projeto foi desenvolvido inteiramente em Python, após a desenvolvedora ter aulas de Python como eletiva na Universidade Federal de Juiz de Fora - Campus Governador Valadares.')
        st.write('🔹 Muitas vezes há uma necessidade dos alunos conferirem as respostas de um exercício simples, tanto quanto os professores também em confirmar o gabarito das listas de exercício')
        st.write('🔹 Dessa forma, esse projeto veio como uma ferramenta para auxiliar quaisquer pessoas que precisem dos cálculos econômicos, conversor de moedas, ferramentas rápidas e práticas...')
        st.write('🔹 É óbvio que pretendo expandir esse aplicativo ao máximo, adicionar outras bibliotecas, fazer com que a maior parte dos cálculos econômicos e vivências desse curso possam ser calculadas aqui')
        st.write('🔹 Porém será uma longa jornada de erros, raivas e desafios, e acima de tudo: empenho!')
        st.markdown('---')
        st.caption('Detalhe: apenas 10% do projeto foi utilizado com auxílio de IA. Apenas para ajuda com integração de API, tratamentos básicos de erros e caminhos para auxiliar e garantir que a lógica da programação seja a melhor possível')
    if st.button('Voltar ao Menu'):
            st.session_state.tela = 'menu'    

# Menu (main)
def main(): #DESENVOLVIDO
    if 'tela' not in st.session_state:
        st.session_state.tela = 'menu'

    match st.session_state.tela:
        case 'menu':
            opcoes_menu()
        case 'macro':
            tela_macro()
        case 'micro':
            tela_micro()
        case 'fin':
            tela_fin()
        case 'est':
            tela_est()
        case 'conv':
            tela_conv()

#loop 
if __name__ == "__main__":
    main()
