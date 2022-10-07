options (skip = 1)
load data
infile 'C:\app\test1.csv'
append
into table TEST_TBL
fields terminated by ','
trailing nullcols
(
    col1,
    col2,
    col3,
    col4
)