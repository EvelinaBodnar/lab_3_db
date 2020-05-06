CREATE OR REPLACE VIEW Tables AS
    SELECT
        Chocolate.bar_id,
        Chocolate.bar_name,
        Company.company,
        Bean.bean_type,
        Chocolate.cocoa_perc

    FROM
        Chocolate
        JOIN Company ON Chocolate.company = Company.company
        JOIN Bean ON Chocolate.bean_type = Bean.bean_type
