import streamlit as st
import math, cmath

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮")
st.title("🧮 Advanced Python Calculator")

st.markdown("""
Type your math expression below 👇  
Examples: `2+3*4`, `sin(30)`, `(3+4j)*(2-5j)`
""")

expr = st.text_input("Enter Expression")

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

if expr:
    try:
        result = eval(expr, env)
        st.success(f"✅ Result: {result}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
