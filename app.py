import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np 
import math

st.set_page_config(
    page_title="Fórmula Econômica",
    page_icon="logo.square.png",
    layout="wide"
)

#tela inicial 
def opcoes_menu():  #feito
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
def tela_macro(): #feito
    st.title('Simulador Macroeconômico')
    st.subheader('Simule e analise os principais indicadores da economia', divider = True)

    opcao = st.selectbox("Escolha uma operação:", 
                         ["Cálculo PIB", "Índice de Preços, Quantidade e Inflação", "Crescimento Econômico"])

    if st.button("Avançar"):
        if opcao == "Cálculo PIB":
            st.session_state.tela = 'pib'
        elif opcao == "Índice de Preços e Inflação":
            st.session_state.tela = 'indices'
        elif opcao == "Crescimento Econômico":
            st.session_state.tela = 'crescimento'
#eu utilizo dois ifs pois dentro da biblioteca streamlit há mt disso de associar if e elif a botões DEPENDENTES, o que ferra o processo. preciso que cada botão seja independente sabe?
    if st.button("Voltar ao Menu Principal"):
        st.session_state.tela = 'menu'

#opcoes do selectbox macroeconômico, criam outras telas dentro:
def tela_PIB(): #feito
    st.title("Cálculo do PIB")
    if 'pib_etapa1_ok' not in st.session_state:
        st.session_state.pib_etapa1_ok = False
    if 'pib_opcao' not in st.session_state:
        st.session_state.pib_opcao = None

    #ETAPA 1: SELECIONAR O QUE DESEJA CALCULAR
    if not st.session_state.pib_etapa1_ok:
        opcao_PIB = st.selectbox("Selecione o modo que deseja calcular o PIB:", ['PIB Real, Nominal e Deflator', 'PIB pela Demanda', 'PIB pela Oferta', 'PIB pela Renda'])

    if st.button("Avançar"):
        st.session_state.pib_opcao = opcao_PIB
        st.session_state.pib_etapa1_ok = True

        if opcao_PIB == 'PIB Real, Nominal e Deflator':
            st.session_state.tela = 'pib_nom_real_defl'
        elif opcao_PIB == 'PIB pela Demanda':
            st.session_state.tela = 'pib_demanda'
        elif opcao_PIB == 'PIB pela Oferta':
            st.session_state.tela = 'pib_oferta'
        elif opcao_PIB == 'PIB pela Renda':
            st.session_state.tela = 'pib_renda'
            
    if st.button("Voltar para Macroeconômico"):
        st.session_state.tela = 'macro'

