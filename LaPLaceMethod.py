import cv2
import numpy
import math
import sys

def imageToGrey(img):
	i = 0
	j = 0

	newImg = []
	for pixel in img:
		row = []
		for colors in pixel:
			red = img[i][j][0] / 3
			green = img[i][j][1] / 3
			blue = img[i][j][2] / 3
			avg = (red + green + blue)
			img[i][j] = [avg, avg, avg]
			avg = (int(avg))
			row.append(avg)
			j += 1
		newImg.append(row)
		j = 0
		i += 1

	newImg = numpy.asarray(newImg)

	return newImg


def laPlaceMethod(imgName):

	image = cv2.imread(imgName)
	img = imageToGrey(image)

	mask = [[-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1],
			[-1,-1,24,-1,-1],
			[-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1]]

	newImg = []
	for x in range(len(img) - 4):
		row = []
		for y in range(len(img[0]) - 4):
			totalSum = 0
			for i in range(5):
				for j in range(5):
					totalSum = totalSum + (mask[i][j] * img[x+j][y+i])

			totalSum = totalSum / 4
			row.append(abs(totalSum))
		newImg.append(row)

	newImg = numpy.asarray(newImg)
	cv2.imwrite("laPlace-" + imgName, newImg)


def main():
	imageName = list(sys.argv)[1]
	laPlaceMethod(imageName)

if __name__ == "__main__":
	main()