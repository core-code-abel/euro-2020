def set_header(st):
    header = st.columns((1, 16, 1))
    with header[1]:
    	st.image("images/banner.png")

    title = f"""
		<h1 style="text-align:center">
			{'⚽'*3}&nbsp;&nbsp;Euro 2020: Road to Glory&nbsp;&nbsp;{'⚽'*3}
		</h1>
	"""
    st.markdown(title, unsafe_allow_html=True)
