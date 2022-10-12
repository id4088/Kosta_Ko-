options (skip = 1)
load data
infile 'C:\app\breast-cancer.csv'
append
into table TEST_TBL
fields terminated by ','
trailing nullcols
(
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10,
	 col11, col12, col13, col14, col15, col16, col17, col18, col19, col20,
	 col21, col22, col23, col24, col25, col26, col27, col28, col29, col30,
	 col31, col32
)