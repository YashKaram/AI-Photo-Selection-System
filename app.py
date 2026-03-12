import streamlit as st
import os
from scorer import total_score

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Photo Selector",
    page_icon="📸",
    layout="wide"
)
st.markdown("""
<div class="bg-animation">
  <canvas id="particleCanvas"></canvas>
  <div class="floating-photos">
    <img src="https://picsum.photos/120?1">
    <img src="https://picsum.photos/120?2">
    <img src="https://picsum.photos/120?3">
    <img src="https://picsum.photos/120?4">
    <img src="https://picsum.photos/120?5">
  </div>
  <div class="shutter"></div>
</div>

<style>

/* ---------- BASE BG ---------- */
.bg-animation {
  position: fixed;
  inset: 0;
  z-index: -1;
  overflow: hidden;
}

/* Animated gradient */
.bg-animation::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(-45deg,#1f1c2c,#928DAB,#3a7bd5,#00d2ff);
  background-size: 400% 400%;
  animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
  0%{background-position:0% 50%}
  50%{background-position:100% 50%}
  100%{background-position:0% 50%}
}

/* ---------- FLOATING PHOTOS ---------- */
.floating-photos img {
  position: absolute;
  width: 120px;
  border-radius: 12px;
  opacity: 0.25;
  animation: float 20s linear infinite;
}

.floating-photos img:nth-child(1){left:10%;top:80%;animation-duration:25s}
.floating-photos img:nth-child(2){left:30%;top:90%;animation-duration:22s}
.floating-photos img:nth-child(3){left:60%;top:85%;animation-duration:27s}
.floating-photos img:nth-child(4){left:80%;top:88%;animation-duration:24s}
.floating-photos img:nth-child(5){left:50%;top:95%;animation-duration:26s}

@keyframes float {
  from{transform:translateY(0)}
  to{transform:translateY(-120vh)}
}

/* ---------- CANVAS ---------- */
#particleCanvas {
  position:absolute;
  inset:0;
}

/* ---------- SHUTTER ---------- */
.shutter {
  position: fixed;
  inset: 0;
  background: black;
  animation: shutterFlash 1.2s ease forwards;
  pointer-events:none;
}

@keyframes shutterFlash {
  0%{opacity:1}
  40%{opacity:0}
  100%{opacity:0}
}

</style>

<script>
const canvas = document.getElementById("particleCanvas");
const ctx = canvas.getContext("2d");

function resize(){
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
resize();
window.addEventListener("resize",resize);

let particles=[];
for(let i=0;i<60;i++){
  particles.push({
    x:Math.random()*canvas.width,
    y:Math.random()*canvas.height,
    r:Math.random()*2+1,
    vx:(Math.random()-0.5)*0.5,
    vy:(Math.random()-0.5)*0.5
  });
}

let mouse={x:0,y:0};
window.addEventListener("mousemove",e=>{
  mouse.x=e.clientX;
  mouse.y=e.clientY;
});

function draw(){
  ctx.clearRect(0,0,canvas.width,canvas.height);

  particles.forEach(p=>{
    let dx=p.x-mouse.x;
    let dy=p.y-mouse.y;
    let dist=Math.sqrt(dx*dx+dy*dy);

    if(dist<120){
      p.x+=dx*0.01;
      p.y+=dy*0.01;
    }

    p.x+=p.vx;
    p.y+=p.vy;

    if(p.x<0)p.x=canvas.width;
    if(p.x>canvas.width)p.x=0;
    if(p.y<0)p.y=canvas.height;
    if(p.y>canvas.height)p.y=0;

    ctx.beginPath();
    ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
    ctx.fillStyle="rgba(255,255,255,0.5)";
    ctx.fill();
  });

  requestAnimationFrame(draw);
}
draw();
</script>
""", unsafe_allow_html=True)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

/* -------- Animated Gradient Background -------- */
.stApp {
    background: linear-gradient(-45deg, #1f1c2c, #928DAB, #3a7bd5, #00d2ff);
    background-size: 400% 400%;
    animation: gradientMove 12s ease infinite;
}

/* Gradient Animation */
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* -------- Floating Particles -------- */
.stApp::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    top: -50%;
    left: -50%;
    background-image: radial-gradient(white 1px, transparent 1px);
    background-size: 40px 40px;
    opacity: 0.08;
    animation: particlesMove 60s linear infinite;
    pointer-events: none;
}

/* Particle Motion */
@keyframes particlesMove {
    from { transform: translate(0,0); }
    to { transform: translate(200px,200px); }
}

/* -------- Glass UI Panels -------- */
.upload-box, .photo-card {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
}

/* -------- Title Glow -------- */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: white;
    text-shadow: 0 0 15px rgba(255,255,255,0.5);
}

/* -------- Subtitle -------- */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #f1f1f1;
    margin-bottom: 30px;
}

/* -------- Buttons -------- */
button {
    border-radius: 10px !important;
    transition: 0.25s;
}

button:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">📸 AI Best Photo Selector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload many photos → AI picks your best shots ✨</div>', unsafe_allow_html=True)

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# ---------- OPTIONS ----------
col1, col2 = st.columns([2,1])

with col1:
    uploaded_files = st.file_uploader(
        "Upload Photos",
        type=["jpg","jpeg","png"],
        accept_multiple_files=True
    )

with col2:
    best_n = st.slider(
        "How many best photos?",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )
    insta_mode = st.toggle("Instagram Preview Mode")
    photo_mode = st.radio(
    "Photo Type",
    ["Single", "Group", "Mixed"],
    horizontal=True
    )

# ---------- PROCESS ----------
if uploaded_files:

    image_paths = []

    for file in uploaded_files:
        path = os.path.join(UPLOAD_DIR, file.name)
        with open(path, "wb") as f:
            f.write(file.read())
        image_paths.append(path)

    from duplicate_remover import remove_duplicates

    unique_paths = remove_duplicates(image_paths)
    scores = [(p, total_score(p, photo_mode)) for p in unique_paths]
    scores.sort(key=lambda x: x[1], reverse=True)

    st.markdown(f"## 🏆 Top {best_n} Best Photos")

    cols = st.columns(best_n)

    for i, (img, sc) in enumerate(scores[:best_n]):
        with cols[i]:
            st.markdown('<div class="photo-card">', unsafe_allow_html=True)
            if insta_mode:
                st.image(img, width=250)
            else:
                st.image(img, use_container_width=True)
            st.markdown(f"**Rank #{i+1}**")
            st.progress(min(sc,1.0))
            st.markdown(f"Score: **{round(sc,3)}**")
            st.markdown('</div>', unsafe_allow_html=True)