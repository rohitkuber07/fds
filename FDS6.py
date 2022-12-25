input_list = [1,20,0.22,0.43,0.36,0.39,0.27]
print('ORIGINAL LIST:')

###################################INSERTION SORT ##############################
def intersection_sort(bucket):
    for i in range(1,len(bucket)):
        var = bucket[i]
        j=i-1
        while(j>=0 and var<bucket[j]):
            bucket[j+1]
            j=j-1
            bucket[j+1]=var

def bucket_sort(input_list):
    #Dind th maximaum value in list and use length of the list to determine which value in the list goes into which bucket
    max_value = max(input_list)
    size = max_value/len(input_list)

    #Create n empty buckets n where n is equal to the length of the input ist
    bucket_list = []
    for x in range(len(input_list)):
        bucket_list.append([])

    #put list element in different bucket based on the size
    for i in range(len(input_list)):
        j = int(input_list[i]/size)
        
        if j!=len(input_list):
            bucket_list[j].append(input_list[i])
        else:
            bucket_list[len(input_list) -1].append(input_list[i])
    
    #Sort element within the bucket using Insertion sort
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])

    #Concenate bucket with sorted element into a single list
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + bucket_list[x]
    return final_output

    ########################## Main ##################################
    sorted_list = bucket_sort(input_list)
    print('SORTED LIST BY BUCKET SORT :')
    print(sorted_list)
    