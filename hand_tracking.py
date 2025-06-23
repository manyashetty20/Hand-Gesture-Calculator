import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

finger_tips = [4, 8, 12, 16, 20]  # Thumb to pinky

def detect_hands(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    return results

def draw_landmarks(img, results):
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS)

def count_fingers(hand):
    lm_list = hand.landmark
    fingers = []

    # Thumb
    fingers.append(1 if lm_list[finger_tips[0]].x < lm_list[finger_tips[0] - 1].x else 0)

    # 4 fingers
    for tip in finger_tips[1:]:
        fingers.append(1 if lm_list[tip].y < lm_list[tip - 2].y else 0)

    return fingers.count(1)
