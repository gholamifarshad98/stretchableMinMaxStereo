from Matcher import Matcher
import cv2

# leftImage = cv2.imread('/home/farshad/Desktop/Phd/downloadData/drivingStereo_left/2018-07-09-16-11-56_2018-07-09-16-32-35-850.jpg', 0)
# rightImage = cv2.imread('/home/farshad/Desktop/Phd/downloadData/drivingStereo_right/2018-07-09-16-11-56_2018-07-09-16-32-35-850.jpg', 0)

leftImage = cv2.imread('leftPic.png', 0)
rightImage = cv2.imread('rightPic.png', 0)

scale_percent = 100 # percent of original size
width = int(leftImage.shape[1] * scale_percent / 100)
height = int(leftImage.shape[0] * scale_percent / 100)
dim = (width, height)

print("the dim is ",dim)
leftImage = cv2.resize(leftImage, dim, interpolation = cv2.INTER_AREA)
rightImage = cv2.resize(rightImage, dim, interpolation = cv2.INTER_AREA)
IUSTMatcher = Matcher(minNumOfRow=9, minNumOfColumn= 5, stretchThreshold= 25,leftImage= leftImage, rightImage= rightImage, disparity= 10)
IUSTMatcher.stretch()
print("initilazation of match")
IUSTMatcher.match()

print("stretch algorithm is finished!!!")
