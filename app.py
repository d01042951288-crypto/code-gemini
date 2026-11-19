import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="나만의 학습게임 기획하기", page_icon="🎮", layout="wide")

# 커스텀 CSS (다채롭고 고채도의 둥근 디자인 적용)
st.markdown('''
    <style>
    /* 전체적으로 둥글고 다채로운 고채도 디자인 */
    .step-header {
        color: #111;
        font-weight: 900;
        font-size: 1.6rem;
        margin-top: 2.5rem;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .badge {
        background: linear-gradient(135deg, #FF007F, #7000FF); /* 핫핑크~네온보라 그라데이션 */
        color: white;
        padding: 8px 22px;
        border-radius: 50px; /* 완전 둥글게 */
        font-size: 1rem;
        font-weight: 900;
        box-shadow: 0 4px 15px rgba(255, 0, 127, 0.4);
    }
    .recommend-box {
        background-color: #E0FFFF; /* 밝고 쨍한 시안(Cyan) 바탕 */
        border: 4px solid #00DDFF; /* 고채도 시안 테두리 */
        border-radius: 30px; /* 아주 둥글게 */
        padding: 25px;
        height: 100%;
        box-shadow: 0 8px 20px rgba(0, 221, 255, 0.25);
    }
    .topic-item {
        background: white; 
        padding: 12px 15px; 
        border-radius: 20px; /* 둥근 내부 박스 */
        border: 2px solid #00DDFF; 
        margin-bottom: 12px;
        font-weight: bold;
        color: #005566;
        box-shadow: 0 2px 8px rgba(0, 221, 255, 0.1);
    }
    .guide-box {
        background-color: #FFFFFF;
        border-radius: 30px; /* 아주 둥글게 */
        padding: 25px;
        margin-bottom: 10px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.08);
        border: 4px solid;
    }
    
    /* 스트림릿 기본 입력창 둥글게 & 고채도 테두리 설정 */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        border-radius: 20px !important;
        border: 2px solid #7000FF !important; /* 네온 보라색 테두리 */
        padding: 10px 15px !important;
    }
    .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
        border-color: #FF007F !important; /* 클릭 시 핫핑크 */
        box-shadow: 0 0 12px rgba(255, 0, 127, 0.4) !important;
    }
    </style>
''', unsafe_allow_html=True)

# --- STEP 1 ---
st.markdown('<div class="step-header"><span class="badge">STEP 1</span> 나만의 게임 기획하기</div>', unsafe_allow_html=True)
st.caption("빈칸을 채워서 재미있는 게임을 만들어보세요. 예시가 들어가 있어요.")

col1, col2 = st.columns([2, 1])

with col1:
    game_type = st.radio(
        "게임 종류", 
        ["📝 퀴즈", "⚔️ 액션", "🎲 보드", "🗺️ 어드벤처", "🧩 퍼즐", "⌨️ 타이핑", "⏱️ 타이머 경쟁", "🚪 방탈출"], 
        horizontal=True
    )
    
    grade = st.radio(
        "학년 수준", 
        ["1학년", "2학년", "3학년", "4학년", "5학년", "6학년"], 
        index=5, 
        horizontal=True
    )
    
    # 흐린 글씨(placeholder) 유지
    title_input = st.text_input("게임 제목", placeholder="예: 역사 히어로즈 대작전")
    topic_input = st.text_area("학습 주제", placeholder="예: 우리나라 역사 인물 알아보기 (단군왕검, 세종대왕, 이순신 등)")
    rules_input = st.text_area("게임 규칙 및 방법", placeholder="예: 각 스테이지마다 역사 인물에 대한 퀴즈가 나오고, 맞히면 다음 단계로 넘어감. 틀리면 목숨이 줄어듦. 총 3번 틀리면 게임 오버.")
    design_input = st.text_input("디자인 스타일", placeholder="예: 레트로 픽셀 아트 스타일, 배경음악은 웅장하게")
    
    title = title_input if title_input else "[제목을 입력해주세요]"
    topic = topic_input if topic_input else "[주제를 입력해주세요]"
    rules = rules_input if rules_input else "[게임 규칙을 입력해주세요]"
    design = design_input if design_input else "[디자인 스타일을 입력해주세요]"

with col2:
    st.markdown(f'''
    <div class="recommend-box">
        <h4 style="color: #0088AA; margin-top: 0; font-weight: 900; font-size: 1.3rem;">{grade} 추천 학습 주제</h4>
        <p style="font-size: 0.95rem; color: #006688; font-weight: bold;">스스로 학습 주제를 정하기 어렵다면 활용해보세요.</p>
        <div class="topic-item">
            <span style="color: #FF007F;">국어:</span> 우리말의 구조와 쓰임
        </div>
        <div class="topic-item">
            <span style="color: #FF007F;">과학:</span> 우리 몸의 구조와 기능
        </div>
        <div class="topic-item">
            <span style="color: #FF007F;">역사:</span> 조선시대의 문화와 과학 발전
        </div>
        <p style="font-size: 0.85rem; color: #007799; margin-top: 15px;">
            💡 작성하신 내용, 특히 칸에 쓰인 모든 의견장에는 추천 정보입니다.
        </p>
    </div>
    ''', unsafe_allow_html=True)


# --- STEP 2 ---
st.markdown("---")
st.markdown('<div class="step-header"><span class="badge">STEP 2</span> 게임 제작 프롬프트 복사하기</div>', unsafe_allow_html=True)
st.caption("내가 쓴 내용을 기반으로 AI에게 명령할 프롬프트가 완성되었어요!")

clean_game_type = game_type.split(" ")[1]

