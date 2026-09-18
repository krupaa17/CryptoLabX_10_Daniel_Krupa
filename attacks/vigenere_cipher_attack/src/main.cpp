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

int main()
{
    ifstream input("../testcases/ciphertext.txt");

    if (!input)
    {
        cout << "Unable to open ciphertext.txt\n";
        return 1;
    }

    string text;
    string line;

    while (getline(input, line))
    {
        text += line;
    }

    input.close();

    
    cout << " VIGENERE CIPHER CRYPTANALYSIS\n";
    cout << "========================================\n\n";

    cout << "Original ciphertext length : "
         << text.length() << "\n";

    string ciphertext = clean_ciphertext(text);

    cout << "Cleaned ciphertext length  : "
         << ciphertext.length() << "\n\n";

    cout << "Cleaned Ciphertext:\n";
    cout << ciphertext << "\n";

    return 0;
}
