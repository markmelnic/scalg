
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

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
    int i;
    double maxreg = 0, minreg = 9999999999;
    double maxprice = 0, minprice = 9999999999;
    double maxmil = 0, minmil = 9999999999;
    for (auto row : fields) {
        i = 0;
        for (auto field : row) {
            if (i == 0) { // registration
                if (maxreg < field) {
                    maxreg = field;
                }
                if (minreg > field) {
                    minreg = field;
                }
            }
            if (i == 1) { // price
                if (maxprice < field) {
                    maxprice = field;
                }
                if (minprice > field) {
                    minprice = field;
                }
            }
            if (i == 2) { // mileage
                if (maxmil < field) {
                    maxmil = field;
                }
                if (minmil > field) {
                    minmil = field;
                }
            }
            i++;
        }
    }
    cout << "maxreg == ";
    cout << maxreg;
    cout << "\nminreg == ";
    cout << minreg;

    cout << "\n\nmaxprice == ";
    cout << maxprice;
    cout << "\nmaxprice == ";
    cout << minprice;

    cout << "\n\nmaxmil == ";
    cout << maxmil;
    cout << "\nmaxmil == ";
    cout << minmil;

    double multiplier = 2;
    double score_reg, score_price, score_mil;
    double score;
    for (auto row : fields) {
        i = 0;
        score = 0;
        score_reg = 0;
        score_price = 0;
        score_mil = 0;
        for (auto field : row) {
            if (i == 0) { // registration
                score_reg = (1 - ((field - minreg) / (maxreg - minreg))) * multiplier;
            }
            if (i == 1) { // price
                score_price = (1 - ((field - minprice) / (maxprice - minprice))) * multiplier;
            }
            if (i == 2) { // mileage
                score_mil = (1 - ((field - minmil) / (maxmil - minmil))) * multiplier;
            }
            i++;
        }
        score = score_reg + score_price + score_mil;
        cout << '\n' << score;
    }
}