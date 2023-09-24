import streamlit as st


st.markdown("# Fundamentos Fiscais📄")
st.sidebar.markdown("- REGIME TRIBUTÁRIO ")
st.sidebar.markdown("- REGIME SIMPLES NACIONAL")
st.sidebar.markdown("- REGIME LUCRO REAL")
st.sidebar.markdown("- LUCRO PRESUMIDO")





st.markdown("***Regime Tributário***.")
st.text("""Conceito : Regime Tributário é o conjunto de leis que regulamenta a forma de tributação da pessoa
jurídica no que diz respeito ao imposto de renda (IRPJ) e a contribuição social sobre o lucro líquido
(CSLL). A variação dá-se nas alíquotas de imposto e na base de cálculo, que pode ser a partir do ***Lucro
Presumido*** ou do ***Lucro real***, ***Simples Nacional.""")

# URL do vídeo hospedado no Google Drive
video_url = 'https://drive.google.com/file/d/1O9pmjqPFWUzlLZwb6dmB_PGYxIwGlqPr/preview'

# Use o IPython para incorporar o vídeo
video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
st.markdown(video_html, unsafe_allow_html=True)

st.markdown("***REGIME SIMPLES NACIONAL***.")
st.text("""Simples Nacional: Neste regime tributário há duas grandes vantagens: uma refere-se aos valores de
alíquotas que são menores e a outra se refere à simplicidade da agenda tributária, facilitando o controle.
Neste caso, enquadram-se empresas com receita bruta de até R$4,8 milhões. Este regime apresenta
alíquotas reduzidas, pois há a união de oito impostos e contribuições: PIS, Cofins, IPI, ICMS, CSLL, ISS,
Imposto de Renda da pessoa jurídica e, em alguns casos, INSS patronal. 
        
Contudo, nem sempre este é o regime mais vantajoso, especialmente para empresas prestadoras de serviços, 
que recolhem à parte a contribuição do INSS e por isso suas alíquotas variam conforme a folha de pagamento.""")
# URL do vídeo hospedado no Google Drive
video_url = 'https://drive.google.com/file/d/1fOEVLCzXJbkfyIQH5GV52VAxDm6Bswd2/preview'

# Use o IPython para incorporar o vídeo
video_html = f'<iframe src="{video_url}" width="640" height="360" frameborder="0" allowfullscreen="true"></iframe>'
st.markdown(video_html, unsafe_allow_html=True)

st.markdown("***REGIME LUCRO REAL***.")
st.text("""Este regime é obrigatório para empresas com faturamento superior a R$ 78 milhões e empresas com
atividades voltadas para o setor financeiro. Neste caso, as alíquotas são calculadas com base no lucro real, ou seja,
receita menos despesas. Por este motivo, é preciso que a empresa seja muito organizada com suas contas.""")

# URL do vídeo hospedado no Google Drive
video_url = 'https://drive.google.com/file/d/1yxOgOWzQMYxSpxwL-DGVmFuWFU7Sw-Nt/view?usp=drive_link'
st.markdown(video_html, unsafe_allow_html=True)

st.markdown("***REGIME PRESUMIDO***.")
st.text("""Este regime é obrigatório para empresas com faturamento superior a R$ 78 milhões e empresas com
atividades voltadas para o setor financeiro. Neste caso, as alíquotas são calculadas com base no lucro real, ou seja,
receita menos despesas. Por este motivo, é preciso que a empresa seja muito organizada com suas contas.""")

# URL do vídeo hospedado no Google Drive
video_url = 'https://drive.google.com/file/d/1uYoHqnpOCay8yu2pZZp4Lyrm1qC3yTgy/view?usp=drive_link'
st.markdown(video_html, unsafe_allow_html=True)
