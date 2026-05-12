import streamlit as st
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MicroDegree | Register",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

html, body, [class*="css"] { font-family: 'Lora', Georgia, serif; }

/* Hero */
.hero-banner {
    background: linear-gradient(135deg, #0d0d12 0%, #1a1228 50%, #0d0d1a 100%);
    border-radius: 18px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
}
.hero-banner .badge {
    display: inline-block;
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .15em;
    text-transform: uppercase;
    color: #e8a020;
    border: 1px solid rgba(232,160,32,.4);
    border-radius: 2rem;
    padding: 4px 14px;
    margin-bottom: 1rem;
}
.hero-banner h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    line-height: 1.2;
    background: linear-gradient(135deg, #fff 40%, #fde68a 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: .6rem;
}
.hero-banner p { color: #9090b0; font-style: italic; }

/* Stats bar */
.stats-bar { display: flex; justify-content: center; gap: 3rem; margin: 1.5rem 0 0; flex-wrap: wrap; }
.stat-item { text-align: center; }
.stat-item strong { display: block; font-family: 'Syne', sans-serif; font-size: 1.5rem; font-weight: 800; color: #e8a020; }
.stat-item span { font-size: .72rem; color: #9090b0; text-transform: uppercase; letter-spacing: .09em; }

/* Section labels */
.section-label {
    font-family: 'Syne', sans-serif;
    font-size: .68rem;
    font-weight: 700;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: #e8a020;
    margin: 2rem 0 .75rem;
}

/* Project cards */
.proj-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: .9rem; margin: 1rem 0 1.5rem; }
.proj-card {
    background: #1e1e2e;
    border: 1px solid #2e2e44;
    border-radius: 14px;
    padding: 1.1rem;
    transition: border .2s;
}
.proj-card:hover { border-color: rgba(232,160,32,.55); }
.proj-card .icon { font-size: 1.6rem; margin-bottom: .4rem; }
.proj-card h4 { font-family: 'Syne', sans-serif; font-size: .82rem; font-weight: 700; color: #e8e8f0; margin-bottom: .3rem; }
.proj-card p { font-size: .74rem; color: #9090b0; line-height: 1.55; font-style: italic; }

/* Congrats banner */
.congrats-banner {
    background: linear-gradient(135deg, #1a2e0d, #0d1a1e);
    border: 1px solid rgba(100,200,100,.3);
    border-radius: 16px;
    padding: 1.75rem;
    text-align: center;
    margin: 1rem 0 1.5rem;
}
.congrats-banner h2 {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: #7edd7e;
    margin: .5rem 0 .3rem;
}
.congrats-banner p { font-size: .9rem; color: #9eb8a0; font-style: italic; }

/* Submit button */
div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #c8880a, #e8a020);
    color: #0d0d12;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: .95rem;
    border: none;
    border-radius: 10px;
    padding: .75rem 1rem;
    cursor: pointer;
    transition: opacity .2s;
}
div.stButton > button:hover { opacity: .9; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="badge">MicroDegree Organisation</div>
  <h1>Unlock your tech future,<br>one skill at a time.</h1>
  <p>Industry-led courses designed for the real world.<br>Register now and start building.</p>
  <div class="stats-bar">
    <div class="stat-item"><strong>12,000+</strong><span>Learners</span></div>
    <div class="stat-item"><strong>48</strong><span>Courses</span></div>
    <div class="stat-item"><strong>94%</strong><span>Job-ready rate</span></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Registration Form ─────────────────────────────────────────────────────────
st.markdown('<p class="section-label">Create your account</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    first_name = st.text_input("First Name", placeholder="e.g. Arjun")
with col2:
    last_name = st.text_input("Last Name", placeholder="e.g. Sharma")

email = st.text_input("Email Address", placeholder="you@example.com")

col3, col4 = st.columns(2)
with col3:
    phone = st.text_input("Phone Number", placeholder="+91 98765 43210")
with col4:
    city = st.text_input("City", placeholder="Bangalore")

track = st.selectbox("Choose Your Track", [
    "— Select a course track —",
    "Full Stack Web Development",
    "Data Science & Machine Learning",
    "Python Programming",
    "Cloud & DevOps Engineering",
    "UI/UX Design",
    "Cybersecurity Fundamentals",
])

source = st.selectbox("How did you hear about us?", [
    "— Select —", "YouTube", "Friends / Referral",
    "LinkedIn", "Google Search", "Instagram",
])

register = st.button("Register & Unlock Projects →")

# ── Post-submit excitement ────────────────────────────────────────────────────
if register:
    if not first_name or not email or track == "— Select a course track —":
        st.error("Please fill in your name, email, and select a track to continue.")
    else:
        with st.spinner("Setting up your learning journey..."):
            time.sleep(1.2)

        st.balloons()

        st.markdown(f"""
        <div class="congrats-banner">
          <div style="font-size:2.5rem">🎉</div>
          <h2>Welcome, {first_name}! 🎊</h2>
          <p>You've unlocked <strong style="color:#7edd7e">3 exclusive projects</strong> to get started right away.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<p class="section-label">Your unlocked projects</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="proj-grid">
          <div class="proj-card">
            <div class="icon">⚡</div>
            <h4>Build a Portfolio Site</h4>
            <p>HTML, CSS & JS from scratch. Ship a live site in 3 days.</p>
          </div>
          <div class="proj-card">
            <div class="icon">🧠</div>
            <h4>Sentiment Analyser</h4>
            <p>Python + ML. Classify product reviews with real data.</p>
          </div>
          <div class="proj-card">
            <div class="icon">🚀</div>
            <h4>REST API with FastAPI</h4>
            <p>Build & deploy a JSON API with authentication.</p>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        st.markdown('<p class="section-label">Watch before you begin</p>', unsafe_allow_html=True)

        vid1, vid2 = st.columns(2)
        with vid1:
            st.video("https://youtu.be/epRCCsUvJN8?si=x7sjAFhCniYhvbk3")
        with vid2:
            st.video("https://youtu.be/m3YFGPoefeM?si=lhisBOhdvyvJbfs_")

        st.divider()

        st.markdown(
            "📺 Explore all our content on the "
            "[MicroDegree YouTube channel →](https://www.youtube.com/@MicroDegree/videos)",
            unsafe_allow_html=False,
        )