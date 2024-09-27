-- Set the valid_email field to 0 if the email field is updated
DROP TRIGGER IF EXISTS reset_valid_email;
DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END//
DELIMITER ;