#include <bits/stdc++.h>
using namespace std;

int n,dp[103][103][2],a[103],z;
int main(){
	cin>>n;
	for(int i=1;i<n+1;i++) cin>>a[i];
	for(int i=0;i<103;i++)
	{
	    for(int j=0;j<103; j++) 
	        dp[i][j][0]=dp[i][j][1]=1e9;
	    
	}
	dp[0][0][0]=0;dp[0][0][1]=0;
	for(int i=1;i<n+1;i++){
		for(int j=0;j<i+1;j++){
			if(a[i]%2==0) 
			    dp[i][j][0]=min(dp[i-1][j-1][0],dp[i-1][j-1][1]+1);
			if(a[i]%2==1 || a[i]==0) 
			dp[i][j][1]=min(dp[i-1][j][0]+1,dp[i-1][j][1]);
		}
	}
	cout<<min(dp[n][n/2][0],dp[n][n/2][1]);
}
