"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)



def _binary_search(mylist, key, left, right): 
    if right >= left: 
        mid = (right + left) // 2
        if mylist[mid] == key: 
            return mid 
        elif mylist[mid] > key: 
            return _binary_search(mylist, key, left, mid - 1) 
        else: 
            return _binary_search(mylist, key, mid + 1, right) 
  
    else: 
        return -1

def test_binary_search():
  assert binary_search([1,2,3,4,5], 5) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 6) == -1
  assert binary_search([1,2,3], 1) == 0
  assert binary_search([1,2,3,4], 4) == 3



def time_search(search_fn, mylist, key):
	start_time = time.time()
	search_fn(mylist, key)
	end_time = time.time()
	return (end_time - start_time) * 1000

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6]):
	ls = []
	num_ls = []
	key = -1
  
	for size in sizes:
		for i in range(0, size -1):
			num_ls.append(i)
			lin_search_time = time_search(linear_search, num_ls, key)
			bin_search_time = time_search(binary_search, num_ls, key)
			ls.append([size, lin_search_time, bin_search_time])

	return ls

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search([10, 100])
	print_results(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1


