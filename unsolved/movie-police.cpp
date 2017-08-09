#include <iostream>
#include <string.h>
#include <climits>
#include <vector>
#include <bitset>

using namespace std;

int distance(string clip, string movie) {
	int min_distance = INT_MAX;
	int movie_len = movie.length();
	int clip_len = clip.length();

	for (int i = 0; i < movie_len-clip_len+1; i++) {

		bitset<100> movie_i(movie);
		bitset<100> clip_i(clip);

		movie_i >>= i;
		movie_i &= (1 << clip_len)-1;

		int count = (movie_i ^ clip_i).count();

		if (count < min_distance) min_distance = count;
	}
	return min_distance;
}

int main() {
	int m,q;
	cin >> m >> q; 
	cin.ignore(256,'\n');

	vector<string> movies;
	for (int i=0; i<m; i++) {
		string movie;
		getline(cin, movie);
		movies.push_back(movie);
	}

	for (int i=0; i<q; i++) {
		string clip;
		getline(cin, clip);
		
		//cout << "Clip " << clip << endl;

		int min_distance = INT_MAX;
		int min_index = 0;

		for (int j=0; j<m; j++) {
			int haming_distance = distance(clip, movies[j]);

			//cout << "Clip " << clip << endl;
			//cout << "Movie " << movies[j] << endl;
			//cout << "Haming " << haming_distance << endl;

			if (haming_distance < min_distance) {
				min_distance = haming_distance;
				min_index = j+1;
			}

			//cout << "On j " << j << endl;
		}

		//cout << "Clip " << clip << endl;
		//cout << "Movie " << movies[min_index-1] << endl;
		//cout << "Haming " << min_distance << endl;
		cout << min_index << endl;
	}
	
	return 0;
}
