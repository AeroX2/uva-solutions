#include <iostream>
#include <math.h>

using namespace std;

//def generate_factors(n,k):
//    total = 0
//    for i in range(math.floor(math.sqrt(n)),0,-1):
//        div,mod = divmod(n,i)
//
//        if (mod == 0):
//            if (i % k != 0):
//                total += i
//            if (div != i and div % k != 0):
//                total += div
//    return total
 
int main() {
	long n,k,cases;
	cin >> cases;
	for (long j = 0; j < cases; j++) {
		long total = 0;

		cin >> n;
		cin >> k;
		for (long i = 1; i < floor(sqrt(n)+1); i++) {
			int div = n/i;
			int mod = n%i;
			if (mod == 0) {
				if (i % k != 0) {
					//cout << i << " " << i%k << endl;
					total += i;
				}
				if (div != i && div % k != 0) {
					//cout << div << " " << div%k << endl;
					total += div;
				}
			}
		}
		cout << total << endl;
	}
	 
	return 0;
}
