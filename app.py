import streamlit as st
from model import generate_story

st.set_page_config(page_title="AI Story Continuation", page_icon="📖", layout="centered")

st.title("📖 AI Story Continuation System")
st.write("Enter the beginning of a story and let DistilGPT2 continue it.")

prompt = st.text_area(
    "Your story opening",
    placeholder="One rainy evening, a student discovered a mysterious box in the college library...",
    height=150,
)
col1, col2 = st.columns(2)
with col1:
    length_choice = st.selectbox("Continuation length", ["Short", "Long"])
with col2:
    temperature = st.slider("Creativity (temperature)", 0.2, 1.5, 0.8, 0.1)

max_new_tokens = 45 if length_choice == "Short" else 110

if st.button("Continue my story", type="primary", use_container_width=True):
    if not prompt.strip():
        st.warning("Please enter a story opening first.")
    else:
        with st.spinner("Generating your story..."):
            try:
                continuation = generate_story(prompt, max_new_tokens, temperature)
                st.subheader("Your original opening")
                st.info(prompt.strip())
                st.subheader("Generated continuation")
                st.write(continuation)
            except Exception as exc:
                st.error(str(exc))

st.caption(
    "Demo notice: AI-generated text may be repetitive, incomplete, or incorrect. "
    "Review the generated continuation before using it."
)
