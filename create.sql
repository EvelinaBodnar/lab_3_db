

CREATE TABLE Company(
    company VARCHAR2(128) NOT NULL);
ALTER TABLE Company
    ADD CONSTRAINT company_pk PRIMARY KEY(company);    
    
CREATE TABLE Bean(
    bean_type VARCHAR2(128) NOT NULL);
ALTER TABLE Bean
    ADD CONSTRAINT bean_type_pk PRIMARY KEY(bean_type); 

CREATE TABLE Chocolate(
    bar_id NUMBER(16) NOT NULL,
    bar_name VARCHAR2(128) NOT NULL,
    company VARCHAR2(128) NOT NULL,
    bean_type VARCHAR2(128) NOT NULL,
    cocoa_perc float NOT NULL);
ALTER TABLE Chocolate
    ADD CONSTRAINT bar_name_pk PRIMARY KEY(bar_name);
    
ALTER TABLE Chocolate
    ADD CONSTRAINT company_fk FOREIGN KEY(company) REFERENCES Company(company);
ALTER TABLE Chocolate
    ADD CONSTRAINT bean_type_fk FOREIGN KEY(bean_type) REFERENCES Bean(bean_type); 
