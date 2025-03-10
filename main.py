import numpy as np


camera_port = 0
cap = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)

cap.set(3,600)
cap.set(4,400)
zeros = None

while True:
  ret_value, frame = cap.read()
  
  if ret_value == True:
    #adding median blurring to smooth image
    frame = cv2.medianBlur(frame, 5)
    #splitting the image into frames
    b, g, r = cv2.split(frame)
    #time.sleep(1)
    l = np.logical_or(r, g)
    #time.sleep(1)
    ot1 = np.multiply(r, r)
    ot2 = np.multiply(g, b)
    ot1 = ot1.astype(np.float)
    ot2 = ot2.astype(np.float)
    intensity = np.floor_divide(ot1, ot2)
    ret, thresh1 = cv2.threshold(intensity, 1, 255, cv2.THRESH_BINARY)
    image1copy = np.uint8(thresh1)
    # doing connected components
    processing
    nlabels, labels, stats,
    centroids =
    cv2.connectedComponentsWithStats(image1c
    opy, None, None, None, 8, cv2.CV_32S)
    # get CC_STAT_AREA component as
    stats[label, COLUMN]
    areas = stats[1:,
    cv2.CC_STAT_AREA]
    result =
    np.zeros((labels.shape), np.uint8)
    for i in range(0, nlabels - 1):
    if areas[i] >= 900: # keep
      result[labels == i + 1] = 255
    #contours
    contours0, hierarchy = cv2.findContours(result.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # calculate moments of
    binary image
    M = cv2.moments(result)
    # calculate x,y
    coordinate of center
    if M["m00"] != 0:
      cX = int(M["m10"] / M["m00"])
      cY = int(M["m01"] / M["m00"])
    else:
      cX, cY = 0, 0
    # put text and highlight
    the center
    cv2.circle(frame, (cX,
    cY), 5, (0, 0, 0), -1)
    # showing the centroid on frame
    cv2.imshow("centroid", frame)

    k = cv2.waitKey(10)
    if k == 27:
    break
    cap.release()
    cv2.destroyAllWindows()
