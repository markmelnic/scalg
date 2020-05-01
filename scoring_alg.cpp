
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;


int main()
{
    ifstream in("input.csv");
    vector<vector<double>> fields;
    if (in) {
        string line;
        while (getline(in, line)) {
            stringstream sep(line);
            string field;
            fields.push_back(vector<double>());
            while (getline(sep, field, ',')) {
                fields.back().push_back(stod(field));
            }
        }
    }
    for (auto row : fields) {
        for (auto field : row) {
            cout << field << ' ';
        }
        cout << '\n';
    }
}