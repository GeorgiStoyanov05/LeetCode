def merge(nums1, m, nums2, n):
        mIndex = 0
        nIndex = 0
        for i in range(0, m+n):
            if(mIndex>=m+nIndex):
                 nums1[i] = nums2[nIndex]
                 nIndex+=1
            elif(nIndex>=n):
                continue
            elif (nums1[mIndex]>nums2[nIndex]):
                nums1.insert(mIndex, nums2[nIndex])
                nums1.pop()
                nIndex+=1
            mIndex+=1
        print(nums1)
merge([1,2,3,0,0,0], 3, [2,5,6], 3)