import random as rd
from math import sqrt
def mean(li,total):
	sum=0
	for n in li:
		sum +=n
	return sum/total


def main():
	k=3
	total=100
	l1 = rd.sample(range(1000),total) # [0-1000]
	l2 = rd.sample(range(2000),total) # [0-2000]
	
	cluster1,cluster2=	cluster(l1, l2,k,total)
	print(f'L1: {cluster1}') 
	print(f'L2: {cluster2}') 
def cluster(l1,l2,k,total):
	i=0
	while i<k:
		cluster1 = []
		cluster2 = []
		mean_l1 = mean(l1,total)
		mean_l2 = mean(l2,total)
		#print(f'Mean L1: {mean_l1} Mean L2: {mean_l2}')
		for n in l1: 
			d1 = sqrt((n-mean_l1) **2 +  (n-mean_l2) **2)
			d2 = sqrt((n-mean_l2) **2 + (n-mean_l2)**2)
			if	d1 < d2:
				cluster1.append(n)	
			else:
				cluster2.append(n)
		for l in l2:
			d1 = sqrt((l-mean_l1) **2 +  (l-mean_l2) **2)
			d2 = sqrt((l-mean_l2) **2 + (l-mean_l2)**2)
			if	d1 < d2:
				cluster1.append(n)	
			else:
				cluster2.append(n)
		i+=1

	return [cluster1,cluster2]
if __name__ == '__main__':
	main()
