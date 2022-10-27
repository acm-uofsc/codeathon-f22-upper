

# Vars
#: N - Number of prompts
#: B - Base of the function
#: U - Upper bound on what terms will be asked
def sol(N,B,U):
  arr = [None] * (U+1)

  for _ in range(N):
    target = int(input()) #: Print f(target)
    ret, arr = sol_help(target,arr,B,U)
    print(ret)

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


N,B,U = list(map(int,input().split(" ")))
sol(N,B,U)