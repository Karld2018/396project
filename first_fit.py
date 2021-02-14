try:
    import matplotlib.pyplot as plt
except:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

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
  plt.bar(range(usage+1), blocks[:usage+1])
  plt.show()

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
    
  plt.bar(range(usage+1), blocks[:usage+1])
  plt.show()

def firstFitDecreasing(blockSize, items):
  items[::-1].sort()
  firstFit(blockSize, items)

def bestFitDecreasing(blockSize, items):
  items[::-1].sort()
  bestFit(blockSize, items)


if __name__ == '__main__':
  blockSize = 300
  items = [212, 30, 80, 100, 120, 40, 70, 200, 150, 250, 50, 250, 160, 70, 170, 112, 45, 60,160,100,160, 150, 150, 50, 50]
  #items = [100, 210, 50]
  firstFit(blockSize, items)
  bestFit(blockSize, items)
  firstFitDecreasing(blockSize, items)
  bestFitDecreasing(blockSize, items)