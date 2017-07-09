from numpy import *
print random.rand(4,4) # array

randMat = mat(random.rand(4,4)) # convert an array to a matrix
print randMat.I # .I operator solves the inverse of a matrix

print eye(4) # eye(4) just creates an identity matrix of size 4.