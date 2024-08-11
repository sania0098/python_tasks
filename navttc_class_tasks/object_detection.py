# import cv2
# # threshold to etect object
#
# thres = 0.5
#
#
# cap = cv2.VideoCapture(0)
# cap.set (3,648)
# cap.set(4,488)
#
# classNames= []
# classFile= 'coco.names'
# with open(classFile,'rt') as f:
#     classNames = f.read().rstrip('\n').split('\n')
#
# configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
# weightspath = 'frozen_inference_graph.pb'
#
# net = cv2.dnn_DetectionModel(weightspath,configPath)
# net.setInputSize(320,320)
# net.setInputScale(1.0/127.5)
# net.setInputMean((127.5,127.5,127.5))
# net.setInputSwapRB(True)
#
# while True:
#     success,img = cap.read()
#     classIds, confs, bbox =  net.detect(img,confThreshold=0.5)
#     print(classIds,bbox)
#
#     if len(classIds)!=0:
#        for classId,confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
#            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
#            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
#                        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
#
#
#        cv2.imshow("Output",img)
#        cv2.waitKey(1)
import cv2

# Threshold for object detection
thres = 0.4

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 648)  # Set the width of the frame
cap.set(4, 488)  # Set the height of the frame

# Load class names from the coco.names file
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Paths to the configuration and weights files
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

# Load the network
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    # Read a frame from the webcam
    success, img = cap.read()
    if not success:
        break

    # Detect objects in the frame
    classIds, confs, bbox = net.detect(img, confThreshold=thres)

    # Print the detected class IDs and bounding boxes
    print(classIds, bbox)

    if len(classIds) != 0:
        # Draw bounding boxes and labels on the image
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            if classId - 1 < len(classNames) and classId - 1 >= 0:
                cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    # Display the output image
    cv2.imshow("Output", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()