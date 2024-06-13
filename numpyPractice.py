# Numpy Practice and importance

import cv2
import numpy as np
import matplotlib.pyplot as plt

a,b,c,d = (1,2,np.nan,4),(7,8,9,10),(11,12,13,14),(17,18,19,20)
A = np.array([a,b,c,d])
mean = A.mean(axis=0)
zeroo = np.all(A)
nonZero = np.any(A)
nAn = np.isnan(A)
arr = np.arange(30,70,2)
rnd = np.random.uniform(0,1,1)
'''
print("Original", A)
print("Mean", mean)
print(arr)
print(arr[1:-1])
print(rnd)'''

'''
x = np.arange(4,18,2)
x[(x>4)&(x<14)]*=-1
print(x)'''

'''
nDim = np.arange(10,22).reshape((3,4))
print(nDim)

header = "col1, col2, col3, col4"
np.savetxt("arrTxt.txt", nDim, fmt="%d",header=header)

result = np.loadtxt("arrTxt.txt")
print(result)'''

'''
x = np.array([1,2,3,4,7,8,9])
xByte = x.tobytes()

x2 = np.fromstring(xByte, dtype=x.dtype)

print(np.array_equal(x,x2))'''

'''
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.2)
y = np.sin(x)
print("Plot the points using matplotlib:")
plt.plot(x, y)
plt.show() '''

'''
nums = np.array([[3, 2, np.nan, 1],
                 [10, 12, 10, 9],
                 [5, np.nan, 1, np.nan]])

print("Original array:")
print(nums)
print("\nFind the missing data of the said array:")
print(np.isnan(nums)) '''

'''
nums = np.array([[5.54, 3.38, 7.99],
              [3.54, 8.32, 6.99],
              [1.54, 2.39, 9.29]])
print("Original array:")
print(nums)
n = 8.32
r = 18.32
print("\nReplace elements of the said array which are equal to ",n,"with",r)
print(np.where(nums == n, r, nums))
print("\nReplace elements with of the said array which are less than",n,"with",r)
print(np.where(nums < n, r, nums))
print("\nReplace elements with of the said array which are greater than",n,"with",r)
print(np.where(nums > n, r, nums))'''

'''
nums = np.array([[5.54, 3.38, 7.99],
              [3.54, 4.38, 6.99],
              [1.54, 2.39, 9.29]])
print("Original array:")
print(nums)
n = 5
print("\nElements of the said array greater than",n)
print(nums[nums > n])
n = 6
print("\nElements of the said array less than",n)
print(nums[nums < n])'''

'''
nums1 = np.array([[2, 5, 2],
              [1, 5, 5]])
nums2 = np.array([[5, 3, 4],
              [3, 2, 5]])
print("Array1:") 
print(nums1)
print("Array2:") 
print(nums2)
print("\nMultiply said arrays of same size element-by-element:")
print(np.multiply(nums1, nums2))'''

'''
nums = np.array([[[1, 2, 3, 4],
               [0, 1, 3, 4],
               [90, 91, 93, 94],
               [5, 0, 3, 2]]])
print("Original array:")
print(nums)
print("\nSwap rows and columns of the said array in reverse order:")
new_nums = print(nums[::-1, ::-1])
print(new_nums)'''


'''
nums = np.arange(16, dtype='int').reshape(-1, 4)
print("Original array:")
print(nums)
print("\nNew array after swapping first and last columns of the said array:")
new_nums = nums[:, ::-1]
print(new_nums)'''

# 3 dimensional Array

'''
nums = np.array([[[1, 5, 2, 1],
                  [4, 3, 5, 6],
                  [6, 3, 0, 6],
                  [7, 3, 5, 0],
                  [2, 3, 3, 5]],

                 [[2, 2, 3, 1],
                  [4, 0, 0, 5],
                  [6, 3, 2, 1],
                  [5, 1, 0, 0],
                  [0, 1, 9, 1]],

                 [[3, 1, 4, 2],
                  [4, 1, 6, 0],
                  [1, 2, 0, 6],
                  [8, 3, 4, 0],
                  [2, 0, 2, 8]]])
print("Array:")
print(nums)
'''

x = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("Original numbers:")
print(x)
print(y)
print("Comparison - equal:")
print(np.equal(x, y))
print("Comparison - equal within a tolerance:")
print(np.allclose(x, y))