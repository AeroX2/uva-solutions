
#include <iostream>
#include <algorithm>
#include <string>
#include <strings.h>

using namespace std;

bool compare(const char lhs, const char rhs) {
    //TODO This the correct way of doing it but
    //I don't understand how to modify this function to return the correct order
    return lhs < rhs;
}

int main() {
    int cases;
    string word;

    getline(cin,word);
    cases = stoi(word);

    for (int i = 0; i < cases; i++) {
        getline(cin, word);
        sort(word.begin(), word.end());
        do {
            cout << word << endl;
        } while (next_permutation(word.begin(), word.end(), compare));
    }

    return 0;
}
