#include <iostream>
#include "math.h"
using namespace std;

int main(int argc, char *argv[]){
	int vol,count=0,num=10;

	if(argc != 2){
		cout << "Got"<<argc-1<<"argument(s), need one int\n";
		return -1;
	}
	vol = atoi(argv[1]);
	// cout << vol <<endl;

	while(count < vol)
	{
		num++;
		double sq =sqrt((double)num);
		int i=2,sum=1;
		while(i<=(int)sq && sum<=num)
		{
			if(num % i == 0)
			{
				sum = (i == num/i) ? sum+i : sum+i+num/i;
			}
			i++;
		}
		if(sum > num)
		{
			count++;
			cout<<num<<endl;
		}
	}
}
