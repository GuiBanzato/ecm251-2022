import streamlit as st

from src.controllers.user_controller import UserController
from src.controllers.product_controller import ProductController
from src.models.user_model import User
from src.models.product_model import Product


product_controller = ProductController()
user_controller = UserController()

colA, colB = st.columns(2)

with colA:
    st.title("MyHeroShop")

with colB:
    
    try:
        st.image("./src/imagens/Utec.png", width=200)
    except FileNotFoundError:
        st.image("./imagens/Utec.png", width=200)

if st.session_state.usuario != None:
    st.markdown("## Produtos") 

    def show_product(produto):
        from PIL import Image
        try:
            img = Image.open(produto.get_imagem())
        except FileNotFoundError:
            img = Image.open("./src/" + produto.get_imagem()[2:])
        st.image(img, width=200)
        st.markdown(f"### {produto.get_nome()}")
        st.markdown(f"{produto.get_descricao()}")
        st.markdown(f"#### R${produto.get_preco()}")
        button = st.button("Comprar", key=produto.get_nome())
        if button:
            st.session_state.carrinho.append(produto)

    for product in st.session_state.estoque:
        show_product(product)
else:
    st.error("Você precisa estar logado para ver os produtos, vá até a tela de login e coloque seu usuário e senha")