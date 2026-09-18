#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

void create_key(char key[]) {

    string substitution =
        "QWERTYUIOPASDFGHJKLZXCVBNM";

    for (int i = 0; i < 26; i++) {
        key[i] = substitution[i];
    }
}

string encrypt(string text, char key[]) {

    string result = "";

    for (char ch : text) {

        if (isalpha(static_cast<unsigned char>(ch))) {

            bool upper =
                isupper(static_cast<unsigned char>(ch));

            char upperChar =
                toupper(static_cast<unsigned char>(ch));

            char encrypted =
                key[upperChar - 'A'];

            if (!upper) {
                encrypted =
                    tolower(static_cast<unsigned char>(
                        encrypted));
            }

            result += encrypted;
        }
        else {
            result += ch;
        }
    }

    return result;
}

int main() {

    ifstream input("../testcases/plaintext.txt");
    ofstream output("../testcases/ciphertext.txt");

    if (!input) {

        cout << "Unable to open plaintext.txt\n";
        return 1;
    }

    char key[26];

    create_key(key);

    string text;
    string line;

    while (getline(input, line)) {

        text += line;

        if (!input.eof())
            text += "\n";
    }

    string ciphertext =
        encrypt(text, key);

    output << ciphertext;

    cout << "========================================\n";
    cout << " MONOALPHABETIC SUBSTITUTION CIPHER\n";
    cout << "========================================\n";

    cout << "\nEncryption Key:\n";

    cout << "Plain : ";

    for (char c = 'A'; c <= 'Z'; c++)
        cout << c << " ";

    cout << "\nCipher: ";

    for (int i = 0; i < 26; i++)
        cout << key[i] << " ";

    cout << "\n\nCiphertext generated successfully.\n";

    input.close();
    output.close();

    return 0;
}