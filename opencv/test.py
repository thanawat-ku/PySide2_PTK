from PIL import Image
from util_func import *
import cv2
import time
import numpy as np

#@title Run object detection and show the detection results

#INPUT_IMAGE_URL = "https://www.collinsdictionary.com/images/thumb/apple_158989157_250.jpg" #@param {type:"string"}
DETECTION_THRESHOLD = 0.6 #@param {type:"number"}

TEMP_FILE = 'fruit.jpg'
#!wget -q -O $TEMP_FILE $INPUT_IMAGE_URL
im = Image.open(TEMP_FILE)
im.thumbnail((512, 512), Image.ANTIALIAS)
image_np = np.asarray(im)

# Load the TFLite model
options = ObjectDetectorOptions(
      num_threads=4,
      score_threshold=DETECTION_THRESHOLD,
)
model_path="model_fruit.tflite"
detector = ObjectDetector(model_path=model_path, options=options)


# Run object detection estimation using the model.
start_time=time.time()
detections = detector.detect(image_np)
end_time=time.time()
print(end_time-start_time)

# Draw keypoints and edges on input image
image_np = visualize(image_np, detections)

# Show the detection result
img_rgb = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
cv2.imshow('',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

