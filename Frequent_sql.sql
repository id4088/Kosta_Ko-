CREATE TABLE CANCER_FACTOR_TBL
(   
    col1   BINARY_DOUBLE NOT NULL,
    col2   CHAR(5) NOT NULL,
    col3   BINARY_DOUBLE NOT NULL,
    col4   BINARY_DOUBLE NOT NULL,
    col5   BINARY_DOUBLE NOT NULL,
    col6   BINARY_DOUBLE NOT NULL,
    col7   BINARY_DOUBLE NOT NULL,
    col8   BINARY_DOUBLE NOT NULL,
    col9   BINARY_DOUBLE NOT NULL,
    col10  BINARY_DOUBLE NOT NULL,
    col11  BINARY_DOUBLE NOT NULL,
    col12  BINARY_DOUBLE NOT NULL,
    col13  BINARY_DOUBLE NOT NULL,
    col14  BINARY_DOUBLE NOT NULL,
    col15  BINARY_DOUBLE NOT NULL,
    col16  BINARY_DOUBLE NOT NULL,
    col17  BINARY_DOUBLE NOT NULL,
    col18  BINARY_DOUBLE NOT NULL,
    col19  BINARY_DOUBLE NOT NULL,
    col20  BINARY_DOUBLE NOT NULL,
    col21  BINARY_DOUBLE NOT NULL,
    col22  BINARY_DOUBLE NOT NULL,
    col23  BINARY_DOUBLE NOT NULL,
    col24  BINARY_DOUBLE NOT NULL,
    col25  BINARY_DOUBLE NOT NULL,
    col26  BINARY_DOUBLE NOT NULL,
    col27  BINARY_DOUBLE NOT NULL,
    col28  BINARY_DOUBLE NOT NULL,
    col29  BINARY_DOUBLE NOT NULL,
    col30  BINARY_DOUBLE NOT NULL,
    col31  BINARY_DOUBLE NOT NULL,
    col32  BINARY_DOUBLE NOT NULL
);



$sqlldr userid=c##sqldb/1234 control='C:\app\ML_load_csv.ctl'

ALTER TABLE sample_product DROP COLUMN factory_name;

create user [id] identified by [pw];
grant connect, resource, dba to [id];
commit;
select * from all_users;
