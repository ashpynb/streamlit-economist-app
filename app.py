import streamlit as st
import requests
from datetime import datetime
from PIL import Image



st.set_page_config(
    page_title="Fórmula Econômica",
    page_icon="logo.square.png",
    layout="wide"
)

logo = logo.square.png
#tela inicial 
def opcoes_menu():  #feito
    st.title(logo, ":orange[Fórmula] :orange[Econômica]")
    st.header('_Os melhores simuladores e cálculos econômicos estão aqui!_', divider = 'orange')
    #vou criar uma barra lateral para entrarem em contato, informações complementares e deixar o site bonito!
    with st.sidebar:
        st.sidebar.image("logo.square.png", width=70)
        st.markdown("## 🪙 Bem-vindo!")
        st.markdown(":orange[Fórmula econômica!]")
        st.link_button('Entre em Contato',"https://wa.me/5533998488760?text=Ol%C3%A1%21%20Vim%20pelo%20seu%20site%20F%C3%B3rmula%20Econ%C3%B4mica.%20Gostaria%20de%20mais%20informa%C3%A7%C3%B5es%21")
        st.markdown("---")
        st.caption("Versão 1.0 • 2025")
        st.caption("Todos os direitos reservados")
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
    st.write('Feito por Ash Machado')
    

#menu macroeconômico
def tela_macro(): #feito
    st.title('Simulador Macroeconômico')
    st.subheader('Simule e analise os principais indicadores da economia', divider = True)

    opcao = st.selectbox("Escolha uma operação:", 
                         ["Cálculo PIB", "Índice de Preços, Quantidade e Inflação", "Crescimento Econômico"])

    if st.button("Avançar"):
        if opcao == "Cálculo PIB":
            st.session_state.tela = 'pib'
        elif opcao == "Índice de Preços, Quantidade e Inflação":
            st.session_state.tela = 'indices'
        elif opcao == "Crescimento Econômico":
            st.session_state.tela = 'crescimento'
#eu utilizo dois ifs pois dentro da biblioteca streamlit há mt disso de associar if e elif a botões DEPENDENTES, o que ferra o processo. preciso que cada botão seja independente sabe?
    if st.button("Voltar ao Menu Principal"):
        st.session_state.tela = 'menu'

#opcoes do selectbox macroeconômico, criam outras telas dentro:
def tela_PIB(): #feito
    st.title("Cálculo do PIB")
    opcao_PIB = st.selectbox("Selecione o modo que deseja calcular o PIB:", ['PIB Real, Nominal e Deflator', 'PIB pela Demanda', 'PIB pela Oferta', 'PIB pela Renda'])
    if st.button("Avançar"):
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
def tela_PIBS_nom_real_defl():  #Preciso apenas refinar, corrigir **************
    st.title('Calcule aqui os PIBs reais, nominais e deflator do PIB')

    #percebi que msm com um botao avançar, não havia um controle para determinar se o usuário acabou ou não, dava muuuito erro
    #então pedi ajuda pro amigo chat aqui:

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
    print()
def tela_PIB_oferta():
    print()
def tela_PIB_renda():
    print()

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
def tela_micro():
    st.title('Simulador Microeconômico')
    st.write('simulador micro...')

    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_fin():
    st.title('Simulador Financeiro')
    st.write('simulador financeiro...')

    if st.button('Voltar ao Menu'):
        st.session_state.tela = 'menu'

def tela_est():
    st.title('Simulador Estatístico')
    st.write('simulador estatístico...')

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




# Menu (main)
def main():
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

#loop 
if __name__ == "__main__":
    main()
