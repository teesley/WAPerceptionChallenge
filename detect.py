import cv2
import numpy as np

# Load in the image given to us
img = cv2.imread("red.png")

# converts image into HSV color format
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# used a HSV color thresholder to determine optimal lower and upper
# bounds to best detect the color of the cone for the mask
lr = np.array([170, 194, 156])
ur = np.array([179, 255, 255])
mask = cv2.inRange(hsv, lr, ur)

# finds the cones in the mask by finding all of the contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#top left x-cord of image (impo = important)
impox = 0
#top left y-cord of image
impoy = 0
# width of image we will search
impow = 1816
# region at the top of image to exclude (cones are not found in roughly the top 650 pixels of the image)
# therefore it is unecessary to include that area
impoh = 650

# x and y coordinates that will help us draw our line through the cones
# sets the boundaries for where we start and finish the lines
# (b -> bottom), (t -> top), (lef -> left), (rig -> right)
blefy = 1816
tlefy = 0
brigy = 1816
trigy =  0
blefx = 0
tlefx = 0
brigx = 0
trigx = 0


# Go through all the contours which represent where we hope think are detected
# and keep track of the minimum and maximum y values in the area we are searching
# We keep track of the coordinates associated with this min and max x and y so that later
# we know where to map the start and end of our line on the image to successfully
# draw a line through each row of cones
for c in contours:
    for p in c:
        x, y = p[0]
        # If x is in an important (impo) region, make updates to left line 
        # (less than half the width of image)
        
        # If x is in the important region on the left half of the image
        if (x >= impox and x < impow/2) and (y >= impoh): 
            # If it is less than bottom left, update blef coordinates
            if(y < blefy): 
                blefy = y
                blefx = x
            # If it is greater than top left, update tlef coordinates
            if(y > tlefy):
                tlefy = y
                tlefx = x
        # X in range for important region on the rights side of the image
        if (x >= impow/2 and x < impow) and (y >= impoh):
            # If y is less than the bottom right y, update brigy coordinates
            if(y < brigy):
                brigy = y
                brigx = x
            # If y is greater than the top right y, set trigy to x and y coords
            if(y > trigy): 
                trigy = y
                trigx = x

# Now that we know the key points where the lines will start and end on each side
# we can use this to calculate where the line will be

# Good old y = mx+b, we will use this to plot our lines
leftM = (tlefy - blefy)/(tlefx - blefx)
leftB = tlefy - (leftM * tlefx)

# Have to calculate where the lines will hit the edge of the image
blCornerX = int(1)
blCornerY = int(leftB)
tlCornerY = int(1)
tlCornerX = int((tlCornerY - leftB)/leftM)


rightM = (trigy - brigy)/(trigx - brigx)
rightB = trigy - (rightM * trigx)

# Have to calculate where the lines will hit the edge of the image
brCornerX = int(1816)
brCornerY = int(rightB)
trCornerY = int(1)
trCornerX = int((trCornerY - rightB)/rightM)

p1 = (blCornerX, blCornerY)
p2 = (tlCornerX, tlCornerY)
p3 = (brCornerX, blCornerY)
p4 = (trCornerX, trCornerY)

final_img = cv2.line(img, p1, p2, (0, 0, 255), 4) # draw first line on orignal image 
final_img = cv2.line(img, p3, p4, (0, 0, 255), 4) # draw second line on original image to give final answer image
cv2.imwrite('answer.png', final_img)


cv2.imshow('Result', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
        
    




