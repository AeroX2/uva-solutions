
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <strings.h>

using namespace std;

bool compare(const string lhs, const string rhs) {
	for (int i = 0; i < min(lhs.length(), rhs.length()); i++) {
		char l = lhs[i];
		char r = rhs[i];

		//Stagger the sorting
		//So A then a, B then b, C then c
		if (islower(l)) l = (l-'a')*2+1;
		else l = (l-'A')*2;

		if (islower(r)) r = (r-'a')*2+1;
		else r = (r-'A')*2;

		if (l != r) {
			return l < r;
		}
	}
}

int main() {
    int cases;
    string word;

    getline(cin,word);
    cases = stoi(word);

    for (int i = 0; i < cases; i++) {
		vector<string> anagrams;

        getline(cin, word);
        sort(word.begin(), word.end());
        do {
			anagrams.push_back(word);
        } while (next_permutation(word.begin(), word.end()));

        sort(anagrams.begin(), anagrams.end(), compare);
		for (string word : anagrams) cout << word << endl;
    }

    return 0;
}
