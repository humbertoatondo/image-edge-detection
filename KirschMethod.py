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


def kirschMethod(imgName):
	img = cv2.imread(imgName)
	img = imageToGrey(img)

	maskG1 = [[5,5,5],
			  [-3,0,-3],
			  [-3,-3,-3]]

	maskG2 = [[5,5,-3],
			  [5,0,-3],
			  [-3,-3,-3]]

	maskG3 = [[5,-3,-3],
			  [5,0,-3],
			  [5,-3,-3]]

	maskG4 = [[-3,-3,-3],
			  [5,0,-3],
			  [5,5,-3]]

	maskG5 = [[-3,-3,-3],
			  [-3,0,-3],
			  [5,5,5]]

	maskG6 = [[-3,-3,-3],
			  [-3,0,5],
			  [-3,5,5]]

	maskG7 = [[-3,-3,5],
			  [-3,0,5],
			  [-3,-3,5]]

	maskG8 = [[-3,5,5],
			  [-3,0,5],
			  [-3,-3,-3]]


	newImg = []
	for x in range(len(img) - 2):
		row = []
		for y in range(len(img[0]) - 2):
			sum1 = 0
			sum2 = 0
			sum3 = 0
			sum4 = 0
			sum5 = 0
			sum6 = 0
			sum7 = 0
			sum8 = 0
			directions = []
			for i in range(3):
				for j in range(3):
					sum1 = sum1 + (maskG1[i][j] * img[x+j][y+i])
					sum2 = sum2 + (maskG2[i][j] * img[x+j][y+i])
					sum3 = sum3 + (maskG3[i][j] * img[x+j][y+i])
					sum4 = sum4 + (maskG4[i][j] * img[x+j][y+i])
					sum5 = sum5 + (maskG5[i][j] * img[x+j][y+i])
					sum6 = sum6 + (maskG6[i][j] * img[x+j][y+i])
					sum7 = sum7 + (maskG7[i][j] * img[x+j][y+i])
					sum8 = sum8 + (maskG8[i][j] * img[x+j][y+i])

			directions.append(sum1)
			directions.append(sum2)
			directions.append(sum3)
			directions.append(sum4)
			directions.append(sum5)
			directions.append(sum6)
			directions.append(sum7)
			directions.append(sum8)
			
			maxSum = 0
			for k in range(len(directions)):
				if k == 0:
					maxSum = directions[k]
				elif k > maxSum:
					maxSum = directions[k]

			maxSum = maxSum/2
			row.append(abs(maxSum))

		newImg.append(row)

	newImg = numpy.asarray(newImg)
	cv2.imwrite("kirsch-" + imgName, newImg)


def main():
	imageName = list(sys.argv)[1]
	kirschMethod(imageName)


if __name__ == "__main__":
	main()