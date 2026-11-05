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

map<string, vector<int>> find_repeated_patterns(const string& ciphertext)
{
    map<string, vector<int>> patterns;

    for (int length = 3; length <= 5; length++)
    {
        for (int i = 0; i <= (int)ciphertext.length() - length; i++)
        {
            string pattern = ciphertext.substr(i, length);
            patterns[pattern].push_back(i);
        }
    }

    return patterns;
}

map<string, vector<int>> calculate_distances(
    const map<string, vector<int>>& patterns)
{
    map<string, vector<int>> distances;

    for (const auto& entry : patterns)
    {
        const string& pattern = entry.first;
        const vector<int>& positions = entry.second;

        if (positions.size() < 2)
            continue;

        for (size_t i = 1; i < positions.size(); i++)
        {
            int distance = positions[i] - positions[i - 1];
            distances[pattern].push_back(distance);
        }
    }

    return distances;
}

vector<int> find_factors(int number)
{
    vector<int> factors;

    for (int i = 2; i <= number; i++)
    {
        if (number % i == 0)
            factors.push_back(i);
    }

    return factors;
}

int kasiski_analysis(const string& ciphertext)
{
    map<string, vector<int>> patterns =
        find_repeated_patterns(ciphertext);

    map<string, vector<int>> distances =
        calculate_distances(patterns);
    cout << "         REPEATED PATTERNS\n";
    cout << "========================================\n\n";

    for (const auto& entry : patterns)
    {
        if (entry.second.size() >= 2)
        {
            cout << "Pattern: " << entry.first << " | Positions: ";

            for (int position : entry.second)
                cout << position << " ";

            cout << "\n";
        }
    }
    cout << "         KASISKI DISTANCES\n";
    cout << "========================================\n\n";

    for (const auto& entry : distances)
    {
        cout << "Pattern: " << entry.first << " | Distances: ";

        for (int distance : entry.second)
            cout << distance << " ";

        cout << "\n";
    }
    cout << "      FACTORS OF KASISKI DISTANCES\n";
    cout << "========================================\n\n";

    map<int, int> factor_count;

    for (const auto& entry : distances)
    {
        cout << "Pattern: " << entry.first << "\n";

        for (int distance : entry.second)
        {
            vector<int> factors = find_factors(distance);

            cout << "Distance " << distance << ": ";

            for (int factor : factors)
            {
                cout << factor << " ";

                if (factor <= 20)
                    factor_count[factor]++;
            }

            cout << "\n";
        }

        cout << "\n";
    }

    cout << "          KASISKI ANALYSIS\n";
    cout << "========================================\n\n";

    cout << "Candidate Key Lengths:\n\n";

    for (const auto& entry : factor_count)
    {
        cout << "Length " << entry.first
             << " -> " << entry.second
             << " occurrences\n";
    }

    int best_length = 0;
    int best_count = 0;

    for (const auto& entry : factor_count)
    {
        if (entry.second > best_count)
        {
            best_count = entry.second;
            best_length = entry.first;
        }
    }

    cout << "\nEstimated Key Length: "
         << best_length << "\n";

    return best_length;
}

double calculate_ic(const string& text)
{
    if (text.length() < 2)
        return 0.0;

    int frequency[26] = {0};

    for (char ch : text)
        frequency[ch - 'A']++;

    long long numerator = 0;

    for (int i = 0; i < 26; i++)
        numerator += frequency[i] * (frequency[i] - 1);

    int n = text.length();

    return (double)numerator / (n * (n - 1));
}

double calculate_average_ic(
    const string& ciphertext,
    int key_length)
{
    if (key_length <= 0)
        return 0.0;

    vector<string> groups(key_length);

    for (int i = 0; i < (int)ciphertext.length(); i++)
        groups[i % key_length] += ciphertext[i];

    double total = 0.0;

    for (const string& group : groups)
        total += calculate_ic(group);

    return total / key_length;
}

vector<string> split_into_groups(
    const string& ciphertext,
    int key_length)
{
    vector<string> groups(key_length);

    for (int i = 0; i < (int)ciphertext.length(); i++)
        groups[i % key_length] += ciphertext[i];

    return groups;
}

vector<int> frequency_analysis(const string& group)
{
    vector<int> frequency(26, 0);

    for (char ch : group)
        frequency[ch - 'A']++;

    return frequency;
}

int find_shift(const string& group)
{
    double english_frequency[26] =
    {
        0.082, 0.015, 0.028, 0.043, 0.127,
        0.022, 0.020, 0.061, 0.070, 0.0015,
        0.0077, 0.040, 0.024, 0.067, 0.075,
        0.019, 0.00095, 0.060, 0.063, 0.091,
        0.028, 0.0098, 0.024, 0.0015, 0.020,
        0.00074
    };

    vector<int> observed = frequency_analysis(group);

    int n = group.length();

    double best_score = 1e18;
    int best_shift = 0;

    for (int shift = 0; shift < 26; shift++)
    {
        double chi_square = 0.0;

        for (int plain = 0; plain < 26; plain++)
        {
            int cipher =
                (plain + shift) % 26;

            double expected =
                english_frequency[plain] * n;

            if (expected > 0)
            {
                double difference =
                    observed[cipher] - expected;

                chi_square +=
                    (difference * difference) / expected;
            }
        }

        if (chi_square < best_score)
        {
            best_score = chi_square;
            best_shift = shift;
        }
    }

    return best_shift;
}

