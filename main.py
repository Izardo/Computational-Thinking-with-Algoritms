'''
1: Sorting Algorithms
        1. Insertion Sort
        2. Quick Sort
        3. Bucket Sort
        4. Bubble Sort
        5. Merge Sort
2: Benchmarking
3: Plotting data

Author: Isabella Doyle
'''

# Imports modules
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

''' 
1. Insertion Sort algorithm | Ref: [1]
'''

def insertionSort(arr):
    
    # Iterates over elements in the given array starting at second position
    for i in range(1, len(arr)):
        
        # If value at index 0 is greater than value at index 1, they are swapped
        while arr[i - 1] > arr[i] and i > 0:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1  # Moves down one index
    
    return arr

''' 
2. Quick Sort algorithm | Ref: [2]
'''

def quickSort(arr):
    
    # Base case for recursion when the array contains one item
    if len(arr) < 2:       
        return arr
    else:
        
        # Chooses random value in array to use as pivot(position of partition)
        pivot = random.choice(arr)  

        # Empty lists to store partitioned arrays        
        less = []
        pivotList = []
        more = []

        # Partitioning loop creates smaller arrays
        for i in arr: 
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        
        # Recursively calls function breaking down arrays into smaller arrays & sorts them
        less = quickSort(less)
        more = quickSort(more)

        # Merges ordered lists into one sorted list
        return less + pivotList + more

'''
3. Bucket Sort algorithm | Ref: [3]
'''

def bucketSort(arr):
    
    # Finds biggest value in the arr, using length of list to decide what value is placed into each bucket
    maximum = max(arr)
    size = maximum / len(arr)

    # Creates empty buckets corresponding to the length of input array
    bucketList = []
    for x in range(len(arr)):
        bucketList.append([]) 

    # Places the items in the arr into the appropriate bucket depending on its size
    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            bucketList[j].append(arr[i])
        else:
            bucketList[len(arr) - 1].append(arr[i])

    # Sorts items in each bucket using the insertionSort() function
    for k in range(len(arr)):
        insertionSort(bucketList[k])
            
    # Concatenates the sorted items from each bucket to form one sorted arr
    final = []
    for l in range(len(arr)):
        final = final + bucketList[l]
    return final

'''
4. Bubble Sort algorithm | Ref: [4]
'''

def bubbleSort(arr):
    
    # Iterates over each element in the array
    for i in range(len(arr)):
        
        # Compares elements beside each other
        for i in range(len(arr) - 1):
            
            # Swaps elements
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr

'''
5. Merge Sort algorithm | Ref: 5
'''

# This part of the mergeSort alogrithm sorts the elements in the array
def merge(left, right): # Takes in two lists from the mergeSort() function
    
    # If left arr is empty return right
    if len(left) == 0:
        return right

    # If second is empty return left arr
    if len(right) == 0:
        return left

    result = []     # Empty list that stores result of merge
    indexLeft = 0   # Pointers 
    indexRight = 0  

    # Executes until result contains all items from original array
    while len(result) < len(left) + len(right):
        
        # Decides which element to take next from the arrays
        if left[indexLeft] <= right[indexRight]:
            result.append(left[indexLeft])
            indexLeft += 1
        else:
            result.append(right[indexRight])
            indexRight += 1

        # When the end of one array is reached, the remaining items from the 
        # other array are added to it
        if indexRight == len(right):
            result += left[indexLeft:]
            break

        if indexLeft == len(left):
            result += right[indexRight:]
            break

    return result

# This part of the merge sort algorithm uses the 'divide and conquer' method
def mergeSort(arr):
    
    # Base case if array has less than 2 items
    if len(arr) < 2:
        return arr

    # Identifies midpoint of array
    midpoint = len(arr) // 2 

    # Using recursion the partitioned portions of the array are 
    # broken down until they are individual components, after being
    # re-organised with mergeSort() function, two arrays (left and right) 
    # are returned and merged together to create a final sorted list
    return merge(
        left = mergeSort(arr[:midpoint]),
        right = mergeSort(arr[midpoint:]))

'''
2. Benchmarking the sorting algorithms
'''

