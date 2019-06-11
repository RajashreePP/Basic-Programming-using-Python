import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print (numpy.concatenate((array_1, array_2), axis = 1))

import numpy

array_1 = numpy.ndarray([[1,2,],[1,2,],[1,2,],[1,2,]])
array_2 = numpy.array([[3,4],[3,4],[3,4]])

print (numpy.concatenate((array_1, array_2), axis = 0))

import numpy
N, M, P = map(int, input().split())
n = numpy.array([map(int, input().split()) for _ in range(N)])
m = numpy.array([map(int, input().split()) for _ in range(M)])
print (numpy.concatenate((n, m),axis=0))

   
    