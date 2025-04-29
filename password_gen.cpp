#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

string generatePassword(int length) {
    string lowercase = "abcdefghijklmnopqrstuvwxyz";
    string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string digits = "0123456789";
    string symbols = "!@#$%^&*()-_=+<>?";
    
    string allChars = lowercase + uppercase + digits + symbols;
    string password = "";

    srand(time(0)); // Seed random number generator

    for (int i = 0; i < length; ++i) {
        int index = rand() % allChars.size();
        password += allChars[index];
    }

    return password;
}

int main() {
    int length;
    cout << "Enter desired password length: ";
    cin >> length;

    if (length <= 0) {
        cout << "Length must be greater than 0." << endl;
        return 1;
    }

    string password = generatePassword(length);
    cout << "Generated password: " << password << endl;

    return 0;
}
