#include <bits/stdc++.h>
using namespace std;

void frequency_analysis(string text) {
    int frequency[26] = {0};
    int total = 0;

    for (char ch : text) {

        ch = toupper(static_cast<unsigned char>(ch));

        if (ch >= 'A' && ch <= 'Z') {
            frequency[ch - 'A']++;
            total++;
        }
    }
    vector<pair<char, int>> frequencies;

    for (int i = 0; i < 26; i++) {
        frequencies.push_back(
            {char('A' + i), frequency[i]}
        );
    }

    sort(frequencies.begin(),
         frequencies.end(),
         [](const pair<char, int>& a,
            const pair<char, int>& b) {

             return a.second > b.second;
         });

    cout << "\n========== LETTER FREQUENCY ==========\n";

    cout << "Letter   Frequency   Percentage\n";

    for (auto item : frequencies) {

        double percentage = 0;

        if (total > 0)
            percentage =
                item.second * 100.0 / total;

        cout << item.first << "        "
             << item.second << "          "
             << percentage << "%\n";
    }

    cout << "\nMost frequent letters:\n";

    for (int i = 0;
         i < 5 && i < (int)frequencies.size();
         i++) {

        cout << frequencies[i].first
             << " (" << frequencies[i].second
             << " occurrences)\n";
    }
}


void word_frequency_analysis(string text) {

    map<string, int> wordFrequency;

    string word = "";

    for (int i = 0; i <= (int)text.length(); i++) {

        if (i < (int)text.length() &&
            isalpha(static_cast<unsigned char>(text[i]))) {

            word +=
                toupper(static_cast<unsigned char>(text[i]));
        }
        else {

            if (!word.empty()) {

                wordFrequency[word]++;
                word = "";
            }
        }
    }

    cout << "\n========== WORD FREQUENCY ==========\n";

    vector<pair<string, int>> words(
        wordFrequency.begin(),
        wordFrequency.end()
    );

    sort(words.begin(),
         words.end(),
         [](const pair<string, int>& a,
            const pair<string, int>& b) {

             return a.second > b.second;
         });

    cout << "Repeated words:\n";

    for (auto item : words) {

        if (item.second > 1) {

            cout << item.first
                 << " -> "
                 << item.second
                 << " times\n";
        }
    }

    cout << "\nOne-letter words:\n";

    for (auto item : words) {

        if (item.first.length() == 1)
            cout << item.first
                 << " -> "
                 << item.second
                 << "\n";
    }

    cout << "\nTwo-letter words:\n";

    for (auto item : words) {

        if (item.first.length() == 2)
            cout << item.first
                 << " -> "
                 << item.second
                 << "\n";
    }

    cout << "\nThree-letter words:\n";

    for (auto item : words) {

        if (item.first.length() == 3)
            cout << item.first
                 << " -> "
                 << item.second
                 << "\n";
    }
}


string get_pattern(string word) {

    int mapping[26];

    for (int i = 0; i < 26; i++)
        mapping[i] = -1;

    int next = 0;

    string result = "";

    for (char ch : word) {

        int index = ch - 'A';

        if (mapping[index] == -1) {
            mapping[index] = next++;
        }

        result +=
            char('0' + mapping[index]);
    }

    return result;
}


void pattern_analysis(string text) {

    cout << "\n========== PATTERN ANALYSIS ==========\n";

    string word = "";

    map<string, vector<string>> patternWords;

    for (int i = 0; i <= (int)text.length(); i++) {

        if (i < (int)text.length() &&
            isalpha(static_cast<unsigned char>(text[i]))) {

            word +=
                toupper(static_cast<unsigned char>(text[i]));
        }
        else {

            if (!word.empty()) {

                string pattern =
                    get_pattern(word);

                patternWords[pattern].push_back(word);

                word = "";
            }
        }
    }

    for (auto item : patternWords) {

        if (item.second.size() > 1) {

            cout << "Pattern "
                 << item.first
                 << " : ";

            for (string word : item.second)
                cout << word << " ";

            cout << "\n";
        }
    }
}


string apply_substitution(string text,
                          char substitution[]) {

    string result = "";

    for (char ch : text) {

        if (isalpha(static_cast<unsigned char>(ch))) {

            bool upper =
                isupper(static_cast<unsigned char>(ch));

            int index =
                toupper(static_cast<unsigned char>(ch))
                - 'A';

            if (substitution[index] == '?') {

                result += '_';
            }
            else {

                char replacement =
                    substitution[index];

                if (!upper)
                    replacement =
                        tolower(static_cast<unsigned char>(
                            replacement));

                result += replacement;
            }
        }
        else {

            result += ch;
        }
    }

    return result;
}


