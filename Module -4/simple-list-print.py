

import sys

fd=open(sys.argv[1],"r")
lines = [line.rstrip() for line in fd]
print lines


======
Related output 

["1'1", '1 exec sp_ (or exec xp_)', '1 and 1=1', "1' and 1=(select count(*) from tablenames); --", '1 or 1=1', "1' or '1'='1", '1or1=1', "1'or'1'='1", "fake@ema'or'il.nl'='il.nl"]


=======================================================================================================================================================================================================================


import sys

with open('sqlipayload.txt') as f:
    lines = [line.rstrip() for line in f]
    print lines

======
Related output 

["1'1", '1 exec sp_ (or exec xp_)', '1 and 1=1', "1' and 1=(select count(*) from tablenames); --", '1 or 1=1', "1' or '1'='1", '1or1=1', "1'or'1'='1", "fake@ema'or'il.nl'='il.nl"]

=======================================================================================================================================================================================================================





import sys
with open("sqlipayload.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
        print lines

======
Related output 




["1'1\n"]
["1'1\n", '1 exec sp_ (or exec xp_)\n']
["1'1\n", '1 exec sp_ (or exec xp_)\n', '1 and 1=1\n']
["1'1\n", '1 exec sp_ (or exec xp_)\n', '1 and 1=1\n', "1' and 1=(select count(*) from tablenames); --\n"]
["1'1\n", '1 exec sp_ (or exec xp_)\n', '1 and 1=1\n', "1' and 1=(select count(*) from tablenames); --\n", '1 or 1=1\n']
["1'1\n", '1 exec sp_ (or exec xp_)\n', '1 and 1=1\n', "1' and 1=(select count(*) from tablenames); --\n", '1 or 1=1\n', "1' or '1'='1\n"]
["1'1\n", '1 exec sp_ (or exec xp_)\n', '1 and 1=1\n', "1' and 1=(select count(*) from tablenames); --\n", '1 or 1=1\n', "1' or '1'='1\n", '1or1=1\n']
["1'1\n", '1 exec sp_ (or exec xp_)\n', '1 and 1=1\n', "1' and 1=(select count(*) from tablenames); --\n", '1 or 1=1\n', "1' or '1'='1\n", '1or1=1\n', "1'or'1'='1\n"]
["1'1\n", '1 exec sp_ (or exec xp_)\n', '1 and 1=1\n', "1' and 1=(select count(*) from tablenames); --\n", '1 or 1=1\n', "1' or '1'='1\n", '1or1=1\n', "1'or'1'='1\n", "fake@ema'or'il.nl'='il.nl\n"]




=======================================================================================================================================================================================================================




#https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

