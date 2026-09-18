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

    return 0;
}