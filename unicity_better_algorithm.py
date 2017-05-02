from itertools import chain
from itertools import combinations

data = '''11111 1 1 1 1
12222 1 2 2 2 
13333 1 2 2 2
14444 2 2 1 4
15555 3 1 2 1
16666 3 2 3 2
17777 1 3 1 3
18888 2 3 2 4
19999 3 3 3 1
20000 1 1 1 2
21111 2 2 2 3
22222 3 3 3 4
22223 4 1 1 1
22224 4 2 2 2
22225 4 3 3 3
22226 4 4 4 4'''

#data to be entered
data = data.split('\n')
data =[i.split()[1:] for i in data]

# print data
#-----------------------------

def index_variable(variable):
	l = len(variable)
	a = {}
	for i in xrange(l):
		a[variable[i]] = i
	return a

index_info = index_variable('ABCD') # index info of each variable
print index_info
#length passed as 4 at first

#print index_info
final_ans = {}


def unicity(data, length, val): # val are variables
	if length == 0:
		return True
	all_combo = list(combinations(val, length))
	for first in all_combo: #get ABCD, ABC etc
		if first not in final_ans:
			# print first
			#do work here and update new data
			data_freq = {}
			for j in data: # 1 2 2 2, 2 1 1 3 etc
				val = ''
				
				for k in first: # individual A B C D
					# print k
					val += j[index_info[k]]
				if val not in data_freq:
					data_freq[val] = [1, j]
				else:
					data_freq[val][0] += 1 

			# print data
			new_data = [data_freq[i][1] for i in data_freq if data_freq[i][0] == 1]
			# print new_data
			
			final_ans[first] = new_data
			
			unicity(new_data, length-1, first)
	return True
		
unicity(data, 4, 'ABCD')
print "----------------------"
# print final_ans

for i in final_ans:
	print i
	for j in final_ans[i]:
		for k in i:
			print j[index_info[k]],
		print

	

	
		


	


