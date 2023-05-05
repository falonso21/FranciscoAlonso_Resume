import streamlit as st
from PIL import Image

image = Image.open("assets/Iceland.jpg")

st.header("🧐 Interests")
with st.expander("Philosophy"):
    st.markdown("There is a book that inspired me a lot about Artificial Intelligence and  social dilemas. "
                "That book is named 'Weapons of Math Destruction' by Cathy O'Neil. Through this book "
                "I realized how important are going to be ethics and philosophy for the future of both "
                "society and Artificial Intelligence. "
                "That book along with my interests for History brought me to start Philosophy Bachelor at "
                "UNED (Universidad Española a Distancia). I take it as a hobbie and I do it step by step so I am still "
                "finishing the first yea.")
with st.expander("Natural Language Processing"):
    st.markdown("Of all the fields of study within artificial intelligence, this is undoubtedly the one that interests "
                "me the most. As a curiosity, for an assignment for my master's studies I did a study of the 7 "
                "Harry Potter books using NLP techniques.")
with st.expander("Divulgation and writing"):
    st.markdown("I love talking about science in general but specially about Data Science in a divulgative way. "
                "That brought me to be lecturar at my Home University as as you can see in other sections of this "
                "dashboard. But also, I love writing articles about IA, "
                "[here](https://www.futurespace.es/author/francisco-alonso-fernandez/) "
                "you can read some of them that I wrote for Future Space's blog ")
with st.expander("Sports"):
    st.markdown("I hardly support the said _Mens sana in corpore sano_. As a Data Scientist I spend a lot of hours "
                "sitting in front of the computer. That's why I try to spend my free time in motion. As a teenager I "
                "used to play football for my hometown's team. Nowadays I love playing padel and running. My next goal? "
                "The half-marathon of Paris!")
with st.expander("Travelling"):
    st.markdown("Probably the thing that motivates me the most. I guess you are never the same after Erasmus, and this "
                "desire of adventure will stay with me. See a picture of my last road trip around Iceland!")
    st.image(image, caption="Road 1 Iceland")