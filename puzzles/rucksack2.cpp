#include <bits/stdc++.h>
using namespace std;
void count(string s,bool seen[52]){
	for(int i=0;i<(int)s.size();i++){
		int val=0;
		if(s[i]<'a')
			val=s[i]-'A'+26;
		else
			val=s[i]-'a';
		seen[val]=true;
	}
}
int main(){
	ifstream fin("rucksack2.in");
	int ans=0;
	while(!fin.eof()){
		bool seen1[52]={false};
		bool seen2[52]={false};
		bool seen3[52]={false};
		string s1,s2,s3;
		fin>>s1;
		fin>>s2;
		fin>>s3;
		count(s1,seen1);
		count(s2,seen2);
		count(s3,seen3);
		for(int i=0;i<52;i++){
			if(seen1[i]&&seen2[i]&&seen3[i]){
				ans+=i+1;
				break;
			}
		}
	}
	cout<<ans<<"\n";
}
