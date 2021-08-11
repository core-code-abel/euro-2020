from .tab_home import render_tab_home
from .tab_events import render_tab_events
from .tab_statistics import render_tab_statistics
from ._404 import render_404

tabs = {
  "Home": lambda st: render_tab_home(st),
  "Events": lambda st: render_tab_events(st),
  "Match Statistics": lambda st: render_tab_statistics(st),
}

def set_tabs(st):

  query_params = st.experimental_get_query_params()

  active_tab = query_params["tab"][0] if "tab" in query_params else "Home"

  li_items = "".join(
      f"""
      <li class="nav-item">
          <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
      </li>
      """
      for t in tabs
  )
  tabs_html = f"""
      <ul class="nav nav-tabs">
        {li_items}
      </ul>
  """
  st.markdown(tabs_html, unsafe_allow_html=True)
  st.markdown("<br>", unsafe_allow_html=True)

  if active_tab in tabs:
    tabs[active_tab](st)
  else:
    render_404(st)
