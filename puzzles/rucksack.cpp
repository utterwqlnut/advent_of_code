#include <bits/stdc++.h>
using namespace std;
int main(){
	ifstream fin("rucksack.in");
	int ans=0;
	while(!fin.eof()){
		bool seen1[52]={false};
		bool seen2[52]={false};
		string s;
		fin>>s;
		for(int i=0;i<(int)s.size();i++){
			int val=0;
			if(s[i]<'a')
				val=s[i]-'A'+26;
			else
				val=s[i]-'a';
			if(i<s.size()/2)
				seen1[val]=true;
			else
				seen2[val]=true;
		}
		for(int i=0;i<52;i++){
			if(seen1[i]&&seen2[i]){
				ans+=i+1;
				break;
			}
		}
	}
	cout<<ans<<"\n";
}
