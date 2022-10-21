import numpy as np
from random import randint


DATA_PATH="data/"
IN_PATH="input/"
OUT_PATH="output/"

NUM_EASY = 10
NUM_MED = 10
NUM_HARD = 10

NUM_CASES = NUM_EASY + NUM_MED + NUM_HARD

# Vars
#: N - Number of prompts
#: B - Base of the function
#: U - Upper bound on what terms will be asked
def sol(N,B,U,ts):
  arr = [None] * (U+1)

  ret_arr = []
  for t in ts:
    target = int(t) #: Print f(target)
    ret, arr = sol_help(target,arr,B,U)
    ret_arr.append(ret)
  return ret_arr

def sol_help(n,arr,B,U):
  if n < B: return n,arr
  
  if arr[n-B] is None:
    s = 0
    for i in range(1,B+1):
      ret,arr = sol_help(n-i,arr,B,U)
      s += ret
    arr[n-B] = s
    return s,arr 
  
  else:
    return arr[n-B],arr

def num_to_text(num,digits=2):
  assert (digits >= 1)
  ret = str(num)
  while len(ret) < digits: ret = "0" + ret
  return ret

def write_case(data,fn):
  N,B,U = list(map(str,data[:3]))
  with open(fn,'w') as file:
    file.write(N + " " + B + " " + U + "\n")
    for num in list(map(str,data[3:])):
      file.write(num+"\n")

#$ Generate an easy test case
#: Number of requests ranges from 5 to 30
#: The base of the function ranges from 2 to 10
#: Requests range between B and 25+B
def gen_easy_case():
  
  NRG = (5,30)
  BRG = (2,10)
  U = 20

  N = randint(NRG[0],NRG[1])
  B = randint(BRG[0],BRG[1])

  arr = [N,B,U]
  for _ in range(N): arr.append(randint(B,U+B))
  
  return np.array(arr)

#$ Generate a medium test case
#: Number of requests will be very high, 500-1000
#: Base does not matter but will range from 2 to 10
#: Requests will all be the same number B+22
def gen_med_case():
  NRG = (500,1000)
  BRG = (2,10)
  U = 22

  N = randint(NRG[0],NRG[1])
  B = randint(BRG[0],BRG[1])

  arr = [N,B,U]
  for _ in range(N): arr.append(U+B)
  
  return np.array(arr)

#$ Generate a hard test case
#: Number of requests ranges from 100 to 1000
#: The base of the function ranges from 10 to 30
#: Prompts range between B and 40+B
def gen_hard_case():
  
  NRG = (100,1000)
  BRG = (10,30)
  U = 40

  N = randint(NRG[0],NRG[1])
  B = randint(BRG[0],BRG[1])

  arr = [N,B,U]
  for _ in range(N): arr.append(randint(B,U+B))
  
  return np.array(arr)

def gen_case(case):
  if case < NUM_EASY:
    return gen_easy_case()
  elif case < NUM_EASY + NUM_MED:
    return gen_med_case()
  elif case < NUM_CASES:
    return gen_hard_case()
  # else:
  #   return gen_empty_case()
  
  
  targets = np.round((np.random.rand(N) * U) + B)
  for i in range(N):
    print(int(targets[i]))

def solve_case(fin,fout):
  with open(fin) as file:
    lines = [line[:-1] for line in file.readlines()]
    N,B,U = list(map(int,lines[0].split(" ")))
    ts = lines[1:]
  
  data = sol(N,B,U,ts)

  with open(fout,'w') as file:
    for d in data:
      file.write(str(d) + "\n")
    



for i in range(NUM_CASES):
  case_num = num_to_text(i,digits=len(str(NUM_CASES)))
  data = gen_case(i)
  fin = DATA_PATH + IN_PATH + "input" + case_num + ".txt"
  fout = DATA_PATH + OUT_PATH + "output" + case_num + ".txt" 
  write_case(data,fin)
  solve_case(fin,fout)


  



