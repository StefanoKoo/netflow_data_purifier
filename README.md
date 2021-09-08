netflow_data_purifier
======================

과제에서 사용하기 위한 Netflow Data 정제기

config/config_date.json 에서 시작 날짜와 끝나는 날짜를 정하면
data/flows_{num}.csv 파일에서 해당 시간만큼의 Netflow data만 data.csv 로 추출
추후 webserver 형태로 로컬에서 진행 예정(Django)
