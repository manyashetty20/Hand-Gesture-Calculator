import cv2
from hand_tracking import detect_hands, draw_landmarks
from ui_overlay import draw_buttons, draw_result, get_selected_operation
from utils import extract_finger_counts
from calculator import calculate

cap = cv2.VideoCapture(0)
selected_operation = None
op_selected_time = 0

while True:
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 1)
    
    results = detect_hands(frame)
    draw_landmarks(frame, results)
    
    draw_buttons(frame, selected_op=selected_operation)

    if results.multi_hand_landmarks:
        hands = list(results.multi_hand_landmarks)

        # Use index finger tip from first hand to select operation
        index_tip = hands[0].landmark[8]
        h, w, _ = frame.shape
        ix, iy = int(index_tip.x * w), int(index_tip.y * h)

        if selected_operation is None:
            op = get_selected_operation(ix, iy)
            if op:
                selected_operation = op

        counts = extract_finger_counts(results)
        if len(counts) == 2:
            a, b = counts[0], counts[1]
        elif len(counts) == 1:
            a, b = counts[0], 0
        else:
            a, b = 0, 0

        if selected_operation:
            result = calculate(a, b, selected_operation)
            draw_result(frame, a, b, selected_operation, result)

    cv2.imshow("Finger Calculator", frame)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        selected_operation = None  # Reset on 'r'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
