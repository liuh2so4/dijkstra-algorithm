#include<iostream>
#include<climits>
#include<cmath>
#include<stdlib.h>
#include<time.h>
using namespace std;

// Prototype of a utility function to swap two integers
template<typename tt>
void swap(tt *x, tt *y);

// A class for Min Heap
class MinHeap
{
	int *arrxtoi;
	int *arritox;
	double *harr; // pointer to array of elements in heap
	int capacity; // maximum possible size of min heap
	int heap_size; // Current number of elements in min heap
	public:

	// Constructor
	MinHeap(int capacity);

	// to heapify a subtree with the root at given index
	void MinHeapify(int );

	int parent(int i) { return (i-1)/2; }

	// to get index of left child of node at index i
	int left(int i) { return (2*i + 1); }

	// to get index of right child of node at index i
	int right(int i) { return (2*i + 2); }

	// to extract the root which is the minimum element
	int extractMin();

	// Decreases key value of key at index i to new_val
	void decreaseKey(int x, int new_val);

	// Returns the minimum key (key at root) from min heap
	int getMin() { return harr[0]; }

	// Deletes a key stored at index i
	void deleteKey(int x);

	// Inserts a new key 'k'
	void insertKey(double k, int x);
};

// Constructor: Builds a heap from a given array a[] of given size
MinHeap::MinHeap(int cap)
{
	heap_size = 0;
	capacity = cap;
	harr = new double[cap];
	arritox = new int[cap];
	arrxtoi = new int[cap];
}

// Inserts a new key 'k'
void MinHeap::insertKey(double k, int x)
{
	if (heap_size == capacity)
	{
		cout << "\nOverflow: Could not insertKey\n";
		return;
	}

	// First insert the new key at the end
	heap_size++;
	int i = heap_size - 1;
	harr[i] = k;
	arrxtoi[x] = i;
	arritox[i] = x;

	// Fix the min heap property if it is violated
	while (i != 0 && harr[parent(i)] > harr[i])
	{
		swap(&harr[i], &harr[parent(i)]);
		i = parent(i);
	}
}

// Decreases value of key at index 'i' to new_val. It is assumed that
// new_val is smaller than harr[i].
void MinHeap::decreaseKey(int x, int new_val)
{
	int i = arrxtoi[x];
	harr[i] = new_val;
	while (i != 0 && harr[parent(i)] > harr[i])
	{
		swap(&harr[i], &harr[parent(i)]);
		swap(&arrxtoi[arritox[parent(i)]], &arrxtoi[arritox[i]]);
		swap(&arritox[i], &arritox[parent(i)]);
		i = parent(i);
	}
}

// Method to remove minimum element (or root) from min heap
int MinHeap::extractMin()
{
	if (heap_size <= 0)
		return INT_MAX;
	if (heap_size == 1)
	{
		heap_size--;
		return arritox[0];
	}

	// Store the minimum value, and remove it from heap
	int root = arritox[0];
	harr[0] = harr[heap_size-1];
	arritox[0] = arritox[heap_size - 1];
	arrxtoi[0] = arrxtoi[heap_size - 1];
	heap_size--;
	MinHeapify(0);

	return root;
}


// This function deletes key at index i. It first reduced value to minus
// infinite, then calls extractMin()
void MinHeap::deleteKey(int x)
{
	decreaseKey(arrxtoi[x], INT_MIN);
	extractMin();
}

// A recursive method to heapify a subtree with the root at given index
// This method assumes that the subtrees are already heapified
void MinHeap::MinHeapify(int i)
{
	int l = left(i);
	int r = right(i);
	int smallest = i;
	if (l < heap_size && harr[l] < harr[i])
		smallest = l;
	if (r < heap_size && harr[r] < harr[smallest])
		smallest = r;
	if (smallest != i)
	{
		swap(&harr[i], &harr[smallest]);
		swap(&arrxtoi[arritox[smallest]], &arrxtoi[arritox[i]]);
		swap(&arritox[i], &arritox[smallest]);
		MinHeapify(smallest);
	}
}

// A utility function to swap two elements
	template<typename tt>
void swap(tt *x, tt *y)
{
	tt temp = *x;
	*x = *y;
	*y = temp;
}

int edgeLim(int a){
	if(a % 20 == 0)
		return 10;
	else if (a % 5 == 0)
		return 5;
	else
		return 3;
}

double distance(double x, double y, double z, double w){
	return sqrt((x - z)*(x - z) + (y - w)*(y - w));
}

const int dat = 20000;
const int boarder = 20000;

