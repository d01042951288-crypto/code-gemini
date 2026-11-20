import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="나만의 학습게임 만들기!", page_icon="🎮", layout="wide")

st.markdown('''
    <style>
    .stApp {
        background-color: #f8f9fa;
        scroll-behavior: smooth;
    }
    .header-section {
        background: linear-gradient(135deg, #6c3ce9, #8b5cf6);
        color: white;
        padding: 3rem 2rem;
        border-radius: 0 0 30px 30px;
        margin-top: -3rem; 
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 15px rgba(108, 60, 233, 0.3);
    }
    .header-text h1 {
        color: #fde047; 
        font-weight: 900;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .header-text p {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    .step-badge {
        background-color: #3b0764; 
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    .step-title {
        font-size: 1.5rem;
        font-weight: 900;
        color: #1e1e1e;
        margin-bottom: 1.5rem;
    }
    .game-card {
        background-color: white;
        border-radius: 20px;
        padding: 0;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 2px solid transparent;
        transition: all 0.3s ease;
        margin-bottom: 15px;
        overflow: hidden;
    }
    .game-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    .card-header {
        padding: 15px;
        font-weight: bold;
        font-size: 1.2rem;
        border-radius: 20px 20px 0 0;
    }
    .bg-purple { background-color: #c4b5fd; color: #4c1d95; }
    .bg-blue { background-color: #bfdbfe; color: #1e3a8a; }
    .bg-green { background-color: #bbf7d0; color: #14532d; }
    .bg-yellow { background-color: #fef08a; color: #713f12; }
    .bg-cyan { background-color: #a5f3fc; color: #164e63; }
    .bg-red { background-color: #fecaca; color: #7f1d1d; }
    
    .card-body {
        padding: 20px;
        font-size: 0.9rem;
        color: #4b5563;
        text-align: left;
    }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        border-radius: 15px !important;
        border: 1px solid #d1d5db !important;
        padding: 12px 15px !important;
    }
    .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2) !important;
    }
    .recommend-box {
        background-color: #e0f2fe; 
        border: 2px solid #bae6fd;
        border-radius: 20px;
        padding: 20px;
        height: 100%;
    }
    .topic-item {
        background: white; 
        padding: 10px 15px; 
        border-radius: 12px;
        border: 1px solid #e5e7eb; 
        margin-bottom: 10px;
        font-size: 0.9rem;
        color: #1f2937;
    }
    .prompt-section {
        background-color: #4c1d95;
        border-radius: 20px;
        padding: 30px;
        color: white;
        margin-top: 2rem;
    }
    .guide-box {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #e5e7eb;
        text-align: center;
        height: 100%;
    }
    .guide-step {
        background-color: #f3f4f6;
        color: #4b5563;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-bottom: 10px;
        display: inline-block;
    }
    </style>
''', unsafe_allow_html=True)

