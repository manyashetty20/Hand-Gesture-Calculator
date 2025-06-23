import cv2

# Button positions: (x1, y1, x2, y2)
operations = {
    'Add': (50, 50, 150, 100),
    'Subtract': (170, 50, 270, 100),
    'Multiply': (290, 50, 390, 100),
    'Divide': (410, 50, 510, 100),
}

def draw_buttons(img, selected_op=None):
    for op, (x1, y1, x2, y2) in operations.items():
        color = (0, 255, 0) if selected_op == op else (200, 200, 200)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, -1)
        cv2.putText(img, op, (x1 + 10, y2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

def get_selected_operation(x, y):
    for op, (x1, y1, x2, y2) in operations.items():
        if x1 <= x <= x2 and y1 <= y <= y2:
            return op
    return None

def draw_result(img, left, right, op, result):
    cv2.putText(img, f"{left} {op} {right} = {result}", (50, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)
