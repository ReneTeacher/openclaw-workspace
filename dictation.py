#!/usr/bin/env python3
"""
英文生字聽寫程式
Vocabulary Dictation Program
"""

import random
import time
from pathlib import Path

# ====== 你自己改呢度 ======
VOCAB_FILE = "vocabulary.txt"  # 生字檔案（每行一個字）
SPEAK = True                   # 係咪要讀出嚟？（需要 pip install pyttsx3）
# =========================

def load_vocabulary(filename):
    """load 生字 from file"""
    if Path(filename).exists():
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    return []

def speak(text):
    """讀個字出嚟"""
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print(f"🔊 [讀緊: {text}]")

def dictation():
    words = load_vocabulary(VOCAB_FILE)
    
    if not words:
        # 如果冇file，用呢啲default生字
        words = ["apple", "beautiful", "computer", "dictionary", 
                 "education", "friendship", "government", "happiness"]
        print(f"📝 用 default 生字庫（共 {len(words)} 個）")
    
    random.shuffle(words)
    correct = 0
    
    print("\n" + "="*40)
    print("🎧 英文生字聽寫程式")
    print("="*40)
    print(f"總共有 {len(words)} 個字\n")
    
    for i, word in enumerate(words, 1):
        print(f"\n【第 {i}/{len(words)} 題】")
        
        if SPEAK:
            speak(word)
            time.sleep(0.5)
        
        user_input = input("寫低個字: ").strip().lower()
        
        if user_input == word.lower():
            print("✅ 正呀！")
            correct += 1
        else:
            print(f"❌ 錯咗，正確係: {word}")
    
    # 結果
    print("\n" + "="*40)
    print(f"🎯 總分: {correct}/{len(words)} ({correct*100//len(words)}%)")
    
    if correct == len(words):
        print("🌟 全對！叻叻！")
    elif correct >= len(words)*0.8:
        print("💪 好叻呀！差少少咋！")
    else:
        print("📚 繼續努力！多啲溫習！")
    print("="*40 + "\n")

if __name__ == "__main__":
    dictation()