#funções dentro da tela do pib   
def tela_PIBS_nom_real_defl():  #Preciso apenas refinar, corrigir, foi o primeiro que eu fiz
    st.title('Calcule aqui os PIBs reais, nominais e deflator do PIB')

    #percebi que msm com um botao avançar, não havia um controle para determinar se o usuário acabou ou não, dava muuuito erro
    #então pedi ajuda pro chatgpt aqui:

    # Controle para mostrar os inputs depois do clique
    if 'pib_produtos_ok' not in st.session_state:
        st.session_state.pib_produtos_ok = False
    if 'qtd_produtos' not in st.session_state:
        st.session_state.qtd_produtos = None

    #selectbox para selecionar a quantidade pra calcular, deixei só 2 a 4 produtos mesmo viu, esse é a versão demo, depois eu expando!
    produtos = st.selectbox('indique a quantidade de produtos que deseja calcular:', ['2 produtos', '3 produtos', '4 produtos'])
    
    if st.button("Avançar"):
        st.session_state.pib_produtos_ok = True
        st.session_state.qtd_produtos = produtos
    # para mostrar que ta ok e pode continuar!

    if st.button("Voltar para Cálculo do PIB"):
        st.session_state.tela = 'pib'
       #volta para a outra tela do pib lá
     
    if st.session_state.pib_produtos_ok:
        produtos = st.session_state.qtd_produtos

    #os ifs estão assim pq pra mostrar independência ok?

        if produtos == '2 produtos':
            st.warning('Produtos no ANO BASE')
            preco_base_1 = st.number_input('Preço do 1° produto no ANO BASE: ')
            quantidade_base_1 = st.number_input('Quantidade do 1° produto no ANO BASE:')
            preco_base_2 = st.number_input('Preço do 2° produto no ANO BASE:')
            quantidade_base_2 = st.number_input('Quantidade do 2° produto no ANO BASE:')
            st.warning('Produtos no ANO ATUAL')
            preco_atual_1 = st.number_input('Preço do 1° produto no ANO ATUAL: ')
            quantidade_atual_1 = st.number_input('Quantidade do 1° produto no ANO ATUAL:')
            preco_atual_2 = st.number_input('Preço do 2° produto no ANO ATUAL: ')
            quantidade_atual_2 = st.number_input('Quantidade do 2° produto no ANO ATUAL:')

            if st.button('Calcular'):
                pib_real = 100 * ((quantidade_atual_1 * preco_base_1 + quantidade_atual_2 * preco_base_2 )/(quantidade_base_1 * preco_base_1 + quantidade_base_2 * preco_base_2))
                pib_nominal = ((preco_atual_1 * quantidade_atual_1 + preco_atual_2 * quantidade_atual_2))
                deflator_pib = 100 * ((quantidade_atual_1 * preco_atual_1 + quantidade_atual_2 * preco_atual_2)/(preco_atual_1 *quantidade_base_1 + preco_atual_2 * quantidade_base_2))
                with st.expander("Resultados do PIB"):
                        st.write(f"O crescimento do PIB Real (Laspeyres de Quantidade): {pib_real:.4f}%")
                        st.write(f"PIB Nominal: {pib_nominal:4f}")
                        st.write(f"Deflator do PIB (Paasche de Quantidade): {deflator_pib:.5f} %")

        elif produtos == '3 produtos':
            st.warning('Produtos no ANO BASE')
            preco_base_1 = st.number_input('Preço do 1° produto no ANO BASE: ')
            quantidade_base_1 = st.number_input('Quantidade do 1° produto no ANO BASE:')
            preco_base_2 = st.number_input('Preço do 2° produto no ANO BASE:')
            quantidade_base_2 = st.number_input('Quantidade do 2° produto no ANO BASE:')
            preco_base_3 = st.number_input('Preço do 3° produto no ANO BASE:')
            quantidade_base_3 = st.number_input('Quantidade do 3° produto no ANO BASE:')
            st.warning('Produtos no ANO ATUAL')
            preco_atual_1 = st.number_input('Preço do 1° produto no ANO ATUAL: ')
            quantidade_atual_1 = st.number_input('Quantidade do 1° produto no ANO ATUAL:')
            preco_atual_2 = st.number_input('Preço do 2° produto no ANO ATUAL: ')
            quantidade_atual_2 = st.number_input('Quantidade do 2° produto no ANO ATUAL:')
            preco_atual_3 = st.number_input('Preço do 3° produto no ANO ATUAL: ')
            quantidade_atual_3 = st.number_input('Quantidade do 3° produto no ANO ATUAL:')
            
            if st.button('Calcular'):
                pib_real = 100 * (((quantidade_atual_1 * preco_base_1 + quantidade_atual_2 * preco_base_2 + quantidade_atual_3 * preco_base_3  )/(quantidade_base_1 * preco_base_1 + quantidade_base_2 * preco_base_2 + quantidade_base_3 * preco_base_3)))
                pib_nominal = ((preco_atual_1 * quantidade_atual_1 + preco_atual_2 * quantidade_atual_2 + preco_atual_3 * quantidade_atual_3))
                deflator_pib = (100 * ((quantidade_atual_1 * preco_atual_1 + quantidade_atual_2 * preco_atual_2 + quantidade_atual_3 * preco_atual_3)/(preco_atual_1 *quantidade_base_1 + preco_atual_2 * quantidade_base_2 + preco_atual_3 * quantidade_base_3)))
                with st.expander("Resultados do PIB"):
                    st.write(f"O crescimento do PIB Real (Laspeyres de Quantidade): {pib_real:.4f}%")
                    st.write(f"PIB Nominal: {pib_nominal:4f}")
                    st.write(f"Deflator do PIB (Paasche de Quantidade): {deflator_pib:.5f} %")


        elif produtos == '4 produtos':
            st.warning('Produtos no ANO BASE')
            preco_base_1 = st.number_input('Digite o preço do 1° produto no ANO BASE: ')
            quantidade_base_1 = st.number_input('Digite a quantidade do 1° produto no ANO BASE:')
            preco_base_2 = st.number_input('Digite o preço do 2° produto no ANO BASE:')
            quantidade_base_2 = st.number_input('Digite a quantidade do 2° produto no ANO BASE:')
            preco_base_3 = st.number_input('Digite o preço do 3° produto no ANO BASE:')
            quantidade_base_3 = st.number_input('Digite a quantidade do 3° produto no ANO BASE:')
            preco_base_4 = st.number_input('Digite o preço do 4° produto no ANO BASE:')
            quantidade_base_4 = st.number_input('Digite a quantidade do 4° produto no ANO BASE:')
            st.warning('Produtos no ANO ATUAL')
            preco_atual_1 = st.number_input('Digite o preço do 1° produto no ANO ATUAL: ')
            quantidade_atual_1 = st.number_input('Digite a quantidade do 1° produto no ANO ATUAL:')
            preco_atual_2 = st.number_input('Digite o preço do 2° produto no ANO ATUAL: ')
            quantidade_atual_2 = st.number_input('Digite a quantidade do 2° produto no ANO ATUAL:')
            preco_atual_3 = st.number_input('Digite o preço do 3° produto no ANO ATUAL: ')
            quantidade_atual_3 = st.number_input('Digite a quantidade do 3° produto no ANO ATUAL:')
            preco_atual_4 = st.number_input('Digite o preço do 4° produto no ANO ATUAL: ')
            quantidade_atual_4 = st.number_input('Digite a quantidade do 4° produto no ANO ATUAL:')
            
            if st.button('Calcular'):
                pib_real = 100 * (((quantidade_atual_1 * preco_base_1 + quantidade_atual_2 * preco_base_2 + quantidade_atual_3 * preco_base_3 + quantidade_atual_4 * preco_base_4  )/(quantidade_base_1 * preco_base_1 + quantidade_base_2 * preco_base_2 + quantidade_base_3 * preco_base_3 + quantidade_base_4 * preco_base_4 )))
                pib_nominal = ((preco_atual_1 * quantidade_atual_1 + preco_atual_2 * quantidade_atual_2 + preco_atual_3 * quantidade_atual_3 + preco_atual_4 * quantidade_atual_4))
                deflator_pib = (100 * ((quantidade_atual_1 * preco_atual_1 + quantidade_atual_2 * preco_atual_2 + quantidade_atual_3 * preco_atual_3 + quantidade_atual_4 * preco_atual_4)/(preco_atual_1 *quantidade_base_1 + preco_atual_2 * quantidade_base_2 + preco_atual_3 * quantidade_base_3 + preco_atual_4 * quantidade_base_4)))
                with st.expander("Resultados do PIB"):
                    st.write(f"O crescimento do PIB Real (Laspeyres de Quantidade): {pib_real:.4f}%")
                    st.write(f"PIB Nominal: {pib_nominal:4f}")
                    st.write(f"Deflator do PIB (Paasche de Quantidade): {deflator_pib:.5f} %")