prompt_text = f'''너는 훌륭하고 실력 있는 게임 개발 프로그래머야. 초등학생 {grade} 수준에 맞게 좋아하는 요소들과 학습을 결합해 즐길 수 있는 재미있는 웹 기반 게임을 만들어야 해. HTML, CSS, JavaScript 코드를 합쳐서 하나의 HTML 파일 코드로 결과를 완성해서 보여줘.

[게임 기획]
- 게임 제목: {title}
- 학습 주제: {topic}
- 게임 규칙 및 방법: {rules}
- 디자인 스타일: {design}
- 게임 종류: {clean_game_type}
- 학년 수준: 초등학생 {grade} (이 수준의 학생이 이해하고 즐길 수 있도록 만들어 줘)

[코드 작성 시 필수 조건]
- 코드는 반드시 분리하지 말고 하나의 index.html 파일 안에 HTML, CSS, JS가 모두 포함되도록 작성해 줘.

[세부 개발 조건]
1. 모바일 기기에서도 화면이 깨지지 않고 잘 보이도록 반응형으로 만들어 줘.
2. 게임 시작 전 타이틀 화면이 있어야 하며, '게임 시작' 버튼을 만들어 줘.
3. 점수나 남은 시간, 목숨 등을 화면 상단에 잘 보이게 표시해 줘.
4. 정답을 맞추거나 틀렸을 때 시각적인 효과나 색상 변화를 줘서 바로 알 수 있게 해 줘.
5. 게임이 끝나면 최종 점수와 함께 '다시 하기' 버튼이 나타나게 해 줘.
6. 디자인은 제시한 스타일에 맞게 최대한 예쁘고 가독성 좋게 꾸며 줘.
7. 필요한 이미지가 있다면 CSS 속성을 이용해 직접 그리거나 이모지를 활용해 줘.
8. 배경색, 글꼴색 등은 눈이 편안한 색상 조합을 사용해 줘.
9. 코드 실행은 간단하게 구동 가능하며, 실행 가능한 전체 코드를 코드 블록에 넣어 줘.
'''

st.info("💡 아래 코드 박스 우측 상단의 📋 버튼을 누르면 프롬프트가 복사됩니다.")
st.code(prompt_text, language="markdown")

if st.button("🌟 제미나이(Gemini) 열기", use_container_width=True):
    st.markdown('<meta http-equiv="refresh" content="0; url=https://gemini.google.com/">', unsafe_allow_html=True)


# --- STEP 3 ---
st.markdown("---")
st.markdown('<div class="step-header"><span class="badge">STEP 3</span> 게임 제작 방법 안내</div>', unsafe_allow_html=True)

st.markdown('''
<div style="display: flex; gap: 15px; flex-wrap: wrap;">
    <div class="guide-box" style="flex: 1; min-width: 200px; border-color: #FF007F;">
        <h4 style="color: #FF007F; font-weight: 900; margin-top: 0;">STEP 1</h4>
        <p style="font-weight: bold; color: #333;">만들고 싶은 게임을 기획한다.</p>
    </div>
    <div class="guide-box" style="flex: 1; min-width: 200px; border-color: #00DDFF;">
        <h4 style="color: #00DDFF; font-weight: 900; margin-top: 0;">STEP 2</h4>
        <p style="font-weight: bold; color: #333;">게임 제목, 규칙/방법 내용, 규칙, 디자인을 정한다.</p>
    </div>
    <div class="guide-box" style="flex: 1; min-width: 200px; border-color: #00FF55;">
        <h4 style="color: #00CC44; font-weight: 900; margin-top: 0;">STEP 3</h4>
        <p style="font-weight: bold; color: #333;">작성된 제작 프롬프트를 복사하여 AI에게 명령을 내린다.</p>
    </div>
    <div class="guide-box" style="flex: 1; min-width: 200px; border-color: #7000FF;">
        <h4 style="color: #7000FF; font-weight: 900; margin-top: 0;">STEP 4</h4>
        <p style="font-weight: bold; color: #333;">제미나이가 만들어준 코드를 복사해서 HTML 파일을 만들어 확인하고 수정한다.</p>
    </div>
</div>

<div style="background-color: #FFFF00; border: 4px solid #FF9900; border-radius: 30px; padding: 25px; margin-top: 20px; box-shadow: 0 8px 20px rgba(255, 153, 0, 0.3);">
    <h4 style="color: #FF5500; margin-top: 0; font-weight: 900; font-size: 1.3rem;">💡 제미나이가 만든 코드로 게임 실행하기</h4>
    <ol style="color: #AA3300; line-height: 1.8; font-weight: bold; padding-left: 20px;">
        <li>제미나이가 만든 HTML 코드를 우측 상단의 <span style="background: #FF5500; color: white; padding: 2px 8px; border-radius: 10px;">복사 버튼</span>을 눌러 복사합니다.</li>
        <li>컴퓨터(PC) 바탕화면에서 마우스 우클릭 후 <span style="color: #FF007F;">새로 만들기 > 텍스트 문서</span>를 선택합니다.</li>
        <li>텍스트 문서(메모장)를 열고 복사한 코드를 <span style="color: #7000FF;">붙여넣기(Ctrl+V)</span> 합니다.</li>
        <li>상단 메뉴에서 <span style="color: #00AAFF;">파일 > 다른 이름으로 저장</span>을 클릭합니다.</li>
        <li>파일 이름을 <code style="background: white; padding: 3px 8px; border-radius: 8px; border: 2px solid #FF9900;">game.html</code>로 적고, 파일 형식은 '모든 파일'로 변경 후 저장합니다.</li>
        <li>저장된 <code style="background: white; padding: 3px 8px; border-radius: 8px; border: 2px solid #FF9900;">game.html</code> 파일을 더블클릭하면 웹 브라우저에서 나만의 게임이 실행됩니다!</li>
    </ol>
</div>
''', unsafe_allow_html=True)
