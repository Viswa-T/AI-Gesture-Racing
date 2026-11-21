import cv2
import mediapipe as mp
import hand_tracking
import gesture_control


# Initialize webcam
cap = cv2.VideoCapture(0)


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 60)


# Initialize MediaPipe hand connections
connections = mp.tasks.vision.HandLandmarksConnections.HAND_CONNECTIONS

print("AI Gesture Racing Started!")

while True:

    # Capture webcam frame
    ret, frame = cap.read()

    if not ret:
        print("Camera not detected!")
        break

    # Mirror webcam
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert frame into MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    # Generate timestamp
    timestamp = cv2.getTickCount() * 1000 / cv2.getTickFrequency()

    # Detect hands
    result = hand_tracking.detector.detect_for_video(
        mp_image,
        int(timestamp)
    )

    height, width, _ = frame.shape

    # Check if two hands are detected
    if len(result.hand_landmarks) == 2:

        # Get both hands
        hand1 = result.hand_landmarks[0]
        hand2 = result.hand_landmarks[1]

        # Detect steering direction
        direction = gesture_control.detect_steering(
            hand1,
            hand2
        )

        # Control keyboard
        gesture_control.control_car(direction)

        # Display direction
        cv2.putText(
            frame,
            f"Steering: {direction}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Draw both hands
        for hand_landmarks in result.hand_landmarks:

            # Draw landmark points
            for landmark in hand_landmarks:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )

            # Draw hand connections
            for connection in connections:

                start = hand_landmarks[connection.start]
                end = hand_landmarks[connection.end]

                x1 = int(start.x * width)
                y1 = int(start.y * height)

                x2 = int(end.x * width)
                y2 = int(end.y * height)

                cv2.line(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (255, 0, 0),
                    2
                )

    else:

        # Release keys if both hands are not detected
        gesture_control.control_car("CENTER")

        cv2.putText(
            frame,
            "Show both hands",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # Display webcam
    cv2.imshow(
        "AI Gesture Racing - Two Hand Steering",
        frame
    )

    # Exit using Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release keyboard keys
gesture_control.control_car("CENTER")

# Release resources
cap.release()
hand_tracking.detector.close()
cv2.destroyAllWindows()