st.markdown('''
<div class="header-section">
    <div class="header-text">
        <h1>🎮 나만의 학습게임 만들기!</h1>
        <p>공부도 게임처럼 재미있게! 내가 직접 게임을 기획하고 AI와 함께 만들어보자!</p>
        <p style="font-size: 0.9rem; margin-top: 10px;">어떤 게임을 만들고 싶나요? 마음에 드는 게임을 골라 나만의 학습게임을 만들어보세요!</p>
    </div>
    <div style="background: white; padding: 15px; border-radius: 15px; border: 3px solid #1e1e1e; width: 250px; text-align: center;">
        <div style="background: #facc15; padding: 5px; border-radius: 5px; font-weight: bold; margin-bottom: 10px;">게임 메이커</div>
        <div style="background: #1e1e1e; padding: 20px; border-radius: 10px; color: white;">
            <div style="font-size: 2rem;">👾</div>
            <div style="margin-top: 10px; color: #4ade80;">액션 게임</div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

st.markdown('<div class="step-badge">STEP 1</div><div class="step-title">어떤 게임을 만들까요?</div>', unsafe_allow_html=True)
st.caption("카드를 눌러 게임을 고르고, 마음을 정했다면 버튼을 눌러요.")

games = [
    {"title": "🚀 슈팅 게임", "color": "bg-purple", "desc": "화면에 나타나는 적이나 물체를 조준하고 발사하는 게임", "subject": "수학, 영어, 과학, 사회"},
    {"title": "🏃 액션 게임", "color": "bg-blue", "desc": "캐릭터를 움직여 장애물을 피하고 미션을 수행하는 게임", "subject": "영어, 국어, 음악"},
    {"title": "❓ 퀴즈 게임", "color": "bg-green", "desc": "문제를 풀고 정답을 맞히면서 점수를 얻는 게임", "subject": "전 과목"},
    {"title": "🗺️ 어드벤처 게임", "color": "bg-yellow", "desc": "여러 장소를 탐험하면서 문제를 해결하고 보물을 찾는 게임", "subject": "과학, 사회, 국어"},
    {"title": "🧩 퍼즐 게임", "color": "bg-cyan", "desc": "규칙을 발견하거나 조각을 맞추어 문제를 해결하는 게임", "subject": "수학, 과학"},
    {"title": "🏎️ 레이싱 게임", "color": "bg-red", "desc": "자동차나 캐릭터를 조종하여 목표 지점까지 달리는 게임", "subject": "수학, 영어"},
    {"title": "🏪 타이쿤·경영", "color": "bg-green", "desc": "가게나 도시를 운영하며 목표를 달성하는 게임", "subject": "수학, 사회"},
    {"title": "🔒 방탈출 게임", "color": "bg-yellow", "desc": "숨겨진 단서를 찾고 문제를 해결하여 방을 탈출하는 게임", "subject": "국어, 수학, 사회"}
]

if 'selected_game' not in st.session_state:
    st.session_state.selected_game = "❓ 퀴즈 게임"
if 'scroll_to_step2' not in st.session_state:
    st.session_state.scroll_to_step2 = False

cols = st.columns(4)
for i, game in enumerate(games):
    with cols[i % 4]:
        st.markdown(f'''
        <div class="game-card">
            <div class="card-header {game['color']}">{game['title']}</div>
            <div class="card-body">
                <p><strong>{game['desc']}</strong></p>
                <p style="font-size: 0.8rem; color: #6b7280; margin-top: 10px;">활용 과목: {game['subject']}</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button(f"{game['title']} 선택", key=f"btn_{i}", use_container_width=True):
            st.session_state.selected_game = game['title']
            st.session_state.scroll_to_step2 = True

st.success(f"현재 선택된 게임: **{st.session_state.selected_game}**")
st.markdown("---")

st.markdown('<div id="step2-anchor" style="padding-top: 2rem;"></div>', unsafe_allow_html=True)
st.markdown('<div class="step-badge">STEP 2</div><div class="step-title">나만의 게임 기획하기</div>', unsafe_allow_html=True)

if st.session_state.scroll_to_step2:
    # time.time()을 주입하여 코드가 매번 다르도록(고유하게) 만듦 -> 스트림릿이 강제로 다시 실행함
    js_code = f'''
    <script>
        // Force refresh: {time.time()}
        const anchor = window.parent.document.getElementById('step2-anchor');
        if (anchor) {{
            anchor.scrollIntoView({{behavior: 'smooth', block: 'start'}});
        }}
    </script>
    '''
    components.html(js_code, height=0)
    st.session_state.scroll_to_step2 = False 

st.caption("빈칸을 채워도 괜찮아요. 비워 둔 칸에는 예시가 들어가요.")

col1, col2 = st.columns([2, 1])
with col1:
    grade = st.radio("학년 수준", ["1학년", "2학년", "3학년", "4학년", "5학년", "6학년"], index=5, horizontal=True)
    title_input = st.text_input("게임 제목", placeholder="예: 역사 히어로즈 대작전")
    topic_input = st.text_area("학습 주제", placeholder="예: 우리나라 역사 인물 알아보기 (단군왕검, 세종대왕, 이순신 등)")
    rules_input = st.text_area("게임 규칙 및 방법", placeholder="예: 각 스테이지마다 역사 인물에 대한 퀴즈가 나오고, 맞히면 다음 단계로 넘어감.")
    design_input = st.text_input("디자인 스타일", placeholder="예: 레트로 픽셀 아트 스타일, 배경음악은 웅장하게")
    
    title = title_input if title_input else "[제목을 입력해주세요]"
    topic = topic_input if topic_input else "[주제를 입력해주세요]"
    rules = rules_input if rules_input else "[게임 규칙을 입력해주세요]"
    design = design_input if design_input else "[디자인 스타일을 입력해주세요]"

with col2:
    st.markdown(f'''
    <div class="recommend-box">
        <h4 style="color: #0284c7; margin-top: 0;">{grade} 추천 학습 주제</h4>
        <p style="font-size: 0.85rem; color: #475569;">스스로 학습 주제를 정하기 어렵다면 활용해보세요.</p>
        <div class="topic-item"><strong>국어:</strong> 우리말의 구조와 쓰임</div>
        <div class="topic-item"><strong>과학:</strong> 우리 몸의 구조와 기능</div>
        <div class="topic-item"><strong>역사:</strong> 조선시대의 문화와 과학 발전</div>
        <p style="font-size: 0.8rem; color: #64748b; margin-top: 15px;">💡 작성하신 내용, 특히 칸에 쓰인 모든 의견장에는 추천 정보입니다.</p>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="step-badge">STEP 3</div><div class="step-title">게임 제작 프롬프트 복사하기</div>', unsafe_allow_html=True)
st.caption("내가 쓴 내용을 기반으로 AI에게 명령할 프롬프트가 완성되었어요!")

clean_game_type = st.session_state.selected_game.split(" ")[1] if " " in st.session_state.selected_game else st.session_state.selected_game

prompt_text = f'''너는 훌륭하고 실력 있는 게임 개발 프로그래머야. 초등학생 {grade} 수준에 맞게 좋아하는 요소들과 학습을 결합해 즐길 수 있는 재미있는 웹 기반 게임을 만들어야 해. HTML, CSS, JavaScript 코드를 합쳐서 하나의 HTML 파일 코드로 결과를 완성해서 보여줘.

[게임 기획]
- 게임 제목: {title}
- 학습 주제: {topic}
- 게임 규칙 및 방법: {rules}
- 디자인 스타일: {design}
- 게임 종류: {clean_game_type}
- 학년 수준: 초등학생 {grade}

[코드 작성 시 필수 조건]
- 코드는 반드시 분리하지 말고 하나의 index.html 파일 안에 포함되도록 작성해 줘.
'''

st.info("💡 아래 코드 박스 우측 상단의 📋 버튼을 누르면 프롬프트가 복사됩니다.")
st.markdown('<div class="prompt-section">', unsafe_allow_html=True)
st.code(prompt_text, language="markdown")
st.markdown('</div>', unsafe_allow_html=True)

if st.button("🌟 제미나이(Gemini) 열기", use_container_width=True):
    st.markdown('<meta http-equiv="refresh" content="0; url=https://gemini.google.com/">', unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="step-badge">STEP 4</div><div class="step-title">게임 제작 방법 안내</div>', unsafe_allow_html=True)

cols2 = st.columns(4)
steps = [
    ("STEP 1", "만들고 싶은 게임을 선택한다.", "#9333ea"),
    ("STEP 2", "게임 제목, 규칙/방법, 디자인을 정한다.", "#2563eb"),
    ("STEP 3", "작성된 프롬프트를 복사하여 AI에게 명령을 내린다.", "#16a34a"),
    ("STEP 4", "AI가 만든 코드를 복사해서 HTML 파일을 만든다.", "#ca8a04")
]

for i, (step, text, color) in enumerate(steps):
    with cols2[i]:
        st.markdown(f'''
        <div class="guide-box" style="border-top: 4px solid {color};">
            <div class="guide-step" style="color: {color}; background-color: {color}20;">{step}</div>
            <p style="font-weight: bold; color: #374151; font-size: 0.9rem;">{text}</p>
        </div>
        ''', unsafe_allow_html=True)
