
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="R25 Formative Calculator",
    page_icon="📊",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.title {
    text-align: center;
    color: #2457a7;
    font-size: 32px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: gray;
    font-size: 16px;
}
.result {
    background-color: #e8f1ff;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Heading
st.markdown(
    '<div class="title">📊 R25 Formative Assessment Calculator</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Calculate your formative marks out of 60</div>',
    unsafe_allow_html=True
)

st.divider()

# Module I
st.header("📘 Module-I Marks")

col1, col2 = st.columns(2)

with col1:
    fa1 = st.number_input("FA-1 (Out of 10)", 0.0, 10.0, 0.0)
    fa2 = st.number_input("FA-2 (Out of 20)", 0.0, 20.0, 0.0)

with col2:
    cla1 = st.number_input("CLA-1 (Out of 10)", 0.0, 10.0, 0.0)
    cla2 = st.number_input("CLA-2 (Out of 10)", 0.0, 10.0, 0.0)

module1 = fa1 + fa2 + cla1 + cla2
module1_scaled = (module1 / 50) * 20

st.info(f"Module-I: {module1:.2f} / 50  →  {module1_scaled:.2f} / 20")

st.divider()

# Module II
st.header("📗 Module-II Marks")

col3, col4 = st.columns(2)

with col3:
    fa3 = st.number_input("FA-3 (Out of 20)", 0.0, 20.0, 0.0)
    fa4 = st.number_input("FA-4 (Out of 20)", 0.0, 20.0, 0.0)

with col4:
    cla3 = st.number_input("CLA-3 (Out of 10)", 0.0, 10.0, 0.0)
    cla4 = st.number_input("CLA-4 (Out of 10)", 0.0, 10.0, 0.0)

module2 = fa3 + fa4 + cla3 + cla4
module2_scaled = (module2 / 60) * 30

st.info(f"Module-II: {module2:.2f} / 60  →  {module2_scaled:.2f} / 30")

st.divider()

# Experiential Learning
st.header("🧪 Experiential Learning")

el = st.number_input(
    "Enter Experiential Learning Marks (Out of 10)",
    min_value=0.0,
    max_value=10.0,
    value=0.0
)

st.divider()

# Calculate total
total = module1_scaled + module2_scaled + el

# Results
st.header("🎯 Your Formative Result")

col5, col6, col7 = st.columns(3)

with col5:
    st.metric("Module-I", f"{module1_scaled:.2f}/20")

with col6:
    st.metric("Module-II", f"{module2_scaled:.2f}/30")

with col7:
    st.metric("Experiential", f"{el:.2f}/10")

st.markdown("### Total Formative Score")

st.markdown(
    f"""
    <div class="result">
        <h1 style="color:#2457a7;">{total:.2f} / 60</h1>
        <h4>R25 Formative Assessment Score</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.progress(min(total / 60, 1.0))

st.caption(f"Percentage: {(total / 60) * 100:.2f}%")

st.divider()

# Disclaimer
st.warning("""
**Disclaimer:** This calculation is based on the R25 assessment pattern
provided for this calculator. It is an estimated formative score, not
the final academic score. Actual scores may vary according to department
rules, assessment changes and relative grading.
""")

st.markdown(
    "<center>Made for R25 Students ❤️</center>",
    unsafe_allow_html=True
)
