##Importing neccessary library for the riddles
import streamlit as st
from PIL import Image
import time


#setting page configuration for the app via streamlit
st.set_page_config(
page_title="Orijinal Cool Riddles",
page_icon="🧊",
layout="centered",
initial_sidebar_state="collapsed",
menu_items={
'Get Help': 'https://gdmgroup.com.ng/',
'Report a bug': None,
'About': "##This Riddle is designed to see how ORIJINAL YOU ARE AS AN HEROE"
}
)

#Main code snippet for the web app
 #creating column on webpage where the first column from left is less than second column in width size
# html_temp = """<div style=background-color:{};height:{};width:{};border:{};border-radius:{};border-style:{};border-color:{};margin-left:{};margin-right:{};"> <h2 style="font-size:{};text-align:{};padding-top:{};padding-bottom:{};font-family:{};">The</h1>
# </div>"""
# st.markdown(html_temp.format('grey','70px','1250px','7px','8px','groove','green','10px','5px','16px','center','30px','30px','Monospace'),unsafe_allow_html=True)
st.header("RIDDLES FOR ORIJINAL HEROES")
st.header("🔢 🕹️ 🕸️ 🔐 🔯 💰 🎲 🎯 🎮  🏅")
img=Image.open('WhatsApp Image 2021-11-03 at 17.05.07.jpeg')
st.image(img,use_column_width=True)
def is_quiz_active():
    if 'quiz_active' in st.session_state.keys() and st.session_state['quiz_active']:
        return True
    else:
        return False
if is_quiz_active():
    st.info("Please ensure you fill all quizes in this riddle")
    QUIZ1=st.selectbox("👯‍♀️How do you party?",["",'With Friends','With Everyone',])
    st.session_state["How do you party?"]=QUIZ1
    time.sleep(0.1)
    QUIZ2=st.selectbox("🏡You see a burning house, what do you do?",["","Run into the house, to help","Call for help"])
    st.session_state["You see a burning house, what do you do?"]=QUIZ2
    time.sleep(0.1)
    QUIZ3=st.selectbox("🧍Which of these best describes you?",["","Loud and Bold","Silent and courageous"])
    st.session_state["Which of these best describes you?"]=QUIZ3
    time.sleep(0.1)
    QUIZ4=st.selectbox("😦What's your first response to any challenge?",["","Tactical and careful considerations","Spontaneous and quick to act"])
    st.session_state["What's your first response to any challenge?"]=QUIZ4
    time.sleep(0.1)
    QUIZ5=st.selectbox("👨‍👩‍👧‍👦What is your gender?",["","Male","Female"])
    st.session_state["What's your first response to any challenge?"]=QUIZ5
    time.sleep(0.1)


    Outcome1=['Queen Amina', 'Queen Idia', 'Olokun', 'Oya', 'Ala']
#Male
    Outcome2=['Sango', 'Ogun', 'Amadioha', 'Bayajidda', 'Anyanwu']

    #Define points for responses
    #QUIZ5
    if QUIZ5=="Male":
        QUIZ5_Point=20
    elif QUIZ5=="Female":
        QUIZ5_Point=10
    else:
        QUIZ5_Point=0
            #QUIZ1
    if QUIZ1=="With Friends":
        QUIZ1_Point=3
    elif QUIZ1=="With Everyone":
        QUIZ1_Point=5
    else:
        QUIZ1_Point=0
            #QUIZ2
    if QUIZ2=="Run into the house, to help":
        QUIZ2_Point=5
    elif QUIZ2=="Call for help":
        QUIZ2_Point=3
    else:
        QUIZ2_Point=0
            #QUIZ3
    if QUIZ3=="Loud and Bold":
        QUIZ3_Point=3
    elif QUIZ3=="Silent and courageous":
        QUIZ3_Point=5
    else:
        QUIZ3_Point=0
    if QUIZ4=="Tactical and careful considerations":
        QUIZ4_Point=4
    elif QUIZ4=="Spontaneous and quick to act":
        QUIZ4_Point=3
    else:
        QUIZ4_Point=0
            #Calculate overall points
    overall_point=QUIZ1_Point+QUIZ2_Point+QUIZ3_Point+QUIZ4_Point+QUIZ5_Point
    if overall_point==44:
            link='[Submit QUIZ](http://orijindp.local/)'
            st.markdown(link, unsafe_allow_html=True)
    elif overall_point==35:
            link="[Submit QUIZ](http://orijindp.local/sample-page/)"
            st.markdown(link,unsafe_allow_html=True)
    else:
            link=("","")
            st.warning("📱You Can Reload Your Browser To Restart The Quiz")



else:
    if st.button("START QUIZ"):
        st.session_state['quiz_active']=True
        st.experimental_rerun()


    #QUIZ2=st.selectbox("You see a burning house, what do you do?",["","Run into the house, to help","Call for help"])
    #
    # QUIZ3=st.selectbox("Which of these best describes you?",["","Loud and Bold","Silent and courageous"])
    #
    # QUIZ4=st.selectbox("What's your first response to any challenge?",["","Tactical and careful considerations","Spontaneous and quick to act"])
    #
    # QUIZ5=st.selectbox("What is your gender?",["","Male","Female"])


#Define outcome of response from riddles players
#Female
