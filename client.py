# importing the requests library 
import requests
import time
from concurrent.futures import ThreadPoolExecutor
# api-endpoint 
URL = "$enter url here$"
count=0;
# location given here 
location = """thisisarandomstringtoeversethisisarandomstringtoeversethisisarandomstringtoeversethisisarandomstringtoeversethisisarandomstringtoeversethisisarandomstringtoeverse"""
number_of_req=3500
my_list=[]
global_start=time.time()
#end_max=time.time()
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'q':location2}
def caller():
	#start=time.time()
	start=time.time()
	r = requests.get(url = URL, params = PARAMS,headers={'Connection':'close'})
	end = time.time()
	my_list.append(end-start)
	#count=count+1
	# extracting data in json format 
	#print(r.text)
	#end = time.time()
	#if (end-start)>(end_max-start):
	#print(end-start)
	#end_max=end


with ThreadPoolExecutor(max_workers=350) as executor:
	for i in range(number_of_req):
		executor.submit(caller)
#print(end_max-start)
executor.shutdown(wait=True)
global_end=time.time()
my_sum=0
with open('read_'+str(number_of_req)+'.txt', 'w+') as f:
    for item in my_list:
        f.write("%s\n" % item)
        my_sum=my_sum+item
my_sum=my_sum/number_of_req
print(global_end-global_start)
f2 = open('output_'+str(number_of_req)+'.txt', 'w+')
f2.write(str(my_sum))
f2.close()

#print(count)

