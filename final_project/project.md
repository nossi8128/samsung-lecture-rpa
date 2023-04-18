1. 3개의 엑셀파일(data1.xlsx, data2.xlsx, data3.xlsx)을 각각 읽어들인다.
2. 읽어들인 데이터를 병합하여 하나의 데이터 프레임을 생성한다.
3. 데이터프레임에서 성별이 '여성'이고 '27세 이상'인 데이터만 추출한다.
4. '점수' 열을 기준으로 내림차순 정렬한다.
5. 이 중에서 '점수' 상위 5명의 나이 합계를 구한다.
6. 엑셀파일을 생성해서 나이 합계를 any 셀에 적는다.
7. 'result.xlsx' 이름으로 저장


./project
[data1.xlsx, data2.xlsx, data3.xlsx, project.py, results.xlsx]