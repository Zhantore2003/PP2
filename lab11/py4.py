SELECT * FROM person


CREATE OR REPLACE FUNCTION get_users_with_pagination(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone INT, gender CHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT person.id, person.name, person.phone, person.gender
    FROM person
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
SELECT * FROM get_users_with_pagination(2, 0);
SELECT * FROM get_users_with_pagination(2, 2);