var findMedianSortedArrays = (nums1, nums2)=>{
    if(nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);
    if(nums1.length == 0){
        if(nums2.length % 2 == 0){
            let i = nums2.length/2;
            return (nums2[i-1]+nums2[i])/2;
        } else {
            return nums2[Math.floor(nums2.length/2)];
        }
    }
    let half = Math.floor((nums1.length + nums2.length)/2);
    let partitionX = Math.floor(nums1.length/2);
    let partitionY = half - partitionX;

    while(nums1[partitionX-1] > nums2[partitionY] || nums2[partitionY-1] > nums1[partitionX]){   
        if(nums1[partitionX-1] > nums2[partitionY]){
            partitionX--;
            partitionY++;
        } else if(nums2[partitionY-1] > nums1[partitionX]){
            partitionX++;
            partitionY--;
        }
    }
    
    let total = nums1.length + nums2.length;
    if(total % 2 == 0){
        return (Math.max(nums1[partitionX-1] ?? -Infinity, nums2[partitionY-1] ?? -Infinity) + Math.min(nums1[partitionX] ?? Infinity, nums2[partitionY] ?? Infinity))/2;
    } else {
        return Math.min(nums1[partitionX] ?? Infinity, nums2[partitionY] ?? Infinity);
    }
};