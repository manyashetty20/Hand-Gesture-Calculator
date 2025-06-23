def calculate(a, b, operation):
    try:
        if operation == 'Add':
            return a + b
        elif operation == 'Subtract':
            return a - b
        elif operation == 'Multiply':
            return a * b
        elif operation == 'Divide':
            return round(a / b, 2) if b != 0 else "∞"
        else:
            return "?"
    except Exception as e:
        return f"Error: {e}"
