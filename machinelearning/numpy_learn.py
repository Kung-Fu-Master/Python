import numpy as np
import os

print(os.path.abspath('.')) #current working directory
print(os.path.abspath(os.curdir)) #current working directory
print(os.path.abspath('..')) #current working directory parent directory

array = np.array([1,2,3,4,5])
print(type(array))

array2 = array + 1
print(array2)

array3 = array + array2
print(array3)
print(array3[1])

print(array.shape) #(5,) 

array = np.array([[1,2,3],[4,5,6]])
print(array)
print(type(array))
print(array.dtype)
print(array.itemsize)
print(array.shape)
print(array.size)
print(np.size(array))

#array.fill(0)
#print(array)

print(array[1][1:3])
print(array[1])
print(array[1,1])

###################################################################################################
### copy()
array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
copy_array = array         #copy_array and array point to the same memory address.
copy_array[1,1] = 100
print(copy_array)
print(array)
array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
copy_array = array.copy()  #copy_array and array point to the different memory address.
copy_array[1,1] = 100
print(copy_array)
print(array)

###################################################################################################
## array([...], [dtype=...])

tang_array = np.arange(0,100,10)
mask = np.array([0,0,0,0,0,0,1,1,1,1], dtype=bool)
print(tang_array[mask])
print(tang_array[tang_array > 50]) #same effect as the above two lines

random_array = np.random.rand(10)
print(random_array > 0.5)

indexs = np.where(tang_array > 30)
print(indexs)

tang_array = np.array([1,2,3,4,5])
tang_array = np.array([1,2,3,4,5], dtype=float)        #[1. 2. 3. 4. 5.]
tang_array = np.array([1,2,3,4,5], dtype=np.float32)   #[1. 2. 3. 4. 5.]
tang_array = np.array([1,2,3,4,5], dtype=np.float64)   #[1. 2. 3. 4. 5.]
tang_array = np.array([1,2,3,4,5,"str"])               #['1' '2' '3' '4' '5' 'str']
tang_array = np.array([1,2,3,4,5,"str"], dtype=object) #[1 2 3 4 5 'str']

tang_array = np.array([1,2,3,4,5])
tang_float_array = tang_array.astype(np.float32)
print(tang_float_array) #[1. 2. 3. 4. 5.]
print(tang_array)       #[1 2 3 4 5] tang_array don't change it's type


###################################################################################################
## sum, min, mean, max, standard_deviation, variance

tang_array = np.array([[1,2,3],
                       [4,5,6]])
sum_all = np.sum(tang_array)
sum_column = np.sum(tang_array, axis=0)     #add column elements into row vectors [5 7 9]
sum_row = np.sum(tang_array, axis=1)  #add row elements into column vectors [6 15]
dimension = tang_array.ndim              # 2

min_value = tang_array.min()
min_column = tang_array.min(axis=0)
min_row = tang_array.min(axis=1)
max_value = tang_array.max()

index_min = tang_array.argmin()
index_min_column = tang_array.argmin(axis=0)
index_min_row = tang_array.argmin(axis=1)

index_max = tang_array.argmax()

mean = tang_array.mean()
mean_column = tang_array.mean(axis=0)
mean_row = tang_array.mean(axis=1)

standard_deviation = tang_array.std()
standard_deviation_column = tang_array.std(axis=0)
standard_deviation_row = tang_array.std(axis=1)

variance = tang_array.var()
variance_column = tang_array.var(axis=0)
variance_row = tang_array.var(axis=1)

###################################################################################################
## clip(), round() np.sort() linspace() searchsorted(array, values) lexsort() logspace()

arr = np.array([[1,2,3],[4,5,6]])
#only 2 to 4 data are retained, less than 2 becomes 2 and greater than 4 becomes 4
clip_arr = arr.clip(2,4) 
"""
[[2 2 3]
 [4 4 4]]
"""

arr = np.array([1.2, 3.56, 6.41])
approximately_value = arr.round()            # to the nearest whole number
approximately_value = arr.round(1)
approximately_value = arr.round(decimals=1)  # the same as above
approximately_value = arr.round(2)           # how many digits are after the decimal point
print(approximately_value)

