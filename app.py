import streamlit as st

st.title("Banco Central Da Sua Maquinna De Churros")
st.write('texta ai se funciona e depois coloca frente e verso do cartao')
casa = st.number_input('qual valor do cafofo q vc vai financiar:', min_value=0.0)
salario = st.number_input('fala ai pa nois quanto vc rece:', min_value=0.0)
anos = st.number_input('quantos anos vai pagar o barraco?', min_value=1)

if st.button('Simular empréstimo'):
    meses = anos * 12
    prestacao = casa / meses
    limite = salario * 0.30

    if prestacao <= limite:
        st.success('Empréstimo aprovado')
    else:
        st.error('Empréstimo negado')

    st.write(f'Prestação: R$ {prestacao:.2f}')