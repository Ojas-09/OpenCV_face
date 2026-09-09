import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recoder = cv2.VideoWriter("my_vi.avi", codec, 30, (frame_width, frame_height))

while True:
    success, image = camera.read()

    if not success:
        break

    recoder.write(image)
    cv2.imshow("test", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
recoder.release()
cv2.destroyAllWindows()