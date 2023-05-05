import streamlit as st
from PIL import Image
from streamlit.components.v1 import components

image = Image.open("assets/PicUCA.jpg")

st.header("💻 Work Experience")

with st.expander("Senior Data Scientist at Future Space 03/2023 - PRESENT"):
    st.write("As a Senior Data Scientist, I am still involved in the development and implementation of"
             "Machine Learning models. The main difference with my previous role is that now I will be more involved "
             "in the customer side: from kick-off meetings and project presentation to the development of "
             "commercial proposals.  ")
with st.expander("International Project at Future Space 10/21 - 04/2023"):
    st.write("During this project I worked directly at the client's offices in Paris (France) for 18 months. There I wrote code "
             "for various office specific software. My responsibilities included analysis and design of full stack "
             "applications and services. During this period I mainly maintained and enhanced legacy Python-based search "
             "interface to an elastic cloud database. The team worked using agile methodology of Scrum. Also, one of "
             "the main tasks was to impletent a service to parse user input in order to carry out entity extraction and"
             "natural language processing. Within this project I was also in contact with some Java/Kotlin and "
             "Sprinboot applications.")
    st.markdown("Obviously, this project also boosted my language skills. English was the driving language at the office, "
                "but as it was based in France, I also took the opportunity to learn French.")
with st.expander("Lecturer at University of Cadiz 01/2021 - PRESENT"):
        st.markdown("This opportunity came up thanks to my master's final dissertation and a series of articles on OSINT, "
                    "fingerprinting and Artificial Intelligence that I wrote for the Future Space blog. Every year I "
                    "give a lecutre on Artificial Intelligence models in the Human Resources sector for two masters of "
                    "the University of Cadiz: MBA in Business Management and Master in Human Resources Management. ")
        st.image(image, caption="Lecture while Covid times")
with st.expander("Data Scientist Junior at Future Space 07/2020 - 03/2023"):
    st.markdown("By that time my internship was done so I was used to work with the team but the next step was to be "
                "involved in all stages of a Data Science projects, beyond development. Especially, I started to be in "
                "contact with the datas ingestion and the production of the models. Some of the projects on which I had "
                "the opportunity to work during that period were:")
    st.markdown("- Inbox emails clusterization. Our customer had an email for complaints and comments, but they were not "
                "able to read all those emails one by one. However, they wanted to classify them in groups and also to have "
                "an idea of the most representative and meaningful words/sentences/topics for each group so they could "
                "understand the requests and questions.")
    st.markdown("- Characterization of prospects. Some of our customers were very interested in OSINT, digital fingerprint "
                "and social networks. This kind of projects were mainly based in Descriptive Analysis from social network data "
                "but also prescriptive analysis trying to find out socioeconomic variables such as economic level, Big5 personality traits, etc.")
    st.markdown("- Industry 4.0. One of our customers was in the middle of the digitalization proccess of their factories. "
                "What we did was to create an algorithm to optimize the roadmaps of their manufacturing processes. This "
                "algorithm was a mix of Operations Research, Machine Learning models and Graphs theory.")
    st.markdown("- Fraud detection: This is a project carried out for a client in the banking sector. By means of graph "
                "theory we tried to find relationships between high ranking positions in different companies in order "
                "to detect fraudulent cases.")
with st.expander("Data Analytics Intern at Future Space 10/2019 - 07/2020"):
    st.write("Being an intern at Future Space was the best way for me to put into practice everything I learned in "
             "the Master's program. This allowed me to have direct contact with real-life projects. I was even able to "
             "dig into the development and context of one of these projects to use it as my Master's final dissertation "
             "entitled 'Models of economic prediction from social networks'.")
