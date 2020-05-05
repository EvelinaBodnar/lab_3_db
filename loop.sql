DECLARE
    TYPE CHARS IS VARRAY(15) OF Chocolate.company%TYPE;
    TYPE CHARS IS VARRAY(15) OF Chocolate.bar_name%TYPE;

BEGIN
    bar_id := NUMBERS(12,16,30,32,40,44,46);
    bar_name := CHARS('Madaga','Kpim','Mad','Quil','Akat','Dominic','Ecuado');
    company := CHARS('Soma','Bonnat','Bonnat','Fresco','Pralus','A.Morin','Fresco');
    bean_type := CHARS('OER','Criollo','Forastero','Criollo','Trinitario','Trinitario','OER');
    cocoa_perc := FLOATS(80,35,56,64,72,30,43);
    rating := FLOATS(1.2,4.5,3.8,2.3,3.2,4.4,5.0);
    
    
    FOR i IN 1 .. bar_id.count LOOP
        INSERT INTO Chocolate (bar_id,bar_name,company,bean_type,cocoa_perc,rating) VALUES (bar_id(i), bar_name(i), company(i), bean_type(i), cocoa_perc(i), rating(i));
        COMMIT;
    END LOOP;
END;
