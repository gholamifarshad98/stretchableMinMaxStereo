from Matcher import Matcher
import cv2

leftImage = cv2.imread('/home/farshad/Desktop/Phd/downloadData/drivingStereo_left/2018-07-09-16-11-56_2018-07-09-16-32-35-850.jpg', 0)
rightImage = cv2.imread('/home/farshad/Desktop/Phd/downloadData/drivingStereo_right/2018-07-09-16-11-56_2018-07-09-16-32-35-850.jpg', 0)
scale_percent = 20 # percent of original size
width = int(leftImage.shape[1] * scale_percent / 100)
height = int(leftImage.shape[0] * scale_percent / 100)
dim = (width, height)


leftImage = cv2.resize(leftImage, dim, interpolation = cv2.INTER_AREA)
rightImage = cv2.resize(rightImage, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("leftImage", leftImage)
cv2.waitKey(0)
IUSTMatcher = Matcher(minNumOfRow=2, minNumOfColumn= 2, stretchThreshold= 5,leftImage= leftImage, rightImage= rightImage, disparity= 13)
IUSTMatcher.stretch()

print("stretch algorithm is finished!!!")
