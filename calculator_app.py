import streamlit as st
import math, cmath

# ==============================
# PAGE SETUP
# ==============================
st.set_page_config(page_title="Advanced Calculator", page_icon="🧮", layout="centered")

# Custom CSS for styling (dark & light themes)
st.markdown("""
<style>
    .stTextInput input {
        font-size: 20px !important;
        text-align: right;
    }
    .calc-button {
        font-size: 20px;
        width: 70px;
        height: 70px;
        margin: 5px;
        border-radius: 15px;
        font-weight: bold;
    }
    .title {
        text-align: center;
        font-size: 30px;
        color: #10c132;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🧮 Advanced Python Calculator</div>", unsafe_allow_html=True)

# ==============================
# ENVIRONMENT
# ==============================
env = {
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "asin": lambda x: math.degrees(math.asin(x)),
    "acos": lambda x: math.degrees(math.acos(x)),
    "atan": lambda x: math.degrees(math.atan(x)),
    "sqrt": math.sqrt,
    "log": math.log,
    "ln": math.log,
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
    "fact": math.factorial,
    "abs": abs,
    "pow": pow,
    "complex": complex,
    "cmath": cmath,
    "__builtins__": {},
}

# ==============================
# HISTORY (Saves past calculations)
# ==============================
if "history" not in st.session_state:
    st.session_state.history = []

# ==============================
# DISPLAY
# ==============================
expr = st.session_state.get("expr", "")

st.text_input("Expression", value=expr, key="expr", label_visibility="collapsed")

col1, col2, col3, col4 = st.columns(4)

# Button Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "(", ")"],
    ["sin", "cos", "tan", "+"],
    ["sqrt", "log", "fact", "="],
    ["C", "DEL", "pi", "e"],
]

def click_button(btn):
    if btn == "C":
        st.session_state.expr = ""
    elif btn == "DEL":
        st.session_state.expr = st.session_state.expr[:-1]
    elif btn == "=":
        try:
            result = eval(st.session_state.expr, env)
            st.session_state.history.insert(0, f"{st.session_state.expr} = {result}")
            st.session_state.expr = str(result)
        except Exception as e:
            st.session_state.expr = "Error"
    else:
        st.session_state.expr += btn

# Create all buttons
for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        cols[i].button(btn, key=btn + str(row), on_click=click_button, args=(btn,), use_container_width=True)

# ==============================
# HISTORY DISPLAY
# ==============================
st.subheader("📜 History")
for item in st.session_state.history[:5]:
    st.text(item)
