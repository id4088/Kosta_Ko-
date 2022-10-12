set closep ,
set feedback off        -- 피드백 문장을 지운다.
set heading off
set newp none           -- 조회 한 데 이 터 를 몇 페이지로
                        -- 나누어 표시 할 지 설정
                        -- 연속 적인 데이터가 필요하면 중간에 
                        -- 빈 줄 이 나타나지 않도록 newp 를 none 으로 설정
set pagesize 0          -- 컬럼 이름을 쓰지 않는다.
set linesize 200        -- 오른쪽 여백을 200자까지만 놔두고 자른다.
set echo off            -- 컬럼이름, sql문장 빼고 데이터만 export받는다.
set tirmout on          -- 스크립트를 다 실행시켜도 화면상에 아무것도 출력하지 않는다.
set termouth off        -- 스크립트 명령 실행결과를 표시
set trimspool on        -- linesize를 했을때 공백을 좀 줄인다.

spool test_csv_01.csv        -- csv 파일을 만든다.

select col1||','||col2||','||col3||','||col4
from TEST_TBL;          -- 이것을 실행시켜서 만든다.

spool off               -- 끝내기