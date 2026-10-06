import os, tempfile
from pathlib import Path
import streamlit as st
from PIL import Image
from gtts import gTTS
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

st.set_page_config(page_title='The Belief Machine', page_icon='🐍', layout='centered')
AVATAR = Path(__file__).parent / '17080.png'
SYSTEM_PROMPT = '''You are The Belief Machine, an intelligent fictional conversational character. Your personality is warm, mysterious, philosophical, playful and curious. You enjoy discussing consciousness, time, physics, music, spirituality, creativity and the user's ideas. Be engaging and conversational rather than robotic. You may be playfully flirtatious when appropriate, but remain non-explicit.'''

def get_client():
    if OpenAI is None: return None
    key = st.secrets.get('OPENAI_API_KEY', os.getenv('OPENAI_API_KEY'))
    return OpenAI(api_key=key) if key else None

def ai_reply(messages):
    client = get_client()
    if client is None:
        return 'I am ready to talk. Add an OpenAI API key in Streamlit Secrets to activate my full conversational intelligence.'
    response = client.responses.create(model=os.getenv('OPENAI_MODEL', 'gpt-5'), instructions=SYSTEM_PROMPT, input=messages)
    return response.output_text

def speak(text, path):
    gTTS(text=text, lang='en', slow=False).save(path)

if 'messages' not in st.session_state: st.session_state.messages = []
st.title('🐍 The Belief Machine')
st.caption('Your conversational AI character')
if AVATAR.exists(): st.image(str(AVATAR), use_container_width=True)
st.markdown('Ask me about **time, consciousness, physics, music, spirituality, The Belief Machine**, or anything else.')
for m in st.session_state.messages:
    with st.chat_message(m['role']): st.write(m['content'])
prompt = st.chat_input('Talk to the Belief Machine…')
if prompt:
    st.session_state.messages.append({'role':'user','content':prompt})
    with st.chat_message('user'): st.write(prompt)
    with st.chat_message('assistant'):
        with st.spinner('Thinking…'): reply = ai_reply(st.session_state.messages)
        st.write(reply)
        st.session_state.messages.append({'role':'assistant','content':reply})
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f: audio_path=f.name
        try:
            speak(reply, audio_path)
            with open(audio_path,'rb') as audio: st.audio(audio.read(), format='audio/mp3')
        finally:
            try: os.remove(audio_path)
            except OSError: pass
st.divider()
st.subheader('Character mode')
mode = st.selectbox('Choose personality', ['Philosophical','Mysterious','Playful','Flirtatious','Science-focused'])
st.caption(f'Current mode: {mode}. The production version can pass this mode into the character prompt.')
st.info('V2 is designed so the voice and facial-animation engine can be replaced with a realistic talking-head/lip-sync service later.')
