def render_404(st):
    error_msg = """
        <h1 style="text-align:center">
            404: You are offside
        </h1>
    """
    st.markdown(error_msg, unsafe_allow_html=True)
    st.image("./images/offside.jpg")