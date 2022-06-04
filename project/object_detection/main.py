import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

image = cv2.imread('car.jpg')
bbox, label, conf = cvimagedetect_common_objects(image)
output = draw_bbox(image, bbox, label, conf)
plt.imshow(output)
plt.show()
print('num car' + str(label.count))