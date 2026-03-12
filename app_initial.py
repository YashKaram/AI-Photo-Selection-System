import streamlit as st
import os
from scorer import total_score

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

st.title("📸 AI Best Photo Selector")
st.write("Upload many photos → AI picks best 5")

uploaded_files = st.file_uploader(
    "Upload Photos",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    image_paths = []

    for file in uploaded_files:
        path = os.path.join(UPLOAD_DIR, file.name)
        with open(path, "wb") as f:
            f.write(file.read())
        image_paths.append(path)

    scores = []

    for path in image_paths:
        s = total_score(path)
        scores.append((path, s))

    scores.sort(key=lambda x: x[1], reverse=True)

    st.subheader("🏆 Best 5 Photos")

    for img, sc in scores[:5]:
        st.image(img, caption=f"Score: {round(sc,3)}", use_container_width=True)