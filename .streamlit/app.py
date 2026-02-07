from openai import OpenAI, api_key
import streamlit as st
st.set_page_config(page_title="Streamlit Chat",page_icon="message")
st.title("Chatbot")

st.subheader("personal info", divider="rainbow")
name = st.text_input("Name",max_chars=None,placeholder="Enter your name")
experiance = st.text_area("experiance",value="",max_chars=None,placeholder="Enter your experiance")
skills = st.text_area("skills",value="",max_chars=None,placeholder="Enter your skills") 

st.write(f"**name**: {name}")
st.write(f"**experiance**: {experiance}")
st.write(f"**skills**: {skills}")

st.subheader("company and experiance", divider="rainbow")

col1, col2 = st.columns(2)
with col1:
    level = st.selectbox("level", options=["entry level", "mid level", "senior level"])
with col2:
    position = st.selectbox("position", options=["software engineer", "data scientist", "product manager"])
    
company = st.selectbox(
    "company",
    options=[
        "Google",
        "Microsoft",
        "Amazon",
        "Facebook",
        "Apple",
        "Netflix",
        "Tesla",
        "SpaceX",
        "Airbnb",
        "Uber",
    ],
)
    

client = OpenAI(api_key==st.secrets["OpenAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": f"You are an hr executive at {company} and you are interviewing a candidate for the position of {position} at {level} level. The candidate's name is {name} and they have the following experiance: {experiance}. They also have the following skills: {skills}. You will ask them questions about their experiance and skills and then give them feedback on how they can improve their chances of getting the job."}]
    
for message in st.session_state.messages: #taking the messages from assistant and user
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
if prompt := st.chat_input("Your answer."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)