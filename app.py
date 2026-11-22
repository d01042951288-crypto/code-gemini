import streamlit as st
import streamlit.components.v1 as components

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
    
    /* 프롬프트 박스 커스텀 디자인 */
    .prompt-box {
        background-color: #4c1d95; /* 짙은 보라색 */
        border-radius: 15px;
        padding: 20px;
        color: white;
        margin-top: 10px;
        line-height: 1.8;
        font-size: 0.95rem;
    }
    .prompt-header {
        background-color: #8b5cf6;
        display: inline-block;
        padding: 4px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .highlight-user {
        background-color: #fef08a; /* 노란색 형광펜 (사용자 입력) */
        color: #713f12;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
    }
    .highlight-example {
        background-color: #86efac; /* 초록색 형광펜 (예시 문구) */
        color: #14532d;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
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
    {"title": "🚀 슈팅 게임", "color": "bg-purple", "desc": "화면에 나타나는 적이나 물체를 조준하고 발사하는 게임", "subject": "수학, 영어, 과학, 사회", "raw_title": "슈팅 게임 (화면에 나타나는 적이나 물체를 조준하고 발사하는 게임)"},
    {"title": "🏃 액션 게임", "color": "bg-blue", "desc": "캐릭터를 움직여 장애물을 피하고 미션을 수행하는 게임", "subject": "영어, 국어, 음악", "raw_title": "액션 게임 (캐릭터를 움직여 장애물을 피하고 미션을 수행하는 게임)"},
    {"title": "❓ 퀴즈 게임", "color": "bg-green", "desc": "문제를 풀고 정답을 맞히면서 점수를 얻는 게임", "subject": "전 과목", "raw_title": "퀴즈 게임 (문제를 풀고 정답을 맞히면서 점수를 얻는 게임)"},
    {"title": "🗺️ 어드벤처 게임", "color": "bg-yellow", "desc": "여러 장소를 탐험하면서 문제를 해결하고 보물을 찾는 게임", "subject": "과학, 사회, 국어", "raw_title": "어드벤처 게임 (여러 장소를 탐험하면서 문제를 해결하고 보물을 찾는 게임)"},
    {"title": "🧩 퍼즐 게임", "color": "bg-cyan", "desc": "규칙을 발견하거나 조각을 맞추어 문제를 해결하는 게임", "subject": "수학, 과학", "raw_title": "퍼즐 게임 (규칙을 발견하거나 조각을 맞추어 문제를 해결하는 게임)"},
    {"title": "🏎️ 레이싱 게임", "color": "bg-red", "desc": "자동차나 캐릭터를 조종하여 목표 지점까지 달리는 게임", "subject": "수학, 영어", "raw_title": "레이싱 게임 (자동차나 캐릭터를 조종하여 목표 지점까지 달리는 게임)"},
    {"title": "🏪 타이쿤·경영", "color": "bg-green", "desc": "가게나 도시를 운영하며 목표를 달성하는 게임", "subject": "수학, 사회", "raw_title": "타이쿤 게임 (가게나 도시를 운영하며 목표를 달성하는 게임)"},
    {"title": "🔒 방탈출 게임", "color": "bg-yellow", "desc": "숨겨진 단서를 찾고 문제를 해결하여 방을 탈출하는 게임", "subject": "국어, 수학, 사회", "raw_title": "방탈출 게임 (숨겨진 단서를 찾고 문제를 해결하여 방을 탈출하는 게임)"}
]

if 'selected_game_raw' not in st.session_state:
    st.session_state.selected_game_raw = "퀴즈 게임 (문제를 풀고 정답을 맞히면서 점수를 얻는 게임)"
    st.session_state.selected_game_short = "❓ 퀴즈 게임"
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
            st.session_state.selected_game_raw = game['raw_title']
            st.session_state.selected_game_short = game['title']
            st.session_state.scroll_to_step2 = True

st.success(f"현재 선택된 게임: **{st.session_state.selected_game_short}**")
st.markdown("---")

st.markdown('<div id="step2-anchor" style="padding-top: 2rem;"></div>', unsafe_allow_html=True)
st.markdown('<div class="step-badge">STEP 2</div><div class="step-title">나만의 게임 기획하기</div>', unsafe_allow_html=True)

if st.session_state.scroll_to_step2:
    js_code = '''
    <script>
        const anchor = window.parent.document.getElementById('step2-anchor');
        if (anchor) {
            anchor.scrollIntoView({behavior: 'smooth', block: 'start'});
        }
    </script>
    '''
    components.html(js_code, height=0)
    st.session_state.scroll_to_step2 = False 

col1, col2 = st.columns([2, 1])
with col1:
    grade = st.radio("학년 수준", ["1학년", "2학년", "3학년", "4학년", "5학년", "6학년"], index=5, horizontal=True)
    title_input = st.text_input("게임 제목", placeholder="예: 역사 히어로즈 대작전")
    topic_input = st.text_area("학습 주제", placeholder="예: 우리나라 역사 인물 알아보기 (단군왕검, 세종대왕, 이순신 등)")
    rules_input = st.text_area("게임 규칙 및 방법", placeholder="예: 문제 10개가 하나씩 나오고 보기 4개 중에서 정답을 골라요. 빨리 맞힐수록 점수를 더 많이 얻고, 끝나면 최고 점수를 보여 줘요.")
    design_input = st.text_input("디자인 스타일", placeholder="예: 신나는 TV 퀴즈 쇼, 파란색과 노란색")
    
    title_val = title_input if title_input else "역사 퀴즈왕 도전!"
    title_cls = "highlight-user" if title_input else "highlight-example"
    
    topic_val = topic_input if topic_input else "사회 - 우리나라 역사 인물"
    topic_cls = "highlight-user" if topic_input else "highlight-example"
    
    rules_val = rules_input if rules_input else "문제 10개가 하나씩 나오고 보기 4개 중에서 정답을 골라요. 빨리 맞힐수록 점수를 더 많이 얻고, 끝나면 최고 점수를 보여 줘요."
    rules_cls = "highlight-user" if rules_input else "highlight-example"
    
    design_val = design_input if design_input else "신나는 TV 퀴즈 쇼, 파란색과 노란색"
    design_cls = "highlight-user" if design_input else "highlight-example"

with col2:
    st.markdown(f'''
    <div class="recommend-box">
        <h4 style="color: #0284c7; margin-top: 0;">{grade} 추천 학습 주제</h4>
        <p style="font-size: 0.85rem; color: #475569;">스스로 학습 주제를 정하기 어렵다면 활용해보세요.</p>
        <div class="topic-item"><strong>국어:</strong> 우리말의 구조와 쓰임</div>
        <div class="topic-item"><strong>과학:</strong> 우리 몸의 구조와 기능</div>
        <div class="topic-item"><strong>역사:</strong> 조선시대의 문화와 과학 발전</div>
        <p style="font-size: 0.8rem; color: #64748b; margin-top: 15px;">💡 빈 칸에 들어갈 예시가 적혀 있어요.</p>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="step-badge">STEP 3</div><div class="step-title">게임 제작 프롬프트 복사하기</div>', unsafe_allow_html=True)
st.caption("내가 쓴 내용을 기반으로 AI에게 명령할 프롬프트가 완성되었어요!")

st.markdown('''
    <div style="display: flex; gap: 10px; margin-bottom: 10px; font-size: 0.85rem; font-weight: bold;">
        <span style="background-color: #fef08a; padding: 2px 8px; border-radius: 5px;">노란색: 내가 쓴 내용</span>
        <span style="background-color: #86efac; padding: 2px 8px; border-radius: 5px;">민트색: 비워 둔 칸에 들어간 예시</span>
    </div>
''', unsafe_allow_html=True)

visual_prompt = f'''
<div class="prompt-box">
    <div class="prompt-header">🔴🟡🟢 복사할 게임 제작 프롬프트</div><br>
    너는 친절하고 실력 있는 게임 개발 프로그래머야. 초등학교 {grade} 학생인 내가 혼자서도 실행하고 친구들과 함께 즐길 수 있는 재미있는 웹 학습 게임을 만들려고 해. HTML, CSS, JavaScript 코문을 합쳐서 하나의 HTML 파일 코드로 전체를 완성해서 보여줘.<br><br>
    
    [게임 조건]<br><br>
    
    게임 제목: <span class="{title_cls}">{title_val}</span><br>
    학습 주제: <span class="{topic_cls}">{topic_val}</span><br>
    게임 규칙 및 방법: <span class="{rules_cls}">{rules_val}</span><br>
    디자인 스타일: <span class="{design_cls}">{design_val}</span><br>
    게임 종류: <span class="highlight-example">{st.session_state.selected_game_raw}</span><br>
    학년 수준: <span class="highlight-example">초등학교 {grade}</span> (문제 난이도와 낱말을 이 학년에 맞춰 줘)<br><br>
    
    코드는 복사해서 바로 실행할 수 있도록 &lt;!DOCTYPE html&gt;부터 시작해서 전체 코드를 빠짐없이 완벽하게 작성해 줘.<br><br>
    
    [추가 개발 조건]<br><br>
    
    <span class="highlight-example">초등학교 {grade}</span> 학생도 쉽게 이해하고 즐길 수 있도록 만들어 줘.<br>
    게임 시작, 일시정지, 다시 시작 버튼을 만들어 줘.<br>
    점수와 남은 시간 또는 게임 진행 상황을 표시해 줘.<br>
    정답과 오답에 따라 재미있는 피드백을 보여 줘.<br>
    게임이 끝나면 최종 점수와 결과를 보여 줘.<br>
    마우스와 키보드, 스마트폰 터치로 조작할 수 있도록 해 줘.<br>
    별도의 설치나 유료 프로그램 없이 실행할 수 있게 해 줘.<br>
    외부 라이브러리나 서버 없이 하나의 HTML 파일만으로 실행되도록 해 줘.<br>
    게임에 필요한 문제와 정답을 충분히 포함해 줘.<br>
    오류 없이 작동하도록 코드를 점검해 줘.<br>
    코드 설명은 간단하게 하고, 실행 가능한 전체 코드를 먼저 보여 줘.
</div>
'''

plain_prompt_text = f'''너는 친절하고 실력 있는 게임 개발 프로그래머야. 초등학교 {grade} 학생인 내가 혼자서도 실행하고 친구들과 함께 즐길 수 있는 재미있는 웹 학습 게임을 만들려고 해. HTML, CSS, JavaScript 코드를 합쳐서 하나의 HTML 파일 코드로 전체를 완성해서 보여줘.

[게임 조건]

게임 제목: {title_val}
학습 주제: {topic_val}
게임 규칙 및 방법: {rules_val}
디자인 스타일: {design_val}
게임 종류: {st.session_state.selected_game_raw}
학년 수준: 초등학교 {grade} (문제 난이도와 낱말을 이 학년에 맞춰 줘)

코드는 복사해서 바로 실행할 수 있도록 <!DOCTYPE html>부터 시작해서 전체 코드를 빠짐없이 완벽하게 작성해 줘.

[추가 개발 조건]

초등학교 {grade} 학생도 쉽게 이해하고 즐길 수 있도록 만들어 줘.
게임 시작, 일시정지, 다시 시작 버튼을 만들어 줘.
점수와 남은 시간 또는 게임 진행 상황을 표시해 줘.
정답과 오답에 따라 재미있는 피드백을 보여 줘.
게임이 끝나면 최종 점수와 결과를 보여 줘.
마우스와 키보드, 스마트폰 터치로 조작할 수 있도록 해 줘.
별도의 설치나 유료 프로그램 없이 실행할 수 있게 해 줘.
외부 라이브러리나 서버 없이 하나의 HTML 파일만으로 실행되도록 해 줘.
게임에 필요한 문제와 정답을 충분히 포함해 줘.
오류 없이 작동하도록 코드를 점검해 줘.
코드 설명은 간단하게 하고, 실행 가능한 전체 코드를 먼저 보여 줘.'''

st.markdown(visual_prompt, unsafe_allow_html=True)
st.caption("👇 아래 '프롬프트 복사하기' 버튼을 눌러 복사한 뒤, 제미나이(Gemini)에 붙여넣기 해주세요.")

# --- 추가된 복사 버튼 (HTML/JS 컴포넌트 활용) ---
copy_button_html = f'''
<textarea id="prompt-text" style="display:none;">{plain_prompt_text}</textarea>
<button onclick="copyText()" style="width: 100%; padding: 12px; background-color: #8b5cf6; color: white; border: none; border-radius: 10px; font-size: 1rem; font-weight: bold; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 10px;">
    📋 프롬프트 복사하기
</button>
<script>
function copyText() {{
    var text = document.getElementById("prompt-text").value;
    navigator.clipboard.writeText(text).then(function() {{
        alert("프롬프트가 복사되었습니다! 제미나이(Gemini)에 붙여넣어 주세요.");
    }}).catch(function(err) {{
        console.error("복사 실패:", err);
        alert("복사에 실패했습니다. 다른 브라우저를 이용해주세요.");
    }});
}}
</script>
'''
components.html(copy_button_html, height=70)
# ---------------------------------------------------

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
