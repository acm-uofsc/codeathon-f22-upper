It seems that sounds are able to influence some hardware [(True Story)](https://devblogs.microsoft.com/oldnewthing/20220816-00/?p=106994). In your case, the bits in row $B$ of your outdated calculator have been completely messed up. Good thing the **Bit Bird Brigade** is here to help! Their chirps and tweets are able to do different bit operations. 

Since you don't have all day, you want to find the fewest number of operations that can be done to make row $B$ (the starting state of the bits) match row $A$ (the desired state). While only row $B$ can be changed, they are able to perform operations that require two inputs by using rows $B$ and $C$ and store the result in row $B$. NOTE: all rows have a fixed width

The operations the **Bit Bird Brigade** can do are:
* xor ($B$ ^ $C$)
* or ($B$ | $C$)
* and ($B$ & $C$)
* not (flip all bits in row $B$)
* left shift (shift all bits in row $B$ once to the left. If a bit is in the "on" state in the far left position of the row, left shift cannot be performed)
* right shift (shift all bits in row $B$ once to the right. If a bit is in the "on" state in the far right position of the row, when right shift is performed, the bit is lost i.e. if $B$ is `0101` and right shift is performed, $B$ becomes `0010`)
