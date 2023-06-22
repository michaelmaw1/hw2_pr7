class S:
    def intersection(self, nums1, nums2):
        #Create a Hash Map to store the fequency of elements in nums1
        hashMap, result = {}, []
        #Loop to store the elements in nums1 as a key:value pair in the Hash Map
        for x in nums1:hashMap[x] = hashMap.get(x, 0 ) + 1
        #Loop to check if each element in nums2 is present and appears more than once in the Hash Map
        for x in nums2:
            if x in hashMap and hashMap[x] != 0:
                #Add given element to array
                result.append(x)
                #Decrease the frequency
                hashMap[x] -= 1

        return result

array1 = [3,7,2,6,6,9,5,1,1]
array2 = [9,4,9,8,6,1,0,6,6]
test = S()
print(test.intersection(array1,array2))

