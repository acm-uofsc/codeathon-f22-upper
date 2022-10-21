You are in charge of Taylor Swift's upcoming concert and must assign seat numbers to all of the seats in the stadium. However, Miss Swift is very particular about what the seat numbers should be. 

To start, the first row is the VIP row, and has its own numbering system so you do not need to worry about it. For every other row __M__, the first seat (That is seat 0, since 0-based indexing is used), is given the value of 0 , the next __M__ - 1 seats numbers are all 1 more than the previous. For any seat __N__ where __N__ > __M__, the number is decided by the sum of the previous __M__ seats. For example, where M==4, S(4) = S(3) + S(2) + S(1) + S(0) = 3 + 2 + 1 + 0 = 6.

For any given row, you will be asked to find __L__ seat numbers, with the maximum seat being __M+K__.


