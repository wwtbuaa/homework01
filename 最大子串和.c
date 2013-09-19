int maxsum(int *p,int size){
	int i;
	int sum,ans;
	sum=0;
	ans=-1000000;
	for(i=0;i<size;i++){
		if(sum+p[i]<p[i])
			sum=0;
		sum+=p[i];
		if(ans<sum)
			ans=sum;
	}
	return ans;
}

int maxsum2(int *p,int m,int n){
	int i,j,k;
	int temp[m]={0};
	sum=0;
	ans=-1000000;
	for(i=0;i<n;i++){
		for(j=i;j<n;j++){
			for(k=0;k<m;k++){
				temp[k]+=p[j][k];
				if(sum+temp[k]<temp[k])
					sum=0;
				sum+=temp[k];
				if(ans<sum)		
					ans=sum;
			}
		sum=0;
		}
		sum=0;
		temp[m]={0};
	}
	return ans;
}
		
					