COLUMN first_name heading "NAME" format A15
COLUMN last_name heading "Last" format A20
COLUMN email heading "E-mail" format A20
COLUMN phone_number heading "Mobile" format A20

CREATE TABLE userTBL
(   user_ID    CHAR(10) NOT NULL PRIMARY KEY,
    user_Name   NVARCHAR2(5) NOT NULL,
    BirthYear   NUMBER(10) NOT NULL,
    Address     NCHAR(10) NOT NULL,
    Mobile1     CHAR(3),
    Mobile2     CHAR(8),
    Height      NUMBER(3),
    mDate       DATE
);

CREATE TABLE buyTBL
(   idNum       NUMBER(8) NOT NULL PRIMARY KEY,
    user_ID     CHAR(10) NOT NULL,
    Prod_Name   NCHAR(5) NOT NULL,
    Group_Name  NCHAR(5),
    Price       NUMBER(8) NOT NULL,
    Amount      NUMBER(3) NOT NULL,
    FOREIGN KEY (user_ID) REFERENCES userTBL(user_ID)
);


CREATE TABLE TEST_TBL
(   
    ability_s   CHAR(10) NOT NULL,
    current_n   CHAR(10) NOT NULL,
    predict_n   CHAR(10) NOT NULL,
    residu_su   CHAR(10) NOT NULL,
    ratio_resi  CHAR(10) NOT NULL,
    residu_op   CHAR(10) NOT NULL,
    ratio_op    CHAR(10) NOT NULL,
    Warning     CHAR(10) NOT NULL
);

CREATE TABLE TEST_TBL
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