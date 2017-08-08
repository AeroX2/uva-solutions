#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int find(unordered_map<int,int>& parents,
		 int vert) {
	if (parents[vert] != vert) {
		parents[vert] = find(parents,parents[vert]);
	}
	return parents[vert];
}

void union_set(unordered_map<int,int>& parents,
			   unordered_map<int,int>& ranks,
			   int v1,
			   int v2) {
    int r1 = find(parents, v1);
    int r2 = find(parents, v2);
    if (r1 != r2) {
        int rank1 = ranks[r1];
        int rank2 = ranks[r2];
        if (rank1 > rank2) parents[r2] = r1;
        else {
            parents[r1] = r2;
            if (rank1 == rank2) ranks[r2]++;
		}
	}
}

void kruskals(unordered_map<unsigned int,int>& mst, 
			  unordered_map<int,int>& parents,
			  int locations,
			  vector<tuple<int,int,int,int>>& edges) {

	unordered_map<int, int> ranks;
	for (int i = 1; i < locations+1; i++) {
		parents[i] = i;
		ranks[i] = 0;
	}

	sort(edges.begin(), edges.end());
	for (tuple<int,int,int,int> edge : edges) {
		unsigned int cost = get<0>(edge);
		unsigned int parent = get<1>(edge);
		unsigned int child = get<2>(edge);
		if (find(parents, parent) != find(parents, child)) {
			union_set(parents, ranks, parent, child);
			//unsigned int hash = cost;
			//hash *= 37;
			//hash += parent;
			//hash *= 37;
			//hash += child;
			unsigned int index = get<3>(edge);
			mst[index] = cost;
		}
	}
}

int main() {
	//Should probably switch over to scanf
	//But why is the question time limit so tight
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
		int locations, roads, airport_cost;
		cin >> locations;
		cin >> roads;
		cin >> airport_cost;

		vector<tuple<int,int,int,int>> edges;
		for (int road = 0; road < roads; road++) {
			int parent, child, cost;
			cin >> parent;
			cin >> child;
			cin >> cost;
			if (cost < airport_cost) {
				edges.push_back(make_tuple(cost,parent,child,road));
				//edges.push_back(make_tuple(cost,child,parent));
			}
		}

		unordered_map<unsigned int,int> mst;
		unordered_map<int,int> parents;
		kruskals(mst, parents, locations, edges);

		unordered_set<int> total_airports;
		for (auto edge : parents) {
			total_airports.insert(find(parents,edge.first));
		}

		int total_cost = total_airports.size()*airport_cost;
		for (auto cost : mst) {
			total_cost += cost.second;
		}

		printf("Case #%d: %d %d\n", i+1, total_cost, total_airports.size());
	}
	return 0;
}