def tela_PIB_demanda(): 
    st.warning('EM DESENVOLVIMENTO')
    if st.button("Voltar ao Menu Principal"):
        st.session_state.tela = 'menu'

def tela_PIB_oferta():
    st.warning('EM DESENVOLVIMENTO')
    if st.button("Voltar ao Menu Principal"):
        st.session_state.tela = 'menu'

def tela_PIB_renda():
    st.warning('EM DESENVOLVIMENTO')
    if st.button("Voltar ao Menu Principal"):
        st.session_state.tela = 'menu'

def tela_indices():
    st.title("Índices de Preços e Inflação")
    st.selectbox("Selecione o modo que deseja calcular os Índices: ")

    if st.button("Voltar para Macroeconômico"):
        st.session_state.tela = 'macro'

def tela_crescimento():
    st.title("Crescimento Econômico")
    st.write("Simulação de crescimento com base em dados anuais...")

    if st.button("Voltar para Macroeconômico"):
        st.session_state.tela = 'macro'

@st.cache_data(ttl=86400)  # cache diário (86400 segundos = 24 horas)     #via chat gpt

# Função para obter taxas de câmbio atualizadas via API (via chat gpt ajuda)
def obter_taxas(): #finalizado com api e gpt
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
def tela_micro():  #pretendo integrar MATPLOTLIB para simular os gráficos
    st.title('Simulador Microeconômico')
    st.subheader('Simule aqui suas principais necessidades microeconômicas', divider = True)
    opcao = st.selectbox("Escolha uma operação:", 
                         ["Linha de Restrição Orçamentária", "Curva de indiferença", "Equilíbrio do Consumidor", "Curva de Demanda Individual", "Maximização de Utilidade", "Elasticidades", "Excedente do Consumidor"])
    if st.button("Avançar"):
        if opcao == "Linha de Restrição Orçamentária":
            st.session_state.tela = 'linha_orcamentaria'
        elif opcao == "Curva de indiferença":
            st.session_state.tela = 'curva_indiferenca'
        elif opcao == "Equilíbrio do Consumidor":
            st.session_state.tela = 'equilibrio_consumidor'
        elif opcao == "Curva de Demanda Individual":
            st.session_state.tela = 'curva_demanda_indiv'
        elif opcao == "Maximização de Utilidade":
            st.session_state.tela = 'maximizacao_utilidade'
        elif opcao == "Elasticidades":
            st.session_state.tela = 'elasticidades'
        elif opcao == "Excedente do Consumidor":
            st.session_state.tela = 'excedentes_consumidor'
    st.write('EM CONSTRUÇÃO, VOLTE DEPOIS...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_fin():
    st.title('Simulador Financeiro')
    st.subheader('_Todos os cálculos de Matemática Financeira aqui!_', divider='orange')
    lista_fin = ['Juros Simples', 'Descontos Simples','Juros Compostos','Taxa Real de Juros', 'Equivalência de Capitais', 'Sequências Uniformes e Não Uniformes', 'Amortização']
    opcoes = st.selectbox("Escolha o tópico:", lista_fin)
    if st.button("Avançar"):
        if opcoes == 'Juros Simples':
            st.session_state.tela = 'juros_simples'
        elif opcoes == 'Descontos Simples':
            st.session_state.tela = 'descontos_simples'
        elif opcoes == 'Juros Compostos':
            st.session_state.tela = 'juros_compostos'
        elif opcoes == 'Taxa Real de Juros':
            st.session_state.tela = 'taxa_real'
        elif opcoes == 'Equivalência de Capitais':
            st.session_state.tela = 'equival_capitais'
        elif opcoes == 'Sequências Uniformes e Não Uniformes':
            st.session_state.tela = 'sequencias'
        elif opcoes == 'Amortização':
            st.session_state.tela = 'amortizacao'
            
    st.markdown("---")
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_est():  
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

def tela_conv():   #finalizado
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

def tela_sobre():
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

def tela_juross():
    '''Vamos dividir sua tela_juross() em etapas com controle por variáveis de sessão. Assim:

            Passo a passo:
            Etapa 1: selecionar tipo de cálculo (Juros Simples, Hot Money, etc)

            Etapa 2: selecionar variável a calcular (Montante, Capital, etc)

            Etapa 3: mostrar os inputs'''  #pedi ajuda ao chat gpt pois a tela não estava se fixando ao selecionar os números para input

    # Inicializando estados
    if 'js_etapa1_ok' not in st.session_state:
        st.session_state.js_etapa1_ok = False
    if 'js_etapa2_ok' not in st.session_state:
        st.session_state.js_etapa2_ok = False
    if 'js_tipo' not in st.session_state:
        st.session_state.js_tipo = None
    if 'js_objetivo' not in st.session_state:
        st.session_state.js_objetivo = None

    # Etapa 1: tipo de cálculo
    if not st.session_state.js_etapa1_ok:
        tipo = st.selectbox("Escolha qual opção deseja calcular:", [
                'Juros Simples', 'Taxas Equivalentes', 'Juro Exato', 'Juro Comercial',
                'Operações com Hot Money', 'Valor Nominal', 'Valor Atual' ])
        if st.button("Avançar para escolha da variável"):
            st.session_state.js_tipo = tipo
            st.session_state.js_etapa1_ok = True

    # Etapa 2: o que calcular
    if st.session_state.js_etapa1_ok and not st.session_state.js_etapa2_ok:
        if st.session_state.js_tipo == 'Juros Simples': #coloquei um if aqui para eu fazer posteriormente o código dos outros simuladores, como taxas equivalentes...
            objetivo = st.selectbox("Escolha o que precisa calcular:", ['Montante', 'Capital', 'Juros', 'Prazo'])
            if st.button("Avançar para os dados"):
                st.session_state.js_objetivo = objetivo
                st.session_state.js_etapa2_ok = True    
        else:
            st.warning('EM CONSTRUÇÃO, VOLTE DEPOIS...')
            if st.button("Voltar"):
                st.session_state.tela = 'fin'

    # Etapa 3: mostrar inputs e calcular
    if st.session_state.js_etapa1_ok and st.session_state.js_etapa2_ok:
        st.subheader(f"Cálculo: {st.session_state.js_tipo} - {st.session_state.js_objetivo}")
        if st.session_state.js_objetivo == 'Montante':  # o restante foi desenvolvido por mim
            capital = st.number_input('Capital (C):', min_value=0.0)
            prazo = st.number_input('Prazo (t):', min_value=0.0)
            taxa = st.number_input('Taxa de juros (%):', min_value=0.0)
            if st.button("Calcular Montante"):
                montante = capital * (1 + (prazo * taxa / 100))
                st.metric("Montante (M)", f"R$ {montante:.2f}")

        elif st.session_state.js_objetivo == 'Capital':
            montante = st.number_input('Montante (M):', min_value=0.0)
            prazo = st.number_input('Prazo (t):', min_value=0.0)
            taxa = st.number_input('Taxa de juros (%):', min_value=0.0)
            if st.button("Calcular Capital"):
                capital = montante / (1 + (prazo * taxa / 100))
                st.metric("Capital (C)", f"R$ {capital:.2f}")

        elif st.session_state.js_objetivo == 'Juros':
            montante = st.number_input('Montante (M):', min_value=0.0)
            capital = st.number_input('Capital (C):', min_value=0.0)
            prazo = st.number_input('Prazo (t):', min_value=0.0)
            if st.button("Calcular Juros"):
                if capital > 0 and prazo > 0:
                    taxa = ((montante / capital) - 1)/ prazo
                    st.metric("Taxa de Juros (i)", f"{taxa * 100:.2f}%")
                else: 
                    st.warning("Capital e Prazo devem ser maiores que zero")
        elif st.session_state.js_objetivo == 'Prazo':
            montante = st.number_input('Montante (M):', min_value=0.0)
            capital = st.number_input('Capital (C):', min_value=0.0)
            taxa = st.number_input('Taxa de juros (%):', min_value=0.0)
            if st.button("Calcular Prazo"):
                if capital > 0 and taxa > 0:
                    prazo = ((montante / capital) - 1)/ taxa
                    st.metric("Prazo (n)", f"{prazo:.2f}")
                else: 
                    st.warning("Capital e Taxa devem ser maiores que zero")
    # Botões de voltar
    if st.session_state.js_etapa2_ok:
        if st.button("⬅️ Escolher outra variável"):
            st.session_state.js_etapa2_ok = False

    elif st.session_state.js_etapa1_ok:
        if st.button("⬅️ Escolher outra conta financeira"):
            st.session_state.js_etapa1_ok = False

    if st.button("Menu"):
        st.session_state.tela = 'menu'
                 
def tela_descontos_simples():   #AINDA NÃO DESENVOLVIDO
    st.write('descontos simples')
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_juroscompostos(): #AINDA NÃO DESENVOLVIDO
    st.write('juros compostos')
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_taxa_real(): #AINDA NÃO DESENVOLVIDO
    st.write('taxa real')
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_equivalencia_capitais(): #AINDA NÃO DESENVOLVIDO
    st.write('equivalencia de capitais')
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_sequencias(): #AINDA NÃO DESENVOLVIDO
    st.write('sequencias uniformes e não uniformes')
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_amortizacao(): #AINDA NÃO DESENVOLVIDO
    st.write('amortização')
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_linha_orcamentaria(): #AINDA NÃO DESENVOLVIDO
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_curva_indiferenca(): #AINDA NÃO DESENVOLVIDO
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_equilibrio_consumidor(): #AINDA NÃO DESENVOLVIDO
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_curva_demanda_indiv(): #AINDA NÃO DESENVOLVIDO
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_maximizacao_util(): #AINDA NÃO DESENVOLVIDO
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'
         
def tela_elasticidades(): #AINDA NÃO DESENVOLVIDO
    st.write('EM CONSTRUÇÃO...')
    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_excedente_consumidor(): #AINDA NÃO DESENVOLVIDO
    st.write('EM CONSTRUÇÃO...')
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
        case 'pib':
            tela_PIB()
        case 'indices':
            tela_indices()
        case 'crescimento':
            tela_crescimento()
        case 'micro':
            tela_micro()
        case 'fin':
            tela_fin()
        case 'juros_simples':
            tela_juross()
        case 'descontos_simples':
            tela_descontos_simples()
        case 'juros_compostos':
            tela_juroscompostos()
        case 'taxa_real':
            tela_taxa_real()
        case 'equival_capitais':
            tela_equivalencia_capitais()
        case 'sequencias':
            tela_sequencias()
        case 'amortizacao':
            tela_amortizacao()
        case 'est':
            tela_est()
        case 'conv':
            tela_conv()
        case 'pib_nom_real_defl':
            tela_PIBS_nom_real_defl()
        case 'pib_demanda':
            tela_PIB_demanda()
        case 'pib_oferta':
            tela_PIB_oferta()
        case 'pib_renda':
            tela_PIB_renda()
        case 'sobre':
            tela_sobre()
        case 'linha_orcamentaria':
            tela_linha_orcamentaria()
        case 'curva_indiferenca':
            tela_curva_indiferenca()
        case 'equilibrio_consumidor':
            tela_equilibrio_consumidor()
        case 'curva_demanda_indiv':
            tela_curva_demanda_indiv()
        case 'maximizacao_utilidade':
            tela_maximizacao_util()
        case 'elasticidades':
            tela_elasticidades()
        case 'excedentes_consumidor':
            tela_excedente_consumidor()

#loop 
if __name__ == "__main__":
    main()
