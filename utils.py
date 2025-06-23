def extract_finger_counts(results):
    counts = []
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            from hand_tracking import count_fingers
            count = count_fingers(hand)
            counts.append(count)
    return counts
