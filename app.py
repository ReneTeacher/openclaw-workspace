"""
English Vocabulary Review App - Streamlit Version
靚靚英文生字溫習程式
"""

import streamlit as st
import random
import json
from pathlib import Path
from datetime import datetime

# ======== 設定 ========
st.set_page_config(
    page_title="English Vocab Trainer",
    page_icon="📚",
    layout="centered"
)

VOCAB_FILE = "vocabulary.txt"
DATA_FILE = "progress.json"

# ======== CSS - 靚靚介面 ========
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .card {
        background: white;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        text-align: center;
    }
    .word-display {
        font-size: 48px;
        font-weight: bold;
        color: #2c3e50;
        margin: 20px 0;
        padding: 20px;
        background: #f8f9fa;
        border-radius: 15px;
    }
    .score-display {
        font-size: 72px;
        font-weight: bold;
        color: #27ae60;
    }
    .progress-text {
        font-size: 24px;
        color: #7f8c8d;
    }
    .correct {
        color: #27ae60;
        font-size: 20px;
    }
    .wrong {
        color: #e74c3c;
        font-size: 20px;
    }
    .stButton>button {
        border-radius: 25px;
        padding: 15px 40px;
        font-size: 18px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 15px;
        padding: 15px;
        font-size: 20px;
    }
    h1, h2, h3 {
        color: #2c3e50 !important;
    }
    .stat-box {
        background: white;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# ======== Functions ========
def load_vocabulary():
    """Load vocabulary from file"""
    if Path(VOCAB_FILE).exists():
        with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    return ["apple", "beautiful", "computer", "education", "friendship"]

def load_progress():
    """Load user progress"""
    if Path(DATA_FILE).exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"total": 0, "correct": 0, "history": []}

def save_progress(progress):
    """Save user progress"""
    with open(DATA_FILE, 'w') as f:
        json.dump(progress, f)

def text_to_speech(word):
    """Generate speech using browser's speech synthesis"""
    return f"""
    <script>
    function speak() {{
        const utterance = new SpeechSynthesisUtterance('{word}');
        utterance.lang = 'en-US';
        utterance.rate = 0.8;
        speechSynthesis.speak(utterance);
    }}
    </script>
    <button onclick="speak()" style="
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border: none;
        border-radius: 50%;
        width: 80px;
        height: 80px;
        font-size: 32px;
        cursor: pointer;
        box-shadow: 0 5px 20px rgba(245, 87, 108, 0.4);
    ">🔊</button>
    """

# ======== Session State ========
if 'current_word' not in st.session_state:
    st.session_state.current_word = ""
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'words_queue' not in st.session_state:
    st.session_state.words_queue = []
if 'feedback' not in st.session_state:
    st.session_state.feedback = None
if 'quiz_mode' not in st.session_state:
    st.session_state.quiz_mode = False

# ======== Main App ========
st.markdown('<div class="card">', unsafe_allow_html=True)

# Header
st.title("📚 English Vocab Trainer")
st.markdown("**英文生字溫習程式**")

# Load data
vocab = load_vocabulary()
progress = load_progress()

# Menu
menu = st.selectbox("選擇模式 / Choose Mode:", 
    ["🎯 開始溫習 / Start Quiz", "📊 統計 / Statistics", "📝 生字表 / Word List"])

if menu == "🎯 開始溫習 / Start Quiz":
    if not st.session_state.quiz_mode:
        if st.button("🚀 開始 Start"):
            st.session_state.words_queue = random.sample(vocab, min(10, len(vocab)))
            st.session_state.current_word = st.session_state.words_queue.pop(0)
            st.session_state.score = 0
            st.session_state.total = 0
            st.session_state.feedback = None
            st.session_state.quiz_mode = True
            st.rerun()
    
    if st.session_state.quiz_mode:
        st.markdown("---")
        
        # Score display
        st.markdown(f'<p class="progress-text">問題 {st.session_state.total + 1}/10</p>', unsafe_allow_html=True)
        
        # Play audio button
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            st.markdown(text_to_speech(st.session_state.current_word), unsafe_allow_html=True)
        
        # Word display (hidden for dictation)
        st.markdown(f'<div class="word-display">🔤</div>', unsafe_allow_html=True)
        
        # Input
        user_answer = st.text_input("寫低個字 / Type the word:", 
            key="answer", placeholder="Type here...")
        
        # Submit
        if st.button("✅ 提交 Submit"):
            if user_answer.strip().lower() == st.session_state.current_word.lower():
                st.session_state.score += 1
                st.session_state.feedback = "correct"
                st.success("✅ 正呀！Correct!")
            else:
                st.session_state.feedback = "wrong"
                st.error(f"❌ 錯咗！正確係: **{st.session_state.current_word}**")
            
            st.session_state.total += 1
            
            # Next word or finish
            if st.session_state.words_queue:
                st.session_state.current_word = st.session_state.words_queue.pop(0)
                # Clear input by changing key
                st.rerun()
            else:
                # Quiz finished
                st.markdown("---")
                st.markdown(f'<div class="score-display">🎯 {st.session_state.score}/{st.session_state.total}</div>', unsafe_allow_html=True)
                
                pct = st.session_state.score / st.session_state.total * 100
                if pct >= 90:
                    st.balloons()
                    st.markdown("🌟 **全對！叻叻！Perfect!**")
                elif pct >= 70:
                    st.markdown("💪 **做得好好！Good Job!**")
                else:
                    **繼續努力！Keep Practicing!**
                
                # Save progress
                progress["total"] += st.session_state.total
                progress["correct"] += st.session_state.score
                save_progress(progress)
                
                if st.button("🔄 再試過 Try Again"):
                    st.session_state.quiz_mode = False
                    st.rerun()

elif menu == "📊 統計 / Statistics":
    st.markdown("### 📊 你的統計 Your Statistics")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="stat-box"><h2>{progress["correct"]}</h2><p>正確 Correct</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stat-box"><h2>{progress["total"]}</h2><p>總題目 Total</p></div>', unsafe_allow_html=True)
    
    if progress["total"] > 0:
        pct = progress["correct"] / progress["total"] * 100
        st.progress(pct / 100)
        st.write(f"**準確率: {pct:.1f}%**")
    
    if st.button("🗑️ 清除統計 Clear Stats"):
        progress = {"total": 0, "correct": 0, "history": []}
        save_progress(progress)
        st.rerun()

elif menu == "📝 生字表 / Word List":
    st.markdown("### 📝 生字表 Word List")
    st.write(f"**總共 {len(vocab)} 個生字**")
    
    # Show words in a nice grid
    cols = st.columns(4)
    for i, word in enumerate(vocab):
        with cols[i % 4]:
            st.markdown(f"**{i+1}.** {word}")

st.markdown('</div>', unsafe_allow_html=True)
