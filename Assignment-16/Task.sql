CREATE TABLE Members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    join_date DATE
);

CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    available BOOLEAN
);

CREATE TABLE Loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    book_id INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
INSERT INTO Members (name, email, join_date)
VALUES
('Amit Sharma', 'amit@gmail.com', '2024-11-01'),
('Priya Verma', 'priya@gmail.com', '2024-12-05'),
('Rahul Singh', 'rahul@gmail.com', '2025-01-10');
INSERT INTO Books (title, author, available)
VALUES
('The Alchemist', 'Paulo Coelho', TRUE),
('Wings of Fire', 'Dr. APJ Abdul Kalam', TRUE),
('Rich Dad Poor Dad', 'Robert Kiyosaki', TRUE);
SELECT Members.name AS Member_Name, Books.title AS Book_Title, Loans.loan_date, Loans.return_date
FROM Loans
JOIN Members ON Loans.member_id = Members.member_id
JOIN Books ON Loans.book_id = Books.book_id
WHERE Members.member_id = 1;
UPDATE Books
SET available = FALSE
WHERE book_id IN (
    SELECT book_id FROM Loans WHERE return_date IS NULL
);
DELETE FROM Loans
WHERE member_id = 3;