string find_key(const vector<string>& groups)
{
    string key = "";

    for (const string& group : groups)
    {
        int shift = find_shift(group);
        key += char('A' + shift);
    }

    return key;
}

string vigenere_decrypt(
    const string& ciphertext,
    const string& key)
{
    string plaintext = "";

    for (int i = 0; i < (int)ciphertext.length(); i++)
    {
        int c = ciphertext[i] - 'A';
        int k = key[i % key.length()] - 'A';

        int p = (c - k + 26) % 26;

        plaintext += char('A' + p);
    }

    return plaintext;
}

string vigenere_encrypt(
    const string& plaintext,
    const string& key)
{
    string ciphertext = "";

    for (int i = 0; i < (int)plaintext.length(); i++)
    {
        int p = plaintext[i] - 'A';
        int k = key[i % key.length()] - 'A';

        int c = (p + k) % 26;

        ciphertext += char('A' + c);
    }

    return ciphertext;
}

bool verify(
    const string& original,
    const string& encrypted)
{
    return original == encrypted;
}

void display_frequency_table(
    const vector<string>& groups)
{
    cout << "       FREQUENCY ANALYSIS\n";
    cout << "========================================\n";

    for (int i = 0; i < (int)groups.size(); i++)
    {
        vector<int> frequency =
            frequency_analysis(groups[i]);

        cout << "\nGroup " << i + 1;
        cout << " (Length: " << groups[i].length() << ")\n";

        cout << "----------------------------------------\n";

        for (int j = 0; j < 26; j++)
        {
            cout << char('A' + j)
                 << ": " << frequency[j] << "\t";

            if ((j + 1) % 5 == 0)
                cout << "\n";
        }

        cout << "\n";
    }
}

void display_shift_analysis( const vector<string>& groups){
    cout << "          SHIFT ANALYSIS\n";
    cout << "========================================\n\n";

    for (int i = 0; i < (int)groups.size(); i++)
    {
        int shift = find_shift(groups[i]);

        cout << "Group " << i + 1
             << " -> Shift = " << shift
             << " -> Key Letter = "
             << char('A' + shift) << "\n";
    }
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
        text += line;

    input.close();

    cout << "    VIGENERE CIPHER CRYPTANALYSIS\n";
    cout << "========================================\n\n";

    string ciphertext =
        clean_ciphertext(text);

    cout << "Cleaned ciphertext length: "
         << ciphertext.length() << "\n";

    int key_length =
        kasiski_analysis(ciphertext);

    if (key_length <= 0)
    {
        cout << "\nUnable to estimate key length.\n";
        return 1;
    }

    cout << "       INDEX OF COINCIDENCE\n";
    cout << "========================================\n\n";

    cout << fixed << setprecision(6);

    cout << "Estimated Key Length : "
         << key_length << "\n";

    double average_ic =
        calculate_average_ic(
            ciphertext,
            key_length);

    cout << "Average IC           : "
         << average_ic << "\n";

    cout << "\nIC for Candidate Key Lengths:\n\n";

    for (int length = 2; length <= 12; length++)
    {
        double ic =
            calculate_average_ic(
                ciphertext,
                length);

        cout << "Key Length "
             << setw(2) << length
             << " -> Average IC = "
             << ic << "\n";
    }

    vector<string> groups =
        split_into_groups(
            ciphertext,
            key_length);

    cout << "        CIPHERTEXT GROUPS\n";
    cout << "========================================\n\n";

    for (int i = 0; i < (int)groups.size(); i++)
    {
        cout << "Group " << i + 1 << ": "
             << groups[i] << "\n\n";
    }

    display_frequency_table(groups);

    display_shift_analysis(groups);

    string key =
        find_key(groups);
    cout << "          RECOVERED KEY\n";
    cout << "========================================\n\n";

    cout << "Recovered Key: "
         << key << "\n";

    string plaintext =
        vigenere_decrypt(
            ciphertext,
            key);

    cout << "       RECOVERED PLAINTEXT\n";
    cout << "========================================\n\n";

    cout << plaintext << "\n";

    string reencrypted =
        vigenere_encrypt(
            plaintext,
            key);

    bool result =
        verify(
            ciphertext,
            reencrypted);
    cout << "            VERIFICATION\n";
    cout << "========================================\n\n";

    cout << "Original Ciphertext Length : "
         << ciphertext.length() << "\n";

    cout << "Re-encrypted Length        : "
         << reencrypted.length() << "\n\n";

    if (result)
    {
        cout << "Re-encryption Result : MATCH\n";
        cout << "Verification Successful!\n";
    }
    else
    {
        cout << "Re-encryption Result : NOT MATCH\n";
        cout << "Verification Failed!\n";
    }



    return 0;
}