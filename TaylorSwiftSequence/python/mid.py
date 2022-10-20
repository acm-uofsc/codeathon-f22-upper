

#$ Vars
#: N - Number of prompts
#: B - Base of the function
#: U - Upper bound on what terms will be asked
def sol(N,B,U):
  arr = [None] * (U+1)


  for _ in range(N):
    target = int(input()) 
    if arr[target-B] is None:
      ret = sol_help(target,B,U)
      arr[target-B] = ret
    print(arr[target-B])

def sol_help(n,B,U):
  if n < B: return n

  else:
    s = 0
    for i in range(1,B+1):
      s += sol_help(n-i,B,U)
    return s

N,B,U = list(map(int,input().split(" ")))
sol(N,B,U)