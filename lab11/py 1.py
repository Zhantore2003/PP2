SELECT * from person

CREATE OR REPLACE FUNCTION get_records_by_pattern(p_pattern VARCHAR)
RETURNS TABLE(id INT, name VARCHAR, phone INT, gender CHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT person.id, person.name, person.phone, person.gender
    FROM person
    WHERE person.name ILIKE '%' || p_pattern || '%'
    OR person.phone::TEXT ILIKE '%' || p_pattern || '%'
    OR person.id::TEXT ILIKE '%' || p_pattern || '%'
    OR person.gender::TEXT ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


SELECT * FROM get_records_by_pattern('Johsss');