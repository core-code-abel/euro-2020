
import os

API_URL = os.getenv("API_URL", "http://localhost:5000")

def set_config(st):
	st.set_page_config(
		page_icon="⚽",
		page_title = "EURO-2020",
		layout = 'wide',
		initial_sidebar_state = "collapsed"
	)
	# BOOTSTRAP
	st.markdown(
		'''<link
			rel="stylesheet"
			href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
			integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
			crossorigin="anonymous"
		>''',
		unsafe_allow_html=True,
	)

	with open('styles.css') as f:
			st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
