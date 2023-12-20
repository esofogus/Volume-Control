import cv2 as cv
import mediapipe as mp
import pyautogui

x1 = y1 = x2 = y2 = 0
cap = cv.VideoCapture(0)
myHands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    frameHeight, frameWidth, _ = frame.shape
    imageRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    output = myHands.process(imageRGB)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for Id, landmarks in enumerate(landmarks):
                x = int(landmarks.x * frameWidth)
                y = int(landmarks.y * frameHeight)
                if Id == 8:
                    cv.circle(img=frame, center=(x, y), radius=8, color=(255, 0, 255), thickness=3)
                    x1 = x
                    y1 = y
                if Id == 4:
                    cv.circle(img=frame, center=(x, y), radius=8, color=(255, 0, 255), thickness=3)
                    x2 = x
                    y2 = y
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5//4
        cv.line(frame, (x1, y1), (x2, y2), (255, 255, 255), 5)
        if dist > 50:
            pyautogui.press("volumeUp")
        else:
            pyautogui.press("volumeDown")
    cv.imshow("Volume Control", frame)
    key = cv.waitKey(1)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()