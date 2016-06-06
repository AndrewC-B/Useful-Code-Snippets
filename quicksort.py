def qs(items):
	pivot = items[0]

	smaller = []
	equal = []
	larger = []

	for item items:
		if item < pivot:
			smaller.append(item)
		elif item == pivot:
			equal.append(item)
		else:  # item > pivot
			larger.append(item)
	
	return qs(smaller) + equal + qs(larger)
	
	
def qs_in_place(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    if begin >= end:
        return
    
    pivot = partition(array, begin, end)
    qs_in_place(array, begin, pivot-1)
    qs_in_place(array, pivot+1, end)
    
    
def partition(array, begin, end):
    pivot = begin
    
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    
    array[pivot], array[begin] = array[begin], array[pivot]
    
    return pivot