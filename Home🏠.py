import streamlit as st
import webbrowser
import pandas as pd
import psycopg2
from streamlit_option_menu import option_menu
import pickle
from pathlib import Path
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
   

st.markdown("Seja Bem Vindo")    
st.markdown("# ÁREA DE TREINAMENTO FISCAL📄")





st.markdown("""
                Seja bem vindo a nossa área de treinamento Fiscal, aqui você fará o treinamento dos seguintes modulos :
            
               1- Fundamentos Fiscais 
              
               - REGRAS FISCAIS
               - REGIME SIMPLES NACIONAL
               - REGIME LUCRO REAL
               - LUCRO PRESUMIDO
               - O QUE É UM CFOP?
               - TRIBUTAÇÕES
               - CST
               - CSOSN
               - DOCUMENTOS FISCAIS
               - NFAST
               
            
                """)
st.markdown("Desenvolvido por Welison Coelho")    


