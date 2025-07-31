import time
start = time.time()
import matplotlib.pyplot as plt
import numpy as np
import math
plt.axis('off')

#Some interesting functions to experiment with

"""
x**15 - 2 * x**14 + 3 * x**13 - 4 * x**12 + 5 * x**11 - 6 * x**10 + 7 * x**9 - 8 * x**8 + 9 * x**7 - 10 * x**6 + 11 * x**5 - 12 * x**4 + 13 * x**3 - 14 * x**2 + 15 * x - 16
15 * x**14 - 28 * x**13 + 39 * x**12 - 48 * x**11 + 55 * x**10 - 60 * x**9 + 63 * x**8 - 64 * x**7 + 63 * x**6 - 60 * x**5 + 55 * x**4 - 48 * x**3 + 39 * x**2 - 28 * x + 15
"""
"""
35 * x**9 - 180 * x**7 + 378 * x**5 - 420 * x**3 + 315 * x
315 * x**8 - 1260 * x**6 + 1890 * x**4 - 1260 * x**2 + 315
"""
"""
x**8 + 15 * x**4 - 16
8 * x**7 + 60 * x**3
"""
"""
(x**3 + 10 * x**2 + 169 * x) / (4 * x**5 - 5 * x**4 + 11)
(-8 * x**7 - 115 * x**6 - 2604 * x**5 + 2535 * x**4 + 33 * x**2 + 220 * x + 1859) / ((4 * x**5 - 5 * x**4 + 11)**2)
"""

def equation(x):
    return x**3 - 1
def deriv(x):
    return 3 * x**2

def newtonNova(x, a, c):
    return x - a * (equation(x) / deriv(x)) + c

def compareToRoots(num, rootArr, iterE, maxIter, a, c): #Runs newton's method on the number until the margin of error between two consecutive iterations is small or it has been 100 iterations.
    #Return the closest root and the number of iterations it took to get there
    lastNum = num
    tempNum = newtonNova(lastNum, a, c)
    count = 0
    while abs(tempNum - lastNum) >= iterE and count < maxIter:
        lastNum = tempNum
        tempNum = newtonNova(lastNum, a, c)
        count += 1
    closeRoot = findClosestRoot(tempNum, rootArr)    
    return [closeRoot, count]

#Gets index of root closest to the number. If 
def findClosestRoot(num, rootArr):
    curRoot = 0
    for i in range(1, len(rootArr)):
        if abs(rootArr[i] - num) < abs(rootArr[curRoot] - num):
            curRoot = i
    return curRoot

def main():
    width = 500
    height = 500
    iterError = 0.01
    #Gets roots of function
    roots = np.roots([1, 0, 0, -1])
    maxIteration = 100
    #Makes array representing points on complex plane
    #Makes the range of the graph between the smallest and biggest values in the roots
    """
    minVal = roots[0].real
    maxVal = roots[0].real
    for elem in roots:
        if elem.real < minVal:
            minVal = elem.real
        if elem.imag < minVal:
            minVal = elem.imag
        if elem.real > maxVal:
            maxVal = elem.real
        if elem.imag > maxVal:
            maxVal = elem.imag
    """
    xValues = np.linspace(-2, 2, width)
    yValues = np.linspace(-2, 2, height)
    colorRootMap = { #This maps indices of the root array to colors, so we can color points based on what root they converged to
        -1 : np.array([0, 0, 0]),
         0 : np.array([255, 0, 0]), 1 : np.array([0, 255, 0]), 2 : np.array([0, 0, 255]),
         3 : np.array([255, 255, 0]), 4 : np.array([0, 255, 255]), 5 : np.array([255, 0, 255]),
         6 : np.array([255, 188, 0]), 7 : np.array([137, 0, 255]),
         8 : np.array([255, 51, 153]),
         9 : np.array([0, 102, 51]), 10 : np.array([102, 51, 0]),
        11 : np.array([204, 153, 255]), 12 : np.array([153, 255, 204]),
        13 : np.array([255, 153, 153]), 14 : np.array([196, 255, 0])
        }
    cVals = [0] #Makes constants in a certain range to add to each Newton iteration, changing c and making GIF from images is very interesting
    a = 1 #Constant to multiply by each Newton iteration, haven't experimented with yet
    shading = True #If true, each pixel will be modified by the number of iterations it took to get there
    for i in range(len(cVals)): #Generates a nova fractal for a range of c values
        M = np.zeros((height, width, 3), int) #2D array of points, each will hold an RGB value
        curC = cVals[i]
        for v, y in enumerate(yValues):
            for u, x in enumerate(xValues):
                curP = complex(x, y)
                rootInfo = compareToRoots(curP, roots, iterError, maxIteration, a, curC) #Find closest root to the current complex value and num iterations to get there
                curColor = colorRootMap[rootInfo[0]]
                if shading == True: #If shading desired
                    curColor = np.clip(curColor - rootInfo[1] * 5, 0, 255) #Since Newton is so good, multiply num iterations by 10 and subtract from each RGB value, then make sure all
                    #numbers are in range (0, 255) for RGB
                M[v, u] = curColor #Set the point's color to that of the root
        
        plt.imshow(M, origin="lower")
        plt.savefig('newton_nova_' + str(i + 1) + '.png')
        plt.show()
        print("Picture "  + str(i) + " created")
        
    #print("Time to create: " + str(time.time() - start) + " seconds")
    
if __name__ == "__main__":
    main()
        
