import base64
import tempfile
import subprocess
import os
import random
import hashlib
import string 

PAGE_SIZE = 0x1000

CONST_STR = '_i_hav3_done_my_work_'
CHAL_SIZE = 4

CHARS = string.ascii_letters


def sha256(buff):
    sha_worker = hashlib.sha256()
    sha_worker.update(buff)
    return sha_worker.hexdigest()

    
def gen_PoW_challenge():
    random_chars = [random.choice(CHARS) for _ in range(CHAL_SIZE)]
    rand_const = ''.join([random.choice(CHARS) for _ in range(16)])
    chal_base = CONST_STR + rand_const
    chal_sha = sha256(bytes(''.join(random_chars) + CONST_STR + rand_const, 'utf-8'))

    return chal_base, chal_sha

   
    
def check_PoW(chal_base, chal_sha, ans):
    return sha256(bytes(''.join(ans) + chal_base, 'utf-8')) == chal_sha
    

def do_PoW_challenge(print_help = False):
    chal_base, chal_sha = gen_PoW_challenge()
    
    print ("Find 4 chars that when hashed with sha256 as (YOUR_VALUE || {}) will return {} ".format(chal_base, chal_sha))
    if print_help:
        print ("""\nFor example, if the sha256 is 292e6e7041dae8d484a04c8d224b46c556eb52b585d5f1465dbfaf33b9f0eb9e, and the challenge string is _i_hav3_done_my_work_m0yDq2bHFQQeqqz9
        You should answer ['W', '3', '4', 'j'] - since sha256.hexdigest('W34j_i_hav3_done_my_work_m0yDq2bHFQQeqqz9') is 292e6e7041dae8d484a04c8d224b46c556eb52b585d5f1465dbfaf33b9f0eb9e \n""")
    
    ans = []
    while len(ans) != CHAL_SIZE:
        ans = input('a,b,c,d: ').strip().split(',')
        if len(ans) != CHAL_SIZE:
            print ("Wrong format. Input the data the way I said")
        
    return True



def main():
	subprocess.run(['cat', 'flag.txt'], stdout=subprocess.DEVNULL)
	payload_b64 = input("Please save my cat... I'm ready to run any payload to save him!!! (base64)\n")
	#error handling
	try:
		payload = base64.b64decode(payload_b64)
	except:
		print("meow????????????")
		return
	
	if len(payload_b64) > 2*PAGE_SIZE:
		print("meow????????????")
		return
	
	tf = tempfile.NamedTemporaryFile(delete=False)
	tf.write(payload)
	tf.close()
	
	result = subprocess.run(['./app.out', tf.name], stdout=subprocess.PIPE)
	print(result.stdout)
	
	if os.path.isfile(tf.name):
		os.remove(tf.name)
	else:
		print("meow?????????????")
		return


if __name__ == "__main__":
	if do_PoW_challenge():
		try:
			main()
		except:
			print("meow????????????")
