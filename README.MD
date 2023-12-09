## 기업 모둠 학습
# ☘ 생태 유해성 평가 페이지

# **1. 개요**

**생태 유해성을 평가하기 위해 사용자로부터 데이터를 받아 지도에 시각화하는 기능을 제공**

**사용자는 JSON 형식의 데이터를 POST 요청을 통해 전송하고, 서버는 이 데이터를 바탕으로 마커와 방사형 차트가 있는 지도를 HTML 파일로 생성하여 반환**

# **2. 기능목록**

### ****2.1 Postman****

https://www.postman.com/

➡ **요청 예시**

```python
URL: http://0.0.0.0:8200/mapIntegratedOutcomeReport
Method: POST
Body:
[
    {
        "Name": "대조구역",
        "경도": 126.736021,
        "위도":  35.964362,
        "화학 위해도": 0.9,
        "생태독성 위해도": 0.8,
        "생태 위해도": 0.75,
        "통합위해도": 0.000,
        "표준편차": 0.000
    },
    {
        "Name": "Site 1",
        "경도": 126.735,
        "위도": 35.964,
        "화학 위해도": 0.75,
        "생태독성 위해도": 0.82,
        "생태 위해도": 0.68,
        "통합위해도": 0.932,
        "표준편차": 0.166
    },
    ...
]
```

### **2.2 Flask 애플리케이션 생성**

**Flask 애플리케이션 객체를 생성**

➡ **요청 예시**

```python
from flask import Flask
app = Flask(__name__)
```

### **2.3 데이터 받기**

**사용자로부터 POST 요청을 통해 데이터를 받음** 

**데이터는 JSON 형식이며, 각각의 객체는 하나의 마커에 해당**

**➡ 요청 예시**

```python
 @app.route('/mapIntegratedOutcomeReport', methods=['POST'])
def map_report():
    marker_data = request.get_json()
```

### ****2.4 지도 생성****

**받은 데이터를 바탕으로 Folium을 사용해 지도를 생성**

**각 마커는 방사형 차트를 포함한 팝업을 가지며, 팝업은 해당 지점의 화학 위해도, 생태독성 위해도, 생태 위해도를 시각화함** 

**➡ 요청 예시**

```python
 m = folium.Map(location=[marker_data[0]["위도"], marker_data[0]["경도"]], zoom_start=21)
    for data in marker_data:
        create_marker(data)
```

### **2.5 HTML 파일 반환**

**생성된 지도를 HTML 파일로 저장하고, 반환** 

**➡ 요청 예시** 

```python
 filename = 'map_with_persistent_popup_' + str(uuid.uuid4()) + '.html'
    m.save(filename)
    return send_file(filename, mimetype='text/html')
```

# 3**. Postman**



# 4**. Map**