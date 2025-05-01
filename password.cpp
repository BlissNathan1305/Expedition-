#include <iostream>
#include <cstdlib>
#include <ctime>

const std::string CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+";

std::string generatePassword(int length) {
    std::string password;
    for (int i = 0; i < length; ++i) {
        password += CHARACTERS[rand() % CHARACTERS.length()];
    }
    return password;
}

int main() {
    srand(time(0)); // Seed the random number generator

    int length;
    std::cout << "Enter password length: ";
    std::cin >> length;

    std::string password = generatePassword(length);
    std::cout << "Generated password: " << password << std::endl;

    return 0;
}
