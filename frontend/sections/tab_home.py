def render_tab_home(st):

    cols = st.columns((1, 3))
    with cols[0]:
        st.image('images/photo.jpg')
    with cols[1]:
        st.header("Welcome to my lovely page!")
        st.write("This is my first project as data analyst student, so any kind of feedback received will be welcome!!!")
        st.write("- Check out this code at my [repo](https://github.com/core-code-abel)")
        st.markdown('''
            - Find me at&nbsp;
            [<img
                class="home-image"
                src="https://cdn.svgporn.com/logos/github.svg">
            ](http://github.com/abelalonso)''',
            unsafe_allow_html=True)
        st.markdown('''
            - Or&nbsp;
            [<img
                class="home-image"
                src="https://cdn.svgporn.com/logos/linkedin.svg">
            ](https://www.linkedin.com/in/abel-alonso)''',
            unsafe_allow_html=True)
        st.markdown('''
            <div>
                Made With <span style="font-size: 30px">❤️</span> by Abel Alonso at&nbsp;
                <a id="core-link" href="https://www.corecode.school" target="_blank">
                    <img
                        class="home-image"
                        src="https://api.brandy.run/core/logo">
                    <span style="position: relative; font-size: 30px; font-weight: bold; bottom: -3px">CORE</span>
                </a>
            </div>
            '''
            , unsafe_allow_html=True)
