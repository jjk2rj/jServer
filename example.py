import hashlib
hasher = hashlib.new('md5')
with open('hi.txt', 'rb') as afile:
        buf = afile.read()
        # print("buf: "+buf)
        hasher.update(buf)
        hash = hasher.hexdigest()
        print(hash)
        # print("buffer" + buf)