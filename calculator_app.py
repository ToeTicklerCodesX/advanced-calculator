import streamlit as st
import math, cmath

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="Pro Calculator", page_icon="🧮", layout="centered")

# ==============================
# CUSTOM CSS STYLE
# ==============================
st.markdown("""
<style>
    body {
        background-color: #0f1116;
    }
    .main {
        background-color: #0f1116;
        color: white;
    }
    .calc-container {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        padding: 30px;
        border-radius: 20px;
        background-color: #1e1e2f;
        box-shadow: 0 0 25px rgba(0,0,0,0.5);
        width: 340px;
        margin: auto;
    }
    .screen {
        background-color: #000;
        color: #0f0;
        font-size: 28px;
        border-radius: 10px;
        padding: 15px;
        width: 100%;
        text-align: right;
        margin-bottom: 15px;
        font-family: 'Consolas', monospace;
    }
    .button-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-gap: 10px;
        width: 100%;
    }
    .button {
        border: none;
        font-size: 20px;
        border-radius: 10px;
        padding: 15px;
        font-weight: bold;
        transition: all 0.2s ease;
    }
    .button:hover {
        transform: scale(1.05);
    }
    .num { background-color: #2c2c3a; color: white; }
    .op { background-color: #0078ff; color: white; }
    .func { background-color: #ff9900; color: black; }
    .clear { background-color: #ff4444; color: white; }
    .equal { background-color: #00c853; color: white; }
    .history {
        margin-top: 25px;
        background: #14141f;
        padding: 10px;
        border-radius: 10px;
        width: 100%;
        font-family: monospace;
        font-size: 15px;
        color: #bbb;
    }
</style>
""", unsafe_allow_html=True)

# ==============================
# FUNCTIONS AND ENVIRONMENT
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

if "expr" not in st.session_state:
    st.session_state.expr = ""
if "history" not in st.session_state:
    st.session_state.history = []

# ==============================
# FUNCTIONS
# ==============================
def press(btn):
    if btn == "C":
        st.session_state.expr = ""
    elif btn == "DEL":
        st.session_state.expr = st.session_state.expr[:-1]
    elif btn == "=":
        try:
            result = eval(st.session_state.expr, env)
            st.session_state.history.insert(0, f"{st.session_state.expr} = {result}")
            st.session_state.expr = str(result)
        except:
            st.session_state.expr = "Error"
    else:
        st.session_state.expr += btn

# ==============================
# CALCULATOR UI
# ==============================
st.markdown("<div class='calc-container'>", unsafe_allow_html=True)
st.markdown(f"<div class='screen'>{st.session_state.expr}</div>", unsafe_allow_html=True)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "(", ")"],
    ["sin", "cos", "tan", "+"],
    ["sqrt", "log", "fact", "="],
    ["pi", "e", "DEL", "C"],
]

st.markdown("<div class='button-grid'>", unsafe_allow_html=True)

for row in buttons:
    for btn in row:
        color_class = (
            "num" if btn.isdigit() or btn == "." else
            "op" if btn in ["+", "-", "*", "/", "(", ")"] else
            "func" if btn in ["sin", "cos", "tan", "sqrt", "log", "fact", "pi", "e"] else
            "equal" if btn == "=" else
            "clear"
        )
        if st.button(btn, key=btn, help=btn):
            press(btn)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# HISTORY
# ==============================
if st.session_state.history:
    st.markdown("<div class='history'><b>📜 History:</b><br>" + "<br>".join(st.session_state.history[:5]) + "</div>", unsafe_allow_html=True)
