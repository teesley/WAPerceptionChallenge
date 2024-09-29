# WAPerceptionChallenge

This repository is in response to the Wisconsin Autonomous percetion team challenge. 

![Result of ](answer.png)

I did not come in with much OpenCV experience so the learning curve was initially pretty steep. I initially looked into OpenCV and found out how to create a mask so I could create contours to find the key points to allow me to draw the line.

#Methodology

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






