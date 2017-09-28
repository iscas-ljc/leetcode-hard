class Solution(object):
	def findNNumber(self,nums1,nums2,n):
		len1=len(nums1)
		len2=len(nums2)
		if len1==0:
			return nums2[n-1]
		if len2==0:
			return nums1[n-1]
		x=0
		t1=0
		t2=0
		result=0
		while(x!=n):
			if t1>len1-1:
				result=nums2[t2]
				t2=t2+1
				x+=1
				continue
			if t2>len2-1:
				result=nums1[t1]
				t1=t1+1
				x+=1
				continue
			if t1<=len1-1 and t2<=len2-1:
				if nums1[t1]<nums2[t2]:
					result=nums1[t1]
					t1+=1
				else:
					result=nums2[t2]
					t2+=1
			x+=1
		return result

	def findMedianSortedArrays(self, nums1, nums2):
		len1=len(nums1)
		len2=len(nums2)
		if (len1+len2)%2==0:
			return (self.findNNumber(nums1,nums2,(len1+len2)/2)+self.findNNumber(nums1,nums2,(len1+len2)/2+1))/2.0
		if (len1+len2)%2!=0:
			return self.findNNumber(nums1,nums2,(len1+len2)/2+1)