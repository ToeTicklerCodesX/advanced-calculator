import math
import cmath

# ==========================================
# ADVANCED CALCULATOR (CLI VERSION)
# ==========================================

print("=======================================")
print("      Advanced Python Calculator ")
print("=======================================")
print("Type any math expression below!")
print("Examples:")
print("  2+3*4")
print("  sin(30)")
print("  cos(45) + tan(60)")
print("  sqrt(16) + log(100,10)")
print("  (3+4j)*(2-5j)")
print("---------------------------------------")
print("Type 'help' for function list or 'exit' to quit.")
print("=======================================")

# Map all math functions to eval environment
env = {
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "asin": lambda x: math.degrees(math.asin(x)),
    "acos": lambda x: math.degrees(math.acos(x)),
    "atan": lambda x: math.degrees(math.atan(x)),
    "sqrt": math.sqrt,
    "log": math.log,       # log(x, base)
    "ln": math.log,        # alias for natural log
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
    "fact": math.factorial,
    "abs": abs,
    "pow": pow,
    "complex": complex,
    "cmath": cmath,
    "__builtins__": {},    # disable unsafe functions
}

while True:
    expr = input("\nEnter expression > ")

    if expr.lower() in ["exit", "quit", "q"]:
        print("Goodbye 👋")
        break

    if expr.lower() == "help":
        print("""
Available Functions:
  sin(x), cos(x), tan(x)      -> in degrees
  asin(x), acos(x), atan(x)   -> returns degrees
  sqrt(x)                     -> square root
  log(x, base) or ln(x)       -> log functions
  exp(x)                      -> e^x
  fact(n)                     -> factorial
  pow(a, b) or a**b           -> power
  abs(x)                      -> absolute value
  complex(a, b)               -> complex numbers
  pi, e                       -> constants
Supports complex ops too!
Example: (3+4j)*(2-5j)
        """)
        continue

    try:
        result = eval(expr, env)
        print("Result =", result)
    except Exception as e:
        print("Error:", e)
