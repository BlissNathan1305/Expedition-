
function calculateAge(birthDate) {
    const today = new Date();
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}

// Usage (Year, Month-1, Day)
const myBirthDate = new Date(1990, 7, 15); // August 15, 1990
console.log(`You are ${calculateAge(myBirthDate)} years old.`);

