class Fangfa
{
	public int ff(int[] nums, int length) {
		
		int duplication;
		int t=0;
		int [] b=new int[20];
		if (nums == null || length <= 0)
			return -1;
		for (int i = 0; i < length; i++) {
			while (nums[i] != i) {
				if (nums[i] == nums[nums[i]]) {
				//	duplication = nums[i];
				//	return duplication;
					b[t]= nums[i];
					t++;
					return sum(b);
				}
				swap(nums, i, nums[i]);
			}
		}
		return -1;
	}

	private void swap(int[] nums, int i, int j) {
		int t = nums[i];
		nums[i] = nums[j];
		nums[j] = t;
	}
    public int  sum(int[] a)
		{
		int sum=0;
		for(int i:a)
			sum=sum+i;
		return sum;
		
		}


}
