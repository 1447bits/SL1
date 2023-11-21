
# TITLE :

Unnamed PL/SQLcode block: Use of Control structure and Exception handling is mandatory.
Suggested Problem statement:

Consider Tables:
1. Borrower (Roll_no, Name, Date_of_Issue, Name_of_Book, Status)
2. Fine (Roll_no, Date, Amt)
* Accept Roll_no and Name_of_Book from user.
* Check the number of days (from Date_of_Issue).
* If days are between 15 to 30 then fine amount will be Rs 5per day.
* If no. of days>30, per day fine will be Rs 50 per day and for days less than 30, Rs. 5 per day.
* After submitting the book, status will change from I to R.
* If condition of fine is true, then details will be stored into fine table.
* Also handles the exception by named exception handler or user define exception handler.



HOW TO RUN : 


> mysql -u your_username -p your_database < calculate_fine.sql

Replace your_username, your_database, and calculate_fine.sql with your MySQL username, the name of your database, and the actual file name, respectively.

CODE:



DELIMITER //

CREATE PROCEDURE CalculateFine(IN p_roll_no INT, IN p_name_of_book VARCHAR(50))
BEGIN
  DECLARE v_date_of_issue DATE;
  DECLARE v_days_due INT;
  DECLARE v_fine_amt INT;
  DECLARE v_status CHAR(1);
  
  -- Fetch details from Borrower table
  SELECT Date_of_Issue, Status
  INTO v_date_of_issue, v_status
  FROM Borrower
  WHERE Roll_no = p_roll_no AND Name_of_Book = p_name_of_book;
  
  -- Calculate days due
  SET v_days_due = DATEDIFF(NOW(), v_date_of_issue);
  
  -- Check conditions for fine
  IF v_days_due > 30 THEN
    SET v_fine_amt = 50 * v_days_due;
  ELSEIF v_days_due >= 15 AND v_days_due <= 30 THEN
    SET v_fine_amt = 5 * v_days_due;
  ELSE
    SET v_fine_amt = 0;
  END IF;
  
  -- Update status in Borrower table
  UPDATE Borrower
  SET Status = 'R'
  WHERE Roll_no = p_roll_no AND Name_of_Book = p_name_of_book;
  
  -- Insert fine details into Fine table if fine is applicable
  IF v_fine_amt > 0 THEN
    INSERT INTO Fine (Roll_no, Date, Amt)
    VALUES (p_roll_no, NOW(), v_fine_amt);
  END IF;
  
  SELECT 'Fine Calculation Successful!' AS Result;
  
END //

DELIMITER ;
