from math import sqrt
from random import choice

def mean(l):
    sum=0;
    for a in l:
        sum +=a
    return sum/len(l)

# k--> Clusters
def k_mean(l1, k):
    sample = choice(l1) 
    cluster1 =[]
    cluster2 = []
    data = l1
    centroid1 = sample[0]
    centroid2 = sample[1]
    while centroid1 !=  centroid2:
        if cluster1 != []:
            centroid1 = mean(cluster1) # now, Centroid is from the mean.
            data.append(cluster1)
            cluster1  = []
        if cluster2 != []:  
            centroid2 = mean(cluster2)
            data.append(cluster2)
            cluster2 = []
        for a in (data):
            d = sqrt( (a[0]-centroid1) **2 + (a[1]-centroid2)**2)
            t1 = (a[0], a[1])
            if d < centroid1:
                cluster1.append(t1)
            else:
                cluster2.append(t1)
        return cluster1, cluster2          
    
def main():
    l1 = [(1.1,1,1),(1.5, 2.1),(3.1,4.1), (5.1, 7.1) ,(3.5,5.1), (4.5,5.1), (3.5,4.5)]
    cluster1, cluster2 = k_mean(l1,2)
    print('Cluster1: \n',cluster1)
    print('Cluster2: \n',cluster2)
   
if __name__ == '__main__':
    main();
