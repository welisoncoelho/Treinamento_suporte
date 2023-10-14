# streamlit_app.py

import streamlit as st

def check_password():
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False
        
    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

# Função para alternar entre páginas usando "cache"
st.title("""Área de Treinamento do Analista
                Franquia VAREJO & TECH""")
def toggle_page(page_name):
    session_state = st.session_state
    session_state.page = page_name

if check_password():
    # Substituir o link markdown por um botão que redireciona para financeiro.py
    st.sidebar.markdown("# Seja Benvido(a)!")
    if st.sidebar.button("Ir aos modulos"):
        toggle_page("financeiro")

# Lógica para mostrar conteúdo da página financeiro.py
if hasattr(st.session_state, "page") and st.session_state.page == "financeiro":
   
    # Use a condição correta para verificar qual botão foi pressionado
    module_selection = st.sidebar.radio("Escolha o Módulo", ["EMSYS","Autosystem","Emporio","EMSYSTRR","NFAST"])

    if module_selection == "Emporio":
        st.markdown("## Área de Treinamento Empório")
        # Adicione conteúdo específico para o módulo EMSYS aqui 

        st.markdown("Treinamento Empório")
           # URL do vídeo hospedado no Google Drive
        video_url = 'https://drive.google.com/file/d/1njitjyC7MJ5k16xrBziuXlCe196QWDdY/preview'

        # Use o IPython para incorporar o vídeo
        video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
        st.markdown(video_html, unsafe_allow_html=True)        
        
    elif module_selection == "Autosystem":
        st.markdown("## Área de Treinamento Autosystem")
        st.markdown(''' Treinamento de Implantação Autosystem:
               
    - Instalar Postgres
    - Carregar Load
    - Cadastrar Empresa
    - Certificado
    - Fornecedores
    - Modelo de Tanque
    - Depósito
    - Grupo de Produtos
    - Natureza de operação
    - CFOP
    - Series de Notas Fiscais
    - Produtos
    - Plano de Contas
    - Motivo de mov
    - Bombas
    - Bico
    - Automacao
    - Caixa PDV''')
        
       # Adicione conteúdo específico para o módulo Autosystem aqui
        video_url ='https://drive.google.com/file/d/1EXLQGsGobUQyxZHmkM9U3kXEJ4g6l7lV/preview'
        # Use o IPython para incorporar o vídeo
        video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
        st.markdown(video_html, unsafe_allow_html=True)    

        st.markdown("Treinamento Equals")
        video_url ='https://drive.google.com/file/d/12hgdaoAwrerZmoyxm9k_carWOX07rnzE/preview'
        # Use o IPython para incorporar o vídeo
        video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
        st.markdown(video_html, unsafe_allow_html=True)    
        

        # Adicione conteúdo específico para o módulo Autosystem aqui
    elif module_selection == "EMSYS":
        st.markdown("## Área de Treinamento EMSYS")
        video_url = 'https://drive.google.com/file/d/14Tp0PeQhIQGkmYll0ALg16xbM1lYmvan/preview'

        # Use o IPython para incorporar o vídeo
        video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
        st.markdown(video_html, unsafe_allow_html=True) 

        st.markdown("## Faturamento Automático")
        video_url = 'https://drive.google.com/file/d/1-49rvelHbaY7sBzfgM6Lgqv0r5IdFdhH/preview'
         # Adicione um botão para download do PDF
        if st.button("Baixar Documento Faturamento automático"):
            pdf_url = 'https://drive.google.com/uc?id=1-980zZ89OuJc6pSA9-DnpzEmEaBBpbvo'
            st.markdown(f'Download do [Documento Fiscal]({pdf_url})')
        # Use o IPython para incorporar o vídeo
        video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
        st.markdown(video_html, unsafe_allow_html=True)   

    elif module_selection == "EMSYSTRR":
        st.markdown("## Área de Treinamento EMSYSTRR")

        st.markdown(''' Treinamento de Implantação EMSYS /EMSYSTRR:
               
    - Cadastro de pessoas /Fornecedores
    - Cadastro de itens
    - Cadastro De CFOP
    - Cadastro de tributações
    - Cadastro de CST
    - Configuração de Certificado Eletrônico
    - Entrada de nota Via Xml
    - Contas a Pagar 
    - Contas a Receber''')
        # Adicione conteúdo específico para o módulo Autosystem aqui
           # URL do vídeo hospedado no Google Drive
        video_url = 'https://drive.google.com/file/d/14Tp0PeQhIQGkmYll0ALg16xbM1lYmvan/preview'

        # Use o IPython para incorporar o vídeo
        video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
        st.markdown(video_html, unsafe_allow_html=True)      
        
    elif module_selection == "NFAST":
        st.markdown("## NFAST EMSYS")
        video_url = 'https://drive.google.com/file/d/1YcJhoZglJ8ZiEmMpeF0p8EApYiT82-pH/preview'

        # Use o IPython para incorporar o vídeo
        video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
        st.markdown(video_html, unsafe_allow_html=True)      


    
