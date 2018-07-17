#encoding:utf-8

# kye = > (ip,url,code)
# value - > cnt
access_cnt = {}

h1 = open('ngnix.log','r')
while True:
	ctx = h1.readline()
	#print ctx
	_log = ctx.split()
	if not ctx:
		break
	key = (_log[0],_log[6],_log[8])
	access_cnt[key] = access_cnt.get(key,0) + 1
h1.close()


def sort_array(array):
	for i in range(0,len(array)-1):
		for j in range(0,len(array)-1-i):
			if array[j][1] > array[j+1][1]:
				array[j],array[j+1] = array[j+1],array[j]
	return array

result = sort_array(access_cnt.items())[-1:-11:-1]
print result

h2 = open('result.txt','w+')

for i  in range(0,len(result)-1):
	node =  result[i]
	type(node)
#	print node[1], node[0][0],node[0][1],node[0][2]
	h2.write('%s %s %s %s\n' % (node[1], node[0][0],node[0][1],node[0][2]))

h2.close()


