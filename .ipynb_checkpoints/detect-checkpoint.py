import cv2

# Load in the image given to us
image = cv2.imread("red.png")

# converts image into HSV color format
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# used a HSV color thresholder to determine optimal lower and upper
# bounds to best detect the color of the cone for the mask
mask = cv2.inRange(hsv, (177, 194, 156), (179, 255, 255))

# finds the cones in the mask by finding all of the contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#top left x-cord of image
impox = 0
#top left y-cord of image
impoy = 0
# width of image we will search
impow = 1816
# region at the top of image to exclude (cones are not found in the top 626 pixels of the image)
# therefore it is unecessary to include that area
impoh = 626

# x and y coordinates that will help us draw our line through the cones
# sets the boundaries for where we start and finish the lines
blefy = 1816
tlefy = 0
brigy = 1816
trigy =  0
blefx = 0
tlefx = 0
brigx = 0
trigx = 0


# Go through all the contours which represent where we hope cones are detected
# and keep track of the minimum and maximum y values in the area we are searching
# We keep track of the coordinates associated with this min and max y so that later
# we know where to map the start and end of our line on the image to successfully
# draw a line through each row of cones

for c in contours:
    for p in c:
        x, y = p[0]
        if(x >= impox and x < impow/2) and (y > impoh):
            if(y < blefy):
                # example of keeping track of x and y for minimum y
                # as discusssed in above comment
                blefy = y
                blefx = x
            if(y > tlefy):
                tlefy = y
                tlefx = x
        if(x >= impow/2 and x < impow) and (y >= impoh):
            if(y < brigy):
                brigy = y
                brigx = x
            if(y > trigy):
                trigy = y
                trigx = x

# Now that we know the key points where the lines will start and end on each side
# we can use this to calculate where the line will be

lm = (tlefy - blefy)/(tlefx - blefx)
lb = tlefy - (lm * tlefy)

# Have to calculate where the lines will hit the edge of the image
blex = int(1)
bley = int(lb)
tley = int(1)
tlex = int(tley - lb)/(lm)


rm = (trigy - brigy)/(trigx - brigx)
rb = trigy - (rm * trigx)

# Have to calculate where the lines will hit the edge of the image
brex = int(1816)
brey = int(rb)
trey = int(1)
trex = int((trey - rb)/rm)

p1 = (blex, bley)
p2 = (tlex, tley)
p3 = (brigx, bley)
p4 = (trex, trey)

result = cv2.line(image, p1, p2, (0, 0, 255), 4)
result = cv2.line(image, p3, p4, (o, 0, 255), 4)
cv2.imwrite("result.png", result)


cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

        
        
    




