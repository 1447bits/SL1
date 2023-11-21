
# TITLE :

Cursors: (All types: Implicit, Explicit, Cursor FOR Loop, Parameterized Cursor) Write a PL/SQL block of code using parameterized Cursor that will merge the data available in the newly created table N_Roll_Call with the data available in the table O_Roll_Call. If the data in the first table already exists in the second table then that data should be skipped.
	

### HOW TO RUN ?

1. Create a .sql file 

2. to run mysql -u your_username -p your_database < merge_data.sql


<hr/>


Replace your_username, your_database, and merge_data.sql with your MySQL username, the name of your database, and the actual file name, respectively.


CODE:

DELIMITER //

CREATE PROCEDURE MergeRollCallData()
BEGIN
  DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE v_roll_no INT;
  DECLARE v_name VARCHAR(50);
  
  -- Declare cursor for N_Roll_Call table
  DECLARE cur_n_roll_call CURSOR FOR
    SELECT Roll_no, Name FROM N_Roll_Call;
  
  -- Declare continue handler for the cursor
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  
  -- Open the cursor
  OPEN cur_n_roll_call;
  
  -- Start fetching data from N_Roll_Call
  read_loop: LOOP
    FETCH cur_n_roll_call INTO v_roll_no, v_name;
    IF done THEN
      LEAVE read_loop;
    END IF;
    
    -- Check if data already exists in O_Roll_Call
    IF NOT EXISTS (SELECT 1 FROM O_Roll_Call WHERE Roll_no = v_roll_no AND Name = v_name) THEN
      -- Data doesn't exist, so insert into O_Roll_Call
      INSERT INTO O_Roll_Call (Roll_no, Name) VALUES (v_roll_no, v_name);
    END IF;
  END LOOP;
  
  -- Close the cursor
  CLOSE cur_n_roll_call;
  
END //

DELIMITER ;


