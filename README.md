# GoVegan
비건에 대한 정보제공 및 비건상품 추천 웹서비스 구축 프로젝트 
- 제작기간: 21.12.10 - 21.12.22

### 프로젝트 배경

--- 

<img width="994" alt="스크린샷 2022-07-05 오후 1 13 35" src="https://user-images.githubusercontent.com/86764734/177248499-9be132e7-ccb5-4508-97c2-d56a98210d84.png">
이전부터 환경, 비건에 관심이 많아 비건 상품들에 관심이 많았고 자연스레 같은 물건을 구매한다면 비건상품을 조금 더 선호해 구매하게 되었다. 요즘 비건이 하나의 트랜드로 자리 잡으면서 사회적으로 비건에 대한 관심이 높아지고 있으며 비건을 키워드로 하여 런칭하는 브랜드들도 최근들어 많아지고 있다. 소비재 상품 판매 기업에서 어떤 카테고리에서 비건 제품 관심도가 높은지 궁금해졌고 이 부분을 파악할 수 있다면 비지니스 전략 수립에 유용하지 않을까 생각이 들었다.

### 프로젝트 목표

---

- 사용자로부터 상품검색어를 입력받아 비건제품을 추천해주는 데이터 파이프라인을 웹 서비스로 배포

### 사용 프로그램

---

- HTML5 : 홈페이지 프레임 제작 (검색 페이지)
- CSS3 : 구성요소 디자인, 미디어 쿼리를 통한 반응형 페이지 제작
- Python (Flask) : 서버 연결 (Django보다 좀 더 가벼운 Flask 사용)
- MySQL : Flask-MySQL라이브러리를 사용하여 웹과 DB를 연동
    - 데이터 수집을 위한 DB구성 (검색어, 검색시간)
- Javascript : 버튼 클릭 등 동적인 기능 구성
- 최종 배포는 heroku를 사용

### 서비스 구성 및 제작 과정

---

**데이터파이프라인**

<img width="1037" alt="스크린샷 2022-07-04 오전 9 02 29" src="https://user-images.githubusercontent.com/86764734/177061891-8cda9ca8-2460-4f8f-b2c9-97d418394eeb.png">

**크롤링 코드 작성** : 쿠팡 검색 결과를 크롤링 할 수 있는 코드 작성

- Requests , BeautifulSoup을 통한 html 파싱
- urlencode 를 통해 검색 결과 url 자동 접속
- 검색어(비건) 페이지 검색 결과(제품명, 가격, 이미지URL, 제품페이지URL) 크롤링
- 
**추천 시스템구축 : 키워드기반 추천시스템**

- 크롤링 데이터 전처리 진행
    - 상품 무게, 개수등 불용어 처리를 진행하였으며, 한글이 아닌 특수문자,  숫자, 영어들은 정규식을 통해 제거
    - KoNlpy를 통해 형태소분석 진행한 뒤 토큰화(tokens)
    - tokens에 대해서 TF-IDF 키워드 추출을 진행하고 코사인 유사도를 구해 가장 유사한 상품 3가지를 반환해주는 함수 구현

**검색 페이지** : 고객이 실제로 검색 결과를 볼 수 있는 페이지

- 고객이 입력한 키워드가 포함된 상품을 뽑아서 화면에 버튼으로 표시
- 버튼을 누르면 키워드에 맞춰 크롤링한 결과 추출
- 사용자가 입력한 검색어 기준으로 결과를 추출하며 일치하는 결과가 없는 경우 "아직 비건제품이 제공되지 않네요:-("라는 메시지 출력

**웹과 DB 연동하기**

- DBeaver에 있는 MySQL을 DB로 사용
- Flask-MySQl 라이브러리를 사용하여 웹가 DB 연동

**서버를 통해 배포**

- heroku를 통해 배포


### 결과

---

- 추천시스템

![Untitled (12)](https://user-images.githubusercontent.com/86764734/175309544-bbe5c6b9-ed74-425f-8452-9d5bbf5f3e71.png)

- 웹
![Untitled (13)](https://user-images.githubusercontent.com/86764734/175309973-d8c4cd5e-b6a8-4a4d-8975-f6da0d1cd93d.png)


### 추후 발전 과제

- 추천시스템 서비스

    - 추천시스템을 구현했지만 입력데이터가 상품이름과 완전 일치해야만 상품이름을 기준으로 추천값을 반환해주어서 추천시스템을 웹서비스로 제공하지 못하고 쿼리문을 통해 검색어를 입력받아 결과값을 반환해주는 서비스가 되었음
    
    - 현재 웹에서 사용자가 입력하면 반환되는 상품들을 가지고 추천하는 단계로 진행한다면 구현한 추천시스템을 적용할 수 있을 것으로 생각
    
- 데이터

    - 비건 상품들은 새롭게 업데이트 되기 때문에 매일 크롤링작업을 통해 새로운 데이터들이 자동적으로 업데이트 될 수 있도록 크롤링 자동화
    
        - 쿠팡뿐만 아니라 다양한 카테고리의 상품을 판매하고 있는 사이트들을 종합적으로 크롤링해 데이터 수집
        
    - 크롤링 진행시 이미지 확인되지 않는 데이터들의 원인 파악
    
    - 수집된 데이터를 통해 인사이트를 도출할 수 있는 대시보드 개발


