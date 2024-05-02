 CREATE OR REPLACE FUNCTION insert_users(p_names VARCHAR[], p_phones VARCHAR[])
RETURNS TABLE (name VARCHAR, phone VARCHAR, error_message VARCHAR) AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        -- Check if phone is numeric and has correct length
        IF length(p_phones[i]) <> 9 OR NOT (p_phones[i] ~ '^[0-9]+$') THEN
            -- Return incorrect phone number
            RETURN QUERY SELECT p_names[i], p_phones[i], 'Incorrect phone number'::VARCHAR;
        ELSE
            -- Insert the user
            BEGIN
                INSERT INTO person (id, name, phone, gender) VALUES (DEFAULT, p_names[i], p_phones[i], 'm');
            EXCEPTION WHEN OTHERS THEN
                -- Return error if insertion fails
                RETURN QUERY SELECT p_names[i], p_phones[i], 'No error'::VARCHAR;
            END;
        END IF;
    END LOOP;

    RETURN;
END;
$$ LANGUAGE plpgsql;

-- Example usage
SELECT * FROM insert_users(ARRAY['Dik', 'Bob', 'John Dok'], ARRAY['8747179', 'abc123456', '987654321']);