
import math
import pyautogui

previous_direction = "CENTER"


def detect_steering(left_hand, right_hand):

    left_x = left_hand[0].x
    left_y = left_hand[0].y

    right_x = right_hand[0].x
    right_y = right_hand[0].y

    angle = math.degrees(
        math.atan2(
            right_y - left_y,
            right_x - left_x
        )
    )

    if angle > 15:
        return "RIGHT"

    elif angle < -15:
        return "LEFT"

    else:
        return "CENTER"



def control_car(direction):

    global previous_direction


    if previous_direction == direction:
        return
    
    # Release previous key
    if previous_direction == "LEFT":
        pyautogui.keyUp("left")

    elif previous_direction == "RIGHT":
        pyautogui.keyUp("right")

    # Press new key
    if direction == "LEFT":
        pyautogui.keyDown("left")

    elif direction == "RIGHT":
        pyautogui.keyDown("right")

    # Release both keys when CENTER
    elif direction == "CENTER":
        pyautogui.keyUp("left")
        pyautogui.keyUp("right")

    previous_direction = direction