from pathlib import Path

import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_timeline import timeline

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Francisco Alonso"
PAGE_ICON = ":page_facing_up:"
NAME = "Francisco Alonso Fernández"
DESCRIPTION = """
Data Scientist. "You can have data without information, but you cannot have information without data".
"""
EMAIL = "falonsof96@gmail.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- TIMELINE ---
st.write('\n')
st.subheader("Timeline Overview")
with st.spinner(text="Building line"):
    with open('assets/timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

embed_component = {'linkedin': """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
<div class="badge-base LI-profile-badge" data-locale="es_ES" data-size="medium" 
data-theme="dark" data-type="VERTICAL" data-vanity="franciscoalonsofernandez" data-version="v1"><a 
class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/franciscoalonsofernandez?trk=profile-badge
"></a></div>"""}

with st.sidebar:
    components.html(embed_component['linkedin'], height=310)

