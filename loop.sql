DECLARE 
    items_count INT NOT NULL DEFAULT 1; 
BEGIN
    FOR i IN 1..items_count LOOP
        INSERT INTO Chocolate (bar_id, bar_name, company, bean_type, cocoa_perc)
            VALUES ('11', 'Madaga', 'Soma', 'Criollo', '80'); 

        INSERT INTO Chocolate (bar_id, bar_name, company, bean_type, cocoa_perc)
            VALUES ('12', 'Kpim', 'Bonnat', 'Criollo', '45');

        INSERT INTO Chocolate (bar_id, bar_name, company, bean_type, cocoa_perc)
            VALUES ('13', 'Akat', 'Fresco', 'Trinitario', '75'); 
    END LOOP;
END;
