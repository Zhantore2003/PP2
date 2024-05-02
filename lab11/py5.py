SELECT * from person

CREATE OR REPLACE PROCEDURE delete_user_by_username_or_phone(p_delete_by VARCHAR, p_value VARCHAR)
AS $$
BEGIN
    IF p_delete_by = 'username' THEN
        DELETE FROM person WHERE name = p_value;
    ELSIF p_delete_by = 'phone' THEN
        DELETE FROM person WHERE phone::TEXT = p_value;
    ELSE
        RAISE EXCEPTION 'Invalid delete_by parameter. Use "username" or "phone".';
    END IF;
END;
$$ LANGUAGE plpgsql;

CALL delete_user_by_username_or_phone('phone', '8747179');