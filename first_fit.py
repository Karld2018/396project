import matplotlib.pyplot as plt

from random import seed
from random import randint
import time
import statistics

def firstFit(blockSize, items):
  n = len(items)
  blocks = [blockSize] * n
  usage = 0
  for i in range(n):
    for j in range(n):
      usage = max(usage, j+1)
      if blocks[j] >= items[i]: 
        blocks[j] -= items[i] 
        break
  '''
  fig, ax = plt.subplots()
  ax.bar(range(usage+1), blocks[:usage+1])
  ax.set(xlabel='# bin', ylabel='empty space',
       title='Empty space in the bins')
  fig.savefig("firstFit_"+str(blockSize)+"_"+str(len(items))+".png")
  plt.show()
  '''
  return usage

def bestFit(blockSize, items):
  n = len(items)
  blocks = [blockSize] * n
  usage = 0
  for i in range(n):
    best = blockSize
    best_index = -1
    for j in range(usage):
      if(blocks[j]>=items[i] and blocks[j]<best):
        best = blocks[j]
        best_index = j
    if best_index == -1:
      blocks[usage] -= items[i]
      usage += 1
      

    else:
      blocks[best_index] -= items[i] 
  '''
  plt.bar(range(usage+1), blocks[:usage+1])
  plt.show()
  '''
  return usage

def firstFitDecreasing(blockSize, items):
  items[::-1].sort()
  return firstFit(blockSize, items)

def bestFitDecreasing(blockSize, items):
  items[::-1].sort()
  return bestFit(blockSize, items)

def autolabel(rects, list1):
  """
  Attach a text label above each bar displaying its height
  """
  i = 0
  for rect in rects:
    height = rect.get_height()
    print(height)
    ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
      '%f' % list1[i],
      ha='center', va='bottom')
    i += 1


if __name__ == '__main__':

  blockSize = int(input("input blocksize:"))
  n_item = int(input("input number of items:"))
  n_loop = int(input("input number of loops:"))

  time_used_list = [[], [], [], []]
  bin_used_list = [[], [], [], []]

  for i in range(n_loop):
	#seed(1)
    seed(int(time.time() * 10000))
    items = []
    for i in range(n_item):
      items.append(randint(0, blockSize))
    #print(items)

    time_start=time.time()
    bin_used_list[0].append(firstFit(blockSize, items))
    time_used_list[0].append(time.time()-time_start)

    time_start = time.time()
    bin_used_list[1].append(bestFit(blockSize, items))
    time_used_list[1].append(time.time()-time_start)

    time_start = time.time()
    bin_used_list[2].append(firstFitDecreasing(blockSize, items))
    time_used_list[2].append(time.time()-time_start)

    time_start = time.time()
    bin_used_list[3].append(bestFitDecreasing(blockSize, items))
    time_used_list[3].append(time.time()-time_start)
  
  name_fit = ['first fit', 'best fit', 'first fit decreasing', 'best fit decreasing']

  time_used = []
  bin_used = []
  for i in range(4):
  	time_used.append(statistics.mean(time_used_list[i]))
  	bin_used.append(statistics.mean(bin_used_list[i]))

  fig, ax = plt.subplots()
  rects = ax.bar(name_fit, time_used)
  ax.set( ylabel='Average running time (s)',
       title='The average running time of the algorithms')


  min_time = min(time_used)
  max_time = max(time_used)
  diff_minmax = (max_time - min_time) / 5
  ax.set_ylim(0, max_time + diff_minmax * 2)
  """
  Attach a text label above each bar displaying its height
  """
  for rect in rects:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., height + diff_minmax / 2,
      '%f' % height,
      ha='center', va='bottom')

  fig.savefig("runtime_"+str(blockSize)+"_"+str(n_item)+".png")
  plt.show()

  fig, ax = plt.subplots()
  rects = ax.bar(name_fit, bin_used)
  ax.set( ylabel='Average bin used',
       title='The average bin used by the algorithms')


  
  min_bin = min(bin_used)
  max_bin = max(bin_used)
  diff_minmax = (max_bin - min_bin) / 5
  ax.set_ylim(min_bin - diff_minmax, max_bin + diff_minmax * 2)

  for rect in rects:
    height_0 = rect.get_height()
    print(height_0)
    '''
    height = height_0 - (min_bin - diff_minmax)
    print (height)
	'''

    ax.text(rect.get_x() + rect.get_width()/2.,  height_0 + diff_minmax / 2,
      '%d' % height_0,
      ha='center', va='bottom')

  fig.savefig("nbins_"+str(blockSize)+"_"+str(n_item)+".png")
  plt.show()