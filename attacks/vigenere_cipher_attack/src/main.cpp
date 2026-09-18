#include <bits/stdc++.h>

using namespace std;


string clean_ciphertext(string text)
{
    string cleaned = "";

    for (char ch : text)
    {
        if (isalpha(static_cast<unsigned char>(ch)))
        {
            cleaned += toupper(static_cast<unsigned char>(ch));
        }
    }

    return cleaned;
}

map<string, vector<int>> find_repeated_patterns(const string& ciphertext){
    map<string, vector<int>> patterns;

    int sequence_length = 3;

    for (int i = 0; i <= (int)ciphertext.length() - sequence_length; i++){
        string pattern = ciphertext.substr(i, sequence_length);
        patterns[pattern].push_back(i);
    }

    return patterns;
}
map<string, vector<int>> calculate_distances(const map<string, vector<int>>& patterns){
    map<string, vector<int>> distances;

    for (const auto& entry : patterns){
        const string& pattern = entry.first;
        const vector<int>& positions = entry.second;

        if (positions.size() < 2)
            continue;

        for (size_t i = 1; i < positions.size(); i++) {
            int distance = positions[i] - positions[i - 1];

            distances[pattern].push_back(distance);
        }
    }

    return distances;
}
int main(){
    ifstream input("../testcases/ciphertext.txt");

    if (!input){
        cout << "Unable to open ciphertext.txt\n";
        return 1;
    }

    string text;
    string line;

    while (getline(input, line)) text += line;

    input.close();
    cout << " VIGENERE CIPHER CRYPTANALYSIS\n";

    string ciphertext = clean_ciphertext(text);
    cout << "Cleaned ciphertext length: "<< ciphertext.length() << "\n\n";

    map<string, vector<int>> patterns =find_repeated_patterns(ciphertext);

    cout << " REPEATED PATTERNS\n";

    for (auto& entry : patterns){
        if (entry.second.size() >= 2){
            cout << "Pattern: " << entry.first << " | Positions: ";

            for (int position : entry.second){
                cout << position << " ";
            }

            cout << "\n";
        }
    }

    map<string, vector<int>> distances =
    calculate_distances(patterns);

cout << " KASISKI DISTANCES\n";

for (auto& entry : distances){
    cout << "Pattern: " << entry.first << " | Distances: ";

    for (int d : entry.second){
        cout << d << " ";
    }

    cout << "\n";
}

    return 0;
}