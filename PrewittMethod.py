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
			avg = int(red + green + blue)
			row.append(avg)
			j += 1
		newImg.append(row)
		j = 0
		i += 1

	newImg = numpy.asarray(newImg)

	return newImg


def prewittMethod(imgName):
	img = cv2.imread(imgName)
	img = imageToGrey(img)

	maskGX = [[-1,0,1],
			  [-1,0,1],
			  [-1,0,1]]
	maskGY = [[1,1,1],
			  [0,0,0],
			  [-1,-1,-1]]

	newImg = []
	for x in range(len(img) - 2):
		row = []
		for y in range(len(img[0]) - 2):
			sumX = 0
			sumY = 0
			for i in range(3):
				for j in range(3):
					sumX = sumX + (maskGX[i][j] * img[x+j][y+i])
					sumY = sumY + (maskGY[i][j] * img[x+j][y+i])

			totalSum = math.sqrt(math.pow(sumX, 2) + math.pow(sumY, 2))
			row.append(abs(totalSum))
		newImg.append(row)

	newImg = numpy.asarray(newImg)
	cv2.imwrite("prewitt-" + imgName, newImg)


def main():
	imageName = list(sys.argv)[1]
	prewittMethod(imageName)

if __name__ == "__main__":
	main()