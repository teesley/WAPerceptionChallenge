# WAPerceptionChallenge

This repository is in response to the Wisconsin Autonomous percetion team challenge. 

![Result of ](answer.png)

Methodology

1.Considering my previous lack of experience with OpenCV, I decided to look to the tips section first in the intial problem statment and began looking into image thresholding. 

2. Once finding out some details about thresholding through documentation, I decided to look further into thresholding based on color since the cones were the only thing of that color in the image... or so I thought at first. 

3. I then found HSV thresholding which allowed me to fine to the hue, saturation and value for the colors in the image. 

4. I initially tried somewhat random upper and lower thresholds but that obviously did not work so I used a script I found on StackOverflow for a color thresholder which I could test on the input image which allowed me to find near-ideal values for the upper and lower bounds of the HSV threshold. 

5. Then I used these upper and lower bounds to use the inRange method to apply my mask of the image for the colors in that range which would allow me to detect the the contours of the cones.

6. To actually find the contours, I used the findContours method on my mask which worked well since I had picked those specific ranges for the color of the cone.

7. I then set some boundaries since to exclude the upper portion of the image when iterating through the contours since there were no cones in that zone as well as there being an exit sign whose color matched pretty closely to the cone causing that to be picked up in the mask.

8. Set some intitial x and y values for the starting and ending point of the line so I could later update them to actually important values when iterating through the list of contours.

9. I then iterated through each point in each contour to find minimum and maximum x and y coordinates for both the line for the left set of cones and the line for the right set of cones.

10. Since I now had these values which I could work with, I performed some calculations in order to determine where to start and end my line so it would pass through all (well at least most) the cones as well as continue to the edge of the image.

11. I then used these starting and ending points for each line to draw them onto the image with the line() method and wrote my results to the output file, answer.png.





What I tried that did not work:

1. When I initially looked into color thresholding, there were many options and the HSV format was not the first I tried. However, what I found with the other thresholding techniques is that they were not targeting the codes as I needed it to.

2. Like I mentioned above, when I finally began using HSV, I started by simply messing around with different values which did not work as well as I needed it to to target the cones so I had to find a method to correctly choose the upper and lower bounds for the threshold.

3. Since I did not come in with OpenCV experience, I kind of hit a dead-end at this point once I figured how to target the cones in the image. I knew I needed to somehow take what I had to find the key coordinates in the mask to help me later draw the line, however, I was unsure where to begin. This led to me to research ways to take important coordinates from a masked image in OpenCV which is when I found out about contours.

4. Once researching a bit more about what the findContours() method returned, I knew I would be able to iterate through the points of the cones. I found that the reason I am able to do this is by setting a precise upper and lower color threshold for my mask, it filtered out most other objects in the image so that the only contours would be the cones. This allowed me to assume that any point in any contour (in a region of the image I defined to have cones in) was a cone so then I could set the start and end point for the lines that passed through both groups of cones.

5. Luckily I did not face many issues with actually iterating through the contours because I had an understanding of the format of the contours from my earlier research. Because of this, I was pretty easily able to find the key coordinates of where I would start and finish each line to draw a line through each group of cones.

6. In the sample answer.png in the problem repo, I saw that the lines extended to the edges of the image so I realized I also had to figure out a way to make the lines continue on to the edges. I performed some basic calculations in order to determine where each line should meet the edge of the image. I had a bug in this section originally because of some poor variable names that were too similar to eachother which prevented me from having the right line drawn correctly through the cones for a while, but that was the main issue I had with this portion.






