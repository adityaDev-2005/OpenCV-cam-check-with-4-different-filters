import cv2
# print(cv2.__version__)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
blur_on = False
mode = "Normal"
text_color = (0,255,0)

while True:
   
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    if not ret:
        print("Failed to read frame")
        break
    
    
    # cv2.rectangle(
    #     frame,
    #     (100,100), # top-left
    #     (300,300), # bottom-right
    #     (0,255,0), # color
    #     2   # thickness
    # )
    #blurred = cv2.GaussianBlur(frame,(15,15),0) # (15,15) = kernel size Large kernel means more blur
    

    key = cv2.waitKey(1) & 0xFF

    if key == ord('b'):
        mode = "Blur"
    
    elif key == ord('n'):
        mode = "Normal"
    
    elif key == ord('g'):
        mode = "Grayscale"

    elif key == ord('e'):
        mode = "Edges"

    elif key == ord(' '):
        break

    if mode == "Normal":
        text_color = (0,255,0)

    elif mode == "Blur":
        frame = cv2.GaussianBlur(frame,(25,25),0)
        text_color = (0,0,255)
    
    elif mode == "Grayscale":
        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )
        frame = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2BGR
        )
        text_color = (128,128,128)

    elif mode == "Edges":
        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        edges = cv2.Canny(
            gray,
            100,
            200
        )

        frame = cv2.cvtColor(
            edges,
            cv2.COLOR_GRAY2BGR
        )

        text_color = (255,255,255)


    cv2.putText(
    frame,
    f"MODE: {mode}",
    (50,50),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    text_color,
    2
    )

    cv2.imshow("Camera",frame)


    
cap.release()

cv2.destroyAllWindows()