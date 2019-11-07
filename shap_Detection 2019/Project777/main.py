import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("sss8.png", cv2.IMREAD_GRAYSCALE)
imgcopy = cv2.imread("sss8.png")

_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_TRIPLEX  # the font for the shape name

counter = 0

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)  # number of corners in the shape
    cv2.drawContours(img, [approx], 0, (0), 0, )

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 2:
        cv2.fillPoly(imgcopy, [cnt], color=(200, 155., 70))
        cv2.putText(imgcopy, "Line", (x, y), font-2, 1, (0))

    elif len(approx) == 3:
        cv2.fillPoly(imgcopy, [cnt], color=(0, 255, 0))
        cv2.putText(imgcopy, "Triangle", (x, y), font-3, 1, (0))

    elif len(approx) == 4:
        x2 = approx.ravel()[2]  # the 4 points of the sqare\reqtangle
        y2 = approx.ravel()[3]
        x3 = approx.ravel()[4]
        y3 = approx.ravel()[5]
        x4 = approx.ravel()[6]
        y4 = approx.ravel()[7]

        # cv2.putText(imgcopy, "point1", (x, y), font, 1, (0))          if u wanna see eatch corner
        # cv2.putText(imgcopy, "point2", (x2, y2), font, 1, (0))
        # cv2.putText(imgcopy, "point3", (x3, y3), font, 1, (0))
        # cv2.putText(imgcopy, "point4", (x4, y4), font, 1, (0))

        # print(x,y)
        # print(x2, y2)
        # print(x3,y3)
        # print(x4, y4)
        # print '\n'

        # print x4-x
        # print y-y2
        # print  y4-y3
        # print   x3-x2

        if counter == 0:  # the fram window is asqare too haha
            cv2.fillPoly(imgcopy, [cnt], color=(150, 150, 150))

        # if ((x2-x)-(y4-y)<10   and counter > 0):
        elif (((x2 - x) - (y4 - y)) < 10 and ((x2 - x) - (y4 - y)) > 0 and counter > 0):
            cv2.fillPoly(imgcopy, [cnt], color=(255, 255, 0))
            cv2.putText(imgcopy, "Square", (x, y - 3), font-1, 1, (0))

        elif (counter > 0):  # not the window square...
            cv2.fillPoly(imgcopy, [cnt], color=(150, 150, 200))
            cv2.putText(imgcopy, "Rectangle", (x, y - 3), font-1, 1, (0))

        counter = counter + 1

    elif len(approx) == 5:
        x2 = approx.ravel()[2]
        y2 = approx.ravel()[3]
        cv2.fillPoly(imgcopy, [cnt], color=(255, 0, 0))
        cv2.putText(imgcopy, "Pentagon", (x2, y2), font, 1, (0))

    elif len(approx) == 10 :
        cv2.fillPoly(imgcopy, [cnt], color=(250, 250, 130))
        cv2.putText(imgcopy, "Star", (x, y), font, 1, (0))

    elif 6 < len(approx) < 15  :
        cv2.fillPoly(imgcopy, [cnt], color=(0, 0, 255))
        cv2.putText(imgcopy, "Ellipse", (x, y), font, 1, (20))

    else:
        cv2.fillPoly(imgcopy, [cnt], color=(0, 255, 255))
        cv2.putText(imgcopy, "Circle", (x, y), font, 1, (0))


#     show in matplotlib
plt.imshow(cv2.cvtColor(imgcopy, cv2.COLOR_BGR2RGB))
mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.show()


#     show in cv
# cv2.imshow("shapes", img)
# cv2.imshow("imgcopy", imgcopy)
# cv2.imshow("Threshold", threshold)

# cv2.waitKey(0)
# cv2.destroyAllWindows()