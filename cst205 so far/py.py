from PIL import Image

import re
list_data = re.split(' |;\n',open('data.txt','r').read())
# data convert to list
list_data = [line.rstrip(';') for line in list_data]

mona_data = list(map(int,list_data))

#print( mona_data )

mona = Image.frombytes('L', (18,29), bytes(mona_data))
mona.show()