void display_partial_plaintext(string ciphertext,
                               char substitution[]) {

    cout << "\n========== PARTIAL PLAINTEXT ==========\n";

    string partial =
        apply_substitution(
            ciphertext,
            substitution
        );

    cout << partial << "\n";
}


bool verify_solution(string plaintext,
                     string ciphertext,
                     char key[]) {

    string generated = "";

    for (char ch : plaintext) {

        if (isalpha(static_cast<unsigned char>(ch))) {

            bool upper =
                isupper(static_cast<unsigned char>(ch));

            int index =
                toupper(static_cast<unsigned char>(ch))
                - 'A';

            char encrypted = key[index];

            if (!upper)
                encrypted =
                    tolower(static_cast<unsigned char>(
                        encrypted));

            generated += encrypted;
        }
        else {

            generated += ch;
        }
    }

    return generated == ciphertext;
}

void display_key(char substitution[]) {

    cout << "\n========== RECOVERED KEY ==========\n";

    cout << "Cipher : ";

    for (char c = 'A'; c <= 'Z'; c++)
        cout << c << " ";

    cout << "\nPlain  : ";

    for (int i = 0; i < 26; i++) {

        if (substitution[i] == '?')
            cout << "? ";
        else
            cout << substitution[i] << " ";
    }

    cout << "\n";
}


void interactive_attack(string ciphertext) {

    char substitution[26];

    for (int i = 0; i < 26; i++)
        substitution[i] = '?';

    while (true) {

        display_partial_plaintext(
            ciphertext,
            substitution
        );

        display_key(substitution);

        cout << "\n1. Add substitution\n";
        cout << "2. Remove substitution\n";
        cout << "3. Finish attack\n";
        cout << "4. Exit\n";

        cout << "Enter choice: ";

        int choice;
        cin >> choice;

        if (choice == 1) {

            char cipherLetter;
            char plainLetter;

            cout << "Enter ciphertext letter: ";
            cin >> cipherLetter;

            cout << "Enter guessed plaintext letter: ";
            cin >> plainLetter;

            cipherLetter =
                toupper(static_cast<unsigned char>(
                    cipherLetter));

            plainLetter =
                toupper(static_cast<unsigned char>(
                    plainLetter));

            if (cipherLetter < 'A' ||
                cipherLetter > 'Z' ||
                plainLetter < 'A' ||
                plainLetter > 'Z') {

                cout << "Invalid letters.\n";
                continue;
            }

            bool conflict = false;

            for (int i = 0; i < 26; i++) {

                if (i != cipherLetter - 'A' &&
                    substitution[i] == plainLetter) {

                    conflict = true;
                    break;
                }
            }

            if (conflict) {

                cout << "Conflict: plaintext letter "
                     << plainLetter
                     << " is already assigned.\n";

                continue;
            }

            substitution[cipherLetter - 'A'] =
                plainLetter;

            cout << "Substitution added.\n";
        }

        else if (choice == 2) {

            char cipherLetter;

            cout << "Enter ciphertext letter to remove: ";
            cin >> cipherLetter;

            cipherLetter =
                toupper(static_cast<unsigned char>(
                    cipherLetter));

            if (cipherLetter >= 'A' &&
                cipherLetter <= 'Z') {

                substitution[cipherLetter - 'A'] =
                    '?';

                cout << "Substitution removed.\n";
            }
        }

        else if (choice == 3) {

            cout << "\nAttack finished.\n";
            display_partial_plaintext(
                ciphertext,
                substitution
            );

            display_key(substitution);

            break;
        }

        else if (choice == 4) {

            return;
        }

        else {

            cout << "Invalid choice.\n";
        }
    }
}


int main() {

    ifstream input(
        "../testcases/ciphertext.txt"
    );

    if (!input) {

        cout << "Unable to open ciphertext.txt\n";
        return 1;
    }

    string ciphertext;
    string line;

    while (getline(input, line)) {

        ciphertext += line;

        if (!input.eof())
            ciphertext += "\n";
    }

    input.close();

    cout << " MONOALPHABETIC SUBSTITUTION CRYPTANALYSIS\n";
    cout << "========================================\n";

    frequency_analysis(ciphertext);

    word_frequency_analysis(ciphertext);

    pattern_analysis(ciphertext);

    interactive_attack(ciphertext);

    return 0;
}