
import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# =========================================================
# CẤU HÌNH ỨNG DỤNG
# =========================================================
APP_NAME = "Career Compass_Quynh_"
APP_TITLE = "Khảo sát định hướng nghề nghiệp 30 câu_Quynh_Nhu"

st.set_page_config(
    page_title=f"{APP_TITLE} | {APP_NAME}",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# TIỆN ÍCH SVG -> DATA URI
# =========================================================
def svg_to_data_uri(svg: str) -> str:
    encoded = urllib.parse.quote(svg)
    return f"data:image/svg+xml;charset=UTF-8,{encoded}"

def make_icon_svg(title, subtitle, emoji, c1="#5B5BD6", c2="#14B8A6"):
    svg = f"""
    <svg width="700" height="420" viewBox="0 0 700 420" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="{c1}"/>
          <stop offset="100%" stop-color="{c2}"/>
        </linearGradient>
        <filter id="shadow">
          <feDropShadow dx="0" dy="16" stdDeviation="20" flood-opacity="0.20"/>
        </filter>
      </defs>
      <rect width="700" height="420" rx="40" fill="url(#bg)"/>
      <circle cx="575" cy="80" r="72" fill="#ffffff" opacity=".08"/>
      <circle cx="105" cy="360" r="90" fill="#ffffff" opacity=".07"/>
      <rect x="385" y="72" width="230" height="280" rx="34" fill="#ffffff" filter="url(#shadow)"/>
      <circle cx="500" cy="150" r="58" fill="#F4F5FF"/>
      <text x="500" y="170" text-anchor="middle" font-size="62">{emoji}</text>
      <rect x="430" y="235" width="140" height="13" rx="6.5" fill="#D9DDF3"/>
      <rect x="430" y="267" width="105" height="13" rx="6.5" fill="#D9DDF3"/>
      <rect x="430" y="299" width="155" height="13" rx="6.5" fill="#D9DDF3"/>
      <text x="72" y="132" fill="#EDE9FE" font-size="20" font-weight="700" font-family="Arial">{APP_NAME}</text>
      <text x="72" y="192" fill="#ffffff" font-size="42" font-weight="800" font-family="Arial">{title}</text>
      <text x="72" y="238" fill="#ffffff" font-size="42" font-weight="800" font-family="Arial">{subtitle}</text>
      <text x="72" y="292" fill="#EEF2FF" font-size="18" font-family="Arial">30 câu hỏi • 6 nhóm RIASEC • gợi ý nghề nghiệp</text>
    </svg>
    """
    return svg_to_data_uri(svg)

hero_image = make_icon_svg(
    "Khám phá", "nghề phù hợp", "🧭", "#4338CA", "#0F766E"
)

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
:root{
    --bg:#F5F7FB;
    --card:#FFFFFF;
    --text:#172033;
    --muted:#667085;
    --line:#E8ECF4;
    --primary:#5B5BD6;
    --primary-dark:#4338CA;
    --accent:#14B8A6;
    --soft:#EEF0FF;
    --shadow:0 12px 35px rgba(30,41,59,.08);
}
html, body, [class*="css"] { font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif; }
.stApp{
    background:
      radial-gradient(circle at 10% 0%, rgba(91,91,214,.10), transparent 28%),
      radial-gradient(circle at 90% 4%, rgba(20,184,166,.09), transparent 24%),
      var(--bg);
    color:var(--text);
}
.block-container{
    max-width:1180px;
    padding-top:1.2rem;
    padding-bottom:3rem;
}
#MainMenu, footer, header{visibility:hidden;}
.hero-wrap{
    background:white;
    border:1px solid var(--line);
    border-radius:30px;
    padding:10px;
    box-shadow:var(--shadow);
    margin-bottom:26px;
}
.hero-img{
    width:100%;
    border-radius:24px;
    display:block;
}
.section-title{
    font-size:28px;
    font-weight:900;
    letter-spacing:-.6px;
    margin:10px 0 8px 0;
}
.section-sub{
    color:var(--muted);
    line-height:1.65;
    margin-bottom:18px;
}
.card{
    background:rgba(255,255,255,.95);
    border:1px solid var(--line);
    border-radius:22px;
    padding:20px;
    box-shadow:var(--shadow);
}
.feature-card{
    background:linear-gradient(180deg,#fff,#FBFBFF);
    border:1px solid var(--line);
    border-radius:20px;
    padding:18px;
    min-height:150px;
}
.feature-icon{
    width:46px;height:46px;border-radius:14px;
    display:flex;align-items:center;justify-content:center;
    background:var(--soft);font-size:24px;margin-bottom:12px;
}
.feature-title{font-weight:850;font-size:17px;margin-bottom:6px;}
.feature-desc{color:var(--muted);font-size:14px;line-height:1.55;}
.q-card{
    background:#fff;
    border:1px solid var(--line);
    border-radius:18px;
    padding:16px 18px 12px 18px;
    margin:10px 0 8px 0;
    box-shadow:0 8px 22px rgba(30,41,59,.04);
}
.q-num{
    display:inline-flex;width:34px;height:34px;
    align-items:center;justify-content:center;
    background:var(--soft);color:var(--primary-dark);
    border-radius:10px;font-weight:900;margin-right:10px;
}
.q-text{font-size:16px;font-weight:760;line-height:1.5;}
.metric-box{
    background:linear-gradient(180deg,#FFFFFF,#FAFAFF);
    border:1px solid var(--line);
    border-radius:20px;
    padding:18px;
    text-align:center;
    box-shadow:0 8px 22px rgba(30,41,59,.04);
}
.metric-val{
    font-size:34px;font-weight:950;color:var(--primary-dark);line-height:1.1;
}
.metric-label{color:var(--muted);font-size:13px;font-weight:750;margin-top:5px;}
.result-card{
    background:#fff;
    border:1px solid var(--line);
    border-radius:22px;
    padding:20px;
    box-shadow:var(--shadow);
    height:100%;
}
.rank{
    font-size:12px;
    text-transform:uppercase;
    letter-spacing:.8px;
    font-weight:900;
    color:var(--primary);
}
.result-title{
    font-size:22px;font-weight:900;margin:5px 0 8px 0;
}
.result-desc{
    color:var(--muted);line-height:1.6;font-size:14px;
}
.pill{
    display:inline-block;
    background:#F1F3FF;
    color:#4F46E5;
    padding:6px 10px;
    border-radius:999px;
    margin:4px 5px 0 0;
    font-size:12px;
    font-weight:800;
}
.notice{
    background:#FFF7ED;
    border:1px solid #FED7AA;
    color:#7C2D12;
    border-radius:16px;
    padding:15px 16px;
    line-height:1.6;
}
div.stButton > button,
div[data-testid="stDownloadButton"] button{
    width:100%;
    border:none;
    border-radius:14px;
    padding:.85rem 1.1rem;
    font-weight:850;
    background:linear-gradient(135deg,#4F46E5,#7C3AED);
    color:white;
    box-shadow:0 10px 24px rgba(79,70,229,.20);
}
div.stButton > button:hover,
div[data-testid="stDownloadButton"] button:hover{
    color:white;border:none;transform:translateY(-1px);
}
.stProgress > div > div > div > div{
    background:linear-gradient(90deg,#5B5BD6,#14B8A6);
}
@media (max-width: 768px){
    .section-title{font-size:24px;}
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# DỮ LIỆU RIASEC
# =========================================================
questions = [
    ("R","Tôi thích sửa chữa, lắp ráp hoặc thao tác với máy móc, thiết bị."),
    ("I","Tôi thích tìm hiểu nguyên nhân của một vấn đề và phân tích dữ liệu để tìm câu trả lời."),
    ("A","Tôi thích sáng tạo hình ảnh, nội dung, âm nhạc hoặc những ý tưởng mới."),
    ("S","Tôi cảm thấy hứng thú khi hướng dẫn, hỗ trợ hoặc giúp người khác tiến bộ."),
    ("E","Tôi thích thuyết phục, đàm phán hoặc dẫn dắt người khác cùng đạt mục tiêu."),
    ("C","Tôi thích sắp xếp thông tin, hồ sơ, kế hoạch và làm việc theo quy trình rõ ràng."),
    ("R","Tôi thích những công việc tạo ra kết quả cụ thể bằng tay hoặc công cụ."),
    ("I","Tôi có hứng thú với nghiên cứu, công nghệ, khoa học hoặc giải quyết bài toán khó."),
    ("A","Tôi thường nghĩ ra nhiều cách thể hiện khác nhau cho cùng một ý tưởng."),
    ("S","Tôi thích lắng nghe và đưa ra lời khuyên khi người khác gặp khó khăn."),
    ("E","Tôi muốn thử sức trong kinh doanh, bán hàng hoặc phát triển dự án."),
    ("C","Tôi cảm thấy thoải mái khi làm việc với số liệu, biểu mẫu và lịch trình."),
    ("R","Tôi thích di chuyển, thao tác thực tế hơn là ngồi bàn làm việc suốt ngày."),
    ("I","Tôi thích kiểm chứng thông tin thay vì chỉ chấp nhận câu trả lời có sẵn."),
    ("A","Tôi quan tâm tới thiết kế, truyền thông, nghệ thuật hoặc cách kể chuyện hấp dẫn."),
    ("S","Tôi muốn công việc của mình tạo ra tác động tích cực trực tiếp cho con người."),
    ("E","Tôi thấy hứng thú với việc trình bày ý tưởng trước nhóm hoặc khách hàng."),
    ("C","Tôi chú ý chi tiết và thường phát hiện lỗi nhỏ trong tài liệu hoặc dữ liệu."),
    ("R","Tôi thích học qua thực hành, thử nghiệm trực tiếp và quan sát kết quả."),
    ("I","Tôi có thể kiên trì với một vấn đề trong thời gian dài để tìm ra lời giải hợp lý."),
    ("A","Tôi thích môi trường cho phép thử nghiệm phong cách và cách làm mới."),
    ("S","Tôi hợp với môi trường làm việc có nhiều tương tác và hợp tác giữa mọi người."),
    ("E","Tôi thích đặt mục tiêu, theo dõi kết quả và tạo ảnh hưởng tới quyết định của nhóm."),
    ("C","Tôi thích lập kế hoạch trước và cảm thấy hiệu quả hơn khi có hệ thống rõ ràng."),
    ("R","Tôi hứng thú với kỹ thuật, vận hành, sản xuất, xây dựng hoặc các công việc hiện trường."),
    ("I","Tôi muốn hiểu sâu cách một hệ thống hoạt động và tìm cách tối ưu nó."),
    ("A","Tôi thích viết, quay dựng, thiết kế hoặc phát triển trải nghiệm cho người dùng."),
    ("S","Tôi thích đào tạo, chăm sóc khách hàng, tư vấn hoặc làm việc cộng đồng."),
    ("E","Tôi tự tin khi thương lượng, kết nối quan hệ hoặc trình bày giá trị của một sản phẩm."),
    ("C","Tôi thích kiểm soát tiến độ, ngân sách, chứng từ hoặc các đầu việc cần độ chính xác."),
]

labels = {
    "R":"Thực tế – Kỹ thuật",
    "I":"Nghiên cứu – Phân tích",
    "A":"Sáng tạo – Nghệ thuật",
    "S":"Xã hội – Hỗ trợ",
    "E":"Quản lý – Kinh doanh",
    "C":"Tổ chức – Quy trình",
}

career_map = {
    "R":{
        "title":"Kỹ thuật – Công nghệ ứng dụng",
        "emoji":"🛠️",
        "desc":"Bạn có xu hướng thích thao tác thực tế, công cụ, máy móc, môi trường hiện trường và kết quả hữu hình.",
        "majors":["Cơ khí","Điện – điện tử","Ô tô","Xây dựng","Công nghệ kỹ thuật"],
        "jobs":["Kỹ sư cơ khí","Kỹ thuật điện","Kỹ thuật ô tô","Kỹ sư công trình","Kỹ sư vận hành"],
        "skills":["Tư duy kỹ thuật","Đọc bản vẽ","An toàn lao động","Giải quyết sự cố"],
        "c1":"#0F766E","c2":"#14B8A6"
    },
    "I":{
        "title":"Công nghệ – Dữ liệu – Nghiên cứu",
        "emoji":"🔬",
        "desc":"Bạn thiên về phân tích, tìm nguyên nhân, nghiên cứu hệ thống, dữ liệu và xử lý những vấn đề phức tạp.",
        "majors":["Công nghệ thông tin","Khoa học dữ liệu","AI","Phân tích kinh doanh","Nghiên cứu thị trường"],
        "jobs":["Data Analyst","Lập trình viên","AI/ML Engineer","Business Analyst","R&D"],
        "skills":["Logic","Python/SQL","Nghiên cứu","Tư duy hệ thống","Phân tích dữ liệu"],
        "c1":"#2563EB","c2":"#06B6D4"
    },
    "A":{
        "title":"Sáng tạo – Truyền thông – Thiết kế",
        "emoji":"🎨",
        "desc":"Bạn phù hợp với môi trường cho phép tạo ý tưởng, kể chuyện, thiết kế, nội dung và trải nghiệm mới.",
        "majors":["Marketing","Truyền thông","Thiết kế đồ họa","UI/UX","Sản xuất nội dung"],
        "jobs":["Content Marketing","Graphic Designer","UI/UX Designer","Video Creator","Brand Planner"],
        "skills":["Storytelling","Thiết kế","Viết nội dung","Visual thinking","Sáng tạo ý tưởng"],
        "c1":"#7C3AED","c2":"#EC4899"
    },
    "S":{
        "title":"Giáo dục – Tư vấn – Dịch vụ con người",
        "emoji":"🤝",
        "desc":"Bạn có động lực hỗ trợ, hướng dẫn, giao tiếp và tạo ảnh hưởng tích cực trực tiếp tới người khác.",
        "majors":["Giáo dục","Tâm lý học","Nhân sự","Công tác xã hội","Dịch vụ khách hàng"],
        "jobs":["Giáo viên","HR","Tư vấn viên","Customer Success","Chuyên viên đào tạo"],
        "skills":["Giao tiếp","Lắng nghe","Thuyết trình","Huấn luyện","Giải quyết xung đột"],
        "c1":"#059669","c2":"#84CC16"
    },
    "E":{
        "title":"Kinh doanh – Marketing – Quản lý",
        "emoji":"📈",
        "desc":"Bạn có xu hướng thích phát triển cơ hội, tạo ảnh hưởng, thương lượng, dẫn dắt mục tiêu và làm việc với thị trường.",
        "majors":["Quản trị kinh doanh","Marketing","Thương mại điện tử","Kinh doanh quốc tế","Quản trị dự án"],
        "jobs":["Marketing Executive","Sales","Business Development","Project Manager","Account Manager"],
        "skills":["Đàm phán","Thuyết phục","Lãnh đạo","Tư duy kinh doanh","Quản trị mục tiêu"],
        "c1":"#EA580C","c2":"#F59E0B"
    },
    "C":{
        "title":"Tài chính – Vận hành – Hệ thống",
        "emoji":"📊",
        "desc":"Bạn coi trọng độ chính xác, trật tự, dữ liệu, quy trình, lịch trình và sự ổn định trong công việc.",
        "majors":["Kế toán","Tài chính – Ngân hàng","Kiểm toán","Logistics","Quản trị vận hành"],
        "jobs":["Kế toán viên","Financial Analyst","Kiểm toán viên","Operations Executive","Supply Chain Planner"],
        "skills":["Excel","Quản lý dữ liệu","Kiểm soát quy trình","Lập kế hoạch","Độ chính xác"],
        "c1":"#475569","c2":"#64748B"
    },
}

combo_suggestions = {
    "AI":("Thiết kế sản phẩm số – UX Research",["UX Researcher","Product Designer","Creative Technologist"]),
    "AE":("Marketing sáng tạo – Thương hiệu",["Brand Marketing","Creative Planner","Social Media Strategist"]),
    "AS":("Truyền thông – Giáo dục sáng tạo",["Content Educator","Instructional Designer","Community Content"]),
    "EI":("Chiến lược – Phân tích kinh doanh",["Business Analyst","Growth Analyst","Product Manager"]),
    "EC":("Quản trị – Tài chính – Vận hành",["Operations Manager","Account Manager","Commercial Finance"]),
    "ES":("Kinh doanh dịch vụ – Phát triển khách hàng",["Consultant","Customer Success","HR Business Partner"]),
    "IC":("Dữ liệu – Tài chính – Kiểm soát",["Data Analyst","Risk Analyst","Financial Analyst"]),
    "IR":("Kỹ thuật – Công nghệ – R&D",["Software Engineer","Automation Engineer","R&D Engineer"]),
    "RC":("Vận hành – Kỹ thuật – Chất lượng",["QA/QC","Supply Chain","Production Planner"]),
    "RS":("Dịch vụ kỹ thuật – Hỗ trợ ứng dụng",["Kỹ thuật viên","Kỹ sư dịch vụ","Technical Support"]),
    "CS":("Hành chính – Dịch vụ – Nhân sự",["HR Operations","Academic Coordinator","Customer Operations"]),
}

scale_text = {
    1:"1 · Hoàn toàn không đúng",
    2:"2 · Ít đúng",
    3:"3 · Phân vân",
    4:"4 · Khá đúng",
    5:"5 · Rất đúng",
}

# =========================================================
# HERO
# =========================================================
st.markdown(
    f"""
    <div class="hero-wrap">
        <img src="{hero_image}" class="hero-img">
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# GIỚI THIỆU
# =========================================================
st.markdown('<div class="section-title">Bạn sẽ nhận được gì?</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">Ứng dụng giúp bạn nhìn rõ hơn khuynh hướng nghề nghiệp dựa trên sở thích và phong cách làm việc. Kết quả mang tính định hướng tham khảo.</div>',
    unsafe_allow_html=True
)

f1, f2, f3, f4 = st.columns(4)
features = [
    ("🧠","30 câu hỏi","Khảo sát ngắn gọn, tập trung vào sở thích, cách làm việc và môi trường bạn phù hợp."),
    ("🧭","6 nhóm RIASEC","Phân tích 6 nhóm: Kỹ thuật, Phân tích, Sáng tạo, Xã hội, Kinh doanh và Quy trình."),
    ("💼","Gợi ý ngành & nghề","Đề xuất nhóm ngành, nghề tiêu biểu và những vai trò bạn có thể tìm hiểu thêm."),
    ("🚀","Lộ trình phát triển","Gợi ý kỹ năng nên ưu tiên và các bước tiếp theo để kiểm chứng lựa chọn nghề nghiệp."),
]
for col, item in zip([f1,f2,f3,f4], features):
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-icon">{item[0]}</div>
                <div class="feature-title">{item[1]}</div>
                <div class="feature-desc">{item[2]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# THÔNG TIN NGƯỜI DÙNG
# =========================================================
st.markdown('<div class="section-title">1. Thông tin của bạn</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Thông tin chỉ dùng để cá nhân hóa kết quả trong phiên hiện tại.</div>', unsafe_allow_html=True)

c1,c2,c3 = st.columns([1.5,1,1])
with c1:
    name = st.text_input("Họ và tên", placeholder="Ví dụ: Nguyễn Minh Anh")
with c2:
    education = st.selectbox(
        "Trình độ hiện tại",
        ["THCS","THPT","Sinh viên","Mới tốt nghiệp","Đang đi làm","Khác"]
    )
with c3:
    priority = st.selectbox(
        "Ưu tiên nghề nghiệp",
        ["Chưa xác định","Thu nhập","Ổn định","Sáng tạo","Cơ hội thăng tiến","Cân bằng cuộc sống","Tác động xã hội"]
    )

# =========================================================
# KHẢO SÁT
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">2. Khảo sát 30 câu hỏi</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">Hãy chọn mức độ mô tả đúng với bạn nhất. Không có đáp án đúng hay sai.</div>',
    unsafe_allow_html=True
)

answers = {}
groups = [
    ("Nhóm 1 · Cách bạn thích làm việc",0,10),
    ("Nhóm 2 · Điều khiến bạn hứng thú",10,20),
    ("Nhóm 3 · Môi trường bạn cảm thấy phù hợp",20,30),
]

for gi,(title,start,end) in enumerate(groups):
    with st.expander(title, expanded=(gi==0)):
        for idx in range(start,end):
            cat,q = questions[idx]
            st.markdown(
                f"""
                <div class="q-card">
                    <span class="q-num">{idx+1}</span>
                    <span class="q-text">{q}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            answers[idx] = st.radio(
                f"q{idx+1}",
                options=[1,2,3,4,5],
                index=2,
                format_func=lambda x: scale_text[x],
                horizontal=True,
                key=f"q_{idx}",
                label_visibility="collapsed",
            )

st.markdown("**Tiến độ khảo sát**")
st.progress(1.0)
st.caption("30/30 câu đã sẵn sàng để chấm điểm.")

# =========================================================
# HÀM CHẤM ĐIỂM
# =========================================================
def calculate_scores():
    scores = {k:0 for k in labels}
    for idx,(cat,_) in enumerate(questions):
        scores[cat] += answers[idx]
    percentages = {k: round(v/25*100,1) for k,v in scores.items()}
    ranked = sorted(percentages.items(), key=lambda x:x[1], reverse=True)
    return scores, percentages, ranked

def combo_key(a,b):
    if a+b in combo_suggestions:
        return a+b
    if b+a in combo_suggestions:
        return b+a
    return None

st.markdown("<br>", unsafe_allow_html=True)
if st.button("✨ PHÂN TÍCH KẾT QUẢ NGHỀ NGHIỆP"):
    scores, percentages, ranked = calculate_scores()
    st.session_state["career_result"] = {
        "scores":scores,
        "percentages":percentages,
        "ranked":ranked,
        "name":name.strip() or "Bạn",
        "education":education,
        "priority":priority,
        "time":datetime.now().strftime("%d/%m/%Y %H:%M")
    }

# =========================================================
# KẾT QUẢ
# =========================================================
if "career_result" in st.session_state:
    result = st.session_state["career_result"]
    ranked = result["ranked"]
    top1, top2, top3 = ranked[:3]

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">3. Kết quả định hướng nghề nghiệp</div>', unsafe_allow_html=True)
    st.success(
        f"{result['name']} có khuynh hướng nổi bật nhất ở nhóm **{labels[top1[0]]}**."
    )

    m1,m2,m3 = st.columns(3)
    for col,data,label_rank in zip(
        [m1,m2,m3],[top1,top2,top3],["Top 1","Top 2","Top 3"]
    ):
        with col:
            st.markdown(
                f"""
                <div class="metric-box">
                    <div class="metric-val">{data[1]:.0f}%</div>
                    <div class="metric-label">{label_rank} · {labels[data[0]]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("### Bản đồ 6 nhóm khuynh hướng")
    chart_df = pd.DataFrame({
        "Nhóm":[labels[k] for k,_ in ranked],
        "Mức phù hợp (%)":[v for _,v in ranked]
    }).set_index("Nhóm")
    st.bar_chart(chart_df)

    st.markdown("### 3 hướng nổi bật nhất")
    cols = st.columns(3)
    for i,(cat,pct) in enumerate([top1,top2,top3],start=1):
        info = career_map[cat]
        career_image = make_icon_svg(
            info["title"].split(" – ")[0],
            "Hướng nghề nổi bật",
            info["emoji"],
            info["c1"],
            info["c2"],
        )
        majors_html = "".join([f'<span class="pill">{x}</span>' for x in info["majors"][:4]])
        with cols[i-1]:
            st.image(career_image, use_container_width=True)
            st.markdown(
                f"""
                <div class="result-card">
                    <div class="rank">Gợi ý #{i} · {pct:.0f}%</div>
                    <div class="result-title">{info["title"]}</div>
                    <div class="result-desc">{info["desc"]}</div>
                    <div style="margin-top:12px">{majors_html}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("### Nghề nghiệp nên tham khảo")
    j1,j2,j3 = st.columns(3)
    for col,(cat,pct) in zip([j1,j2,j3],[top1,top2,top3]):
        with col:
            st.markdown(f"**{career_map[cat]['title']}**")
            for job in career_map[cat]["jobs"]:
                st.markdown(f"- {job}")

    ck = combo_key(top1[0], top2[0])
    st.markdown("### Hướng kết hợp tiềm năng")
    if ck:
        combo_title, combo_jobs = combo_suggestions[ck]
        st.info(
            f"**{combo_title}** — sự kết hợp giữa **{labels[top1[0]]}** và **{labels[top2[0]]}**. "
            f"Các vai trò nên tìm hiểu thêm: {', '.join(combo_jobs)}."
        )
    else:
        st.info(
            f"Bạn có sự kết hợp giữa **{labels[top1[0]]}** và **{labels[top2[0]]}**. "
            "Nên trải nghiệm dự án ngắn, khóa học thử hoặc công việc bán thời gian để kiểm chứng mức độ phù hợp."
        )

    skills = []
    for cat in [top1[0], top2[0]]:
        for skill in career_map[cat]["skills"]:
            if skill not in skills:
                skills.append(skill)

    st.markdown("### Kỹ năng nên ưu tiên phát triển")
    s1,s2 = st.columns(2)
    cut = (len(skills)+1)//2
    with s1:
        for skill in skills[:cut]:
            st.markdown(f"- **{skill}**")
    with s2:
        for skill in skills[cut:]:
            st.markdown(f"- **{skill}**")

    st.markdown("### Lộ trình gợi ý trong 4 bước")
    st.markdown("""
1. **Chọn 2–3 nhóm ngành** từ kết quả trên để tìm hiểu kỹ hơn.
2. **Đọc mô tả công việc thực tế** và xem yêu cầu tuyển dụng của các vị trí tiêu biểu.
3. **Thử trải nghiệm ngắn** qua khóa học, dự án cá nhân, CLB, thực tập hoặc việc bán thời gian.
4. **Đối chiếu lại** với năng lực học tập, điều kiện cá nhân, mục tiêu thu nhập và thị trường lao động.
""")

    with st.expander("Xem bảng điểm chi tiết 6 nhóm"):
        detail_df = pd.DataFrame([
            {
                "Mã":cat,
                "Nhóm khuynh hướng":labels[cat],
                "Điểm":result["scores"][cat],
                "Tối đa":25,
                "Mức phù hợp":f"{result['percentages'][cat]:.1f}%"
            }
            for cat,_ in ranked
        ])
        st.dataframe(detail_df, use_container_width=True, hide_index=True)

    export_df = pd.DataFrame([
        {
            "Ho_ten":result["name"],
            "Trinh_do":result["education"],
            "Uu_tien":result["priority"],
            "Ma_RIASEC":cat,
            "Nhom":labels[cat],
            "Diem":result["scores"][cat],
            "Muc_phu_hop_%":result["percentages"][cat],
            "Thoi_gian":result["time"]
        }
        for cat,_ in ranked
    ])
    csv_data = export_df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "⬇️ TẢI KẾT QUẢ CSV",
        data=csv_data,
        file_name=f"ket_qua_dinh_huong_nghe_{result['name'].replace(' ','_')}.csv",
        mime="text/csv"
    )

    st.markdown(
        """
        <div class="notice">
            <b>Lưu ý:</b> Đây là công cụ định hướng tham khảo dựa trên mô hình RIASEC.
            Kết quả không phải chẩn đoán tâm lý và không nên là căn cứ duy nhất để quyết định ngành học hoặc nghề nghiệp.
            Bạn nên kết hợp thêm năng lực học tập, trải nghiệm thực tế, điều kiện cá nhân và thông tin thị trường lao động.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div style="text-align:center;color:#98A2B3;font-size:13px;padding:18px 0">
        {APP_NAME} · {APP_TITLE} · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
