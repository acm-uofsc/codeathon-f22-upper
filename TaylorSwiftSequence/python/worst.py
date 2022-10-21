

# Vars
#: N - Number of prompts
#: B - Base of the function
#: U - Upper bound on what terms will be asked
def sol(N,B,U):
  for _ in range(N):
    target = int(input()) #: Print f(target)
    print(sol_help(target,B,U))
    

def sol_help(n,B,U):
  if n < B: return n

  else:
    s = 0
    for i in range(1,B+1):
      s += sol_help(n-i,B,U)
    return s
  
  


N,B,U = list(map(int,input().split(" ")))
sol(N,B,U)