# calculator_agent.py

import ast
import operator as op
import re

# --- Supported math operators ---
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.Mod: op.mod,
}

# --- Safe evaluator using AST ---
def safe_eval(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp):  # -<operand>
        return operators[type(node.op)](safe_eval(node.operand))
    else:
        raise TypeError("Unsupported or unsafe expression")

# --- Calculator function ---
def safe_calculator(expression: str) -> str:
    """Safely evaluate basic math expressions."""
    try:
        node = ast.parse(expression, mode='eval').body
        result = safe_eval(node)
        return str(result)
    except Exception as e:
        return f"❌ Error evaluating expression: {e}"

# --- Expression checker ---
def is_math_expression(text: str) -> bool:
    """Check if a string looks like a math expression."""
    math_keywords = ["+", "-", "*", "/", "calculate", "of", "percent", "=", "sum", "product", "power", "^"]
    return any(kw in text.lower() for kw in math_keywords) and any(c.isdigit() for c in text)

# --- Final function to integrate in LangGraph ---
def calculator_worker_function(text: str) -> str:
    """LangGraph-compatible calculator worker."""
    if not is_math_expression(text):
        return "🛑 Skipping calculator — no math-like expression detected."
    return safe_calculator(text)
