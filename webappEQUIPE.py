#libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import urllib3
from urllib3 import request
import pandas as pd
import altair as alt
from urllib.error import URLError
import time

def VerificaOpcao(opcao):
    if opcao == 'Equipe 01':
        return 'Equipe+01','PAINEL - EQUIPE 01'
    elif opcao == 'Equipe 02':
        return 'Equipe+02','PAINEL - EQUIPE 02'
    elif opcao == 'Equipe 03':
        return 'Equipe+03','PAINEL - EQUIPE 03'
    elif opcao == 'Equipe 04':
        return 'Equipe+04','PAINEL - EQUIPE 04'
    elif opcao == 'Equipe 05':
        return 'Equipe+05','PAINEL - EQUIPE 05'
    elif opcao == 'Equipe 06':
        return 'Equipe+06','PAINEL - EQUIPE 06'
    elif opcao == 'Equipe 07':
        return 'Equipe+07','PAINEL - EQUIPE 07'
    elif opcao == 'Equipe 08':
        return 'Equipe+08','PAINEL - EQUIPE 08'
    elif opcao == 'Equipe 09':
        return 'Equipe+09','PAINEL - EQUIPE 09'
    elif opcao == 'Equipe 10':
        return 'Equipe+10','PAINEL - EQUIPE 10'
    elif opcao == 'Equipe 11':
        return 'Equipe+11','PAINEL - EQUIPE 11'
    elif opcao == 'Equipe 12':
        return 'Equipe+12','PAINEL - EQUIPE 12'
    elif opcao == 'Equipe 13':
        return 'Equipe+13','PAINEL - EQUIPE 13'
    elif opcao == 'Equipe 14':
        return 'Equipe+14','PAINEL - EQUIPE 14'
    elif opcao == 'Equipe 15':
        return 'Equipe+15','PAINEL - EQUIPE 15'
    else:
        return 'ERRO','ERRO'

image01 = Image.open('ImagemLateral.jpg')
st.sidebar.image(image01, width=300, caption='2º Hackathon Mackenzie Campinas - 2023') 


Titulo_Principal = '<p style="font-weight: bolder; color:DarkBlue; font-size: 32px;">Web App EQUIPES</p>'
st.markdown(Titulo_Principal, unsafe_allow_html=True)
mystyle1 =   '''<style> p{text-align:center;}</style>'''
st.markdown(mystyle1, unsafe_allow_html=True) 

option = 'Equipe 01'
option = st.selectbox(
    'Escolha o número da sua EQUIPE',
    ('Equipe 01', 'Equipe 02', 'Equipe 03', 'Equipe 04', 'Equipe 05', 'Equipe 06', 'Equipe 07', 'Equipe 08', 'Equipe 09', 'Equipe 10', 'Equipe 11', 'Equipe 12', 'Equipe 13', 'Equipe 14', 'Equipe 15'))
st.write('Você selecionou:', option)

resp = VerificaOpcao(option)
EQUIPE = resp[0]
TITULO = resp[1]
st.title(TITULO)

menu = ["Dúvidas",
        "Respostas",
        "Dúvidas e Respostas"]
choice = st.sidebar.selectbox("Menu de Opções",menu)

def exibir():
    #DÚVIDAS
    rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQQNWj747l2uR_TOZ_4cTnajPMmbpLb84ILH1KMzu1eN3BwalrUTuN7XrcWWU6q5qVGnw-Ay4QEG1x_/pub?gid=1381735194&single=true&output=csv')
    dataD = rD.content
    dfD = pd.read_csv(BytesIO(dataD), index_col=0)
    NregD = len(dfD)
    dfD.columns = ['equipe', 'nome', 'duvida', 'obs']
    selecao01D = dfD['equipe']==option
    df01D = dfD[selecao01D]

    #RESPOSTAS
    rR = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTIxe7VmjCRpyVvwKaajuRFyp6T1MRGOx_GCUg7ghiA2QWbiNLYam-xpLYhXE2Gdn6RgLjRRJPD4WZ-/pub?gid=1131399848&single=true&output=csv')
    dataR = rR.content
    dfR = pd.read_csv(BytesIO(dataR), index_col=0)
    NregR = len(dfR)
    dfR.columns = ['enderecoMAIL', 'equipe', 'nome', 'resposta', 'observacao', 'mail']
    selecao01R = dfR['equipe']==option
    df01R = dfR[selecao01R]

    #Cálculo do Número de Registros por EQUIPE
    NregDf01D = len(df01D)
    NregDf01R = len(df01R)
    if choice == "Dúvidas": 
        st.header("Relatório de DÚVIDAS")   
        st.subheader(option)
        st.warning('Dúvida(s) Enviada(s)')
        st.info(df01D['duvida']) 
               
    elif choice == "Respostas":       
        st.header("Relatório de RESPOSTAS")    
        st.subheader(option)   
        st.info('Resposta do(a) TUTOR(A):')
        st.info(df01R['resposta'])  
                   
    elif choice == "Dúvidas e Respostas":       
        st.header("Relatório: DÚVIDAS E RESPOSTAS")  
        colDR1, colDR2 = st.columns((1,1))
        with colDR1:
            st.write("Nº TOTAL de Dúvidas (DESTA EQUIPE):")
            st.warning(NregDf01D)
        with colDR2:
            st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
            st.info(NregDf01R)
        st.subheader(option)
        st.warning('Dúvida(s) Enviada(s)')
        st.warning(df01D['duvida']) 
        st.info('Resposta do(a) TUTOR(A):')
        st.info(df01R['resposta']) 

exibir()
with st.form("FormularioDÚVIDAS", clear_on_submit=True):
    st.write("Formulário para envio de dúvidas da " + option)
    NOME = st.text_input('SEU NOME:')
    DUVIDA = st.text_input('SUA DÚVIDA:')
    OBS = st.text_input('DIGITE OBSERVAÇÃO ADICIONAL:')
    http = urllib3.PoolManager()
    link = 'https://docs.google.com/forms/d/e/1FAIpQLScEItofat2IG1ybAekBip_kGlE6ynobRPBFOhj8TfvI09hr_g/formResponse?&submit=Submit?usp=pp_url&entry.1818151889='
    link += str(EQUIPE)+'&entry.874436440='+str(NOME)+'&entry.517607907='+str(DUVIDA)+'&entry.180883171='+str(OBS)
    submit = st.form_submit_button('✔️ ENVIAR DÚVIDA')
    if submit:
        r = http.request('GET', link)
        st.success("Dúvida enviada pela " + option + " com sucesso!") 
        progress_text = "Tempo de espera necessário para exibição da base de dados atualizada!"
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(1.5)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(0.5)
        my_bar.empty()
                   
        exibir() 

st.sidebar.info("Web app desenvolvido pelo professor Massaki de O. Igarashi para a gestão e acompanhamento do envio de dúvidas e respostas entre alunos, tutores, mentores e professores.")
st.sidebar.info("2ª EDIÇÃO DO DESAFIO HACKATHON: MACKENZIE CAMPINAS - LOGITHINK.IT - IMA (Edição 2023)")
