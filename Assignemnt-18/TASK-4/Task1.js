/**
 * Prints each student name from an array
 * @param {string[]} students - Array of student names
 */
function printStudents(students) {
    console.log("Student List:");
    students.forEach((name) => {
        console.log(name);
    });
}

// Test with sample data
const studentNames = ["Alice", "Bob", "Charlie"];
printStudents(studentNames);