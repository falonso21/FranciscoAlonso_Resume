import base64
import streamlit as st
import extra_streamlit_components as stx
from streamlit.components.v1 import components
import os


# --- AUXILIAR FUNCTIONS ---
def displayPdf(path):
    with open(path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="650" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

tfg_url = "https://rodin.uca.es/handle/10498/22099"
coursera_url = "https://www.coursera.org/account/accomplishments/specialization/certificate/XWGQY77V8X4A"

st.header("📚 Studies")

with st.expander("Main studies"):
    tab1, tab2 = st.tabs(["📈 Maths", "📊 Data Science"])

    with tab1:

        st.write("Graduated in Mathematics with special mention in Mathematical Engineering by the University of Cádiz, "
                 "2014-2019. Maths degree provided me a background with a lot of meaningful skills but, from my point of view, "
                 "the most valuable thing is that this degree structures your mind in a way that allows you to work "
                 "methodically and rationally.")
        st.write("During the degree I was specially interested in those subjects that were closely related with programming and, "
                 "in general, with applied Maths. If I would have to highlight some of them I would bring up Complex Analysis, "
                 "Data Analytics and Mathematical Modelling. I also had the chance to collaborate with the Applied Maths deparment "
                 "preparing documents for the first year students.")
        st.write("During the last year of my bachelor, while I was abroad on Eramus, I wrote my final disseration named "
                 "['Relationship between fuzzy inference systems and multiadjoint logic programming'](https://rodin.uca.es/handle/10498/22099), "
                 " which received Pass with Honors and was published in the University repository. Apart from that, this last year of studies was really pleasant and "
                 "I had the opportunity to learn from amazing mathematicians from all over the world while I was abroad in Ireland, some of them "
                 "took the trouble of writing a recommendation letter for me (find attached below).")

        chosen_id = stx.tab_bar(data=[
            stx.TabBarItemData(id=1, title="Recommendation Letter 1", description="Letter by Philipp Hoevel"),
            stx.TabBarItemData(id=2, title="Recommendation Letter 2", description="Letter by Dr Shirin Moghaddam"),
        ], default=1)
        if chosen_id == "1":
            displayPdf("assets/RecommendationLetterPhilipp.pdf")

        if chosen_id == "2":
            displayPdf("assets/RecommendationLetterShirin.pdf")

    with tab2:
        st.write("Once the bachelor was done and I was sure Data was my thing, I started to explore the possiblities where "
                 "I could do my master studies. After some researching, I decided Madrid and Afi Finance School were the place. "
                 "Indeed, I was right. The master in Data Science & Big Data provided me with all the main knowledge in the field: "
                 "Machine learning techniques such as regression, classification or clustering, optimization, visualization, deep learning, graphs and much more (please see subjects in the "
                 "attached document).")
        st.write("This master also gave me the opportunity to learn from the best Data Scientists in Spain, the teaching staff were just outstanding. "
                 "Furthermore, the master clases about personal coaching were totally a plus.")
        displayPdf(
            "assets/Notas_máster_Francisco_Alonso.pdf")

with st.expander("Courses"):
    st.write("Once I discovered Data was gonna be the main part of my career, I took a couple of courses in order to be familiar "
             "with the Data world before starting the Master's studies. Those courses are Data Analysis with Python, by Universidad Complutense de Madrid "
             "and Introduction to Big Data with R, by Afi Escuela de Finanzas.")
    st.write("Next, when I was already working as Data Scientist I wanted to deepen in Deep Learning so I coursed the "
             "[Specialized program in Deep Learning](https://www.coursera.org/account/accomplishments/specialization/certificate/XWGQY77V8X4A), "
             "by Andrew Ng. This course was composed by Neural Networks and Deep Learning, Hyperparameter Tuning, Regularization and Optimization, " 
             "Structuring Machine Learning Projects, Convolutional Neural Networks and Sequence Models.")
    st.write("As well as the DL course and, more or less at the same time, I thought it was good idea to have some contact with other languages "
             "so I coursed [Become a Junior Java Software Developer.](https://www.udemy.com/certificate/UC-573af00a-cc0d-4a8a-a52a-2722f6ac952c/)")

with st.expander("Languages"):
    st.write("There are two experiences in my life that have especially boosted my English level. The firt one was my Erasmus year in Ireland, "
             "there I learnt a lot about daily English, but also about technical English as all my exams and classes were in that language. "
             "After that year I thought it was a good opportunity to get a higher English certification that would give me more opportunities applying to "
             "masters and internships. So I got the C level by the British Council (see attached).")
    st.write("Then, my project working in Paris within an international environment is enhancing my professional English as it is the driving languge in the office, but in the other and "
             "is also giving my the chance to learn French for everyday life.")
    displayPdf(
        "assets/CAptis_FranciscoAlonso.pdf")