// Driver program to test above functions
int main()
{
	int nodearr[dat][2];
	double me_link_SD[dat][10][2] = {0};
	int edgelim[dat] = {0};
	srand((unsigned)time(NULL));
	for(int g = 0; g < 10; ++g){
		for(int i = 0; i < dat; ++i){
			for(int j = 0; j < dat; ++j)
				nodearr[i][j] = rand() % boarder;
		}

		for (int i = 0; i < dat; ++i){
			if (i % 20 == 0){
				for (int j = i + 1; j < dat; ++j){
					if ((j % 20 == 0 && distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]) <= boarder/2) || (j % 5 == 0 && distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]) <= boarder/4) || distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]) <= boarder/8){
						if (edgelim[i] < edgeLim(i) && edgelim[j] < edgeLim(j)) {
							me_link_SD[i][edgelim[i]][0] = j;
							me_link_SD[i][edgelim[i]][1] = distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]);
							edgelim[i]+=1;
							me_link_SD[j][edgelim[j]][0] = i;
							me_link_SD[j][edgelim[j]][1] = distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]);
							edgelim[j]+=1;
						}
						else if (edgelim[j] < edgeLim(j))
							continue;
						else
							break;
					}
				}
			}
			else if (i % 5 == 0){
				for (int j = i + 1; j < dat; ++j){
					if ((j % 5 == 0 && distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]) <= boarder/2) || distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]) <= boarder/4){
						if (edgelim[i] < edgeLim(i) && edgelim[j] < edgeLim(j)) {
							me_link_SD[i][edgelim[i]][0] = j;
							me_link_SD[i][edgelim[i]][1] = distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]);
							edgelim[i]+=1;
							me_link_SD[j][edgelim[j]][0] = i;
							me_link_SD[j][edgelim[j]][1] = distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]);
							edgelim[j]+=1;
						}
						else if (edgelim[j] < edgeLim(j))
							continue;
						else
							break;
					}
				}
			}
			else{
				for (int j = i + 1; j < dat; ++j){
					if (distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]) <= boarder/3){
						if (edgelim[i] < edgeLim(i) && edgelim[j] < edgeLim(j)) {
							me_link_SD[i][edgelim[i]][0] = j;
							me_link_SD[i][edgelim[i]][1] = distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]);
							edgelim[i]+=1;
							me_link_SD[j][edgelim[j]][0] = i;
							me_link_SD[j][edgelim[j]][1] = distance(nodearr[i][0], nodearr[i][1], nodearr[j][0], nodearr[j][1]);
							edgelim[j]+=1;
						}
						else if (edgelim[j] < edgeLim(j))
							continue;
						else
							break;
					}
				}
			}
		}

		MinHeap h(dat);
		clock_t sec = clock();
		// do something
		double pre_dist[dat][3];
		pre_dist[0][0] = dat + 1;
		pre_dist[0][1] = 0;
		pre_dist[0][2] = 0;
		for(int i = 1; i < dat; ++i){
			pre_dist[i][0] = -1;
			pre_dist[i][1] = -1;
			pre_dist[i][2] = -1;
		}

		for(int i = 0; i < edgelim[0]; i++){
			int abc = (int)me_link_SD[0][i][0];
			pre_dist[abc][0] = 0;
			pre_dist[abc][1] = me_link_SD[0][i][1];
			pre_dist[abc][2] = abc;
			h.insertKey(pre_dist[abc][1], pre_dist[abc][2]);
		}

		double termination = 0;
		while(1){
			int minnode = h.extractMin();

			if(minnode == INT_MAX)
				break;
			if(minnode == dat - 1){
				termination = pre_dist[minnode][1];
				// break;
			}
			for (int i = 0; i < edgelim[minnode]; ++i){
				int abc = (int)me_link_SD[minnode][i][0];
				if (pre_dist[abc][1] < 0){
					pre_dist[abc][0] = minnode;
					pre_dist[abc][1] = pre_dist[minnode][1] + me_link_SD[minnode][i][1];
					pre_dist[abc][2] = abc;
					h.insertKey(pre_dist[abc][1], pre_dist[abc][2]);
				}
				else if (pre_dist[abc][1] > pre_dist[minnode][1] + me_link_SD[minnode][i][1]){
					pre_dist[abc][0] = minnode;
					pre_dist[abc][1] = pre_dist[minnode][1] + me_link_SD[minnode][i][1];
					pre_dist[abc][2] = abc;
					h.decreaseKey(pre_dist[abc][2], pre_dist[abc][1]);
				}
			}
			pre_dist[minnode][0] = dat + 1;
			pre_dist[minnode][1] = 0;
			pre_dist[minnode][2] = minnode;
		}
		/*
		   if (pre_dist[dat - 1][1] < 0)
		   cout<<"Invalid graph! There's no way to exceed the termination\n";
		   else
		   cout<<"The shortest path length is "<<termination<<endl;
		   */
		sec = clock() - sec;
		cout<<(double)sec/CLOCKS_PER_SEC<<endl;
	}
	return 0;
}