arr = np.array([[1.5, 1.3, 7.5],[5.6, 7.8, 1.2]])
sort_arr = np.sort(arr)
sort_arr = np.sort(arr, axis=0)
sort_arr = np.sort(arr, axis=1)

## linspace(start,end,number) 
arr = np.linspace(0,10,10)                   #add 10 digits between 0 and 10(include 10)
values = np.array([2.5, 6.5, 9.5,11])
insert_arr = np.searchsorted(arr, values)    #[ 3  6  9 10] 

arr = np.array([[1,0,6],
                [1,7,0],
                [2,3,1],
                [2,4,0]])
## First in descending(-1) order of the first column, then in ascending order of the third column
index = np.lexsort([-1*arr[:,0], arr[:,2]])
sort_index = arr[index]
print(sort_index)

log_arr = np.logspace(0,1,5) # 10 nth power [ 1. 1.77827941  3.16227766  5.62341325 10.]
print("log_arr",log_arr)

###################################################################################################
## transpose()  concatenate(), vstack(), hstack(), flatten()

arr = np.arange(10)
arr.shape = 2,5

trans_arr = arr.transpose()
trans_arr = arr.T                 #the same as above line

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[10,11,12]])

c = np.concatenate((a,b))         #Vertical stitching matrix 
c = np.vstack((a,b))              #the same as above line

c = np.concatenate((a,b), axis=1)
c = np.hstack((a,b))              #the same as above line

c = c.flatten()
print(c)


###################################################################################################
## zeros()  zeros_like() ones_linke() identity()

zero_arr = np.zeros(3)
zero_arr = np.zeros((3,3))

one_arr = np.ones((3,3))

zero_arr.fill(1)

np.zeros_like(arr)
np.ones_like(arr)

diagonal_array = np.identity(5)
print(diagonal_array)

###################################################################################################
## multiply()  dot()

x = np.array([5, 5])
y = np.array([2, 2])
z = np.multiply(x,y) #[10 10]
z = np.dot(x,y)      #20 inner product, multiply the corresponding positions and add them together.

x.shape = 2,1
y.shape = 1,2
z = np.dot(x,y)       
"""
[[10 10]
 [10 10]]
"""

###################################################################################################
## random  shuffle

random_arr = np.random.rand(3,2)
print(random_arr)
random_arr = np.random.randint(10,size=(5,4))
print(random_arr)
random_arr = np.random.randint(0,10,3)
print(random_arr)

random = np.random.rand()
print(random)

random_sample = np.random.random_sample()
print(random_sample)

mu, sigma = 0, 0.1                        #mean, variance
np.set_printoptions(precision = 2)        #print tow decimal places
arr = np.random.normal(mu, sigma, 10)     #random gaussian distribution
print(arr)

##shuffle
arr = np.arange(10)
print(arr)
arr_shuffle = np.random.shuffle(arr)
print("shuffle",arr_shuffle)

np.random.seed(100)                     #consistent random results
mu, sigma = 0, 0.1
arr = np.random.normal(mu, sigma, 10)
print(arr)

###################################################################################################
### savetxt()  loadtxt()

arr = np.array([[1,2,3],[4,5,6]])
#np.savetxt("arr.txt", arr, fmt="%d")
#np.savetxt("arr.txt", arr, fmt="%d",delimiter=",")
np.savetxt("arr.txt", arr, fmt="%.2f",delimiter=",")

#arr.txt: 
#    1.00,2.00,3.00...
#    4.00,5.00,6.00...
#data = np.loadtxt("arr.txt")
#print(data)
data = np.loadtxt("arr.txt", delimiter=",")
print(data)
#data = np.loadtxt("arr.txt", delimiter=",", skiprows=3)    #skip the first 3 line
#print(data)

arr = np.array([[1,2,3],[4,5,6]])
np.save("arr.npy", arr)
arr = np.load("arr.npy")
print(arr)



