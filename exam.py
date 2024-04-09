from utils import unzip_with_7z
zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 
# WRITE YOUR CODE BELOW
# ---------------------------------------- 
letter1 = [chr(i) for i in range(97, 123)]
letter2 = [chr(i) for i in range(97, 123)]
for l1 in letter1:
    for l2 in letter2:
       secret_password = l1 + l2 + 'bcmpda'
       if unzip_with_7z(zip_file_path, dest_path, secret_password):
           break
    else:
        continue
    break