# Generates an array of random numbers with parameters for size & min/max values
def genRandomArr(n):
    
    # Creates empty array
    arr = []
    
    # Creates random numbers n times & appends them to 'arr'
    for i in range(0, n):
        num = random.randint(0, 100)
        arr.append(num)
    
    # Returns array to caller
    return arr

# Times algorithm
def timeAlgo(algo, arr):
    
    # Starts timing
    start = time.time()
    
    # Executes algorithm
    algo(arr)
    
    # Ends timing
    end = time.time()
    totalTime = end - start
    return totalTime

# Main program
def main():

    # Array of various input sizes for random number generator
    input = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]

    # Arrays to store results from benchmark
    insertionTimes = []
    quickTimes = []
    bucketTimes = []
    bubbleTimes = []
    mergeTimes = []

    # Loops over input array
    for n in input:

        # Generates random arrays with genRandomArr() function & sizes specified in the 'input' array 
        inputArr = genRandomArr(n)

        # Stores 10 run-time values temporarily for each algorithm
        insertionTemp = []
        quickTemp = []
        bucketTemp = []
        bubbleTemp = []
        mergeTemp = []

        # Executes & times each algorithm 10X for each size specified in 'input' array 
        # & appends result of each execution to the temporary lists
        for j in range(10):
            insertionTemp.append(timeAlgo(insertionSort, inputArr))
            quickTemp.append(timeAlgo(quickSort, inputArr))
            bucketTemp.append(timeAlgo(bucketSort, inputArr))
            bubbleTemp.append(timeAlgo(bubbleSort, inputArr))
            mergeTemp.append(timeAlgo(mergeSort, inputArr))
        
        # Appends averaged time results (in miliseconds) from benchmark to lists above
        insertionTimes.append(np.around(np.mean(insertionTemp) * 1000, 3))
        quickTimes.append(np.around(np.mean(quickTemp) * 1000, 3))
        bucketTimes.append(np.around(np.mean(bucketTemp) * 1000, 3))
        bubbleTimes.append(np.around(np.mean(bubbleTemp) * 1000, 3))
        mergeTimes.append(np.around(np.mean(mergeTemp) * 1000, 3))

    # Creates DataFrame object with run-time results of algorithms | Ref: [7]
    df = pd.DataFrame({"Size" : input,
                        "Insertion Sort" : insertionTimes,
                        "Quick Sort" : quickTimes,
                        "Bucket Sort" : bucketTimes,
                        #"Bubble Sort" : bubbleTimes,
                        "Merge Sort" : mergeTimes})
    '''
    3. Plotting Data 
    '''
    
    # Sets 'size' as index
    df.set_index('Size', inplace = True)
    # Flips the columns and rows for improved readability
    flipDf = df.T
    
    # Plots benchmarked data on graph
    df.plot(kind = 'line', 
            title = 'Benchmark Results',
            xlabel = 'Input Size', 
            ylabel = 'Milliseconds')   
    plt.show()

    print(flipDf)
    return df    

# Initiates program       
if __name__ == "__main__":
    main()

'''
REFERENCES

[1] "Insertion Sort In Python Explained (With Example And Code)" by FelixTechTips. Available at: https://www.youtube.com/watch?v=R_wDA-PmGE4 [Accessed: 17 July 2021]
[2] "Quick Sort" by Brilliant. Available at: https://brilliant.org/wiki/quick-sort/ [Accessed: 29 July 2021]
[3] "Bucket Sort in Python" by Muhammad Junaid Khalid. Available at: https://stackabuse.com/bucket-sort-in-python/ [Accessed: 10 Aug 2021]
[4] "Bubble Sort in Python" by Olivera Popović. Available at: https://stackabuse.com/bubble-sort-in-python [Accessed: 11 Aug 2021]
[5] "The Merge Sort Algorithm in Python" by Real Python. Available at: https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python [Accessed: 12 Aug 2021]
[6] "Random - Generate pseudo-random numbers" by Python Docs. Available at: https://docs.python.org/3/library/random.html [Accessed: 20 July 2021]
[7] "DataFrame.plot.line" by pandas, Available at: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html [Accessed: 12 August 2021]

'''