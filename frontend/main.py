from sections.header import set_header
import streamlit as st
from sections.config import set_config
from sections.header import set_header
from sections.tabs import set_tabs

set_config(st)
set_header(st)
set_tabs(st)