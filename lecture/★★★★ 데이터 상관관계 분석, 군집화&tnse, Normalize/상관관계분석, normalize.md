

```python
import pandas as pd
import numpy as np
```


```python
df= pd.read_csv("./data/economy_features_delete_74.csv", encoding="CP949")
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>1인가구비율 (%)</th>
      <th>1인당 자동차 등록대수 (대)</th>
      <th>EQ-5D지표</th>
      <th>가구수 (가구)</th>
      <th>건강보험 적용인구 현황</th>
      <th>고령인구비율 (%)</th>
      <th>교원1인당 학생수 (명)</th>
      <th>남녀성비 (%)</th>
      <th>노인 천명당 노인여가복지시설수 (개)</th>
      <th>...</th>
      <th>단순직비율</th>
      <th>전문직비율</th>
      <th>서비스.사무직</th>
      <th>1차산업비율</th>
      <th>2차산업비율</th>
      <th>3차산업비율</th>
      <th>체육시설</th>
      <th>강력범죄발생건수</th>
      <th>유치원 교원비율</th>
      <th>초등학교 교원비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>29.3</td>
      <td>0.42</td>
      <td>0.953</td>
      <td>214911</td>
      <td>583900</td>
      <td>10.44</td>
      <td>14.96</td>
      <td>92.12</td>
      <td>2.18</td>
      <td>...</td>
      <td>11.905564</td>
      <td>43.888428</td>
      <td>44.206009</td>
      <td>0.010871</td>
      <td>5.527925</td>
      <td>94.461204</td>
      <td>278</td>
      <td>8,617</td>
      <td>8.141467</td>
      <td>6.481443</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>24.3</td>
      <td>0.30</td>
      <td>0.946</td>
      <td>167009</td>
      <td>449179</td>
      <td>11.30</td>
      <td>14.37</td>
      <td>99.46</td>
      <td>1.73</td>
      <td>...</td>
      <td>26.258041</td>
      <td>28.425884</td>
      <td>45.316075</td>
      <td>0.013298</td>
      <td>8.976362</td>
      <td>91.010339</td>
      <td>59</td>
      <td>5,244</td>
      <td>6.449553</td>
      <td>6.586494</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>28.5</td>
      <td>0.23</td>
      <td>0.938</td>
      <td>127462</td>
      <td>314857</td>
      <td>15.87</td>
      <td>14.76</td>
      <td>97.06</td>
      <td>1.50</td>
      <td>...</td>
      <td>33.520775</td>
      <td>20.564836</td>
      <td>45.914389</td>
      <td>0.000000</td>
      <td>10.973518</td>
      <td>89.026482</td>
      <td>67</td>
      <td>4,257</td>
      <td>7.370423</td>
      <td>6.692483</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>26.2</td>
      <td>0.32</td>
      <td>0.956</td>
      <td>220598</td>
      <td>570722</td>
      <td>11.51</td>
      <td>14.64</td>
      <td>95.62</td>
      <td>2.25</td>
      <td>...</td>
      <td>24.523081</td>
      <td>28.244766</td>
      <td>47.232153</td>
      <td>0.003005</td>
      <td>6.870435</td>
      <td>93.126559</td>
      <td>160</td>
      <td>5,585</td>
      <td>8.098529</td>
      <td>6.359084</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>43.9</td>
      <td>0.24</td>
      <td>0.951</td>
      <td>238744</td>
      <td>501170</td>
      <td>12.69</td>
      <td>12.81</td>
      <td>102.11</td>
      <td>1.36</td>
      <td>...</td>
      <td>25.129333</td>
      <td>32.264722</td>
      <td>42.605945</td>
      <td>0.003812</td>
      <td>7.932152</td>
      <td>92.064037</td>
      <td>152</td>
      <td>6,345</td>
      <td>7.342273</td>
      <td>6.913845</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 74 columns</p>
</div>




```python
df.columns
```




    Index(['지역', '1인가구비율 (%)', '1인당 자동차 등록대수 (대)', 'EQ-5D지표', '가구수 (가구)',
           '건강보험 적용인구 현황', '고령인구비율 (%)', '교원1인당 학생수 (명)', '남녀성비 (%)',
           '노인 천명당 노인여가복지시설수 (개)', '대학교 수 (개)', '대학교 학생수 (명)', '도로포장률 (%)',
           '도시지역면적 (km²)', '등록외국인 현황  (명)', '비만율 (%)', '사망률 (인구 10만명당 사망자)',
           '사망자수 (명)', '상수도보급률 (%)', '소년·소녀가정현황 (명)', '순이동인구 (명)', '스트레스 인지율 (%)',
           '아파트매매가격지수 (명)', '아파트월세통합가격지수 (명)', '유아 천명당 보육시설수 (개)', '음주율 (%)',
           '흡연율 (%)', '인구 십만명당 문화기반시설수 (개)', '인구 십만명당 사회복지시설수 (개)',
           '인구 십만명당 자살률 (명)', '인구 천명당 사설학원수 (개)', '인구 천명당 사업체수 (개)',
           '인구 천명당 외국인수 (명)', '인구 천명당 의료기관병상수 (개)', '인구 천명당 의료기관종사의사수 (명)',
           '인구 천명당 종사자수 (명)', '인구증가율 (%)', '일반회계중 사회복지예산비중 (%)',
           '일반회계중 일반공공행정예산비중 (%)', '자동차 천대당 교통사고발생건수 (건)', '장애인고용률 (%)',
           '재정자주도 (%)', '전입인구 (명)', '전출인구 (명)', '조이혼율 (천명당)', '조혼인율 (천명당)',
           '주관적건강수준 인지율 (%)', '주민등록인구 (명)', '주택월세통합가격지수 (명)', '지가변동률 (%)',
           '초등학교수 (개)', '출생아수 (명)', '토지거래 면적 (천㎡)', '토지거래현황 (천m²)', '폐수배출업소수 (개소)',
           '하수도보급률 (%)', '합계출산율 (명)', '총합계', '공원율', '다문화학생수', '한부모가구수', '아파트비율',
           '주택보급율', ' cctv대수', '단순직비율', '전문직비율', '서비스.사무직', '1차산업비율', '2차산업비율',
           '3차산업비율', '체육시설', '강력범죄발생건수', '유치원 교원비율', '초등학교 교원비율'],
          dtype='object')




```python
df.columns=['지역', '1인가구비율', '1인당 자동차 등록대수', 'EQ-5D지표', '가구수',
       '건강보험 적용인구 현황', '고령인구비율', '교원1인당 학생수', '남녀성비',
       '노인 천명당 노인여가복지시설수', '대학교 수', '대학교 학생수', '도로포장률',
       '도시지역면적', '등록외국인 현황', '비만율', '사망률',
       '사망자수', '상수도보급률', '소년·소녀가정현황', '순이동인구', '스트레스 인지율',
       '아파트매매가격지수', '아파트월세통합가격지수', '유아 천명당 보육시설수', '음주율',
       '흡연율', '인구 십만명당 문화기반시설수', '인구 십만명당 사회복지시설수',
       '인구 십만명당 자살률', '인구 천명당 사설학원수', '인구 천명당 사업체수',
       '인구 천명당 외국인수', '인구 천명당 의료기관병상수', '인구 천명당 의료기관종사의사수',
       '인구 천명당 종사자수', '인구증가율', '일반회계중 사회복지예산비중',
       '일반회계중 일반공공행정예산비중', '자동차 천대당 교통사고발생건수', '장애인고용률',
       '재정자주도', '전입인구', '전출인구', '조이혼율', '조혼인율',
       '주관적건강수준 인지율', '주민등록인구', '주택월세통합가격지수', '지가변동률',
       '초등학교수', '출생아수', '토지거래 면적', '토지거래현황', '폐수배출업소수',
       '하수도보급률', '합계출산율', '총합계', '공원율', '다문화학생수', '한부모가구수', '아파트비율',
       '주택보급율', ' cctv대수', '단순직비율', '전문직비율', '서비스.사무직', '1차산업비율', '2차산업비율',
       '3차산업비율', '체육시설', '강력범죄발생건수', '유치원 교원비율', '초등학교 교원비율']
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>1인가구비율</th>
      <th>1인당 자동차 등록대수</th>
      <th>EQ-5D지표</th>
      <th>가구수</th>
      <th>건강보험 적용인구 현황</th>
      <th>고령인구비율</th>
      <th>교원1인당 학생수</th>
      <th>남녀성비</th>
      <th>노인 천명당 노인여가복지시설수</th>
      <th>...</th>
      <th>단순직비율</th>
      <th>전문직비율</th>
      <th>서비스.사무직</th>
      <th>1차산업비율</th>
      <th>2차산업비율</th>
      <th>3차산업비율</th>
      <th>체육시설</th>
      <th>강력범죄발생건수</th>
      <th>유치원 교원비율</th>
      <th>초등학교 교원비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>29.3</td>
      <td>0.42</td>
      <td>0.953</td>
      <td>214911</td>
      <td>583900</td>
      <td>10.44</td>
      <td>14.96</td>
      <td>92.12</td>
      <td>2.18</td>
      <td>...</td>
      <td>11.905564</td>
      <td>43.888428</td>
      <td>44.206009</td>
      <td>0.010871</td>
      <td>5.527925</td>
      <td>94.461204</td>
      <td>278</td>
      <td>8,617</td>
      <td>8.141467</td>
      <td>6.481443</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>24.3</td>
      <td>0.30</td>
      <td>0.946</td>
      <td>167009</td>
      <td>449179</td>
      <td>11.30</td>
      <td>14.37</td>
      <td>99.46</td>
      <td>1.73</td>
      <td>...</td>
      <td>26.258041</td>
      <td>28.425884</td>
      <td>45.316075</td>
      <td>0.013298</td>
      <td>8.976362</td>
      <td>91.010339</td>
      <td>59</td>
      <td>5,244</td>
      <td>6.449553</td>
      <td>6.586494</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>28.5</td>
      <td>0.23</td>
      <td>0.938</td>
      <td>127462</td>
      <td>314857</td>
      <td>15.87</td>
      <td>14.76</td>
      <td>97.06</td>
      <td>1.50</td>
      <td>...</td>
      <td>33.520775</td>
      <td>20.564836</td>
      <td>45.914389</td>
      <td>0.000000</td>
      <td>10.973518</td>
      <td>89.026482</td>
      <td>67</td>
      <td>4,257</td>
      <td>7.370423</td>
      <td>6.692483</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>26.2</td>
      <td>0.32</td>
      <td>0.956</td>
      <td>220598</td>
      <td>570722</td>
      <td>11.51</td>
      <td>14.64</td>
      <td>95.62</td>
      <td>2.25</td>
      <td>...</td>
      <td>24.523081</td>
      <td>28.244766</td>
      <td>47.232153</td>
      <td>0.003005</td>
      <td>6.870435</td>
      <td>93.126559</td>
      <td>160</td>
      <td>5,585</td>
      <td>8.098529</td>
      <td>6.359084</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>43.9</td>
      <td>0.24</td>
      <td>0.951</td>
      <td>238744</td>
      <td>501170</td>
      <td>12.69</td>
      <td>12.81</td>
      <td>102.11</td>
      <td>1.36</td>
      <td>...</td>
      <td>25.129333</td>
      <td>32.264722</td>
      <td>42.605945</td>
      <td>0.003812</td>
      <td>7.932152</td>
      <td>92.064037</td>
      <td>152</td>
      <td>6,345</td>
      <td>7.342273</td>
      <td>6.913845</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 74 columns</p>
</div>




```python
df.to_csv("data/economy_features_74.csv",encoding ="UTF-8")
```


```python
df2= pd.read_csv("./data/economy_target_Version2.3.csv")
df2.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역별</th>
      <th>지역내총생산(당해년가격)</th>
      <th>구성비</th>
      <th>연중인구</th>
      <th>1인당 지역내총생산</th>
      <th>수준지수(서울특별시=100)</th>
      <th>재산세</th>
      <th>1인당 재산세</th>
      <th>재산세 수준지수(서울특별시=100)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울시</td>
      <td>344426006</td>
      <td>100.0</td>
      <td>10297138</td>
      <td>3345</td>
      <td>100.00</td>
      <td>930924579</td>
      <td>90.41</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>27929070</td>
      <td>8.1</td>
      <td>163822</td>
      <td>17048</td>
      <td>509.69</td>
      <td>37036740</td>
      <td>226.08</td>
      <td>250.06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>47887993</td>
      <td>13.9</td>
      <td>134329</td>
      <td>35650</td>
      <td>1065.80</td>
      <td>52642547</td>
      <td>391.89</td>
      <td>433.46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>9871373</td>
      <td>2.9</td>
      <td>247909</td>
      <td>3982</td>
      <td>119.04</td>
      <td>38116748</td>
      <td>153.75</td>
      <td>170.06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>성동구</td>
      <td>9673958</td>
      <td>2.8</td>
      <td>305065</td>
      <td>3171</td>
      <td>94.81</td>
      <td>24212208</td>
      <td>79.37</td>
      <td>87.79</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = df2[1:]
df2.columns=['지역', '지역내총생산(당해년가격)', '구성비', '연중인구', '1인당 지역내총생산', '수준지수(서울특별시=100)',
       '재산세', '1인당 재산세', '재산세 수준지수(서울특별시=100)']
df2.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>지역내총생산(당해년가격)</th>
      <th>구성비</th>
      <th>연중인구</th>
      <th>1인당 지역내총생산</th>
      <th>수준지수(서울특별시=100)</th>
      <th>재산세</th>
      <th>1인당 재산세</th>
      <th>재산세 수준지수(서울특별시=100)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>27929070</td>
      <td>8.1</td>
      <td>163822</td>
      <td>17048</td>
      <td>509.69</td>
      <td>37036740</td>
      <td>226.08</td>
      <td>250.06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>47887993</td>
      <td>13.9</td>
      <td>134329</td>
      <td>35650</td>
      <td>1065.80</td>
      <td>52642547</td>
      <td>391.89</td>
      <td>433.46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>9871373</td>
      <td>2.9</td>
      <td>247909</td>
      <td>3982</td>
      <td>119.04</td>
      <td>38116748</td>
      <td>153.75</td>
      <td>170.06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>성동구</td>
      <td>9673958</td>
      <td>2.8</td>
      <td>305065</td>
      <td>3171</td>
      <td>94.81</td>
      <td>24212208</td>
      <td>79.37</td>
      <td>87.79</td>
    </tr>
    <tr>
      <th>5</th>
      <td>광진구</td>
      <td>5592832</td>
      <td>1.6</td>
      <td>375180</td>
      <td>1491</td>
      <td>44.57</td>
      <td>22379658</td>
      <td>59.65</td>
      <td>65.98</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2[['지역','재산세 수준지수(서울특별시=100)']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>재산세 수준지수(서울특별시=100)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>250.06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>433.46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>170.06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>성동구</td>
      <td>87.79</td>
    </tr>
    <tr>
      <th>5</th>
      <td>광진구</td>
      <td>65.98</td>
    </tr>
    <tr>
      <th>6</th>
      <td>동대문구</td>
      <td>62.89</td>
    </tr>
    <tr>
      <th>7</th>
      <td>중랑구</td>
      <td>36.61</td>
    </tr>
    <tr>
      <th>8</th>
      <td>성북구</td>
      <td>48.72</td>
    </tr>
    <tr>
      <th>9</th>
      <td>강북구</td>
      <td>37.54</td>
    </tr>
    <tr>
      <th>10</th>
      <td>도봉구</td>
      <td>35.53</td>
    </tr>
    <tr>
      <th>11</th>
      <td>노원구</td>
      <td>37.41</td>
    </tr>
    <tr>
      <th>12</th>
      <td>은평구</td>
      <td>41.53</td>
    </tr>
    <tr>
      <th>13</th>
      <td>서대문구</td>
      <td>59.53</td>
    </tr>
    <tr>
      <th>14</th>
      <td>마포구</td>
      <td>99.80</td>
    </tr>
    <tr>
      <th>15</th>
      <td>양천구</td>
      <td>60.13</td>
    </tr>
    <tr>
      <th>16</th>
      <td>강서구</td>
      <td>69.75</td>
    </tr>
    <tr>
      <th>17</th>
      <td>구로구</td>
      <td>54.18</td>
    </tr>
    <tr>
      <th>18</th>
      <td>금천구</td>
      <td>68.31</td>
    </tr>
    <tr>
      <th>19</th>
      <td>영등포구</td>
      <td>111.28</td>
    </tr>
    <tr>
      <th>20</th>
      <td>동작구</td>
      <td>57.71</td>
    </tr>
    <tr>
      <th>21</th>
      <td>관악구</td>
      <td>42.71</td>
    </tr>
    <tr>
      <th>22</th>
      <td>서초구</td>
      <td>248.60</td>
    </tr>
    <tr>
      <th>23</th>
      <td>강남구</td>
      <td>344.20</td>
    </tr>
    <tr>
      <th>24</th>
      <td>송파구</td>
      <td>142.23</td>
    </tr>
    <tr>
      <th>25</th>
      <td>강동구</td>
      <td>75.82</td>
    </tr>
  </tbody>
</table>
</div>




```python
import json
import folium
import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)

geo_path = 'data/skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))
```


```python
map = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='Stamen Toner')
map.choropleth(geo_str, data = df2, columns =["지역", "수준지수(서울특별시=100)"], fill_color='PuRd', #PuRd, YlGnBu
              key_on='feature.id')
map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVM9ZmFsc2U7IExfTk9fVE9VQ0g9ZmFsc2U7IExfRElTQUJMRV8zRD1mYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgPHN0eWxlPiNtYXBfYjY4ZDE2ZDc0MGUwNDc4Yzk3Njg5NDk2MTIwMmIwZDEgewogICAgICAgIHBvc2l0aW9uOiByZWxhdGl2ZTsKICAgICAgICB3aWR0aDogMTAwLjAlOwogICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgdG9wOiAwLjAlOwogICAgICAgIH0KICAgIDwvc3R5bGU+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvZDMvMy41LjUvZDMubWluLmpzIj48L3NjcmlwdD4KPC9oZWFkPgo8Ym9keT4gICAgCiAgICAKICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfYjY4ZDE2ZDc0MGUwNDc4Yzk3Njg5NDk2MTIwMmIwZDEiID48L2Rpdj4KPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgCiAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAKCiAgICB2YXIgbWFwX2I2OGQxNmQ3NDBlMDQ3OGM5NzY4OTQ5NjEyMDJiMGQxID0gTC5tYXAoCiAgICAgICAgJ21hcF9iNjhkMTZkNzQwZTA0NzhjOTc2ODk0OTYxMjAyYjBkMScsIHsKICAgICAgICBjZW50ZXI6IFszNy41NTAyLCAxMjYuOTgyXSwKICAgICAgICB6b29tOiAxMSwKICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICBsYXllcnM6IFtdLAogICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcsCiAgICAgICAgem9vbUNvbnRyb2w6IHRydWUsCiAgICAgICAgfSk7CgogICAgCiAgICAKICAgIHZhciB0aWxlX2xheWVyXzZjY2I0OTk1YThlNzQ3MTE4MWM1MTBlYTVmMDkwYzA3ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgJ2h0dHBzOi8vc3RhbWVuLXRpbGVzLXtzfS5hLnNzbC5mYXN0bHkubmV0L3RvbmVyL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgewogICAgICAgICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgICAgICAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICAgICAgICJtYXhOYXRpdmVab29tIjogMTgsCiAgICAgICAgIm1heFpvb20iOiAxOCwKICAgICAgICAibWluWm9vbSI6IDAsCiAgICAgICAgIm5vV3JhcCI6IGZhbHNlLAogICAgICAgICJzdWJkb21haW5zIjogImFiYyIKfSkuYWRkVG8obWFwX2I2OGQxNmQ3NDBlMDQ3OGM5NzY4OTQ5NjEyMDJiMGQxKTsKICAgIAogICAgICAgIAogICAgICAgIHZhciBnZW9fanNvbl8zYmEwNTRiZGFlNDI0ODdjYTc3Mzk2N2Q3NmJkOTZiZSA9IEwuZ2VvSnNvbigKICAgICAgICAgICAgeyJmZWF0dXJlcyI6IFt7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XSwgWzEyNy4xNjY4MzE4NDM2NjEyOSwgMzcuNTc2NzI0ODczODg2MjddLCBbMTI3LjE4NDA4NzkyMzMwMTUyLCAzNy41NTgxNDI4MDM2OTU3NV0sIFsxMjcuMTY1MzA5ODQzMDc0NDcsIDM3LjU0MjIxODUxMjU4NjkzXSwgWzEyNy4xNDY3MjgwNjgyMzUwMiwgMzcuNTE0MTU2ODA2ODAyOTFdLCBbMTI3LjEyMTIzMTY1NzE5NjE1LCAzNy41MjUyODI3MDA4OV0sIFsxMjcuMTExNjc2NDIwMzYwOCwgMzcuNTQwNjY5OTU1MzI0OTY1XSwgWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFjMTVcdWIzZDlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTI1MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhYzE1XHViM2Q5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkdhbmdkb25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YxZWVmNiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl0sIFsxMjcuMTAwODc1MTk3OTE5NjIsIDM3LjUyNDg0MTIyMDE2NzA1NV0sIFsxMjcuMTExNjc2NDIwMzYwOCwgMzcuNTQwNjY5OTU1MzI0OTY1XSwgWzEyNy4xMjEyMzE2NTcxOTYxNSwgMzcuNTI1MjgyNzAwODldLCBbMTI3LjE0NjcyODA2ODIzNTAyLCAzNy41MTQxNTY4MDY4MDI5MV0sIFsxMjcuMTYzNDk0NDIxNTc2NSwgMzcuNDk3NDQ1NDA2MDk3NDg0XSwgWzEyNy4xNDIwNjA1ODQxMzI3NCwgMzcuNDcwODk4MTkwOTg1MDFdLCBbMTI3LjEyNDQwNTcxMDgwODkzLCAzNy40NjI0MDQ0NTU4NzA0OF0sIFsxMjcuMTExMTcwODUyMDEyMzgsIDM3LjQ4NTcwODM4MTUxMjQ0NV0sIFsxMjcuMDcxOTE0NjAwMDcyNCwgMzcuNTAyMjQwMTM1ODc2NjldLCBbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMWExXHVkMzBjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEyNDAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzFhMVx1ZDMwY1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJTb25ncGEtZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZjFlZWY2IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XSwgWzEyNy4wNjkwNjk4MTMwMzcyLCAzNy41MjIyNzk0MjM1MDUwMjZdLCBbMTI3LjA3MTkxNDYwMDA3MjQsIDM3LjUwMjI0MDEzNTg3NjY5XSwgWzEyNy4xMTExNzA4NTIwMTIzOCwgMzcuNDg1NzA4MzgxNTEyNDQ1XSwgWzEyNy4xMjQ0MDU3MTA4MDg5MywgMzcuNDYyNDA0NDU1ODcwNDhdLCBbMTI3LjA5ODQyNzU5MzE4NzUxLCAzNy40NTg2MjI1Mzg1NzQ2MV0sIFsxMjcuMDg2NDA0NDA1NzgxNTYsIDM3LjQ3MjY5NzkzNTE4NDY1NV0sIFsxMjcuMDU1OTE3MDQ4MTkwNCwgMzcuNDY1OTIyODkxNDA3N10sIFsxMjcuMDM2MjE5MTUwOTg3OTgsIDM3LjQ4MTc1ODAyNDI3NjAzXSwgWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldLCBbMTI3LjAyMzAyODMxODkwNTU5LCAzNy41MzIzMTg5OTU4MjY2M10sIFsxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFjMTVcdWIwYThcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIzMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhYzE1XHViMGE4XHVhZDZjIiwgIm5hbWVfZW5nIjogIkdhbmduYW0tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZDRiOWRhIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDEzOTcxMTk2Njc1MTMsIDM3LjUyNTAzOTg4Mjg5NjY5XSwgWzEyNy4wMzYyMTkxNTA5ODc5OCwgMzcuNDgxNzU4MDI0Mjc2MDNdLCBbMTI3LjA1NTkxNzA0ODE5MDQsIDM3LjQ2NTkyMjg5MTQwNzddLCBbMTI3LjA4NjQwNDQwNTc4MTU2LCAzNy40NzI2OTc5MzUxODQ2NTVdLCBbMTI3LjA5ODQyNzU5MzE4NzUxLCAzNy40NTg2MjI1Mzg1NzQ2MV0sIFsxMjcuMDkwNDY5Mjg1NjU5NTEsIDM3LjQ0Mjk2ODI2MTE0MTg1XSwgWzEyNy4wNjc3ODEwNzYwNTQzMywgMzcuNDI2MTk3NDI0MDU3MzE0XSwgWzEyNy4wNDk1NzIzMjk4NzE0MiwgMzcuNDI4MDU4MzY4NDU2OTRdLCBbMTI3LjAzODgxNzgyNTk3OTIyLCAzNy40NTM4MjAzOTg1MTcxNV0sIFsxMjYuOTkwNzIwNzMxOTU0NjIsIDM3LjQ1NTMyNjE0MzMxMDAyNV0sIFsxMjYuOTgzNjc2NjgyOTE4MDIsIDM3LjQ3Mzg1NjQ5MjY5MjA4Nl0sIFsxMjYuOTgyMjM4MDc5MTYwODEsIDM3LjUwOTMxNDk2Njc3MDMyNl0sIFsxMjcuMDEzOTcxMTk2Njc1MTMsIDM3LjUyNTAzOTg4Mjg5NjY5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWMxMWNcdWNkMDhcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIyMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjMTFjXHVjZDA4XHVhZDZjIiwgIm5hbWVfZW5nIjogIlNlb2Noby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNkNGI5ZGEiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45ODM2NzY2ODI5MTgwMiwgMzcuNDczODU2NDkyNjkyMDg2XSwgWzEyNi45OTA3MjA3MzE5NTQ2MiwgMzcuNDU1MzI2MTQzMzEwMDI1XSwgWzEyNi45NjUyMDQzOTA4NTE0MywgMzcuNDM4MjQ5Nzg0MDA2MjQ2XSwgWzEyNi45NTAwMDAwMTAxMDE4MiwgMzcuNDM2MTM0NTExNjU3MTldLCBbMTI2LjkzMDg0NDA4MDU2NTI1LCAzNy40NDczODI5MjgzMzM5OTRdLCBbMTI2LjkxNjc3MjgxNDY2MDEsIDM3LjQ1NDkwNTY2NDIzNzg5XSwgWzEyNi45MDE1NjA5NDEyOTg5NSwgMzcuNDc3NTM4NDI3ODk5MDFdLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuOTQ5MjI2NjEzODk1MDgsIDM3LjQ5MTI1NDM3NDk1NjQ5XSwgWzEyNi45NzI1ODkxODUwNjYyLCAzNy40NzI1NjEzNjMyNzgxMjVdLCBbMTI2Ljk4MzY3NjY4MjkxODAyLCAzNy40NzM4NTY0OTI2OTIwODZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWQwMFx1YzU0NVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMjEwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFkMDBcdWM1NDVcdWFkNmMiLCAibmFtZV9lbmciOiAiR3dhbmFrLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YxZWVmNiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk4MjIzODA3OTE2MDgxLCAzNy41MDkzMTQ5NjY3NzAzMjZdLCBbMTI2Ljk4MzY3NjY4MjkxODAyLCAzNy40NzM4NTY0OTI2OTIwODZdLCBbMTI2Ljk3MjU4OTE4NTA2NjIsIDM3LjQ3MjU2MTM2MzI3ODEyNV0sIFsxMjYuOTQ5MjI2NjEzODk1MDgsIDM3LjQ5MTI1NDM3NDk1NjQ5XSwgWzEyNi45MDUzMTk3NTgwMTgxMiwgMzcuNDgyMTgwODc1NzU0MjldLCBbMTI2LjkyMTc3ODkzMTc0ODI1LCAzNy40OTQ4ODk4Nzc0MTUxNzZdLCBbMTI2LjkyODEwNjI4ODI4Mjc5LCAzNy41MTMyOTU5NTczMjAxNV0sIFsxMjYuOTUyNDk5OTAyOTgxNTksIDM3LjUxNzIyNTAwNzQxODEzXSwgWzEyNi45ODIyMzgwNzkxNjA4MSwgMzcuNTA5MzE0OTY2NzcwMzI2XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIzZDlcdWM3OTFcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIwMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViM2Q5XHVjNzkxXHVhZDZjIiwgIm5hbWVfZW5nIjogIkRvbmdqYWstZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZjFlZWY2IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuODkxODQ2NjM4NjI3NjQsIDM3LjU0NzM3Mzk3NDk5NzExNF0sIFsxMjYuOTQ1NjY3MzMwODMyMTIsIDM3LjUyNjYxNzU0MjQ1MzM2Nl0sIFsxMjYuOTUyNDk5OTAyOTgxNTksIDM3LjUxNzIyNTAwNzQxODEzXSwgWzEyNi45MjgxMDYyODgyODI3OSwgMzcuNTEzMjk1OTU3MzIwMTVdLCBbMTI2LjkyMTc3ODkzMTc0ODI1LCAzNy40OTQ4ODk4Nzc0MTUxNzZdLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuODk1OTQ3NzY3ODI0ODUsIDM3LjUwNDY3NTI4MTMwOTE3Nl0sIFsxMjYuODgxNTY0MDIzNTM4NjIsIDM3LjUxMzk3MDAzNDc2NTY4NF0sIFsxMjYuODg4MjU3NTc4NjAwOTksIDM3LjU0MDc5NzMzNjMwMjMyXSwgWzEyNi44OTE4NDY2Mzg2Mjc2NCwgMzcuNTQ3MzczOTc0OTk3MTE0XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWM2MDFcdWI0ZjFcdWQzZWNcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTE5MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjNjAxXHViNGYxXHVkM2VjXHVhZDZjIiwgIm5hbWVfZW5nIjogIlllb25nZGV1bmdwby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNkNGI5ZGEiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45MDE1NjA5NDEyOTg5NSwgMzcuNDc3NTM4NDI3ODk5MDFdLCBbMTI2LjkxNjc3MjgxNDY2MDEsIDM3LjQ1NDkwNTY2NDIzNzg5XSwgWzEyNi45MzA4NDQwODA1NjUyNSwgMzcuNDQ3MzgyOTI4MzMzOTk0XSwgWzEyNi45MDI1ODMxNzExNjk3LCAzNy40MzQ1NDkzNjYzNDkxMjRdLCBbMTI2Ljg3NjgzMjcxNTAyNDI4LCAzNy40ODI1NzY1OTE2MDczMDVdLCBbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZTA4XHVjYzljXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExODAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWUwOFx1Y2M5Y1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJHZXVtY2hlb24tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZjFlZWY2IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuODI2ODgwODE1MTczMTQsIDM3LjUwNTQ4OTcyMjMyODk2XSwgWzEyNi44ODE1NjQwMjM1Mzg2MiwgMzcuNTEzOTcwMDM0NzY1Njg0XSwgWzEyNi44OTU5NDc3Njc4MjQ4NSwgMzcuNTA0Njc1MjgxMzA5MTc2XSwgWzEyNi45MDUzMTk3NTgwMTgxMiwgMzcuNDgyMTgwODc1NzU0MjldLCBbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV0sIFsxMjYuODc2ODMyNzE1MDI0MjgsIDM3LjQ4MjU3NjU5MTYwNzMwNV0sIFsxMjYuODQ3NjI2NzYwNTQ5NTMsIDM3LjQ3MTQ2NzIzOTM2MzIzXSwgWzEyNi44MzU0OTQ4NTA3NjE5NiwgMzcuNDc0MDk4MjM2OTc1MDk1XSwgWzEyNi44MjI2NDc5Njc5MTM0OCwgMzcuNDg3ODQ3NjQ5MjE0N10sIFsxMjYuODI1MDQ3MzYzMzE0MDYsIDM3LjUwMzAyNjEyNjQwNDQzXSwgWzEyNi44MjY4ODA4MTUxNzMxNCwgMzcuNTA1NDg5NzIyMzI4OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWQ2Y1x1Yjg1Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTcwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFkNmNcdWI4NWNcdWFkNmMiLCAibmFtZV9lbmciOiAiR3Vyby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi43OTU3NTc2ODU1MjkwNywgMzcuNTc4ODEwODc2MzMyMDJdLCBbMTI2LjgwNzAyMTE1MDIzNTk3LCAzNy42MDEyMzAwMTAxMzIyOF0sIFsxMjYuODIyNTE0Mzg0NzcxMDUsIDM3LjU4ODA0MzA4MTAwODJdLCBbMTI2Ljg1OTg0MTk5Mzk5NjY3LCAzNy41NzE4NDc4NTUyOTI3NDVdLCBbMTI2Ljg5MTg0NjYzODYyNzY0LCAzNy41NDczNzM5NzQ5OTcxMTRdLCBbMTI2Ljg4ODI1NzU3ODYwMDk5LCAzNy41NDA3OTczMzYzMDIzMl0sIFsxMjYuODY2Mzc0NjQzMjEyMzgsIDM3LjU0ODU5MTkxMDk0ODIzXSwgWzEyNi44NjYxMDA3MzQ3NjM5NSwgMzcuNTI2OTk5NjQxNDQ2NjldLCBbMTI2Ljg0MjU3MjkxOTQzMTUzLCAzNy41MjM3MzcwNzgwNTU5Nl0sIFsxMjYuODI0MjMzMTQyNjcyMiwgMzcuNTM3ODgwNzg3NTMyNDhdLCBbMTI2Ljc3MzI0NDE3NzE3NzAzLCAzNy41NDU5MTIzNDUwNTU0XSwgWzEyNi43Njk3OTE4MDU3OTM1MiwgMzcuNTUxMzkxODMwMDg4MDldLCBbMTI2Ljc5NTc1NzY4NTUyOTA3LCAzNy41Nzg4MTA4NzYzMzIwMl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhYzE1XHVjMTFjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExNjAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWMxNVx1YzExY1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJHYW5nc2VvLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YxZWVmNiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2LjgyNDIzMzE0MjY3MjIsIDM3LjUzNzg4MDc4NzUzMjQ4XSwgWzEyNi44NDI1NzI5MTk0MzE1MywgMzcuNTIzNzM3MDc4MDU1OTZdLCBbMTI2Ljg2NjEwMDczNDc2Mzk1LCAzNy41MjY5OTk2NDE0NDY2OV0sIFsxMjYuODY2Mzc0NjQzMjEyMzgsIDM3LjU0ODU5MTkxMDk0ODIzXSwgWzEyNi44ODgyNTc1Nzg2MDA5OSwgMzcuNTQwNzk3MzM2MzAyMzJdLCBbMTI2Ljg4MTU2NDAyMzUzODYyLCAzNy41MTM5NzAwMzQ3NjU2ODRdLCBbMTI2LjgyNjg4MDgxNTE3MzE0LCAzNy41MDU0ODk3MjIzMjg5Nl0sIFsxMjYuODI0MjMzMTQyNjcyMiwgMzcuNTM3ODgwNzg3NTMyNDhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzU5MVx1Y2M5Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTUwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM1OTFcdWNjOWNcdWFkNmMiLCAibmFtZV9lbmciOiAiWWFuZ2NoZW9uLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YxZWVmNiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2LjkwNTIyMDY1ODMxMDUzLCAzNy41NzQwOTcwMDUyMjU3NF0sIFsxMjYuOTM4OTgxNjE3OTg5NzMsIDM3LjU1MjMxMDAwMzcyODEyNF0sIFsxMjYuOTYzNTgyMjY3MTA4MTIsIDM3LjU1NjA1NjM1NDc1MTU0XSwgWzEyNi45NjQ0ODU3MDU1MzA1NSwgMzcuNTQ4NzA1NjkyMDIxNjM1XSwgWzEyNi45NDU2NjczMzA4MzIxMiwgMzcuNTI2NjE3NTQyNDUzMzY2XSwgWzEyNi44OTE4NDY2Mzg2Mjc2NCwgMzcuNTQ3MzczOTc0OTk3MTE0XSwgWzEyNi44NTk4NDE5OTM5OTY2NywgMzcuNTcxODQ3ODU1MjkyNzQ1XSwgWzEyNi44ODQzMzI4NDc3MzI4OCwgMzcuNTg4MTQzMzIyODgwNTI2XSwgWzEyNi45MDUyMjA2NTgzMTA1MywgMzcuNTc0MDk3MDA1MjI1NzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YjljOFx1ZDNlY1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTQwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWI5YzhcdWQzZWNcdWFkNmMiLCAibmFtZV9lbmciOiAiTWFwby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTU1NjU0MjU4NDY0NjMsIDM3LjU3NjA4MDc5MDg4MTQ1Nl0sIFsxMjYuOTY4NzM2MzMyNzkwNzUsIDM3LjU2MzEzNjA0NjkwODI3XSwgWzEyNi45NjM1ODIyNjcxMDgxMiwgMzcuNTU2MDU2MzU0NzUxNTRdLCBbMTI2LjkzODk4MTYxNzk4OTczLCAzNy41NTIzMTAwMDM3MjgxMjRdLCBbMTI2LjkwNTIyMDY1ODMxMDUzLCAzNy41NzQwOTcwMDUyMjU3NF0sIFsxMjYuOTUyNDc1MjAzMDU3MiwgMzcuNjA1MDg2OTI3MzcwNDVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzExY1x1YjMwMFx1YmIzOFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTMwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWMxMWNcdWIzMDBcdWJiMzhcdWFkNmMiLCAibmFtZV9lbmciOiAiU2VvZGFlbXVuLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YxZWVmNiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk3Mzg4NjQxMjg3MDIsIDM3LjYyOTQ5NjM0Nzg2ODg4XSwgWzEyNi45NTQyNzAxNzAwNjEyOSwgMzcuNjIyMDMzNDMxMzM5NDI1XSwgWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTA1MjIwNjU4MzEwNTMsIDM3LjU3NDA5NzAwNTIyNTc0XSwgWzEyNi44ODQzMzI4NDc3MzI4OCwgMzcuNTg4MTQzMzIyODgwNTI2XSwgWzEyNi45MDM5NjY4MTAwMzU5NSwgMzcuNTkyMjc0MDM0MTk5NDJdLCBbMTI2LjkwMzAzMDY2MTc3NjY4LCAzNy42MDk5Nzc5MTE0MDEzNDRdLCBbMTI2LjkxNDU1NDgxNDI5NjQ4LCAzNy42NDE1MDA1MDk5NjkzNV0sIFsxMjYuOTU2NDczNzk3Mzg3LCAzNy42NTI0ODA3MzczMzk0NDVdLCBbMTI2Ljk3Mzg4NjQxMjg3MDIsIDM3LjYyOTQ5NjM0Nzg2ODg4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWM3NDBcdWQzYzlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTEyMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjNzQwXHVkM2M5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkV1bnB5ZW9uZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wODM4NzUyNzAzMTk1LCAzNy42OTM1OTUzNDIwMjAzNF0sIFsxMjcuMDk3MDYzOTEzMDk2OTUsIDM3LjY4NjM4MzcxOTM3MjI5NF0sIFsxMjcuMDk0NDA3NjYyOTg3MTcsIDM3LjY0NzEzNDkwNDczMDQ1XSwgWzEyNy4xMTMyNjc5NTg1NTE5OSwgMzcuNjM5NjIyOTA1MzE1OTI1XSwgWzEyNy4xMDc4MjI3NzY4ODEyOSwgMzcuNjE4MDQyNDQyNDEwNjldLCBbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM10sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wNDM1ODgwMDg5NTYwOSwgMzcuNjI4NDg5MzEyOTg3MTVdLCBbMTI3LjA1ODAwMDc1MjIwMDkxLCAzNy42NDMxODI2Mzg3ODI3Nl0sIFsxMjcuMDUyODg0Nzk3MTA0ODUsIDM3LjY4NDIzODU3MDg0MzQ3XSwgWzEyNy4wODM4NzUyNzAzMTk1LCAzNy42OTM1OTUzNDIwMjAzNF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHViMTc4XHVjNmQwXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExMTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YjE3OFx1YzZkMFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJOb3dvbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wNTI4ODQ3OTcxMDQ4NSwgMzcuNjg0MjM4NTcwODQzNDddLCBbMTI3LjA1ODAwMDc1MjIwMDkxLCAzNy42NDMxODI2Mzg3ODI3Nl0sIFsxMjcuMDQzNTg4MDA4OTU2MDksIDM3LjYyODQ4OTMxMjk4NzE1XSwgWzEyNy4wMTQ2NTkzNTg5MjQ2NiwgMzcuNjQ5NDM2ODc0OTY4MTJdLCBbMTI3LjAyMDYyMTE2MTQxMzg5LCAzNy42NjcxNzM1NzU5NzEyMDVdLCBbMTI3LjAxMDM5NjY2MDQyMDcxLCAzNy42ODE4OTQ1ODk2MDM1OTRdLCBbMTI3LjAxNzk1MDk5MjAzNDMyLCAzNy42OTgyNDQxMjc3NTY2Ml0sIFsxMjcuMDUyODg0Nzk3MTA0ODUsIDM3LjY4NDIzODU3MDg0MzQ3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIzYzRcdWJkMDlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTEwMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViM2M0XHViZDA5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkRvYm9uZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45OTM4MzkwMzQyNCwgMzcuNjc2NjgxNzYxMTk5MDg1XSwgWzEyNy4wMTAzOTY2NjA0MjA3MSwgMzcuNjgxODk0NTg5NjAzNTk0XSwgWzEyNy4wMjA2MjExNjE0MTM4OSwgMzcuNjY3MTczNTc1OTcxMjA1XSwgWzEyNy4wMTQ2NTkzNTg5MjQ2NiwgMzcuNjQ5NDM2ODc0OTY4MTJdLCBbMTI3LjA0MzU4ODAwODk1NjA5LCAzNy42Mjg0ODkzMTI5ODcxNV0sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wMzg5MjQwMDk5MjMwMSwgMzcuNjA5NzE1NjExMDIzODE2XSwgWzEyNy4wMTI4MTU0NzQ5NTIzLCAzNy42MTM2NTIyNDM0NzAyNTZdLCBbMTI2Ljk4NjcyNzA1NTEzODY5LCAzNy42MzM3NzY0MTI4ODE5Nl0sIFsxMjYuOTgxNzQ1MjY3NjU1MSwgMzcuNjUyMDk3NjkzODc3NzZdLCBbMTI2Ljk5MzgzOTAzNDI0LCAzNy42NzY2ODE3NjExOTkwODVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWMxNVx1YmQ4MVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDkwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFjMTVcdWJkODFcdWFkNmMiLCAibmFtZV9lbmciOiAiR2FuZ2J1ay1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NzcxNzU0MDY0MTYsIDM3LjYyODU5NzE1NDAwMzg4XSwgWzEyNi45ODY3MjcwNTUxMzg2OSwgMzcuNjMzNzc2NDEyODgxOTZdLCBbMTI3LjAxMjgxNTQ3NDk1MjMsIDM3LjYxMzY1MjI0MzQ3MDI1Nl0sIFsxMjcuMDM4OTI0MDA5OTIzMDEsIDM3LjYwOTcxNTYxMTAyMzgxNl0sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wNzM1MTI0MzgyNTI3OCwgMzcuNjEyODM2NjAzNDIzMTNdLCBbMTI3LjA3MzgyNzA3MDk5MjI3LCAzNy42MDQwMTkyODk4NjQxOV0sIFsxMjcuMDQyNzA1MjIyMDk0LCAzNy41OTIzOTQzNzU5MzM5MV0sIFsxMjcuMDI1MjcyNTQ1MjgwMDMsIDM3LjU3NTI0NjE2MjQ1MjQ5XSwgWzEyNi45OTM0ODI5MzM1ODMxNCwgMzcuNTg4NTY1NDU3MjE2MTU2XSwgWzEyNi45ODg3OTg2NTk5MjM4NCwgMzcuNjExODkyNzMxOTc1Nl0sIFsxMjYuOTc3MTc1NDA2NDE2LCAzNy42Mjg1OTcxNTQwMDM4OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMTMxXHViZDgxXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwODAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzEzMVx1YmQ4MVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJTZW9uZ2J1ay1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wNzM1MTI0MzgyNTI3OCwgMzcuNjEyODM2NjAzNDIzMTNdLCBbMTI3LjEwNzgyMjc3Njg4MTI5LCAzNy42MTgwNDI0NDI0MTA2OV0sIFsxMjcuMTIwMTI0NjAyMDExNCwgMzcuNjAxNzg0NTc1OTgxODhdLCBbMTI3LjEwMzA0MTc0MjQ5MjE0LCAzNy41NzA3NjM0MjI5MDk1NV0sIFsxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XSwgWzEyNy4wNzM4MjcwNzA5OTIyNywgMzcuNjA0MDE5Mjg5ODY0MTldLCBbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjOTExXHViNzkxXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNzAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzkxMVx1Yjc5MVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJKdW5nbmFuZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjUyNzI1NDUyODAwMywgMzcuNTc1MjQ2MTYyNDUyNDldLCBbMTI3LjA0MjcwNTIyMjA5NCwgMzcuNTkyMzk0Mzc1OTMzOTFdLCBbMTI3LjA3MzgyNzA3MDk5MjI3LCAzNy42MDQwMTkyODk4NjQxOV0sIFsxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA1MDA1NjAxMDgxNTY3LCAzNy41Njc1Nzc2MTI1OTA4NDZdLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdLCBbMTI3LjAyNTI3MjU0NTI4MDAzLCAzNy41NzUyNDYxNjI0NTI0OV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHViM2Q5XHViMzAwXHViYjM4XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNjAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YjNkOVx1YjMwMFx1YmIzOFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJEb25nZGFlbXVuLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YxZWVmNiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA4MDY4NTQxMjgwNDAzLCAzNy41NjkwNjQyNTUxOTAxN10sIFsxMjcuMTAzMDQxNzQyNDkyMTQsIDM3LjU3MDc2MzQyMjkwOTU1XSwgWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XSwgWzEyNy4xMTE2NzY0MjAzNjA4LCAzNy41NDA2Njk5NTUzMjQ5NjVdLCBbMTI3LjEwMDg3NTE5NzkxOTYyLCAzNy41MjQ4NDEyMjAxNjcwNTVdLCBbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl0sIFsxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA4MDY4NTQxMjgwNDAzLCAzNy41NjkwNjQyNTUxOTAxN11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZDExXHVjOWM0XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWQxMVx1YzljNFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJHd2FuZ2ppbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjU0NzI2NjM0OTk3NiwgMzcuNTY4OTQzNTUyMjM3NzM0XSwgWzEyNy4wNTAwNTYwMTA4MTU2NywgMzcuNTY3NTc3NjEyNTkwODQ2XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA1ODY3MzU5Mjg4Mzk4LCAzNy41MjYyOTk3NDkyMjU2OF0sIFsxMjcuMDIzMDI4MzE4OTA1NTksIDM3LjUzMjMxODk5NTgyNjYzXSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzEzMVx1YjNkOVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDQwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWMxMzFcdWIzZDlcdWFkNmMiLCAibmFtZV9lbmciOiAiU2Vvbmdkb25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YxZWVmNiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjAxMDcwODk0MTc3NDgyLCAzNy41NDExODA0ODk2NDc2Ml0sIFsxMjcuMDIzMDI4MzE4OTA1NTksIDM3LjUzMjMxODk5NTgyNjYzXSwgWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldLCBbMTI2Ljk4MjIzODA3OTE2MDgxLCAzNy41MDkzMTQ5NjY3NzAzMjZdLCBbMTI2Ljk1MjQ5OTkwMjk4MTU5LCAzNy41MTcyMjUwMDc0MTgxM10sIFsxMjYuOTQ1NjY3MzMwODMyMTIsIDM3LjUyNjYxNzU0MjQ1MzM2Nl0sIFsxMjYuOTY0NDg1NzA1NTMwNTUsIDM3LjU0ODcwNTY5MjAyMTYzNV0sIFsxMjYuOTg3NTI5OTY5MDMzMjgsIDM3LjU1MDk0ODE4ODA3MTM5XSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzZhOVx1YzBiMFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDMwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM2YTlcdWMwYjBcdWFkNmMiLCAibmFtZV9lbmciOiAiWW9uZ3Nhbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjU0NzI2NjM0OTk3NiwgMzcuNTY4OTQzNTUyMjM3NzM0XSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdLCBbMTI2Ljk4NzUyOTk2OTAzMzI4LCAzNy41NTA5NDgxODgwNzEzOV0sIFsxMjYuOTY0NDg1NzA1NTMwNTUsIDM3LjU0ODcwNTY5MjAyMTYzNV0sIFsxMjYuOTYzNTgyMjY3MTA4MTIsIDM3LjU1NjA1NjM1NDc1MTU0XSwgWzEyNi45Njg3MzYzMzI3OTA3NSwgMzcuNTYzMTM2MDQ2OTA4MjddLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzkxMVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDIwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM5MTFcdWFkNmMiLCAibmFtZV9lbmciOiAiSnVuZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNjZTEyNTYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NzM4ODY0MTI4NzAyLCAzNy42Mjk0OTYzNDc4Njg4OF0sIFsxMjYuOTc3MTc1NDA2NDE2LCAzNy42Mjg1OTcxNTQwMDM4OF0sIFsxMjYuOTg4Nzk4NjU5OTIzODQsIDM3LjYxMTg5MjczMTk3NTZdLCBbMTI2Ljk5MzQ4MjkzMzU4MzE0LCAzNy41ODg1NjU0NTcyMTYxNTZdLCBbMTI3LjAyNTI3MjU0NTI4MDAzLCAzNy41NzUyNDYxNjI0NTI0OV0sIFsxMjcuMDI1NDcyNjYzNDk5NzYsIDM3LjU2ODk0MzU1MjIzNzczNF0sIFsxMjYuOTY4NzM2MzMyNzkwNzUsIDM3LjU2MzEzNjA0NjkwODI3XSwgWzEyNi45NTU2NTQyNTg0NjQ2MywgMzcuNTc2MDgwNzkwODgxNDU2XSwgWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTU0MjcwMTcwMDYxMjksIDM3LjYyMjAzMzQzMTMzOTQyNV0sIFsxMjYuOTczODg2NDEyODcwMiwgMzcuNjI5NDk2MzQ3ODY4ODhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1Yzg4NVx1Yjg1Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDEwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM4ODVcdWI4NWNcdWFkNmMiLCAibmFtZV9lbmciOiAiSm9uZ25vLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M5OTRjNyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn1dLCAidHlwZSI6ICJGZWF0dXJlQ29sbGVjdGlvbiJ9CiAgICAgICAgICAgIAogICAgICAgICAgICApLmFkZFRvKG1hcF9iNjhkMTZkNzQwZTA0NzhjOTc2ODk0OTYxMjAyYjBkMSk7CiAgICAgICAgZ2VvX2pzb25fM2JhMDU0YmRhZTQyNDg3Y2E3NzM5NjdkNzZiZDk2YmUuc2V0U3R5bGUoZnVuY3Rpb24oZmVhdHVyZSkge3JldHVybiBmZWF0dXJlLnByb3BlcnRpZXMuc3R5bGU7fSk7CiAgICAgICAgCiAgICAKICAgIHZhciBjb2xvcl9tYXBfOTQwNjJiMTY0MGFjNDIyZTk2Mjc2MWYxYTg3OTJhMzcgPSB7fTsKCiAgICAKICAgIGNvbG9yX21hcF85NDA2MmIxNjQwYWM0MjJlOTYyNzYxZjFhODc5MmEzNy5jb2xvciA9IGQzLnNjYWxlLnRocmVzaG9sZCgpCiAgICAgICAgICAgICAgLmRvbWFpbihbMTAuMzE5NywgMTIuNDU1ODMzNDY2OTMzODY4LCAxNC41OTE5NjY5MzM4Njc3MzQsIDE2LjcyODEwMDQwMDgwMTYsIDE4Ljg2NDIzMzg2NzczNTQ3LCAyMS4wMDAzNjczMzQ2NjkzMzUsIDIzLjEzNjUwMDgwMTYwMzIwNSwgMjUuMjcyNjM0MjY4NTM3MDcsIDI3LjQwODc2NzczNTQ3MDk0LCAyOS41NDQ5MDEyMDI0MDQ4MSwgMzEuNjgxMDM0NjY5MzM4NjcyLCAzMy44MTcxNjgxMzYyNzI1NCwgMzUuOTUzMzAxNjAzMjA2NDEsIDM4LjA4OTQzNTA3MDE0MDI3NiwgNDAuMjI1NTY4NTM3MDc0MTQ2LCA0Mi4zNjE3MDIwMDQwMDgwMSwgNDQuNDk3ODM1NDcwOTQxODgsIDQ2LjYzMzk2ODkzNzg3NTc0LCA0OC43NzAxMDI0MDQ4MDk2MSwgNTAuOTA2MjM1ODcxNzQzNDc2LCA1My4wNDIzNjkzMzg2NzczNSwgNTUuMTc4NTAyODA1NjExMjIsIDU3LjMxNDYzNjI3MjU0NTA4LCA1OS40NTA3Njk3Mzk0Nzg5NSwgNjEuNTg2OTAzMjA2NDEyODIsIDYzLjcyMzAzNjY3MzM0NjY5LCA2NS44NTkxNzAxNDAyODA1NSwgNjcuOTk1MzAzNjA3MjE0NDIsIDcwLjEzMTQzNzA3NDE0ODMsIDcyLjI2NzU3MDU0MTA4MjE2LCA3NC40MDM3MDQwMDgwMTYwMiwgNzYuNTM5ODM3NDc0OTQ5ODksIDc4LjY3NTk3MDk0MTg4Mzc2LCA4MC44MTIxMDQ0MDg4MTc2MywgODIuOTQ4MjM3ODc1NzUxNDksIDg1LjA4NDM3MTM0MjY4NTM2LCA4Ny4yMjA1MDQ4MDk2MTkyMywgODkuMzU2NjM4Mjc2NTUzMSwgOTEuNDkyNzcxNzQzNDg2OTUsIDkzLjYyODkwNTIxMDQyMDgzLCA5NS43NjUwMzg2NzczNTQ3LCA5Ny45MDExNzIxNDQyODg1NywgMTAwLjAzNzMwNTYxMTIyMjQ0LCAxMDIuMTczNDM5MDc4MTU2MjksIDEwNC4zMDk1NzI1NDUwOTAxNiwgMTA2LjQ0NTcwNjAxMjAyNDAzLCAxMDguNTgxODM5NDc4OTU3OSwgMTEwLjcxNzk3Mjk0NTg5MTc2LCAxMTIuODU0MTA2NDEyODI1NjQsIDExNC45OTAyMzk4Nzk3NTk1MSwgMTE3LjEyNjM3MzM0NjY5MzM4LCAxMTkuMjYyNTA2ODEzNjI3MjUsIDEyMS4zOTg2NDAyODA1NjExMSwgMTIzLjUzNDc3Mzc0NzQ5NDk4LCAxMjUuNjcwOTA3MjE0NDI4ODUsIDEyNy44MDcwNDA2ODEzNjI3MiwgMTI5Ljk0MzE3NDE0ODI5NjU4LCAxMzIuMDc5MzA3NjE1MjMwNDUsIDEzNC4yMTU0NDEwODIxNjQzMiwgMTM2LjM1MTU3NDU0OTA5ODIsIDEzOC40ODc3MDgwMTYwMzIwNiwgMTQwLjYyMzg0MTQ4Mjk2NTkzLCAxNDIuNzU5OTc0OTQ5ODk5OCwgMTQ0Ljg5NjEwODQxNjgzMzY0LCAxNDcuMDMyMjQxODgzNzY3NTQsIDE0OS4xNjgzNzUzNTA3MDE0LCAxNTEuMzA0NTA4ODE3NjM1MjgsIDE1My40NDA2NDIyODQ1NjkxNSwgMTU1LjU3Njc3NTc1MTUwMywgMTU3LjcxMjkwOTIxODQzNjksIDE1OS44NDkwNDI2ODUzNzA3MywgMTYxLjk4NTE3NjE1MjMwNDYzLCAxNjQuMTIxMzA5NjE5MjM4NDcsIDE2Ni4yNTc0NDMwODYxNzIzNCwgMTY4LjM5MzU3NjU1MzEwNjIxLCAxNzAuNTI5NzEwMDIwMDQwMDgsIDE3Mi42NjU4NDM0ODY5NzM5MywgMTc0LjgwMTk3Njk1MzkwNzgzLCAxNzYuOTM4MTEwNDIwODQxNjcsIDE3OS4wNzQyNDM4ODc3NzU1NywgMTgxLjIxMDM3NzM1NDcwOTQsIDE4My4zNDY1MTA4MjE2NDMyOCwgMTg1LjQ4MjY0NDI4ODU3NzE1LCAxODcuNjE4Nzc3NzU1NTExMDIsIDE4OS43NTQ5MTEyMjI0NDQ5LCAxOTEuODkxMDQ0Njg5Mzc4NzYsIDE5NC4wMjcxNzgxNTYzMTI2LCAxOTYuMTYzMzExNjIzMjQ2NSwgMTk4LjI5OTQ0NTA5MDE4MDM0LCAyMDAuNDM1NTc4NTU3MTE0MjQsIDIwMi41NzE3MTIwMjQwNDgwOCwgMjA0LjcwNzg0NTQ5MDk4MTk1LCAyMDYuODQzOTc4OTU3OTE1ODIsIDIwOC45ODAxMTI0MjQ4NDk3LCAyMTEuMTE2MjQ1ODkxNzgzNTQsIDIxMy4yNTIzNzkzNTg3MTc0MywgMjE1LjM4ODUxMjgyNTY1MTMsIDIxNy41MjQ2NDYyOTI1ODUxNywgMjE5LjY2MDc3OTc1OTUxOTA0LCAyMjEuNzk2OTEzMjI2NDUyOSwgMjIzLjkzMzA0NjY5MzM4Njc5LCAyMjYuMDY5MTgwMTYwMzIwNjMsIDIyOC4yMDUzMTM2MjcyNTQ1MywgMjMwLjM0MTQ0NzA5NDE4ODM3LCAyMzIuNDc3NTgwNTYxMTIyMjQsIDIzNC42MTM3MTQwMjgwNTYxLCAyMzYuNzQ5ODQ3NDk0OTg5OTgsIDIzOC44ODU5ODA5NjE5MjM4NSwgMjQxLjAyMjExNDQyODg1NzcyLCAyNDMuMTU4MjQ3ODk1NzkxNTYsIDI0NS4yOTQzODEzNjI3MjU0NiwgMjQ3LjQzMDUxNDgyOTY1OTMsIDI0OS41NjY2NDgyOTY1OTMxNywgMjUxLjcwMjc4MTc2MzUyNzA0LCAyNTMuODM4OTE1MjMwNDYwOSwgMjU1Ljk3NTA0ODY5NzM5NDc4LCAyNTguMTExMTgyMTY0MzI4NiwgMjYwLjI0NzMxNTYzMTI2MjUsIDI2Mi4zODM0NDkwOTgxOTYzNywgMjY0LjUxOTU4MjU2NTEzMDI0LCAyNjYuNjU1NzE2MDMyMDY0MSwgMjY4Ljc5MTg0OTQ5ODk5OCwgMjcwLjkyNzk4Mjk2NTkzMTg1LCAyNzMuMDY0MTE2NDMyODY1NywgMjc1LjIwMDI0OTg5OTc5OTYsIDI3Ny4zMzYzODMzNjY3MzM0NiwgMjc5LjQ3MjUxNjgzMzY2NzI3LCAyODEuNjA4NjUwMzAwNjAxMiwgMjgzLjc0NDc4Mzc2NzUzNTA3LCAyODUuODgwOTE3MjM0NDY4OTQsIDI4OC4wMTcwNTA3MDE0MDI4LCAyOTAuMTUzMTg0MTY4MzM2NywgMjkyLjI4OTMxNzYzNTI3MDU1LCAyOTQuNDI1NDUxMTAyMjA0MzYsIDI5Ni41NjE1ODQ1NjkxMzgzLCAyOTguNjk3NzE4MDM2MDcyMTYsIDMwMC44MzM4NTE1MDMwMDYsIDMwMi45Njk5ODQ5Njk5Mzk4NCwgMzA1LjEwNjExODQzNjg3Mzc3LCAzMDcuMjQyMjUxOTAzODA3NiwgMzA5LjM3ODM4NTM3MDc0MTQ2LCAzMTEuNTE0NTE4ODM3Njc1MywgMzEzLjY1MDY1MjMwNDYwOTI1LCAzMTUuNzg2Nzg1NzcxNTQzMDcsIDMxNy45MjI5MTkyMzg0NzY5NCwgMzIwLjA1OTA1MjcwNTQxMDgsIDMyMi4xOTUxODYxNzIzNDQ3LCAzMjQuMzMxMzE5NjM5Mjc4NTUsIDMyNi40Njc0NTMxMDYyMTI0LCAzMjguNjAzNTg2NTczMTQ2MjMsIDMzMC43Mzk3MjAwNDAwODAxNiwgMzMyLjg3NTg1MzUwNzAxNCwgMzM1LjAxMTk4Njk3Mzk0Nzg0LCAzMzcuMTQ4MTIwNDQwODgxNywgMzM5LjI4NDI1MzkwNzgxNTY0LCAzNDEuNDIwMzg3Mzc0NzQ5NSwgMzQzLjU1NjUyMDg0MTY4MzMsIDM0NS42OTI2NTQzMDg2MTcyLCAzNDcuODI4Nzg3Nzc1NTUxMSwgMzQ5Ljk2NDkyMTI0MjQ4NDkzLCAzNTIuMTAxMDU0NzA5NDE4OCwgMzU0LjIzNzE4ODE3NjM1MjczLCAzNTYuMzczMzIxNjQzMjg2NTQsIDM1OC41MDk0NTUxMTAyMjA0LCAzNjAuNjQ1NTg4NTc3MTU0MywgMzYyLjc4MTcyMjA0NDA4ODIsIDM2NC45MTc4NTU1MTEwMjIsIDM2Ny4wNTM5ODg5Nzc5NTU5LCAzNjkuMTkwMTIyNDQ0ODg5NzcsIDM3MS4zMjYyNTU5MTE4MjM2NCwgMzczLjQ2MjM4OTM3ODc1NzUsIDM3NS41OTg1MjI4NDU2OTE0LCAzNzcuNzM0NjU2MzEyNjI1MiwgMzc5Ljg3MDc4OTc3OTU1OTEsIDM4Mi4wMDY5MjMyNDY0OTMsIDM4NC4xNDMwNTY3MTM0MjY4LCAzODYuMjc5MTkwMTgwMzYwNywgMzg4LjQxNTMyMzY0NzI5NDYsIDM5MC41NTE0NTcxMTQyMjg0NywgMzkyLjY4NzU5MDU4MTE2MjMsIDM5NC44MjM3MjQwNDgwOTYxNSwgMzk2Ljk1OTg1NzUxNTAzMDEsIDM5OS4wOTU5OTA5ODE5NjM5LCA0MDEuMjMyMTI0NDQ4ODk3NzYsIDQwMy4zNjgyNTc5MTU4MzE2MywgNDA1LjUwNDM5MTM4Mjc2NTUsIDQwNy42NDA1MjQ4NDk2OTk0LCA0MDkuNzc2NjU4MzE2NjMzMjUsIDQxMS45MTI3OTE3ODM1NjcwNiwgNDE0LjA0ODkyNTI1MDUwMSwgNDE2LjE4NTA1ODcxNzQzNDg2LCA0MTguMzIxMTkyMTg0MzY4NywgNDIwLjQ1NzMyNTY1MTMwMjYsIDQyMi41OTM0NTkxMTgyMzY0NywgNDI0LjcyOTU5MjU4NTE3MDM0LCA0MjYuODY1NzI2MDUyMTA0MTUsIDQyOS4wMDE4NTk1MTkwMzgxLCA0MzEuMTM3OTkyOTg1OTcxOTUsIDQzMy4yNzQxMjY0NTI5MDU3NiwgNDM1LjQxMDI1OTkxOTgzOTYzLCA0MzcuNTQ2MzkzMzg2NzczNTYsIDQzOS42ODI1MjY4NTM3MDc0MywgNDQxLjgxODY2MDMyMDY0MTI0LCA0NDMuOTU0NzkzNzg3NTc1MSwgNDQ2LjA5MDkyNzI1NDUwOTA0LCA0NDguMjI3MDYwNzIxNDQyODUsIDQ1MC4zNjMxOTQxODgzNzY3LCA0NTIuNDk5MzI3NjU1MzEwNiwgNDU0LjYzNTQ2MTEyMjI0NDQ2LCA0NTYuNzcxNTk0NTg5MTc4MzMsIDQ1OC45MDc3MjgwNTYxMTIyLCA0NjEuMDQzODYxNTIzMDQ2LCA0NjMuMTc5OTk0OTg5OTc5OTUsIDQ2NS4zMTYxMjg0NTY5MTM4LCA0NjcuNDUyMjYxOTIzODQ3NywgNDY5LjU4ODM5NTM5MDc4MTUsIDQ3MS43MjQ1Mjg4NTc3MTU0LCA0NzMuODYwNjYyMzI0NjQ5MywgNDc1Ljk5Njc5NTc5MTU4MzEsIDQ3OC4xMzI5MjkyNTg1MTcsIDQ4MC4yNjkwNjI3MjU0NTA5LCA0ODIuNDA1MTk2MTkyMzg0NywgNDg0LjU0MTMyOTY1OTMxODYsIDQ4Ni42Nzc0NjMxMjYyNTI0NiwgNDg4LjgxMzU5NjU5MzE4NjMzLCA0OTAuOTQ5NzMwMDYwMTIwMiwgNDkzLjA4NTg2MzUyNzA1NDEsIDQ5NS4yMjE5OTY5OTM5ODgsIDQ5Ny4zNTgxMzA0NjA5MjE4LCA0OTkuNDk0MjYzOTI3ODU1NywgNTAxLjYzMDM5NzM5NDc4OTU1LCA1MDMuNzY2NTMwODYxNzIzNCwgNTA1LjkwMjY2NDMyODY1NzMsIDUwOC4wMzg3OTc3OTU1OTExNywgNTEwLjE3NDkzMTI2MjUyNSwgNTEyLjMxMTA2NDcyOTQ1ODgsIDUxNC40NDcxOTgxOTYzOTI3LCA1MTYuNTgzMzMxNjYzMzI2NiwgNTE4LjcxOTQ2NTEzMDI2MDUsIDUyMC44NTU1OTg1OTcxOTQzLCA1MjIuOTkxNzMyMDY0MTI4MiwgNTI1LjEyNzg2NTUzMTA2MjEsIDUyNy4yNjM5OTg5OTc5OTU5LCA1MjkuNDAwMTMyNDY0OTI5OCwgNTMxLjUzNjI2NTkzMTg2MzcsIDUzMy42NzIzOTkzOTg3OTc2LCA1MzUuODA4NTMyODY1NzMxNCwgNTM3Ljk0NDY2NjMzMjY2NTMsIDU0MC4wODA3OTk3OTk1OTkyLCA1NDIuMjE2OTMzMjY2NTMzLCA1NDQuMzUzMDY2NzMzNDY2OSwgNTQ2LjQ4OTIwMDIwMDQwMDgsIDU0OC42MjUzMzM2NjczMzQ1LCA1NTAuNzYxNDY3MTM0MjY4NSwgNTUyLjg5NzYwMDYwMTIwMjQsIDU1NS4wMzM3MzQwNjgxMzYxLCA1NTcuMTY5ODY3NTM1MDcwMSwgNTU5LjMwNjAwMTAwMjAwNCwgNTYxLjQ0MjEzNDQ2ODkzNzksIDU2My41NzgyNjc5MzU4NzE3LCA1NjUuNzE0NDAxNDAyODA1NiwgNTY3Ljg1MDUzNDg2OTczOTUsIDU2OS45ODY2NjgzMzY2NzMzLCA1NzIuMTIyODAxODAzNjA3MSwgNTc0LjI1ODkzNTI3MDU0MTEsIDU3Ni4zOTUwNjg3Mzc0NzUsIDU3OC41MzEyMDIyMDQ0MDg3LCA1ODAuNjY3MzM1NjcxMzQyNywgNTgyLjgwMzQ2OTEzODI3NjYsIDU4NC45Mzk2MDI2MDUyMTAzLCA1ODcuMDc1NzM2MDcyMTQ0MywgNTg5LjIxMTg2OTUzOTA3ODEsIDU5MS4zNDgwMDMwMDYwMTE5LCA1OTMuNDg0MTM2NDcyOTQ1OSwgNTk1LjYyMDI2OTkzOTg3OTcsIDU5Ny43NTY0MDM0MDY4MTM1LCA1OTkuODkyNTM2ODczNzQ3NSwgNjAyLjAyODY3MDM0MDY4MTMsIDYwNC4xNjQ4MDM4MDc2MTUyLCA2MDYuMzAwOTM3Mjc0NTQ5LCA2MDguNDM3MDcwNzQxNDgyOSwgNjEwLjU3MzIwNDIwODQxNjksIDYxMi43MDkzMzc2NzUzNTA2LCA2MTQuODQ1NDcxMTQyMjg0NSwgNjE2Ljk4MTYwNDYwOTIxODUsIDYxOS4xMTc3MzgwNzYxNTIyLCA2MjEuMjUzODcxNTQzMDg2MSwgNjIzLjM5MDAwNTAxMDAyLCA2MjUuNTI2MTM4NDc2OTUzOSwgNjI3LjY2MjI3MTk0Mzg4NzcsIDYyOS43OTg0MDU0MTA4MjE2LCA2MzEuOTM0NTM4ODc3NzU1NSwgNjM0LjA3MDY3MjM0NDY4OTMsIDYzNi4yMDY4MDU4MTE2MjMyLCA2MzguMzQyOTM5Mjc4NTU3MSwgNjQwLjQ3OTA3Mjc0NTQ5MSwgNjQyLjYxNTIwNjIxMjQyNDgsIDY0NC43NTEzMzk2NzkzNTg3LCA2NDYuODg3NDczMTQ2MjkyNSwgNjQ5LjAyMzYwNjYxMzIyNjQsIDY1MS4xNTk3NDAwODAxNjAzLCA2NTMuMjk1ODczNTQ3MDk0MSwgNjU1LjQzMjAwNzAxNDAyOCwgNjU3LjU2ODE0MDQ4MDk2MTksIDY1OS43MDQyNzM5NDc4OTU3LCA2NjEuODQwNDA3NDE0ODI5NywgNjYzLjk3NjU0MDg4MTc2MzQsIDY2Ni4xMTI2NzQzNDg2OTc0LCA2NjguMjQ4ODA3ODE1NjMxMywgNjcwLjM4NDk0MTI4MjU2NSwgNjcyLjUyMTA3NDc0OTQ5OSwgNjc0LjY1NzIwODIxNjQzMjksIDY3Ni43OTMzNDE2ODMzNjY2LCA2NzguOTI5NDc1MTUwMzAwNiwgNjgxLjA2NTYwODYxNzIzNDQsIDY4My4yMDE3NDIwODQxNjgyLCA2ODUuMzM3ODc1NTUxMTAyMiwgNjg3LjQ3NDAwOTAxODAzNiwgNjg5LjYxMDE0MjQ4NDk2OTksIDY5MS43NDYyNzU5NTE5MDM4LCA2OTMuODgyNDA5NDE4ODM3NiwgNjk2LjAxODU0Mjg4NTc3MTUsIDY5OC4xNTQ2NzYzNTI3MDU1LCA3MDAuMjkwODA5ODE5NjM5MiwgNzAyLjQyNjk0MzI4NjU3MzEsIDcwNC41NjMwNzY3NTM1MDcsIDcwNi42OTkyMTAyMjA0NDA4LCA3MDguODM1MzQzNjg3Mzc0NywgNzEwLjk3MTQ3NzE1NDMwODYsIDcxMy4xMDc2MTA2MjEyNDI0LCA3MTUuMjQzNzQ0MDg4MTc2NCwgNzE3LjM3OTg3NzU1NTExMDIsIDcxOS41MTYwMTEwMjIwNDQsIDcyMS42NTIxNDQ0ODg5Nzc5LCA3MjMuNzg4Mjc3OTU1OTExOCwgNzI1LjkyNDQxMTQyMjg0NTcsIDcyOC4wNjA1NDQ4ODk3Nzk1LCA3MzAuMTk2Njc4MzU2NzEzNCwgNzMyLjMzMjgxMTgyMzY0NzMsIDczNC40Njg5NDUyOTA1ODExLCA3MzYuNjA1MDc4NzU3NTE1LCA3MzguNzQxMjEyMjI0NDQ4OCwgNzQwLjg3NzM0NTY5MTM4MjcsIDc0My4wMTM0NzkxNTgzMTY2LCA3NDUuMTQ5NjEyNjI1MjUwNCwgNzQ3LjI4NTc0NjA5MjE4NDQsIDc0OS40MjE4Nzk1NTkxMTgyLCA3NTEuNTU4MDEzMDI2MDUyLCA3NTMuNjk0MTQ2NDkyOTg2LCA3NTUuODMwMjc5OTU5OTE5NywgNzU3Ljk2NjQxMzQyNjg1MzYsIDc2MC4xMDI1NDY4OTM3ODc2LCA3NjIuMjM4NjgwMzYwNzIxMywgNzY0LjM3NDgxMzgyNzY1NTMsIDc2Ni41MTA5NDcyOTQ1ODkyLCA3NjguNjQ3MDgwNzYxNTIzLCA3NzAuNzgzMjE0MjI4NDU2OSwgNzcyLjkxOTM0NzY5NTM5MDgsIDc3NS4wNTU0ODExNjIzMjQ2LCA3NzcuMTkxNjE0NjI5MjU4NSwgNzc5LjMyNzc0ODA5NjE5MjMsIDc4MS40NjM4ODE1NjMxMjYyLCA3ODMuNjAwMDE1MDMwMDYwMSwgNzg1LjczNjE0ODQ5Njk5MzksIDc4Ny44NzIyODE5NjM5Mjc4LCA3OTAuMDA4NDE1NDMwODYxOCwgNzkyLjE0NDU0ODg5Nzc5NTUsIDc5NC4yODA2ODIzNjQ3Mjk0LCA3OTYuNDE2ODE1ODMxNjYzMywgNzk4LjU1Mjk0OTI5ODU5NzEsIDgwMC42ODkwODI3NjU1MzEsIDgwMi44MjUyMTYyMzI0NjQ5LCA4MDQuOTYxMzQ5Njk5Mzk4NywgODA3LjA5NzQ4MzE2NjMzMjYsIDgwOS4yMzM2MTY2MzMyNjY1LCA4MTEuMzY5NzUwMTAwMjAwMywgODEzLjUwNTg4MzU2NzEzNDEsIDgxNS42NDIwMTcwMzQwNjgxLCA4MTcuNzc4MTUwNTAxMDAyLCA4MTkuOTE0MjgzOTY3OTM1OCwgODIyLjA1MDQxNzQzNDg2OTcsIDgyNC4xODY1NTA5MDE4MDM2LCA4MjYuMzIyNjg0MzY4NzM3NCwgODI4LjQ1ODgxNzgzNTY3MTMsIDgzMC41OTQ5NTEzMDI2MDUyLCA4MzIuNzMxMDg0NzY5NTM5LCA4MzQuODY3MjE4MjM2NDcyOSwgODM3LjAwMzM1MTcwMzQwNjcsIDgzOS4xMzk0ODUxNzAzNDA3LCA4NDEuMjc1NjE4NjM3Mjc0NSwgODQzLjQxMTc1MjEwNDIwODMsIDg0NS41NDc4ODU1NzExNDIzLCA4NDcuNjg0MDE5MDM4MDc2MSwgODQ5LjgyMDE1MjUwNTAwOTksIDg1MS45NTYyODU5NzE5NDM5LCA4NTQuMDkyNDE5NDM4ODc3NiwgODU2LjIyODU1MjkwNTgxMTUsIDg1OC4zNjQ2ODYzNzI3NDU1LCA4NjAuNTAwODE5ODM5Njc5MywgODYyLjYzNjk1MzMwNjYxMzEsIDg2NC43NzMwODY3NzM1NDcxLCA4NjYuOTA5MjIwMjQwNDgwOSwgODY5LjA0NTM1MzcwNzQxNDgsIDg3MS4xODE0ODcxNzQzNDg2LCA4NzMuMzE3NjIwNjQxMjgyNSwgODc1LjQ1Mzc1NDEwODIxNjUsIDg3Ny41ODk4ODc1NzUxNTAyLCA4NzkuNzI2MDIxMDQyMDg0MSwgODgxLjg2MjE1NDUwOTAxODEsIDg4My45OTgyODc5NzU5NTE4LCA4ODYuMTM0NDIxNDQyODg1NywgODg4LjI3MDU1NDkwOTgxOTYsIDg5MC40MDY2ODgzNzY3NTM0LCA4OTIuNTQyODIxODQzNjg3MywgODk0LjY3ODk1NTMxMDYyMTIsIDg5Ni44MTUwODg3Nzc1NTUsIDg5OC45NTEyMjIyNDQ0ODg5LCA5MDEuMDg3MzU1NzExNDIyOCwgOTAzLjIyMzQ4OTE3ODM1NjcsIDkwNS4zNTk2MjI2NDUyOTA1LCA5MDcuNDk1NzU2MTEyMjI0NCwgOTA5LjYzMTg4OTU3OTE1ODMsIDkxMS43NjgwMjMwNDYwOTIsIDkxMy45MDQxNTY1MTMwMjYsIDkxNi4wNDAyODk5Nzk5NTk5LCA5MTguMTc2NDIzNDQ2ODkzNiwgOTIwLjMxMjU1NjkxMzgyNzYsIDkyMi40NDg2OTAzODA3NjE1LCA5MjQuNTg0ODIzODQ3Njk1NCwgOTI2LjcyMDk1NzMxNDYyOTIsIDkyOC44NTcwOTA3ODE1NjMsIDkzMC45OTMyMjQyNDg0OTcsIDkzMy4xMjkzNTc3MTU0MzA4LCA5MzUuMjY1NDkxMTgyMzY0NiwgOTM3LjQwMTYyNDY0OTI5ODYsIDkzOS41Mzc3NTgxMTYyMzI1LCA5NDEuNjczODkxNTgzMTY2MiwgOTQzLjgxMDAyNTA1MDEwMDIsIDk0NS45NDYxNTg1MTcwMzQsIDk0OC4wODIyOTE5ODM5Njc4LCA5NTAuMjE4NDI1NDUwOTAxOCwgOTUyLjM1NDU1ODkxNzgzNTYsIDk1NC40OTA2OTIzODQ3Njk0LCA5NTYuNjI2ODI1ODUxNzAzNCwgOTU4Ljc2Mjk1OTMxODYzNzIsIDk2MC44OTkwOTI3ODU1NzEsIDk2My4wMzUyMjYyNTI1MDQ5LCA5NjUuMTcxMzU5NzE5NDM4OCwgOTY3LjMwNzQ5MzE4NjM3MjcsIDk2OS40NDM2MjY2NTMzMDY1LCA5NzEuNTc5NzYwMTIwMjQwNCwgOTczLjcxNTg5MzU4NzE3NDQsIDk3NS44NTIwMjcwNTQxMDgxLCA5NzcuOTg4MTYwNTIxMDQyLCA5ODAuMTI0MjkzOTg3OTc2LCA5ODIuMjYwNDI3NDU0OTA5NywgOTg0LjM5NjU2MDkyMTg0MzYsIDk4Ni41MzI2OTQzODg3Nzc1LCA5ODguNjY4ODI3ODU1NzExNCwgOTkwLjgwNDk2MTMyMjY0NTIsIDk5Mi45NDEwOTQ3ODk1NzkxLCA5OTUuMDc3MjI4MjU2NTEzLCA5OTcuMjEzMzYxNzIzNDQ2OCwgOTk5LjM0OTQ5NTE5MDM4MDcsIDEwMDEuNDg1NjI4NjU3MzE0NiwgMTAwMy42MjE3NjIxMjQyNDgzLCAxMDA1Ljc1Nzg5NTU5MTE4MjMsIDEwMDcuODk0MDI5MDU4MTE2MiwgMTAxMC4wMzAxNjI1MjUwNSwgMTAxMi4xNjYyOTU5OTE5ODM5LCAxMDE0LjMwMjQyOTQ1ODkxNzgsIDEwMTYuNDM4NTYyOTI1ODUxNiwgMTAxOC41NzQ2OTYzOTI3ODU1LCAxMDIwLjcxMDgyOTg1OTcxOTMsIDEwMjIuODQ2OTYzMzI2NjUzMiwgMTAyNC45ODMwOTY3OTM1ODcsIDEwMjcuMTE5MjMwMjYwNTIxLCAxMDI5LjI1NTM2MzcyNzQ1NDgsIDEwMzEuMzkxNDk3MTk0Mzg4NiwgMTAzMy41Mjc2MzA2NjEzMjI1LCAxMDM1LjY2Mzc2NDEyODI1NjQsIDEwMzcuNzk5ODk3NTk1MTkwMywgMTAzOS45MzYwMzEwNjIxMjQxLCAxMDQyLjA3MjE2NDUyOTA1OCwgMTA0NC4yMDgyOTc5OTU5OTE5LCAxMDQ2LjM0NDQzMTQ2MjkyNTcsIDEwNDguNDgwNTY0OTI5ODU5NiwgMTA1MC42MTY2OTgzOTY3OTM1LCAxMDUyLjc1MjgzMTg2MzcyNzQsIDEwNTQuODg4OTY1MzMwNjYxMiwgMTA1Ny4wMjUwOTg3OTc1OTUsIDEwNTkuMTYxMjMyMjY0NTI5LCAxMDYxLjI5NzM2NTczMTQ2MjgsIDEwNjMuNDMzNDk5MTk4Mzk2NywgMTA2NS41Njk2MzI2NjUzMzA2LCAxMDY3LjcwNTc2NjEzMjI2NDQsIDEwNjkuODQxODk5NTk5MTk4MywgMTA3MS45NzgwMzMwNjYxMzIyLCAxMDc0LjExNDE2NjUzMzA2NiwgMTA3Ni4yNTAzXSkKICAgICAgICAgICAgICAucmFuZ2UoWycjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnXSk7CiAgICAKCiAgICBjb2xvcl9tYXBfOTQwNjJiMTY0MGFjNDIyZTk2Mjc2MWYxYTg3OTJhMzcueCA9IGQzLnNjYWxlLmxpbmVhcigpCiAgICAgICAgICAgICAgLmRvbWFpbihbMTAuMzE5NywgMTA3Ni4yNTAzXSkKICAgICAgICAgICAgICAucmFuZ2UoWzAsIDQwMF0pOwoKICAgIGNvbG9yX21hcF85NDA2MmIxNjQwYWM0MjJlOTYyNzYxZjFhODc5MmEzNy5sZWdlbmQgPSBMLmNvbnRyb2woe3Bvc2l0aW9uOiAndG9wcmlnaHQnfSk7CiAgICBjb2xvcl9tYXBfOTQwNjJiMTY0MGFjNDIyZTk2Mjc2MWYxYTg3OTJhMzcubGVnZW5kLm9uQWRkID0gZnVuY3Rpb24gKG1hcCkge3ZhciBkaXYgPSBMLkRvbVV0aWwuY3JlYXRlKCdkaXYnLCAnbGVnZW5kJyk7IHJldHVybiBkaXZ9OwogICAgY29sb3JfbWFwXzk0MDYyYjE2NDBhYzQyMmU5NjI3NjFmMWE4NzkyYTM3LmxlZ2VuZC5hZGRUbyhtYXBfYjY4ZDE2ZDc0MGUwNDc4Yzk3Njg5NDk2MTIwMmIwZDEpOwoKICAgIGNvbG9yX21hcF85NDA2MmIxNjQwYWM0MjJlOTYyNzYxZjFhODc5MmEzNy54QXhpcyA9IGQzLnN2Zy5heGlzKCkKICAgICAgICAuc2NhbGUoY29sb3JfbWFwXzk0MDYyYjE2NDBhYzQyMmU5NjI3NjFmMWE4NzkyYTM3LngpCiAgICAgICAgLm9yaWVudCgidG9wIikKICAgICAgICAudGlja1NpemUoMSkKICAgICAgICAudGlja1ZhbHVlcyhbMTAuMzE5NywgMTg3Ljk3NDgsIDM2NS42Mjk4OTk5OTk5OTk5NiwgNTQzLjI4NSwgNzIwLjk0MDA5OTk5OTk5OTksIDg5OC41OTUxOTk5OTk5OTk5LCAxMDc2LjI1MDNdKTsKCiAgICBjb2xvcl9tYXBfOTQwNjJiMTY0MGFjNDIyZTk2Mjc2MWYxYTg3OTJhMzcuc3ZnID0gZDMuc2VsZWN0KCIubGVnZW5kLmxlYWZsZXQtY29udHJvbCIpLmFwcGVuZCgic3ZnIikKICAgICAgICAuYXR0cigiaWQiLCAnbGVnZW5kJykKICAgICAgICAuYXR0cigid2lkdGgiLCA0NTApCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDQwKTsKCiAgICBjb2xvcl9tYXBfOTQwNjJiMTY0MGFjNDIyZTk2Mjc2MWYxYTg3OTJhMzcuZyA9IGNvbG9yX21hcF85NDA2MmIxNjQwYWM0MjJlOTYyNzYxZjFhODc5MmEzNy5zdmcuYXBwZW5kKCJnIikKICAgICAgICAuYXR0cigiY2xhc3MiLCAia2V5IikKICAgICAgICAuYXR0cigidHJhbnNmb3JtIiwgInRyYW5zbGF0ZSgyNSwxNikiKTsKCiAgICBjb2xvcl9tYXBfOTQwNjJiMTY0MGFjNDIyZTk2Mjc2MWYxYTg3OTJhMzcuZy5zZWxlY3RBbGwoInJlY3QiKQogICAgICAgIC5kYXRhKGNvbG9yX21hcF85NDA2MmIxNjQwYWM0MjJlOTYyNzYxZjFhODc5MmEzNy5jb2xvci5yYW5nZSgpLm1hcChmdW5jdGlvbihkLCBpKSB7CiAgICAgICAgICByZXR1cm4gewogICAgICAgICAgICB4MDogaSA/IGNvbG9yX21hcF85NDA2MmIxNjQwYWM0MjJlOTYyNzYxZjFhODc5MmEzNy54KGNvbG9yX21hcF85NDA2MmIxNjQwYWM0MjJlOTYyNzYxZjFhODc5MmEzNy5jb2xvci5kb21haW4oKVtpIC0gMV0pIDogY29sb3JfbWFwXzk0MDYyYjE2NDBhYzQyMmU5NjI3NjFmMWE4NzkyYTM3LngucmFuZ2UoKVswXSwKICAgICAgICAgICAgeDE6IGkgPCBjb2xvcl9tYXBfOTQwNjJiMTY0MGFjNDIyZTk2Mjc2MWYxYTg3OTJhMzcuY29sb3IuZG9tYWluKCkubGVuZ3RoID8gY29sb3JfbWFwXzk0MDYyYjE2NDBhYzQyMmU5NjI3NjFmMWE4NzkyYTM3LngoY29sb3JfbWFwXzk0MDYyYjE2NDBhYzQyMmU5NjI3NjFmMWE4NzkyYTM3LmNvbG9yLmRvbWFpbigpW2ldKSA6IGNvbG9yX21hcF85NDA2MmIxNjQwYWM0MjJlOTYyNzYxZjFhODc5MmEzNy54LnJhbmdlKClbMV0sCiAgICAgICAgICAgIHo6IGQKICAgICAgICAgIH07CiAgICAgICAgfSkpCiAgICAgIC5lbnRlcigpLmFwcGVuZCgicmVjdCIpCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDEwKQogICAgICAgIC5hdHRyKCJ4IiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC54MDsgfSkKICAgICAgICAuYXR0cigid2lkdGgiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLngxIC0gZC54MDsgfSkKICAgICAgICAuc3R5bGUoImZpbGwiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLno7IH0pOwoKICAgIGNvbG9yX21hcF85NDA2MmIxNjQwYWM0MjJlOTYyNzYxZjFhODc5MmEzNy5nLmNhbGwoY29sb3JfbWFwXzk0MDYyYjE2NDBhYzQyMmU5NjI3NjFmMWE4NzkyYTM3LnhBeGlzKS5hcHBlbmQoInRleHQiKQogICAgICAgIC5hdHRyKCJjbGFzcyIsICJjYXB0aW9uIikKICAgICAgICAuYXR0cigieSIsIDIxKQogICAgICAgIC50ZXh0KCcnKTsKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
df_N = df2[df2["수준지수(서울특별시=100)"]<130]
```


```python
map = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='Stamen Toner')
map.choropleth(geo_str, data = df_N, columns =["지역", "수준지수(서울특별시=100)"], fill_color='PuRd', #PuRd, YlGnBu
              key_on='feature.id')
map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVM9ZmFsc2U7IExfTk9fVE9VQ0g9ZmFsc2U7IExfRElTQUJMRV8zRD1mYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgPHN0eWxlPiNtYXBfNTA0NmJlOTk4ZjliNDdmNjhjNGE3MjBkOWNiNTFlZDggewogICAgICAgIHBvc2l0aW9uOiByZWxhdGl2ZTsKICAgICAgICB3aWR0aDogMTAwLjAlOwogICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgdG9wOiAwLjAlOwogICAgICAgIH0KICAgIDwvc3R5bGU+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvZDMvMy41LjUvZDMubWluLmpzIj48L3NjcmlwdD4KPC9oZWFkPgo8Ym9keT4gICAgCiAgICAKICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfNTA0NmJlOTk4ZjliNDdmNjhjNGE3MjBkOWNiNTFlZDgiID48L2Rpdj4KPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgCiAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAKCiAgICB2YXIgbWFwXzUwNDZiZTk5OGY5YjQ3ZjY4YzRhNzIwZDljYjUxZWQ4ID0gTC5tYXAoCiAgICAgICAgJ21hcF81MDQ2YmU5OThmOWI0N2Y2OGM0YTcyMGQ5Y2I1MWVkOCcsIHsKICAgICAgICBjZW50ZXI6IFszNy41NTAyLCAxMjYuOTgyXSwKICAgICAgICB6b29tOiAxMSwKICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICBsYXllcnM6IFtdLAogICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcsCiAgICAgICAgem9vbUNvbnRyb2w6IHRydWUsCiAgICAgICAgfSk7CgogICAgCiAgICAKICAgIHZhciB0aWxlX2xheWVyX2Y0MGRjYTczZTVmYTRlZGViZGVkOGFkZDFmYTAyYWM5ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgJ2h0dHBzOi8vc3RhbWVuLXRpbGVzLXtzfS5hLnNzbC5mYXN0bHkubmV0L3RvbmVyL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgewogICAgICAgICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgICAgICAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICAgICAgICJtYXhOYXRpdmVab29tIjogMTgsCiAgICAgICAgIm1heFpvb20iOiAxOCwKICAgICAgICAibWluWm9vbSI6IDAsCiAgICAgICAgIm5vV3JhcCI6IGZhbHNlLAogICAgICAgICJzdWJkb21haW5zIjogImFiYyIKfSkuYWRkVG8obWFwXzUwNDZiZTk5OGY5YjQ3ZjY4YzRhNzIwZDljYjUxZWQ4KTsKICAgIAogICAgICAgIAogICAgICAgIHZhciBnZW9fanNvbl84Njc4Yzc4MTA4MDE0YzNkOGNkNGExNTdhMzg1MTk1MyA9IEwuZ2VvSnNvbigKICAgICAgICAgICAgeyJmZWF0dXJlcyI6IFt7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XSwgWzEyNy4xNjY4MzE4NDM2NjEyOSwgMzcuNTc2NzI0ODczODg2MjddLCBbMTI3LjE4NDA4NzkyMzMwMTUyLCAzNy41NTgxNDI4MDM2OTU3NV0sIFsxMjcuMTY1MzA5ODQzMDc0NDcsIDM3LjU0MjIxODUxMjU4NjkzXSwgWzEyNy4xNDY3MjgwNjgyMzUwMiwgMzcuNTE0MTU2ODA2ODAyOTFdLCBbMTI3LjEyMTIzMTY1NzE5NjE1LCAzNy41MjUyODI3MDA4OV0sIFsxMjcuMTExNjc2NDIwMzYwOCwgMzcuNTQwNjY5OTU1MzI0OTY1XSwgWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFjMTVcdWIzZDlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTI1MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhYzE1XHViM2Q5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkdhbmdkb25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2Q0YjlkYSIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl0sIFsxMjcuMTAwODc1MTk3OTE5NjIsIDM3LjUyNDg0MTIyMDE2NzA1NV0sIFsxMjcuMTExNjc2NDIwMzYwOCwgMzcuNTQwNjY5OTU1MzI0OTY1XSwgWzEyNy4xMjEyMzE2NTcxOTYxNSwgMzcuNTI1MjgyNzAwODldLCBbMTI3LjE0NjcyODA2ODIzNTAyLCAzNy41MTQxNTY4MDY4MDI5MV0sIFsxMjcuMTYzNDk0NDIxNTc2NSwgMzcuNDk3NDQ1NDA2MDk3NDg0XSwgWzEyNy4xNDIwNjA1ODQxMzI3NCwgMzcuNDcwODk4MTkwOTg1MDFdLCBbMTI3LjEyNDQwNTcxMDgwODkzLCAzNy40NjI0MDQ0NTU4NzA0OF0sIFsxMjcuMTExMTcwODUyMDEyMzgsIDM3LjQ4NTcwODM4MTUxMjQ0NV0sIFsxMjcuMDcxOTE0NjAwMDcyNCwgMzcuNTAyMjQwMTM1ODc2NjldLCBbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMWExXHVkMzBjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEyNDAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzFhMVx1ZDMwY1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJTb25ncGEtZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZTcyOThhIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XSwgWzEyNy4wNjkwNjk4MTMwMzcyLCAzNy41MjIyNzk0MjM1MDUwMjZdLCBbMTI3LjA3MTkxNDYwMDA3MjQsIDM3LjUwMjI0MDEzNTg3NjY5XSwgWzEyNy4xMTExNzA4NTIwMTIzOCwgMzcuNDg1NzA4MzgxNTEyNDQ1XSwgWzEyNy4xMjQ0MDU3MTA4MDg5MywgMzcuNDYyNDA0NDU1ODcwNDhdLCBbMTI3LjA5ODQyNzU5MzE4NzUxLCAzNy40NTg2MjI1Mzg1NzQ2MV0sIFsxMjcuMDg2NDA0NDA1NzgxNTYsIDM3LjQ3MjY5NzkzNTE4NDY1NV0sIFsxMjcuMDU1OTE3MDQ4MTkwNCwgMzcuNDY1OTIyODkxNDA3N10sIFsxMjcuMDM2MjE5MTUwOTg3OTgsIDM3LjQ4MTc1ODAyNDI3NjAzXSwgWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldLCBbMTI3LjAyMzAyODMxODkwNTU5LCAzNy41MzIzMTg5OTU4MjY2M10sIFsxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFjMTVcdWIwYThcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIzMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhYzE1XHViMGE4XHVhZDZjIiwgIm5hbWVfZW5nIjogIkdhbmduYW0tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjOTEwMDNmIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDEzOTcxMTk2Njc1MTMsIDM3LjUyNTAzOTg4Mjg5NjY5XSwgWzEyNy4wMzYyMTkxNTA5ODc5OCwgMzcuNDgxNzU4MDI0Mjc2MDNdLCBbMTI3LjA1NTkxNzA0ODE5MDQsIDM3LjQ2NTkyMjg5MTQwNzddLCBbMTI3LjA4NjQwNDQwNTc4MTU2LCAzNy40NzI2OTc5MzUxODQ2NTVdLCBbMTI3LjA5ODQyNzU5MzE4NzUxLCAzNy40NTg2MjI1Mzg1NzQ2MV0sIFsxMjcuMDkwNDY5Mjg1NjU5NTEsIDM3LjQ0Mjk2ODI2MTE0MTg1XSwgWzEyNy4wNjc3ODEwNzYwNTQzMywgMzcuNDI2MTk3NDI0MDU3MzE0XSwgWzEyNy4wNDk1NzIzMjk4NzE0MiwgMzcuNDI4MDU4MzY4NDU2OTRdLCBbMTI3LjAzODgxNzgyNTk3OTIyLCAzNy40NTM4MjAzOTg1MTcxNV0sIFsxMjYuOTkwNzIwNzMxOTU0NjIsIDM3LjQ1NTMyNjE0MzMxMDAyNV0sIFsxMjYuOTgzNjc2NjgyOTE4MDIsIDM3LjQ3Mzg1NjQ5MjY5MjA4Nl0sIFsxMjYuOTgyMjM4MDc5MTYwODEsIDM3LjUwOTMxNDk2Njc3MDMyNl0sIFsxMjcuMDEzOTcxMTk2Njc1MTMsIDM3LjUyNTAzOTg4Mjg5NjY5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWMxMWNcdWNkMDhcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIyMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjMTFjXHVjZDA4XHVhZDZjIiwgIm5hbWVfZW5nIjogIlNlb2Noby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiM5MTAwM2YiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45ODM2NzY2ODI5MTgwMiwgMzcuNDczODU2NDkyNjkyMDg2XSwgWzEyNi45OTA3MjA3MzE5NTQ2MiwgMzcuNDU1MzI2MTQzMzEwMDI1XSwgWzEyNi45NjUyMDQzOTA4NTE0MywgMzcuNDM4MjQ5Nzg0MDA2MjQ2XSwgWzEyNi45NTAwMDAwMTAxMDE4MiwgMzcuNDM2MTM0NTExNjU3MTldLCBbMTI2LjkzMDg0NDA4MDU2NTI1LCAzNy40NDczODI5MjgzMzM5OTRdLCBbMTI2LjkxNjc3MjgxNDY2MDEsIDM3LjQ1NDkwNTY2NDIzNzg5XSwgWzEyNi45MDE1NjA5NDEyOTg5NSwgMzcuNDc3NTM4NDI3ODk5MDFdLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuOTQ5MjI2NjEzODk1MDgsIDM3LjQ5MTI1NDM3NDk1NjQ5XSwgWzEyNi45NzI1ODkxODUwNjYyLCAzNy40NzI1NjEzNjMyNzgxMjVdLCBbMTI2Ljk4MzY3NjY4MjkxODAyLCAzNy40NzM4NTY0OTI2OTIwODZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWQwMFx1YzU0NVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMjEwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFkMDBcdWM1NDVcdWFkNmMiLCAibmFtZV9lbmciOiAiR3dhbmFrLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YxZWVmNiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk4MjIzODA3OTE2MDgxLCAzNy41MDkzMTQ5NjY3NzAzMjZdLCBbMTI2Ljk4MzY3NjY4MjkxODAyLCAzNy40NzM4NTY0OTI2OTIwODZdLCBbMTI2Ljk3MjU4OTE4NTA2NjIsIDM3LjQ3MjU2MTM2MzI3ODEyNV0sIFsxMjYuOTQ5MjI2NjEzODk1MDgsIDM3LjQ5MTI1NDM3NDk1NjQ5XSwgWzEyNi45MDUzMTk3NTgwMTgxMiwgMzcuNDgyMTgwODc1NzU0MjldLCBbMTI2LjkyMTc3ODkzMTc0ODI1LCAzNy40OTQ4ODk4Nzc0MTUxNzZdLCBbMTI2LjkyODEwNjI4ODI4Mjc5LCAzNy41MTMyOTU5NTczMjAxNV0sIFsxMjYuOTUyNDk5OTAyOTgxNTksIDM3LjUxNzIyNTAwNzQxODEzXSwgWzEyNi45ODIyMzgwNzkxNjA4MSwgMzcuNTA5MzE0OTY2NzcwMzI2XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIzZDlcdWM3OTFcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIwMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViM2Q5XHVjNzkxXHVhZDZjIiwgIm5hbWVfZW5nIjogIkRvbmdqYWstZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZjFlZWY2IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuODkxODQ2NjM4NjI3NjQsIDM3LjU0NzM3Mzk3NDk5NzExNF0sIFsxMjYuOTQ1NjY3MzMwODMyMTIsIDM3LjUyNjYxNzU0MjQ1MzM2Nl0sIFsxMjYuOTUyNDk5OTAyOTgxNTksIDM3LjUxNzIyNTAwNzQxODEzXSwgWzEyNi45MjgxMDYyODgyODI3OSwgMzcuNTEzMjk1OTU3MzIwMTVdLCBbMTI2LjkyMTc3ODkzMTc0ODI1LCAzNy40OTQ4ODk4Nzc0MTUxNzZdLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuODk1OTQ3NzY3ODI0ODUsIDM3LjUwNDY3NTI4MTMwOTE3Nl0sIFsxMjYuODgxNTY0MDIzNTM4NjIsIDM3LjUxMzk3MDAzNDc2NTY4NF0sIFsxMjYuODg4MjU3NTc4NjAwOTksIDM3LjU0MDc5NzMzNjMwMjMyXSwgWzEyNi44OTE4NDY2Mzg2Mjc2NCwgMzcuNTQ3MzczOTc0OTk3MTE0XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWM2MDFcdWI0ZjFcdWQzZWNcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTE5MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjNjAxXHViNGYxXHVkM2VjXHVhZDZjIiwgIm5hbWVfZW5nIjogIlllb25nZGV1bmdwby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiM5MTAwM2YiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45MDE1NjA5NDEyOTg5NSwgMzcuNDc3NTM4NDI3ODk5MDFdLCBbMTI2LjkxNjc3MjgxNDY2MDEsIDM3LjQ1NDkwNTY2NDIzNzg5XSwgWzEyNi45MzA4NDQwODA1NjUyNSwgMzcuNDQ3MzgyOTI4MzMzOTk0XSwgWzEyNi45MDI1ODMxNzExNjk3LCAzNy40MzQ1NDkzNjYzNDkxMjRdLCBbMTI2Ljg3NjgzMjcxNTAyNDI4LCAzNy40ODI1NzY1OTE2MDczMDVdLCBbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZTA4XHVjYzljXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExODAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWUwOFx1Y2M5Y1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJHZXVtY2hlb24tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjOTEwMDNmIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuODI2ODgwODE1MTczMTQsIDM3LjUwNTQ4OTcyMjMyODk2XSwgWzEyNi44ODE1NjQwMjM1Mzg2MiwgMzcuNTEzOTcwMDM0NzY1Njg0XSwgWzEyNi44OTU5NDc3Njc4MjQ4NSwgMzcuNTA0Njc1MjgxMzA5MTc2XSwgWzEyNi45MDUzMTk3NTgwMTgxMiwgMzcuNDgyMTgwODc1NzU0MjldLCBbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV0sIFsxMjYuODc2ODMyNzE1MDI0MjgsIDM3LjQ4MjU3NjU5MTYwNzMwNV0sIFsxMjYuODQ3NjI2NzYwNTQ5NTMsIDM3LjQ3MTQ2NzIzOTM2MzIzXSwgWzEyNi44MzU0OTQ4NTA3NjE5NiwgMzcuNDc0MDk4MjM2OTc1MDk1XSwgWzEyNi44MjI2NDc5Njc5MTM0OCwgMzcuNDg3ODQ3NjQ5MjE0N10sIFsxMjYuODI1MDQ3MzYzMzE0MDYsIDM3LjUwMzAyNjEyNjQwNDQzXSwgWzEyNi44MjY4ODA4MTUxNzMxNCwgMzcuNTA1NDg5NzIyMzI4OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWQ2Y1x1Yjg1Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTcwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFkNmNcdWI4NWNcdWFkNmMiLCAibmFtZV9lbmciOiAiR3Vyby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNkZjY1YjAiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi43OTU3NTc2ODU1MjkwNywgMzcuNTc4ODEwODc2MzMyMDJdLCBbMTI2LjgwNzAyMTE1MDIzNTk3LCAzNy42MDEyMzAwMTAxMzIyOF0sIFsxMjYuODIyNTE0Mzg0NzcxMDUsIDM3LjU4ODA0MzA4MTAwODJdLCBbMTI2Ljg1OTg0MTk5Mzk5NjY3LCAzNy41NzE4NDc4NTUyOTI3NDVdLCBbMTI2Ljg5MTg0NjYzODYyNzY0LCAzNy41NDczNzM5NzQ5OTcxMTRdLCBbMTI2Ljg4ODI1NzU3ODYwMDk5LCAzNy41NDA3OTczMzYzMDIzMl0sIFsxMjYuODY2Mzc0NjQzMjEyMzgsIDM3LjU0ODU5MTkxMDk0ODIzXSwgWzEyNi44NjYxMDA3MzQ3NjM5NSwgMzcuNTI2OTk5NjQxNDQ2NjldLCBbMTI2Ljg0MjU3MjkxOTQzMTUzLCAzNy41MjM3MzcwNzgwNTU5Nl0sIFsxMjYuODI0MjMzMTQyNjcyMiwgMzcuNTM3ODgwNzg3NTMyNDhdLCBbMTI2Ljc3MzI0NDE3NzE3NzAzLCAzNy41NDU5MTIzNDUwNTU0XSwgWzEyNi43Njk3OTE4MDU3OTM1MiwgMzcuNTUxMzkxODMwMDg4MDldLCBbMTI2Ljc5NTc1NzY4NTUyOTA3LCAzNy41Nzg4MTA4NzYzMzIwMl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhYzE1XHVjMTFjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExNjAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWMxNVx1YzExY1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJHYW5nc2VvLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2Q0YjlkYSIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2LjgyNDIzMzE0MjY3MjIsIDM3LjUzNzg4MDc4NzUzMjQ4XSwgWzEyNi44NDI1NzI5MTk0MzE1MywgMzcuNTIzNzM3MDc4MDU1OTZdLCBbMTI2Ljg2NjEwMDczNDc2Mzk1LCAzNy41MjY5OTk2NDE0NDY2OV0sIFsxMjYuODY2Mzc0NjQzMjEyMzgsIDM3LjU0ODU5MTkxMDk0ODIzXSwgWzEyNi44ODgyNTc1Nzg2MDA5OSwgMzcuNTQwNzk3MzM2MzAyMzJdLCBbMTI2Ljg4MTU2NDAyMzUzODYyLCAzNy41MTM5NzAwMzQ3NjU2ODRdLCBbMTI2LjgyNjg4MDgxNTE3MzE0LCAzNy41MDU0ODk3MjIzMjg5Nl0sIFsxMjYuODI0MjMzMTQyNjcyMiwgMzcuNTM3ODgwNzg3NTMyNDhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzU5MVx1Y2M5Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTUwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM1OTFcdWNjOWNcdWFkNmMiLCAibmFtZV9lbmciOiAiWWFuZ2NoZW9uLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2YxZWVmNiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2LjkwNTIyMDY1ODMxMDUzLCAzNy41NzQwOTcwMDUyMjU3NF0sIFsxMjYuOTM4OTgxNjE3OTg5NzMsIDM3LjU1MjMxMDAwMzcyODEyNF0sIFsxMjYuOTYzNTgyMjY3MTA4MTIsIDM3LjU1NjA1NjM1NDc1MTU0XSwgWzEyNi45NjQ0ODU3MDU1MzA1NSwgMzcuNTQ4NzA1NjkyMDIxNjM1XSwgWzEyNi45NDU2NjczMzA4MzIxMiwgMzcuNTI2NjE3NTQyNDUzMzY2XSwgWzEyNi44OTE4NDY2Mzg2Mjc2NCwgMzcuNTQ3MzczOTc0OTk3MTE0XSwgWzEyNi44NTk4NDE5OTM5OTY2NywgMzcuNTcxODQ3ODU1MjkyNzQ1XSwgWzEyNi44ODQzMzI4NDc3MzI4OCwgMzcuNTg4MTQzMzIyODgwNTI2XSwgWzEyNi45MDUyMjA2NTgzMTA1MywgMzcuNTc0MDk3MDA1MjI1NzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YjljOFx1ZDNlY1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTQwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWI5YzhcdWQzZWNcdWFkNmMiLCAibmFtZV9lbmciOiAiTWFwby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNjZTEyNTYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTU1NjU0MjU4NDY0NjMsIDM3LjU3NjA4MDc5MDg4MTQ1Nl0sIFsxMjYuOTY4NzM2MzMyNzkwNzUsIDM3LjU2MzEzNjA0NjkwODI3XSwgWzEyNi45NjM1ODIyNjcxMDgxMiwgMzcuNTU2MDU2MzU0NzUxNTRdLCBbMTI2LjkzODk4MTYxNzk4OTczLCAzNy41NTIzMTAwMDM3MjgxMjRdLCBbMTI2LjkwNTIyMDY1ODMxMDUzLCAzNy41NzQwOTcwMDUyMjU3NF0sIFsxMjYuOTUyNDc1MjAzMDU3MiwgMzcuNjA1MDg2OTI3MzcwNDVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzExY1x1YjMwMFx1YmIzOFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTMwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWMxMWNcdWIzMDBcdWJiMzhcdWFkNmMiLCAibmFtZV9lbmciOiAiU2VvZGFlbXVuLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M5OTRjNyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk3Mzg4NjQxMjg3MDIsIDM3LjYyOTQ5NjM0Nzg2ODg4XSwgWzEyNi45NTQyNzAxNzAwNjEyOSwgMzcuNjIyMDMzNDMxMzM5NDI1XSwgWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTA1MjIwNjU4MzEwNTMsIDM3LjU3NDA5NzAwNTIyNTc0XSwgWzEyNi44ODQzMzI4NDc3MzI4OCwgMzcuNTg4MTQzMzIyODgwNTI2XSwgWzEyNi45MDM5NjY4MTAwMzU5NSwgMzcuNTkyMjc0MDM0MTk5NDJdLCBbMTI2LjkwMzAzMDY2MTc3NjY4LCAzNy42MDk5Nzc5MTE0MDEzNDRdLCBbMTI2LjkxNDU1NDgxNDI5NjQ4LCAzNy42NDE1MDA1MDk5NjkzNV0sIFsxMjYuOTU2NDczNzk3Mzg3LCAzNy42NTI0ODA3MzczMzk0NDVdLCBbMTI2Ljk3Mzg4NjQxMjg3MDIsIDM3LjYyOTQ5NjM0Nzg2ODg4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWM3NDBcdWQzYzlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTEyMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjNzQwXHVkM2M5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkV1bnB5ZW9uZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wODM4NzUyNzAzMTk1LCAzNy42OTM1OTUzNDIwMjAzNF0sIFsxMjcuMDk3MDYzOTEzMDk2OTUsIDM3LjY4NjM4MzcxOTM3MjI5NF0sIFsxMjcuMDk0NDA3NjYyOTg3MTcsIDM3LjY0NzEzNDkwNDczMDQ1XSwgWzEyNy4xMTMyNjc5NTg1NTE5OSwgMzcuNjM5NjIyOTA1MzE1OTI1XSwgWzEyNy4xMDc4MjI3NzY4ODEyOSwgMzcuNjE4MDQyNDQyNDEwNjldLCBbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM10sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wNDM1ODgwMDg5NTYwOSwgMzcuNjI4NDg5MzEyOTg3MTVdLCBbMTI3LjA1ODAwMDc1MjIwMDkxLCAzNy42NDMxODI2Mzg3ODI3Nl0sIFsxMjcuMDUyODg0Nzk3MTA0ODUsIDM3LjY4NDIzODU3MDg0MzQ3XSwgWzEyNy4wODM4NzUyNzAzMTk1LCAzNy42OTM1OTUzNDIwMjAzNF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHViMTc4XHVjNmQwXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExMTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YjE3OFx1YzZkMFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJOb3dvbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wNTI4ODQ3OTcxMDQ4NSwgMzcuNjg0MjM4NTcwODQzNDddLCBbMTI3LjA1ODAwMDc1MjIwMDkxLCAzNy42NDMxODI2Mzg3ODI3Nl0sIFsxMjcuMDQzNTg4MDA4OTU2MDksIDM3LjYyODQ4OTMxMjk4NzE1XSwgWzEyNy4wMTQ2NTkzNTg5MjQ2NiwgMzcuNjQ5NDM2ODc0OTY4MTJdLCBbMTI3LjAyMDYyMTE2MTQxMzg5LCAzNy42NjcxNzM1NzU5NzEyMDVdLCBbMTI3LjAxMDM5NjY2MDQyMDcxLCAzNy42ODE4OTQ1ODk2MDM1OTRdLCBbMTI3LjAxNzk1MDk5MjAzNDMyLCAzNy42OTgyNDQxMjc3NTY2Ml0sIFsxMjcuMDUyODg0Nzk3MTA0ODUsIDM3LjY4NDIzODU3MDg0MzQ3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIzYzRcdWJkMDlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTEwMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViM2M0XHViZDA5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkRvYm9uZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45OTM4MzkwMzQyNCwgMzcuNjc2NjgxNzYxMTk5MDg1XSwgWzEyNy4wMTAzOTY2NjA0MjA3MSwgMzcuNjgxODk0NTg5NjAzNTk0XSwgWzEyNy4wMjA2MjExNjE0MTM4OSwgMzcuNjY3MTczNTc1OTcxMjA1XSwgWzEyNy4wMTQ2NTkzNTg5MjQ2NiwgMzcuNjQ5NDM2ODc0OTY4MTJdLCBbMTI3LjA0MzU4ODAwODk1NjA5LCAzNy42Mjg0ODkzMTI5ODcxNV0sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wMzg5MjQwMDk5MjMwMSwgMzcuNjA5NzE1NjExMDIzODE2XSwgWzEyNy4wMTI4MTU0NzQ5NTIzLCAzNy42MTM2NTIyNDM0NzAyNTZdLCBbMTI2Ljk4NjcyNzA1NTEzODY5LCAzNy42MzM3NzY0MTI4ODE5Nl0sIFsxMjYuOTgxNzQ1MjY3NjU1MSwgMzcuNjUyMDk3NjkzODc3NzZdLCBbMTI2Ljk5MzgzOTAzNDI0LCAzNy42NzY2ODE3NjExOTkwODVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWMxNVx1YmQ4MVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDkwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFjMTVcdWJkODFcdWFkNmMiLCAibmFtZV9lbmciOiAiR2FuZ2J1ay1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NzcxNzU0MDY0MTYsIDM3LjYyODU5NzE1NDAwMzg4XSwgWzEyNi45ODY3MjcwNTUxMzg2OSwgMzcuNjMzNzc2NDEyODgxOTZdLCBbMTI3LjAxMjgxNTQ3NDk1MjMsIDM3LjYxMzY1MjI0MzQ3MDI1Nl0sIFsxMjcuMDM4OTI0MDA5OTIzMDEsIDM3LjYwOTcxNTYxMTAyMzgxNl0sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wNzM1MTI0MzgyNTI3OCwgMzcuNjEyODM2NjAzNDIzMTNdLCBbMTI3LjA3MzgyNzA3MDk5MjI3LCAzNy42MDQwMTkyODk4NjQxOV0sIFsxMjcuMDQyNzA1MjIyMDk0LCAzNy41OTIzOTQzNzU5MzM5MV0sIFsxMjcuMDI1MjcyNTQ1MjgwMDMsIDM3LjU3NTI0NjE2MjQ1MjQ5XSwgWzEyNi45OTM0ODI5MzM1ODMxNCwgMzcuNTg4NTY1NDU3MjE2MTU2XSwgWzEyNi45ODg3OTg2NTk5MjM4NCwgMzcuNjExODkyNzMxOTc1Nl0sIFsxMjYuOTc3MTc1NDA2NDE2LCAzNy42Mjg1OTcxNTQwMDM4OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMTMxXHViZDgxXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwODAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzEzMVx1YmQ4MVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJTZW9uZ2J1ay1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wNzM1MTI0MzgyNTI3OCwgMzcuNjEyODM2NjAzNDIzMTNdLCBbMTI3LjEwNzgyMjc3Njg4MTI5LCAzNy42MTgwNDI0NDI0MTA2OV0sIFsxMjcuMTIwMTI0NjAyMDExNCwgMzcuNjAxNzg0NTc1OTgxODhdLCBbMTI3LjEwMzA0MTc0MjQ5MjE0LCAzNy41NzA3NjM0MjI5MDk1NV0sIFsxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XSwgWzEyNy4wNzM4MjcwNzA5OTIyNywgMzcuNjA0MDE5Mjg5ODY0MTldLCBbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjOTExXHViNzkxXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNzAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzkxMVx1Yjc5MVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJKdW5nbmFuZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmMWVlZjYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjUyNzI1NDUyODAwMywgMzcuNTc1MjQ2MTYyNDUyNDldLCBbMTI3LjA0MjcwNTIyMjA5NCwgMzcuNTkyMzk0Mzc1OTMzOTFdLCBbMTI3LjA3MzgyNzA3MDk5MjI3LCAzNy42MDQwMTkyODk4NjQxOV0sIFsxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA1MDA1NjAxMDgxNTY3LCAzNy41Njc1Nzc2MTI1OTA4NDZdLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdLCBbMTI3LjAyNTI3MjU0NTI4MDAzLCAzNy41NzUyNDYxNjI0NTI0OV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHViM2Q5XHViMzAwXHViYjM4XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNjAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YjNkOVx1YjMwMFx1YmIzOFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJEb25nZGFlbXVuLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M5OTRjNyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA4MDY4NTQxMjgwNDAzLCAzNy41NjkwNjQyNTUxOTAxN10sIFsxMjcuMTAzMDQxNzQyNDkyMTQsIDM3LjU3MDc2MzQyMjkwOTU1XSwgWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XSwgWzEyNy4xMTE2NzY0MjAzNjA4LCAzNy41NDA2Njk5NTUzMjQ5NjVdLCBbMTI3LjEwMDg3NTE5NzkxOTYyLCAzNy41MjQ4NDEyMjAxNjcwNTVdLCBbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl0sIFsxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA4MDY4NTQxMjgwNDAzLCAzNy41NjkwNjQyNTUxOTAxN11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZDExXHVjOWM0XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWQxMVx1YzljNFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJHd2FuZ2ppbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNkNGI5ZGEiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjU0NzI2NjM0OTk3NiwgMzcuNTY4OTQzNTUyMjM3NzM0XSwgWzEyNy4wNTAwNTYwMTA4MTU2NywgMzcuNTY3NTc3NjEyNTkwODQ2XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA1ODY3MzU5Mjg4Mzk4LCAzNy41MjYyOTk3NDkyMjU2OF0sIFsxMjcuMDIzMDI4MzE4OTA1NTksIDM3LjUzMjMxODk5NTgyNjYzXSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzEzMVx1YjNkOVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDQwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWMxMzFcdWIzZDlcdWFkNmMiLCAibmFtZV9lbmciOiAiU2Vvbmdkb25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2U3Mjk4YSIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjAxMDcwODk0MTc3NDgyLCAzNy41NDExODA0ODk2NDc2Ml0sIFsxMjcuMDIzMDI4MzE4OTA1NTksIDM3LjUzMjMxODk5NTgyNjYzXSwgWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldLCBbMTI2Ljk4MjIzODA3OTE2MDgxLCAzNy41MDkzMTQ5NjY3NzAzMjZdLCBbMTI2Ljk1MjQ5OTkwMjk4MTU5LCAzNy41MTcyMjUwMDc0MTgxM10sIFsxMjYuOTQ1NjY3MzMwODMyMTIsIDM3LjUyNjYxNzU0MjQ1MzM2Nl0sIFsxMjYuOTY0NDg1NzA1NTMwNTUsIDM3LjU0ODcwNTY5MjAyMTYzNV0sIFsxMjYuOTg3NTI5OTY5MDMzMjgsIDM3LjU1MDk0ODE4ODA3MTM5XSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzZhOVx1YzBiMFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDMwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM2YTlcdWMwYjBcdWFkNmMiLCAibmFtZV9lbmciOiAiWW9uZ3Nhbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNjZTEyNTYiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjU0NzI2NjM0OTk3NiwgMzcuNTY4OTQzNTUyMjM3NzM0XSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdLCBbMTI2Ljk4NzUyOTk2OTAzMzI4LCAzNy41NTA5NDgxODgwNzEzOV0sIFsxMjYuOTY0NDg1NzA1NTMwNTUsIDM3LjU0ODcwNTY5MjAyMTYzNV0sIFsxMjYuOTYzNTgyMjY3MTA4MTIsIDM3LjU1NjA1NjM1NDc1MTU0XSwgWzEyNi45Njg3MzYzMzI3OTA3NSwgMzcuNTYzMTM2MDQ2OTA4MjddLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzkxMVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDIwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM5MTFcdWFkNmMiLCAibmFtZV9lbmciOiAiSnVuZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiM5MTAwM2YiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NzM4ODY0MTI4NzAyLCAzNy42Mjk0OTYzNDc4Njg4OF0sIFsxMjYuOTc3MTc1NDA2NDE2LCAzNy42Mjg1OTcxNTQwMDM4OF0sIFsxMjYuOTg4Nzk4NjU5OTIzODQsIDM3LjYxMTg5MjczMTk3NTZdLCBbMTI2Ljk5MzQ4MjkzMzU4MzE0LCAzNy41ODg1NjU0NTcyMTYxNTZdLCBbMTI3LjAyNTI3MjU0NTI4MDAzLCAzNy41NzUyNDYxNjI0NTI0OV0sIFsxMjcuMDI1NDcyNjYzNDk5NzYsIDM3LjU2ODk0MzU1MjIzNzczNF0sIFsxMjYuOTY4NzM2MzMyNzkwNzUsIDM3LjU2MzEzNjA0NjkwODI3XSwgWzEyNi45NTU2NTQyNTg0NjQ2MywgMzcuNTc2MDgwNzkwODgxNDU2XSwgWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTU0MjcwMTcwMDYxMjksIDM3LjYyMjAzMzQzMTMzOTQyNV0sIFsxMjYuOTczODg2NDEyODcwMiwgMzcuNjI5NDk2MzQ3ODY4ODhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1Yzg4NVx1Yjg1Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDEwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM4ODVcdWI4NWNcdWFkNmMiLCAibmFtZV9lbmciOiAiSm9uZ25vLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiIzkxMDAzZiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn1dLCAidHlwZSI6ICJGZWF0dXJlQ29sbGVjdGlvbiJ9CiAgICAgICAgICAgIAogICAgICAgICAgICApLmFkZFRvKG1hcF81MDQ2YmU5OThmOWI0N2Y2OGM0YTcyMGQ5Y2I1MWVkOCk7CiAgICAgICAgZ2VvX2pzb25fODY3OGM3ODEwODAxNGMzZDhjZDRhMTU3YTM4NTE5NTMuc2V0U3R5bGUoZnVuY3Rpb24oZmVhdHVyZSkge3JldHVybiBmZWF0dXJlLnByb3BlcnRpZXMuc3R5bGU7fSk7CiAgICAgICAgCiAgICAKICAgIHZhciBjb2xvcl9tYXBfZTU4MWU4NWM2YjM2NDJkZDgwNmM5ZTQyMGM3OGU0ZGUgPSB7fTsKCiAgICAKICAgIGNvbG9yX21hcF9lNTgxZTg1YzZiMzY0MmRkODA2YzllNDIwYzc4ZTRkZS5jb2xvciA9IGQzLnNjYWxlLnRocmVzaG9sZCgpCiAgICAgICAgICAgICAgLmRvbWFpbihbMTkuNzg3MywgMTkuOTg4MTcyNTQ1MDkwMTgsIDIwLjE4OTA0NTA5MDE4MDM1OCwgMjAuMzg5OTE3NjM1MjcwNTQsIDIwLjU5MDc5MDE4MDM2MDcyLCAyMC43OTE2NjI3MjU0NTA4OTgsIDIwLjk5MjUzNTI3MDU0MTA4LCAyMS4xOTM0MDc4MTU2MzEyNiwgMjEuMzk0MjgwMzYwNzIxNDQyLCAyMS41OTUxNTI5MDU4MTE2MiwgMjEuNzk2MDI1NDUwOTAxOCwgMjEuOTk2ODk3OTk1OTkxOTgzLCAyMi4xOTc3NzA1NDEwODIxNjQsIDIyLjM5ODY0MzA4NjE3MjM0MiwgMjIuNTk5NTE1NjMxMjYyNTIzLCAyMi44MDAzODgxNzYzNTI3MDUsIDIzLjAwMTI2MDcyMTQ0Mjg4MywgMjMuMjAyMTMzMjY2NTMzMDY0LCAyMy40MDMwMDU4MTE2MjMyNDUsIDIzLjYwMzg3ODM1NjcxMzQyMywgMjMuODA0NzUwOTAxODAzNjA1LCAyNC4wMDU2MjM0NDY4OTM3ODYsIDI0LjIwNjQ5NTk5MTk4Mzk2NCwgMjQuNDA3MzY4NTM3MDc0MTQ1LCAyNC42MDgyNDEwODIxNjQzMjYsIDI0LjgwOTExMzYyNzI1NDUwOCwgMjUuMDA5OTg2MTcyMzQ0NjksIDI1LjIxMDg1ODcxNzQzNDg2NywgMjUuNDExNzMxMjYyNTI1MDUsIDI1LjYxMjYwMzgwNzYxNTIzLCAyNS44MTM0NzYzNTI3MDU0MDgsIDI2LjAxNDM0ODg5Nzc5NTU5LCAyNi4yMTUyMjE0NDI4ODU3NywgMjYuNDE2MDkzOTg3OTc1OTQ4LCAyNi42MTY5NjY1MzMwNjYxMywgMjYuODE3ODM5MDc4MTU2MzEsIDI3LjAxODcxMTYyMzI0NjQ5LCAyNy4yMTk1ODQxNjgzMzY2NywgMjcuNDIwNDU2NzEzNDI2ODUsIDI3LjYyMTMyOTI1ODUxNzAzLCAyNy44MjIyMDE4MDM2MDcyMSwgMjguMDIzMDc0MzQ4Njk3MzkyLCAyOC4yMjM5NDY4OTM3ODc1NywgMjguNDI0ODE5NDM4ODc3NzUsIDI4LjYyNTY5MTk4Mzk2NzkzMywgMjguODI2NTY0NTI5MDU4MTEsIDI5LjAyNzQzNzA3NDE0ODI5NSwgMjkuMjI4MzA5NjE5MjM4NDczLCAyOS40MjkxODIxNjQzMjg2NTUsIDI5LjYzMDA1NDcwOTQxODgzNiwgMjkuODMwOTI3MjU0NTA5MDE0LCAzMC4wMzE3OTk3OTk1OTkxOTUsIDMwLjIzMjY3MjM0NDY4OTM3NywgMzAuNDMzNTQ0ODg5Nzc5NTU0LCAzMC42MzQ0MTc0MzQ4Njk3MzYsIDMwLjgzNTI4OTk3OTk1OTkxNywgMzEuMDM2MTYyNTI1MDUwMDk1LCAzMS4yMzcwMzUwNzAxNDAyOCwgMzEuNDM3OTA3NjE1MjMwNDU4LCAzMS42Mzg3ODAxNjAzMjA2NCwgMzEuODM5NjUyNzA1NDEwODE3LCAzMi4wNDA1MjUyNTA1MDEsIDMyLjI0MTM5Nzc5NTU5MTE3NiwgMzIuNDQyMjcwMzQwNjgxMzYsIDMyLjY0MzE0Mjg4NTc3MTU0LCAzMi44NDQwMTU0MzA4NjE3MiwgMzMuMDQ0ODg3OTc1OTUxOSwgMzMuMjQ1NzYwNTIxMDQyMDgsIDMzLjQ0NjYzMzA2NjEzMjI2NCwgMzMuNjQ3NTA1NjExMjIyNDQsIDMzLjg0ODM3ODE1NjMxMjYyLCAzNC4wNDkyNTA3MDE0MDI4LCAzNC4yNTAxMjMyNDY0OTI5OCwgMzQuNDUwOTk1NzkxNTgzMTYsIDM0LjY1MTg2ODMzNjY3MzM0NiwgMzQuODUyNzQwODgxNzYzNTIsIDM1LjA1MzYxMzQyNjg1MzcsIDM1LjI1NDQ4NTk3MTk0Mzg4NiwgMzUuNDU1MzU4NTE3MDM0MDY0LCAzNS42NTYyMzEwNjIxMjQyNSwgMzUuODU3MTAzNjA3MjE0NDMsIDM2LjA1Nzk3NjE1MjMwNDYwNSwgMzYuMjU4ODQ4Njk3Mzk0NzgsIDM2LjQ1OTcyMTI0MjQ4NDk3LCAzNi42NjA1OTM3ODc1NzUxNDUsIDM2Ljg2MTQ2NjMzMjY2NTMzLCAzNy4wNjIzMzg4Nzc3NTU1MSwgMzcuMjYzMjExNDIyODQ1Njg2LCAzNy40NjQwODM5Njc5MzU4NiwgMzcuNjY0OTU2NTEzMDI2MDUsIDM3Ljg2NTgyOTA1ODExNjIyNiwgMzguMDY2NzAxNjAzMjA2NDEsIDM4LjI2NzU3NDE0ODI5NjU5LCAzOC40Njg0NDY2OTMzODY3NywgMzguNjY5MzE5MjM4NDc2OTQ1LCAzOC44NzAxOTE3ODM1NjcxNCwgMzkuMDcxMDY0MzI4NjU3MzE0LCAzOS4yNzE5MzY4NzM3NDc0OSwgMzkuNDcyODA5NDE4ODM3NjcsIDM5LjY3MzY4MTk2MzkyNzg1LCAzOS44NzQ1NTQ1MDkwMTgwMywgNDAuMDc1NDI3MDU0MTA4MjEsIDQwLjI3NjI5OTU5OTE5ODM5NiwgNDAuNDc3MTcyMTQ0Mjg4NTcsIDQwLjY3ODA0NDY4OTM3ODc1LCA0MC44Nzg5MTcyMzQ0Njg5MywgNDEuMDc5Nzg5Nzc5NTU5MTE0LCA0MS4yODA2NjIzMjQ2NDkyOSwgNDEuNDgxNTM0ODY5NzM5NDgsIDQxLjY4MjQwNzQxNDgyOTY1NSwgNDEuODgzMjc5OTU5OTE5ODMsIDQyLjA4NDE1MjUwNTAxMDAxLCA0Mi4yODUwMjUwNTAxMDAxOTUsIDQyLjQ4NTg5NzU5NTE5MDM4LCA0Mi42ODY3NzAxNDAyODA1NiwgNDIuODg3NjQyNjg1MzcwNzM2LCA0My4wODg1MTUyMzA0NjA5MTQsIDQzLjI4OTM4Nzc3NTU1MTEsIDQzLjQ5MDI2MDMyMDY0MTI4LCA0My42OTExMzI4NjU3MzE0NiwgNDMuODkyMDA1NDEwODIxNjQsIDQ0LjA5Mjg3Nzk1NTkxMTgyLCA0NC4yOTM3NTA1MDEwMDE5OTUsIDQ0LjQ5NDYyMzA0NjA5MjE4LCA0NC42OTU0OTU1OTExODIzNiwgNDQuODk2MzY4MTM2MjcyNTQsIDQ1LjA5NzI0MDY4MTM2MjcyLCA0NS4yOTgxMTMyMjY0NTI5LCA0NS40OTg5ODU3NzE1NDMwNzYsIDQ1LjY5OTg1ODMxNjYzMzI2LCA0NS45MDA3MzA4NjE3MjM0NCwgNDYuMTAxNjAzNDA2ODEzNjI0LCA0Ni4zMDI0NzU5NTE5MDM4LCA0Ni41MDMzNDg0OTY5OTM5OCwgNDYuNzA0MjIxMDQyMDg0MTYsIDQ2LjkwNTA5MzU4NzE3NDM1LCA0Ny4xMDU5NjYxMzIyNjQ1MywgNDcuMzA2ODM4Njc3MzU0NzA1LCA0Ny41MDc3MTEyMjI0NDQ4OCwgNDcuNzA4NTgzNzY3NTM1MDYsIDQ3LjkwOTQ1NjMxMjYyNTI0NSwgNDguMTEwMzI4ODU3NzE1NDMsIDQ4LjMxMTIwMTQwMjgwNTYxLCA0OC41MTIwNzM5NDc4OTU3ODYsIDQ4LjcxMjk0NjQ5Mjk4NTk2NCwgNDguOTEzODE5MDM4MDc2MTQsIDQ5LjExNDY5MTU4MzE2NjMyNiwgNDkuMzE1NTY0MTI4MjU2NTA0LCA0OS41MTY0MzY2NzMzNDY2OSwgNDkuNzE3MzA5MjE4NDM2ODcsIDQ5LjkxODE4MTc2MzUyNzA0NSwgNTAuMTE5MDU0MzA4NjE3MjIsIDUwLjMxOTkyNjg1MzcwNzQxLCA1MC41MjA3OTkzOTg3OTc1OSwgNTAuNzIxNjcxOTQzODg3NzcsIDUwLjkyMjU0NDQ4ODk3Nzk1LCA1MS4xMjM0MTcwMzQwNjgxMjYsIDUxLjMyNDI4OTU3OTE1ODMxLCA1MS41MjUxNjIxMjQyNDg0OTYsIDUxLjcyNjAzNDY2OTMzODY3NCwgNTEuOTI2OTA3MjE0NDI4ODUsIDUyLjEyNzc3OTc1OTUxOTAzLCA1Mi4zMjg2NTIzMDQ2MDkyMSwgNTIuNTI5NTI0ODQ5Njk5NCwgNTIuNzMwMzk3Mzk0Nzg5NTgsIDUyLjkzMTI2OTkzOTg3OTc1NSwgNTMuMTMyMTQyNDg0OTY5OTMsIDUzLjMzMzAxNTAzMDA2MDExLCA1My41MzM4ODc1NzUxNTAyOSwgNTMuNzM0NzYwMTIwMjQwNDgsIDUzLjkzNTYzMjY2NTMzMDY2LCA1NC4xMzY1MDUyMTA0MjA4MzYsIDU0LjMzNzM3Nzc1NTUxMTAxNCwgNTQuNTM4MjUwMzAwNjAxMTksIDU0LjczOTEyMjg0NTY5MTM4NCwgNTQuOTM5OTk1MzkwNzgxNTUsIDU1LjE0MDg2NzkzNTg3MTc0LCA1NS4zNDE3NDA0ODA5NjE5MiwgNTUuNTQyNjEzMDI2MDUyMDk1LCA1NS43NDM0ODU1NzExNDIyNywgNTUuOTQ0MzU4MTE2MjMyNDUsIDU2LjE0NTIzMDY2MTMyMjY0LCA1Ni4zNDYxMDMyMDY0MTI4MiwgNTYuNTQ2OTc1NzUxNTAzLCA1Ni43NDc4NDgyOTY1OTMxNzYsIDU2Ljk0ODcyMDg0MTY4MzM1NCwgNTcuMTQ5NTkzMzg2NzczNTQ2LCA1Ny4zNTA0NjU5MzE4NjM3MjQsIDU3LjU1MTMzODQ3Njk1MzksIDU3Ljc1MjIxMTAyMjA0NDA4LCA1Ny45NTMwODM1NjcxMzQyNywgNTguMTUzOTU2MTEyMjI0NDM1LCA1OC4zNTQ4Mjg2NTczMTQ2MywgNTguNTU1NzAxMjAyNDA0ODA1LCA1OC43NTY1NzM3NDc0OTQ5OCwgNTguOTU3NDQ2MjkyNTg1MTYsIDU5LjE1ODMxODgzNzY3NTM0LCA1OS4zNTkxOTEzODI3NjU1MywgNTkuNTYwMDYzOTI3ODU1Njk0LCA1OS43NjA5MzY0NzI5NDU4ODYsIDU5Ljk2MTgwOTAxODAzNjA2NCwgNjAuMTYyNjgxNTYzMTI2MjQsIDYwLjM2MzU1NDEwODIxNjQyLCA2MC41NjQ0MjY2NTMzMDY2LCA2MC43NjUyOTkxOTgzOTY3OSwgNjAuOTY2MTcxNzQzNDg2OTcsIDYxLjE2NzA0NDI4ODU3NzE0NSwgNjEuMzY3OTE2ODMzNjY3MzIsIDYxLjU2ODc4OTM3ODc1NzUxNSwgNjEuNzY5NjYxOTIzODQ3NjksIDYxLjk3MDUzNDQ2ODkzNzg3LCA2Mi4xNzE0MDcwMTQwMjgwNSwgNjIuMzcyMjc5NTU5MTE4MjI2LCA2Mi41NzMxNTIxMDQyMDg0MiwgNjIuNzc0MDI0NjQ5Mjk4NTgsIDYyLjk3NDg5NzE5NDM4ODc3NCwgNjMuMTc1NzY5NzM5NDc4OTUsIDYzLjM3NjY0MjI4NDU2OTEzLCA2My41Nzc1MTQ4Mjk2NTkzMSwgNjMuNzc4Mzg3Mzc0NzQ5NDg1LCA2My45NzkyNTk5MTk4Mzk2OCwgNjQuMTgwMTMyNDY0OTI5ODYsIDY0LjM4MTAwNTAxMDAyMDAzLCA2NC41ODE4Nzc1NTUxMTAyMSwgNjQuNzgyNzUwMTAwMjAwMzksIDY0Ljk4MzYyMjY0NTI5MDU3LCA2NS4xODQ0OTUxOTAzODA3NiwgNjUuMzg1MzY3NzM1NDcwOTQsIDY1LjU4NjI0MDI4MDU2MTExLCA2NS43ODcxMTI4MjU2NTEyOSwgNjUuOTg3OTg1MzcwNzQxNDcsIDY2LjE4ODg1NzkxNTgzMTY2LCA2Ni4zODk3MzA0NjA5MjE4NCwgNjYuNTkwNjAzMDA2MDEyMDIsIDY2Ljc5MTQ3NTU1MTEwMjIsIDY2Ljk5MjM0ODA5NjE5MjM3LCA2Ny4xOTMyMjA2NDEyODI1NiwgNjcuMzk0MDkzMTg2MzcyNzMsIDY3LjU5NDk2NTczMTQ2MjkyLCA2Ny43OTU4MzgyNzY1NTMxLCA2Ny45OTY3MTA4MjE2NDMyOCwgNjguMTk3NTgzMzY2NzMzNDUsIDY4LjM5ODQ1NTkxMTgyMzYzLCA2OC41OTkzMjg0NTY5MTM4MiwgNjguODAwMjAxMDAyMDA0LCA2OS4wMDEwNzM1NDcwOTQxOCwgNjkuMjAxOTQ2MDkyMTg0MzYsIDY5LjQwMjgxODYzNzI3NDU0LCA2OS42MDM2OTExODIzNjQ3MSwgNjkuODA0NTYzNzI3NDU0OSwgNzAuMDA1NDM2MjcyNTQ1MDgsIDcwLjIwNjMwODgxNzYzNTI2LCA3MC40MDcxODEzNjI3MjU0NCwgNzAuNjA4MDUzOTA3ODE1NjIsIDcwLjgwODkyNjQ1MjkwNTgxLCA3MS4wMDk3OTg5OTc5OTU5OSwgNzEuMjEwNjcxNTQzMDg2MTYsIDcxLjQxMTU0NDA4ODE3NjM0LCA3MS42MTI0MTY2MzMyNjY1MiwgNzEuODEzMjg5MTc4MzU2NzEsIDcyLjAxNDE2MTcyMzQ0Njg4LCA3Mi4yMTUwMzQyNjg1MzcwNywgNzIuNDE1OTA2ODEzNjI3MjUsIDcyLjYxNjc3OTM1ODcxNzQyLCA3Mi44MTc2NTE5MDM4MDc2LCA3My4wMTg1MjQ0NDg4OTc4LCA3My4yMTkzOTY5OTM5ODc5NywgNzMuNDIwMjY5NTM5MDc4MTUsIDczLjYyMTE0MjA4NDE2ODMzLCA3My44MjIwMTQ2MjkyNTg1LCA3NC4wMjI4ODcxNzQzNDg3LCA3NC4yMjM3NTk3MTk0Mzg4NiwgNzQuNDI0NjMyMjY0NTI5MDUsIDc0LjYyNTUwNDgwOTYxOTIzLCA3NC44MjYzNzczNTQ3MDk0MSwgNzUuMDI3MjQ5ODk5Nzk5NTksIDc1LjIyODEyMjQ0NDg4OTc2LCA3NS40Mjg5OTQ5ODk5Nzk5NiwgNzUuNjI5ODY3NTM1MDcwMTMsIDc1LjgzMDc0MDA4MDE2MDMxLCA3Ni4wMzE2MTI2MjUyNTA0OSwgNzYuMjMyNDg1MTcwMzQwNjcsIDc2LjQzMzM1NzcxNTQzMDg2LCA3Ni42MzQyMzAyNjA1MjEwNCwgNzYuODM1MTAyODA1NjExMjEsIDc3LjAzNTk3NTM1MDcwMTM5LCA3Ny4yMzY4NDc4OTU3OTE1NywgNzcuNDM3NzIwNDQwODgxNzUsIDc3LjYzODU5Mjk4NTk3MTk0LCA3Ny44Mzk0NjU1MzEwNjIxMiwgNzguMDQwMzM4MDc2MTUyMywgNzguMjQxMjEwNjIxMjQyNDcsIDc4LjQ0MjA4MzE2NjMzMjY1LCA3OC42NDI5NTU3MTE0MjI4NCwgNzguODQzODI4MjU2NTEzLCA3OS4wNDQ3MDA4MDE2MDMyLCA3OS4yNDU1NzMzNDY2OTMzOCwgNzkuNDQ2NDQ1ODkxNzgzNTUsIDc5LjY0NzMxODQzNjg3MzczLCA3OS44NDgxOTA5ODE5NjM5MSwgODAuMDQ5MDYzNTI3MDU0MSwgODAuMjQ5OTM2MDcyMTQ0MjgsIDgwLjQ1MDgwODYxNzIzNDQ2LCA4MC42NTE2ODExNjIzMjQ2NCwgODAuODUyNTUzNzA3NDE0ODEsIDgxLjA1MzQyNjI1MjUwNSwgODEuMjU0Mjk4Nzk3NTk1MTgsIDgxLjQ1NTE3MTM0MjY4NTM2LCA4MS42NTYwNDM4ODc3NzU1NCwgODEuODU2OTE2NDMyODY1NzIsIDgyLjA1Nzc4ODk3Nzk1NTksIDgyLjI1ODY2MTUyMzA0NjA5LCA4Mi40NTk1MzQwNjgxMzYyNiwgODIuNjYwNDA2NjEzMjI2NDQsIDgyLjg2MTI3OTE1ODMxNjYyLCA4My4wNjIxNTE3MDM0MDY4LCA4My4yNjMwMjQyNDg0OTY5OSwgODMuNDYzODk2NzkzNTg3MTUsIDgzLjY2NDc2OTMzODY3NzM1LCA4My44NjU2NDE4ODM3Njc1MiwgODQuMDY2NTE0NDI4ODU3NywgODQuMjY3Mzg2OTczOTQ3OSwgODQuNDY4MjU5NTE5MDM4MDcsIDg0LjY2OTEzMjA2NDEyODI1LCA4NC44NzAwMDQ2MDkyMTg0MywgODUuMDcwODc3MTU0MzA4NiwgODUuMjcxNzQ5Njk5Mzk4OCwgODUuNDcyNjIyMjQ0NDg4OTYsIDg1LjY3MzQ5NDc4OTU3OTE1LCA4NS44NzQzNjczMzQ2NjkzMywgODYuMDc1MjM5ODc5NzU5NTEsIDg2LjI3NjExMjQyNDg0OTY5LCA4Ni40NzY5ODQ5Njk5Mzk4OCwgODYuNjc3ODU3NTE1MDMwMDYsIDg2Ljg3ODczMDA2MDEyMDIyLCA4Ny4wNzk2MDI2MDUyMTA0MSwgODcuMjgwNDc1MTUwMzAwNTksIDg3LjQ4MTM0NzY5NTM5MDc3LCA4Ny42ODIyMjAyNDA0ODA5NiwgODcuODgzMDkyNzg1NTcxMTQsIDg4LjA4Mzk2NTMzMDY2MTMxLCA4OC4yODQ4Mzc4NzU3NTE1LCA4OC40ODU3MTA0MjA4NDE2NywgODguNjg2NTgyOTY1OTMxODUsIDg4Ljg4NzQ1NTUxMTAyMjAzLCA4OS4wODgzMjgwNTYxMTIyMiwgODkuMjg5MjAwNjAxMjAyNCwgODkuNDkwMDczMTQ2MjkyNTcsIDg5LjY5MDk0NTY5MTM4Mjc3LCA4OS44OTE4MTgyMzY0NzI5NCwgOTAuMDkyNjkwNzgxNTYzMSwgOTAuMjkzNTYzMzI2NjUzMywgOTAuNDk0NDM1ODcxNzQzNDgsIDkwLjY5NTMwODQxNjgzMzY1LCA5MC44OTYxODA5NjE5MjM4NSwgOTEuMDk3MDUzNTA3MDE0MDIsIDkxLjI5NzkyNjA1MjEwNDIsIDkxLjQ5ODc5ODU5NzE5NDM3LCA5MS42OTk2NzExNDIyODQ1NiwgOTEuOTAwNTQzNjg3Mzc0NzQsIDkyLjEwMTQxNjIzMjQ2NDkxLCA5Mi4zMDIyODg3Nzc1NTUxLCA5Mi41MDMxNjEzMjI2NDUyOCwgOTIuNzA0MDMzODY3NzM1NDYsIDkyLjkwNDkwNjQxMjgyNTY1LCA5My4xMDU3Nzg5NTc5MTU4MiwgOTMuMzA2NjUxNTAzMDA2LCA5My41MDc1MjQwNDgwOTYxOSwgOTMuNzA4Mzk2NTkzMTg2MzYsIDkzLjkwOTI2OTEzODI3NjU0LCA5NC4xMTAxNDE2ODMzNjY3MiwgOTQuMzExMDE0MjI4NDU2OTEsIDk0LjUxMTg4Njc3MzU0NzA5LCA5NC43MTI3NTkzMTg2MzcyNSwgOTQuOTEzNjMxODYzNzI3NDUsIDk1LjExNDUwNDQwODgxNzYyLCA5NS4zMTUzNzY5NTM5MDc4LCA5NS41MTYyNDk0OTg5OTgsIDk1LjcxNzEyMjA0NDA4ODE3LCA5NS45MTc5OTQ1ODkxNzgzNSwgOTYuMTE4ODY3MTM0MjY4NTQsIDk2LjMxOTczOTY3OTM1ODcsIDk2LjUyMDYxMjIyNDQ0ODg4LCA5Ni43MjE0ODQ3Njk1MzkwNiwgOTYuOTIyMzU3MzE0NjI5MjUsIDk3LjEyMzIyOTg1OTcxOTQzLCA5Ny4zMjQxMDI0MDQ4MDk2MSwgOTcuNTI0OTc0OTQ5ODk5OCwgOTcuNzI1ODQ3NDk0OTg5OTYsIDk3LjkyNjcyMDA0MDA4MDE0LCA5OC4xMjc1OTI1ODUxNzAzMywgOTguMzI4NDY1MTMwMjYwNTEsIDk4LjUyOTMzNzY3NTM1MDY5LCA5OC43MzAyMTAyMjA0NDA4OCwgOTguOTMxMDgyNzY1NTMxMDYsIDk5LjEzMTk1NTMxMDYyMTI0LCA5OS4zMzI4Mjc4NTU3MTE0LCA5OS41MzM3MDA0MDA4MDE1OSwgOTkuNzM0NTcyOTQ1ODkxNzcsIDk5LjkzNTQ0NTQ5MDk4MTk1LCAxMDAuMTM2MzE4MDM2MDcyMTQsIDEwMC4zMzcxOTA1ODExNjIzMiwgMTAwLjUzODA2MzEyNjI1MjUsIDEwMC43Mzg5MzU2NzEzNDI2OSwgMTAwLjkzOTgwODIxNjQzMjg1LCAxMDEuMTQwNjgwNzYxNTIzMDMsIDEwMS4zNDE1NTMzMDY2MTMyLCAxMDEuNTQyNDI1ODUxNzAzNCwgMTAxLjc0MzI5ODM5Njc5MzU4LCAxMDEuOTQ0MTcwOTQxODgzNzUsIDEwMi4xNDUwNDM0ODY5NzM5NSwgMTAyLjM0NTkxNjAzMjA2NDExLCAxMDIuNTQ2Nzg4NTc3MTU0MjksIDEwMi43NDc2NjExMjIyNDQ0OCwgMTAyLjk0ODUzMzY2NzMzNDY2LCAxMDMuMTQ5NDA2MjEyNDI0ODQsIDEwMy4zNTAyNzg3NTc1MTUwMywgMTAzLjU1MTE1MTMwMjYwNTIsIDEwMy43NTIwMjM4NDc2OTUzOCwgMTAzLjk1Mjg5NjM5Mjc4NTU1LCAxMDQuMTUzNzY4OTM3ODc1NzQsIDEwNC4zNTQ2NDE0ODI5NjU5MiwgMTA0LjU1NTUxNDAyODA1NjEsIDEwNC43NTYzODY1NzMxNDYyOSwgMTA0Ljk1NzI1OTExODIzNjQ2LCAxMDUuMTU4MTMxNjYzMzI2NjQsIDEwNS4zNTkwMDQyMDg0MTY4MywgMTA1LjU1OTg3Njc1MzUwNywgMTA1Ljc2MDc0OTI5ODU5NzE4LCAxMDUuOTYxNjIxODQzNjg3MzcsIDEwNi4xNjI0OTQzODg3Nzc1NSwgMTA2LjM2MzM2NjkzMzg2NzcyLCAxMDYuNTY0MjM5NDc4OTU3OSwgMTA2Ljc2NTExMjAyNDA0ODEsIDEwNi45NjU5ODQ1NjkxMzgyNiwgMTA3LjE2Njg1NzExNDIyODQzLCAxMDcuMzY3NzI5NjU5MzE4NjMsIDEwNy41Njg2MDIyMDQ0MDg4LCAxMDcuNzY5NDc0NzQ5NDk4OTgsIDEwNy45NzAzNDcyOTQ1ODkxNywgMTA4LjE3MTIxOTgzOTY3OTM1LCAxMDguMzcyMDkyMzg0NzY5NTMsIDEwOC41NzI5NjQ5Mjk4NTk3MSwgMTA4Ljc3MzgzNzQ3NDk0OTg5LCAxMDguOTc0NzEwMDIwMDQwMDYsIDEwOS4xNzU1ODI1NjUxMzAyNCwgMTA5LjM3NjQ1NTExMDIyMDQzLCAxMDkuNTc3MzI3NjU1MzEwNjEsIDEwOS43NzgyMDAyMDA0MDA3OSwgMTA5Ljk3OTA3Mjc0NTQ5MDk4LCAxMTAuMTc5OTQ1MjkwNTgxMTQsIDExMC4zODA4MTc4MzU2NzEzMiwgMTEwLjU4MTY5MDM4MDc2MTUxLCAxMTAuNzgyNTYyOTI1ODUxNjksIDExMC45ODM0MzU0NzA5NDE4NywgMTExLjE4NDMwODAxNjAzMjA2LCAxMTEuMzg1MTgwNTYxMTIyMjQsIDExMS41ODYwNTMxMDYyMTI0LCAxMTEuNzg2OTI1NjUxMzAyNTgsIDExMS45ODc3OTgxOTYzOTI3NywgMTEyLjE4ODY3MDc0MTQ4Mjk1LCAxMTIuMzg5NTQzMjg2NTczMTMsIDExMi41OTA0MTU4MzE2NjMzMiwgMTEyLjc5MTI4ODM3Njc1MzUsIDExMi45OTIxNjA5MjE4NDM2OCwgMTEzLjE5MzAzMzQ2NjkzMzg1LCAxMTMuMzkzOTA2MDEyMDI0MDMsIDExMy41OTQ3Nzg1NTcxMTQyMSwgMTEzLjc5NTY1MTEwMjIwNDQsIDExMy45OTY1MjM2NDcyOTQ1OCwgMTE0LjE5NzM5NjE5MjM4NDc2LCAxMTQuMzk4MjY4NzM3NDc0OTQsIDExNC41OTkxNDEyODI1NjUxMywgMTE0LjgwMDAxMzgyNzY1NTI5LCAxMTUuMDAwODg2MzcyNzQ1NDcsIDExNS4yMDE3NTg5MTc4MzU2NiwgMTE1LjQwMjYzMTQ2MjkyNTg0LCAxMTUuNjAzNTA0MDA4MDE2MDIsIDExNS44MDQzNzY1NTMxMDYyMSwgMTE2LjAwNTI0OTA5ODE5NjM5LCAxMTYuMjA2MTIxNjQzMjg2NTUsIDExNi40MDY5OTQxODgzNzY3MywgMTE2LjYwNzg2NjczMzQ2NjkyLCAxMTYuODA4NzM5Mjc4NTU3MSwgMTE3LjAwOTYxMTgyMzY0NzI4LCAxMTcuMjEwNDg0MzY4NzM3NDcsIDExNy40MTEzNTY5MTM4Mjc2NSwgMTE3LjYxMjIyOTQ1ODkxNzgyLCAxMTcuODEzMTAyMDA0MDA4LCAxMTguMDEzOTc0NTQ5MDk4MTgsIDExOC4yMTQ4NDcwOTQxODgzNiwgMTE4LjQxNTcxOTYzOTI3ODU1LCAxMTguNjE2NTkyMTg0MzY4NzMsIDExOC44MTc0NjQ3Mjk0NTg5LCAxMTkuMDE4MzM3Mjc0NTQ5MDgsIDExOS4yMTkyMDk4MTk2MzkyNywgMTE5LjQyMDA4MjM2NDcyOTQ0LCAxMTkuNjIwOTU0OTA5ODE5NjIsIDExOS44MjE4Mjc0NTQ5MDk4MSwgMTIwLjAyMjY5OTk5OTk5OTk5XSkKICAgICAgICAgICAgICAucmFuZ2UoWycjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjZDRiOWRhJywgJyNkNGI5ZGEnLCAnI2Q0YjlkYScsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2M5OTRjNycsICcjYzk5NGM3JywgJyNjOTk0YzcnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNkZjY1YjAnLCAnI2RmNjViMCcsICcjZGY2NWIwJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjZTcyOThhJywgJyNlNzI5OGEnLCAnI2U3Mjk4YScsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnI2NlMTI1NicsICcjY2UxMjU2JywgJyNjZTEyNTYnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnLCAnIzkxMDAzZicsICcjOTEwMDNmJywgJyM5MTAwM2YnXSk7CiAgICAKCiAgICBjb2xvcl9tYXBfZTU4MWU4NWM2YjM2NDJkZDgwNmM5ZTQyMGM3OGU0ZGUueCA9IGQzLnNjYWxlLmxpbmVhcigpCiAgICAgICAgICAgICAgLmRvbWFpbihbMTkuNzg3MywgMTIwLjAyMjY5OTk5OTk5OTk5XSkKICAgICAgICAgICAgICAucmFuZ2UoWzAsIDQwMF0pOwoKICAgIGNvbG9yX21hcF9lNTgxZTg1YzZiMzY0MmRkODA2YzllNDIwYzc4ZTRkZS5sZWdlbmQgPSBMLmNvbnRyb2woe3Bvc2l0aW9uOiAndG9wcmlnaHQnfSk7CiAgICBjb2xvcl9tYXBfZTU4MWU4NWM2YjM2NDJkZDgwNmM5ZTQyMGM3OGU0ZGUubGVnZW5kLm9uQWRkID0gZnVuY3Rpb24gKG1hcCkge3ZhciBkaXYgPSBMLkRvbVV0aWwuY3JlYXRlKCdkaXYnLCAnbGVnZW5kJyk7IHJldHVybiBkaXZ9OwogICAgY29sb3JfbWFwX2U1ODFlODVjNmIzNjQyZGQ4MDZjOWU0MjBjNzhlNGRlLmxlZ2VuZC5hZGRUbyhtYXBfNTA0NmJlOTk4ZjliNDdmNjhjNGE3MjBkOWNiNTFlZDgpOwoKICAgIGNvbG9yX21hcF9lNTgxZTg1YzZiMzY0MmRkODA2YzllNDIwYzc4ZTRkZS54QXhpcyA9IGQzLnN2Zy5heGlzKCkKICAgICAgICAuc2NhbGUoY29sb3JfbWFwX2U1ODFlODVjNmIzNjQyZGQ4MDZjOWU0MjBjNzhlNGRlLngpCiAgICAgICAgLm9yaWVudCgidG9wIikKICAgICAgICAudGlja1NpemUoMSkKICAgICAgICAudGlja1ZhbHVlcyhbMTkuNzg3MywgMzYuNDkzMiwgNTMuMTk5MSwgNjkuOTA0OTk5OTk5OTk5OTksIDg2LjYxMDksIDEwMy4zMTY4LCAxMjAuMDIyNjk5OTk5OTk5OTldKTsKCiAgICBjb2xvcl9tYXBfZTU4MWU4NWM2YjM2NDJkZDgwNmM5ZTQyMGM3OGU0ZGUuc3ZnID0gZDMuc2VsZWN0KCIubGVnZW5kLmxlYWZsZXQtY29udHJvbCIpLmFwcGVuZCgic3ZnIikKICAgICAgICAuYXR0cigiaWQiLCAnbGVnZW5kJykKICAgICAgICAuYXR0cigid2lkdGgiLCA0NTApCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDQwKTsKCiAgICBjb2xvcl9tYXBfZTU4MWU4NWM2YjM2NDJkZDgwNmM5ZTQyMGM3OGU0ZGUuZyA9IGNvbG9yX21hcF9lNTgxZTg1YzZiMzY0MmRkODA2YzllNDIwYzc4ZTRkZS5zdmcuYXBwZW5kKCJnIikKICAgICAgICAuYXR0cigiY2xhc3MiLCAia2V5IikKICAgICAgICAuYXR0cigidHJhbnNmb3JtIiwgInRyYW5zbGF0ZSgyNSwxNikiKTsKCiAgICBjb2xvcl9tYXBfZTU4MWU4NWM2YjM2NDJkZDgwNmM5ZTQyMGM3OGU0ZGUuZy5zZWxlY3RBbGwoInJlY3QiKQogICAgICAgIC5kYXRhKGNvbG9yX21hcF9lNTgxZTg1YzZiMzY0MmRkODA2YzllNDIwYzc4ZTRkZS5jb2xvci5yYW5nZSgpLm1hcChmdW5jdGlvbihkLCBpKSB7CiAgICAgICAgICByZXR1cm4gewogICAgICAgICAgICB4MDogaSA/IGNvbG9yX21hcF9lNTgxZTg1YzZiMzY0MmRkODA2YzllNDIwYzc4ZTRkZS54KGNvbG9yX21hcF9lNTgxZTg1YzZiMzY0MmRkODA2YzllNDIwYzc4ZTRkZS5jb2xvci5kb21haW4oKVtpIC0gMV0pIDogY29sb3JfbWFwX2U1ODFlODVjNmIzNjQyZGQ4MDZjOWU0MjBjNzhlNGRlLngucmFuZ2UoKVswXSwKICAgICAgICAgICAgeDE6IGkgPCBjb2xvcl9tYXBfZTU4MWU4NWM2YjM2NDJkZDgwNmM5ZTQyMGM3OGU0ZGUuY29sb3IuZG9tYWluKCkubGVuZ3RoID8gY29sb3JfbWFwX2U1ODFlODVjNmIzNjQyZGQ4MDZjOWU0MjBjNzhlNGRlLngoY29sb3JfbWFwX2U1ODFlODVjNmIzNjQyZGQ4MDZjOWU0MjBjNzhlNGRlLmNvbG9yLmRvbWFpbigpW2ldKSA6IGNvbG9yX21hcF9lNTgxZTg1YzZiMzY0MmRkODA2YzllNDIwYzc4ZTRkZS54LnJhbmdlKClbMV0sCiAgICAgICAgICAgIHo6IGQKICAgICAgICAgIH07CiAgICAgICAgfSkpCiAgICAgIC5lbnRlcigpLmFwcGVuZCgicmVjdCIpCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDEwKQogICAgICAgIC5hdHRyKCJ4IiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC54MDsgfSkKICAgICAgICAuYXR0cigid2lkdGgiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLngxIC0gZC54MDsgfSkKICAgICAgICAuc3R5bGUoImZpbGwiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLno7IH0pOwoKICAgIGNvbG9yX21hcF9lNTgxZTg1YzZiMzY0MmRkODA2YzllNDIwYzc4ZTRkZS5nLmNhbGwoY29sb3JfbWFwX2U1ODFlODVjNmIzNjQyZGQ4MDZjOWU0MjBjNzhlNGRlLnhBeGlzKS5hcHBlbmQoInRleHQiKQogICAgICAgIC5hdHRyKCJjbGFzcyIsICJjYXB0aW9uIikKICAgICAgICAuYXR0cigieSIsIDIxKQogICAgICAgIC50ZXh0KCcnKTsKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
map = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='Stamen Toner')
map.choropleth(geo_str, data = df2, columns =["지역", "재산세 수준지수(서울특별시=100)"], fill_color='YlGnBu', #PuRd, YlGnBu
              key_on='feature.id')
map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVM9ZmFsc2U7IExfTk9fVE9VQ0g9ZmFsc2U7IExfRElTQUJMRV8zRD1mYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgPHN0eWxlPiNtYXBfODI2MjZkNjExM2Q0NDhiMmJjNjE5MGRmMmUyYjI2ZDEgewogICAgICAgIHBvc2l0aW9uOiByZWxhdGl2ZTsKICAgICAgICB3aWR0aDogMTAwLjAlOwogICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgdG9wOiAwLjAlOwogICAgICAgIH0KICAgIDwvc3R5bGU+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvZDMvMy41LjUvZDMubWluLmpzIj48L3NjcmlwdD4KPC9oZWFkPgo8Ym9keT4gICAgCiAgICAKICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfODI2MjZkNjExM2Q0NDhiMmJjNjE5MGRmMmUyYjI2ZDEiID48L2Rpdj4KPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgCiAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAKCiAgICB2YXIgbWFwXzgyNjI2ZDYxMTNkNDQ4YjJiYzYxOTBkZjJlMmIyNmQxID0gTC5tYXAoCiAgICAgICAgJ21hcF84MjYyNmQ2MTEzZDQ0OGIyYmM2MTkwZGYyZTJiMjZkMScsIHsKICAgICAgICBjZW50ZXI6IFszNy41NTAyLCAxMjYuOTgyXSwKICAgICAgICB6b29tOiAxMSwKICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICBsYXllcnM6IFtdLAogICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcsCiAgICAgICAgem9vbUNvbnRyb2w6IHRydWUsCiAgICAgICAgfSk7CgogICAgCiAgICAKICAgIHZhciB0aWxlX2xheWVyXzBlMDM1MTZlNGVhOTRjZDg5YTM0YjZmYjVjZmU5Y2Q2ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgJ2h0dHBzOi8vc3RhbWVuLXRpbGVzLXtzfS5hLnNzbC5mYXN0bHkubmV0L3RvbmVyL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgewogICAgICAgICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgICAgICAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICAgICAgICJtYXhOYXRpdmVab29tIjogMTgsCiAgICAgICAgIm1heFpvb20iOiAxOCwKICAgICAgICAibWluWm9vbSI6IDAsCiAgICAgICAgIm5vV3JhcCI6IGZhbHNlLAogICAgICAgICJzdWJkb21haW5zIjogImFiYyIKfSkuYWRkVG8obWFwXzgyNjI2ZDYxMTNkNDQ4YjJiYzYxOTBkZjJlMmIyNmQxKTsKICAgIAogICAgICAgIAogICAgICAgIHZhciBnZW9fanNvbl8zMjdmNjliY2I2Yzg0ODUyODBkM2Q3ZGE0MzcyY2ZmZCA9IEwuZ2VvSnNvbigKICAgICAgICAgICAgeyJmZWF0dXJlcyI6IFt7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XSwgWzEyNy4xNjY4MzE4NDM2NjEyOSwgMzcuNTc2NzI0ODczODg2MjddLCBbMTI3LjE4NDA4NzkyMzMwMTUyLCAzNy41NTgxNDI4MDM2OTU3NV0sIFsxMjcuMTY1MzA5ODQzMDc0NDcsIDM3LjU0MjIxODUxMjU4NjkzXSwgWzEyNy4xNDY3MjgwNjgyMzUwMiwgMzcuNTE0MTU2ODA2ODAyOTFdLCBbMTI3LjEyMTIzMTY1NzE5NjE1LCAzNy41MjUyODI3MDA4OV0sIFsxMjcuMTExNjc2NDIwMzYwOCwgMzcuNTQwNjY5OTU1MzI0OTY1XSwgWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFjMTVcdWIzZDlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTI1MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhYzE1XHViM2Q5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkdhbmdkb25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZjYyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl0sIFsxMjcuMTAwODc1MTk3OTE5NjIsIDM3LjUyNDg0MTIyMDE2NzA1NV0sIFsxMjcuMTExNjc2NDIwMzYwOCwgMzcuNTQwNjY5OTU1MzI0OTY1XSwgWzEyNy4xMjEyMzE2NTcxOTYxNSwgMzcuNTI1MjgyNzAwODldLCBbMTI3LjE0NjcyODA2ODIzNTAyLCAzNy41MTQxNTY4MDY4MDI5MV0sIFsxMjcuMTYzNDk0NDIxNTc2NSwgMzcuNDk3NDQ1NDA2MDk3NDg0XSwgWzEyNy4xNDIwNjA1ODQxMzI3NCwgMzcuNDcwODk4MTkwOTg1MDFdLCBbMTI3LjEyNDQwNTcxMDgwODkzLCAzNy40NjI0MDQ0NTU4NzA0OF0sIFsxMjcuMTExMTcwODUyMDEyMzgsIDM3LjQ4NTcwODM4MTUxMjQ0NV0sIFsxMjcuMDcxOTE0NjAwMDcyNCwgMzcuNTAyMjQwMTM1ODc2NjldLCBbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMWExXHVkMzBjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEyNDAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzFhMVx1ZDMwY1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJTb25ncGEtZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjYzdlOWI0IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XSwgWzEyNy4wNjkwNjk4MTMwMzcyLCAzNy41MjIyNzk0MjM1MDUwMjZdLCBbMTI3LjA3MTkxNDYwMDA3MjQsIDM3LjUwMjI0MDEzNTg3NjY5XSwgWzEyNy4xMTExNzA4NTIwMTIzOCwgMzcuNDg1NzA4MzgxNTEyNDQ1XSwgWzEyNy4xMjQ0MDU3MTA4MDg5MywgMzcuNDYyNDA0NDU1ODcwNDhdLCBbMTI3LjA5ODQyNzU5MzE4NzUxLCAzNy40NTg2MjI1Mzg1NzQ2MV0sIFsxMjcuMDg2NDA0NDA1NzgxNTYsIDM3LjQ3MjY5NzkzNTE4NDY1NV0sIFsxMjcuMDU1OTE3MDQ4MTkwNCwgMzcuNDY1OTIyODkxNDA3N10sIFsxMjcuMDM2MjE5MTUwOTg3OTgsIDM3LjQ4MTc1ODAyNDI3NjAzXSwgWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldLCBbMTI3LjAyMzAyODMxODkwNTU5LCAzNy41MzIzMTg5OTU4MjY2M10sIFsxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFjMTVcdWIwYThcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIzMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhYzE1XHViMGE4XHVhZDZjIiwgIm5hbWVfZW5nIjogIkdhbmduYW0tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjMWQ5MWMwIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDEzOTcxMTk2Njc1MTMsIDM3LjUyNTAzOTg4Mjg5NjY5XSwgWzEyNy4wMzYyMTkxNTA5ODc5OCwgMzcuNDgxNzU4MDI0Mjc2MDNdLCBbMTI3LjA1NTkxNzA0ODE5MDQsIDM3LjQ2NTkyMjg5MTQwNzddLCBbMTI3LjA4NjQwNDQwNTc4MTU2LCAzNy40NzI2OTc5MzUxODQ2NTVdLCBbMTI3LjA5ODQyNzU5MzE4NzUxLCAzNy40NTg2MjI1Mzg1NzQ2MV0sIFsxMjcuMDkwNDY5Mjg1NjU5NTEsIDM3LjQ0Mjk2ODI2MTE0MTg1XSwgWzEyNy4wNjc3ODEwNzYwNTQzMywgMzcuNDI2MTk3NDI0MDU3MzE0XSwgWzEyNy4wNDk1NzIzMjk4NzE0MiwgMzcuNDI4MDU4MzY4NDU2OTRdLCBbMTI3LjAzODgxNzgyNTk3OTIyLCAzNy40NTM4MjAzOTg1MTcxNV0sIFsxMjYuOTkwNzIwNzMxOTU0NjIsIDM3LjQ1NTMyNjE0MzMxMDAyNV0sIFsxMjYuOTgzNjc2NjgyOTE4MDIsIDM3LjQ3Mzg1NjQ5MjY5MjA4Nl0sIFsxMjYuOTgyMjM4MDc5MTYwODEsIDM3LjUwOTMxNDk2Njc3MDMyNl0sIFsxMjcuMDEzOTcxMTk2Njc1MTMsIDM3LjUyNTAzOTg4Mjg5NjY5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWMxMWNcdWNkMDhcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIyMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjMTFjXHVjZDA4XHVhZDZjIiwgIm5hbWVfZW5nIjogIlNlb2Noby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiM0MWI2YzQiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45ODM2NzY2ODI5MTgwMiwgMzcuNDczODU2NDkyNjkyMDg2XSwgWzEyNi45OTA3MjA3MzE5NTQ2MiwgMzcuNDU1MzI2MTQzMzEwMDI1XSwgWzEyNi45NjUyMDQzOTA4NTE0MywgMzcuNDM4MjQ5Nzg0MDA2MjQ2XSwgWzEyNi45NTAwMDAwMTAxMDE4MiwgMzcuNDM2MTM0NTExNjU3MTldLCBbMTI2LjkzMDg0NDA4MDU2NTI1LCAzNy40NDczODI5MjgzMzM5OTRdLCBbMTI2LjkxNjc3MjgxNDY2MDEsIDM3LjQ1NDkwNTY2NDIzNzg5XSwgWzEyNi45MDE1NjA5NDEyOTg5NSwgMzcuNDc3NTM4NDI3ODk5MDFdLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuOTQ5MjI2NjEzODk1MDgsIDM3LjQ5MTI1NDM3NDk1NjQ5XSwgWzEyNi45NzI1ODkxODUwNjYyLCAzNy40NzI1NjEzNjMyNzgxMjVdLCBbMTI2Ljk4MzY3NjY4MjkxODAyLCAzNy40NzM4NTY0OTI2OTIwODZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWQwMFx1YzU0NVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMjEwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFkMDBcdWM1NDVcdWFkNmMiLCAibmFtZV9lbmciOiAiR3dhbmFrLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZjYyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk4MjIzODA3OTE2MDgxLCAzNy41MDkzMTQ5NjY3NzAzMjZdLCBbMTI2Ljk4MzY3NjY4MjkxODAyLCAzNy40NzM4NTY0OTI2OTIwODZdLCBbMTI2Ljk3MjU4OTE4NTA2NjIsIDM3LjQ3MjU2MTM2MzI3ODEyNV0sIFsxMjYuOTQ5MjI2NjEzODk1MDgsIDM3LjQ5MTI1NDM3NDk1NjQ5XSwgWzEyNi45MDUzMTk3NTgwMTgxMiwgMzcuNDgyMTgwODc1NzU0MjldLCBbMTI2LjkyMTc3ODkzMTc0ODI1LCAzNy40OTQ4ODk4Nzc0MTUxNzZdLCBbMTI2LjkyODEwNjI4ODI4Mjc5LCAzNy41MTMyOTU5NTczMjAxNV0sIFsxMjYuOTUyNDk5OTAyOTgxNTksIDM3LjUxNzIyNTAwNzQxODEzXSwgWzEyNi45ODIyMzgwNzkxNjA4MSwgMzcuNTA5MzE0OTY2NzcwMzI2XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIzZDlcdWM3OTFcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIwMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViM2Q5XHVjNzkxXHVhZDZjIiwgIm5hbWVfZW5nIjogIkRvbmdqYWstZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmNjIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuODkxODQ2NjM4NjI3NjQsIDM3LjU0NzM3Mzk3NDk5NzExNF0sIFsxMjYuOTQ1NjY3MzMwODMyMTIsIDM3LjUyNjYxNzU0MjQ1MzM2Nl0sIFsxMjYuOTUyNDk5OTAyOTgxNTksIDM3LjUxNzIyNTAwNzQxODEzXSwgWzEyNi45MjgxMDYyODgyODI3OSwgMzcuNTEzMjk1OTU3MzIwMTVdLCBbMTI2LjkyMTc3ODkzMTc0ODI1LCAzNy40OTQ4ODk4Nzc0MTUxNzZdLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuODk1OTQ3NzY3ODI0ODUsIDM3LjUwNDY3NTI4MTMwOTE3Nl0sIFsxMjYuODgxNTY0MDIzNTM4NjIsIDM3LjUxMzk3MDAzNDc2NTY4NF0sIFsxMjYuODg4MjU3NTc4NjAwOTksIDM3LjU0MDc5NzMzNjMwMjMyXSwgWzEyNi44OTE4NDY2Mzg2Mjc2NCwgMzcuNTQ3MzczOTc0OTk3MTE0XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWM2MDFcdWI0ZjFcdWQzZWNcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTE5MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjNjAxXHViNGYxXHVkM2VjXHVhZDZjIiwgIm5hbWVfZW5nIjogIlllb25nZGV1bmdwby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNjN2U5YjQiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45MDE1NjA5NDEyOTg5NSwgMzcuNDc3NTM4NDI3ODk5MDFdLCBbMTI2LjkxNjc3MjgxNDY2MDEsIDM3LjQ1NDkwNTY2NDIzNzg5XSwgWzEyNi45MzA4NDQwODA1NjUyNSwgMzcuNDQ3MzgyOTI4MzMzOTk0XSwgWzEyNi45MDI1ODMxNzExNjk3LCAzNy40MzQ1NDkzNjYzNDkxMjRdLCBbMTI2Ljg3NjgzMjcxNTAyNDI4LCAzNy40ODI1NzY1OTE2MDczMDVdLCBbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZTA4XHVjYzljXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExODAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWUwOFx1Y2M5Y1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJHZXVtY2hlb24tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjZmZmZmNjIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuODI2ODgwODE1MTczMTQsIDM3LjUwNTQ4OTcyMjMyODk2XSwgWzEyNi44ODE1NjQwMjM1Mzg2MiwgMzcuNTEzOTcwMDM0NzY1Njg0XSwgWzEyNi44OTU5NDc3Njc4MjQ4NSwgMzcuNTA0Njc1MjgxMzA5MTc2XSwgWzEyNi45MDUzMTk3NTgwMTgxMiwgMzcuNDgyMTgwODc1NzU0MjldLCBbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV0sIFsxMjYuODc2ODMyNzE1MDI0MjgsIDM3LjQ4MjU3NjU5MTYwNzMwNV0sIFsxMjYuODQ3NjI2NzYwNTQ5NTMsIDM3LjQ3MTQ2NzIzOTM2MzIzXSwgWzEyNi44MzU0OTQ4NTA3NjE5NiwgMzcuNDc0MDk4MjM2OTc1MDk1XSwgWzEyNi44MjI2NDc5Njc5MTM0OCwgMzcuNDg3ODQ3NjQ5MjE0N10sIFsxMjYuODI1MDQ3MzYzMzE0MDYsIDM3LjUwMzAyNjEyNjQwNDQzXSwgWzEyNi44MjY4ODA4MTUxNzMxNCwgMzcuNTA1NDg5NzIyMzI4OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWQ2Y1x1Yjg1Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTcwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFkNmNcdWI4NWNcdWFkNmMiLCAibmFtZV9lbmciOiAiR3Vyby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi43OTU3NTc2ODU1MjkwNywgMzcuNTc4ODEwODc2MzMyMDJdLCBbMTI2LjgwNzAyMTE1MDIzNTk3LCAzNy42MDEyMzAwMTAxMzIyOF0sIFsxMjYuODIyNTE0Mzg0NzcxMDUsIDM3LjU4ODA0MzA4MTAwODJdLCBbMTI2Ljg1OTg0MTk5Mzk5NjY3LCAzNy41NzE4NDc4NTUyOTI3NDVdLCBbMTI2Ljg5MTg0NjYzODYyNzY0LCAzNy41NDczNzM5NzQ5OTcxMTRdLCBbMTI2Ljg4ODI1NzU3ODYwMDk5LCAzNy41NDA3OTczMzYzMDIzMl0sIFsxMjYuODY2Mzc0NjQzMjEyMzgsIDM3LjU0ODU5MTkxMDk0ODIzXSwgWzEyNi44NjYxMDA3MzQ3NjM5NSwgMzcuNTI2OTk5NjQxNDQ2NjldLCBbMTI2Ljg0MjU3MjkxOTQzMTUzLCAzNy41MjM3MzcwNzgwNTU5Nl0sIFsxMjYuODI0MjMzMTQyNjcyMiwgMzcuNTM3ODgwNzg3NTMyNDhdLCBbMTI2Ljc3MzI0NDE3NzE3NzAzLCAzNy41NDU5MTIzNDUwNTU0XSwgWzEyNi43Njk3OTE4MDU3OTM1MiwgMzcuNTUxMzkxODMwMDg4MDldLCBbMTI2Ljc5NTc1NzY4NTUyOTA3LCAzNy41Nzg4MTA4NzYzMzIwMl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhYzE1XHVjMTFjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExNjAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWMxNVx1YzExY1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJHYW5nc2VvLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZjYyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2LjgyNDIzMzE0MjY3MjIsIDM3LjUzNzg4MDc4NzUzMjQ4XSwgWzEyNi44NDI1NzI5MTk0MzE1MywgMzcuNTIzNzM3MDc4MDU1OTZdLCBbMTI2Ljg2NjEwMDczNDc2Mzk1LCAzNy41MjY5OTk2NDE0NDY2OV0sIFsxMjYuODY2Mzc0NjQzMjEyMzgsIDM3LjU0ODU5MTkxMDk0ODIzXSwgWzEyNi44ODgyNTc1Nzg2MDA5OSwgMzcuNTQwNzk3MzM2MzAyMzJdLCBbMTI2Ljg4MTU2NDAyMzUzODYyLCAzNy41MTM5NzAwMzQ3NjU2ODRdLCBbMTI2LjgyNjg4MDgxNTE3MzE0LCAzNy41MDU0ODk3MjIzMjg5Nl0sIFsxMjYuODI0MjMzMTQyNjcyMiwgMzcuNTM3ODgwNzg3NTMyNDhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzU5MVx1Y2M5Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTUwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM1OTFcdWNjOWNcdWFkNmMiLCAibmFtZV9lbmciOiAiWWFuZ2NoZW9uLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZjYyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2LjkwNTIyMDY1ODMxMDUzLCAzNy41NzQwOTcwMDUyMjU3NF0sIFsxMjYuOTM4OTgxNjE3OTg5NzMsIDM3LjU1MjMxMDAwMzcyODEyNF0sIFsxMjYuOTYzNTgyMjY3MTA4MTIsIDM3LjU1NjA1NjM1NDc1MTU0XSwgWzEyNi45NjQ0ODU3MDU1MzA1NSwgMzcuNTQ4NzA1NjkyMDIxNjM1XSwgWzEyNi45NDU2NjczMzA4MzIxMiwgMzcuNTI2NjE3NTQyNDUzMzY2XSwgWzEyNi44OTE4NDY2Mzg2Mjc2NCwgMzcuNTQ3MzczOTc0OTk3MTE0XSwgWzEyNi44NTk4NDE5OTM5OTY2NywgMzcuNTcxODQ3ODU1MjkyNzQ1XSwgWzEyNi44ODQzMzI4NDc3MzI4OCwgMzcuNTg4MTQzMzIyODgwNTI2XSwgWzEyNi45MDUyMjA2NTgzMTA1MywgMzcuNTc0MDk3MDA1MjI1NzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YjljOFx1ZDNlY1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTQwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWI5YzhcdWQzZWNcdWFkNmMiLCAibmFtZV9lbmciOiAiTWFwby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNjN2U5YjQiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTU1NjU0MjU4NDY0NjMsIDM3LjU3NjA4MDc5MDg4MTQ1Nl0sIFsxMjYuOTY4NzM2MzMyNzkwNzUsIDM3LjU2MzEzNjA0NjkwODI3XSwgWzEyNi45NjM1ODIyNjcxMDgxMiwgMzcuNTU2MDU2MzU0NzUxNTRdLCBbMTI2LjkzODk4MTYxNzk4OTczLCAzNy41NTIzMTAwMDM3MjgxMjRdLCBbMTI2LjkwNTIyMDY1ODMxMDUzLCAzNy41NzQwOTcwMDUyMjU3NF0sIFsxMjYuOTUyNDc1MjAzMDU3MiwgMzcuNjA1MDg2OTI3MzcwNDVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzExY1x1YjMwMFx1YmIzOFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTMwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWMxMWNcdWIzMDBcdWJiMzhcdWFkNmMiLCAibmFtZV9lbmciOiAiU2VvZGFlbXVuLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZjYyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk3Mzg4NjQxMjg3MDIsIDM3LjYyOTQ5NjM0Nzg2ODg4XSwgWzEyNi45NTQyNzAxNzAwNjEyOSwgMzcuNjIyMDMzNDMxMzM5NDI1XSwgWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTA1MjIwNjU4MzEwNTMsIDM3LjU3NDA5NzAwNTIyNTc0XSwgWzEyNi44ODQzMzI4NDc3MzI4OCwgMzcuNTg4MTQzMzIyODgwNTI2XSwgWzEyNi45MDM5NjY4MTAwMzU5NSwgMzcuNTkyMjc0MDM0MTk5NDJdLCBbMTI2LjkwMzAzMDY2MTc3NjY4LCAzNy42MDk5Nzc5MTE0MDEzNDRdLCBbMTI2LjkxNDU1NDgxNDI5NjQ4LCAzNy42NDE1MDA1MDk5NjkzNV0sIFsxMjYuOTU2NDczNzk3Mzg3LCAzNy42NTI0ODA3MzczMzk0NDVdLCBbMTI2Ljk3Mzg4NjQxMjg3MDIsIDM3LjYyOTQ5NjM0Nzg2ODg4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWM3NDBcdWQzYzlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTEyMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjNzQwXHVkM2M5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkV1bnB5ZW9uZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wODM4NzUyNzAzMTk1LCAzNy42OTM1OTUzNDIwMjAzNF0sIFsxMjcuMDk3MDYzOTEzMDk2OTUsIDM3LjY4NjM4MzcxOTM3MjI5NF0sIFsxMjcuMDk0NDA3NjYyOTg3MTcsIDM3LjY0NzEzNDkwNDczMDQ1XSwgWzEyNy4xMTMyNjc5NTg1NTE5OSwgMzcuNjM5NjIyOTA1MzE1OTI1XSwgWzEyNy4xMDc4MjI3NzY4ODEyOSwgMzcuNjE4MDQyNDQyNDEwNjldLCBbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM10sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wNDM1ODgwMDg5NTYwOSwgMzcuNjI4NDg5MzEyOTg3MTVdLCBbMTI3LjA1ODAwMDc1MjIwMDkxLCAzNy42NDMxODI2Mzg3ODI3Nl0sIFsxMjcuMDUyODg0Nzk3MTA0ODUsIDM3LjY4NDIzODU3MDg0MzQ3XSwgWzEyNy4wODM4NzUyNzAzMTk1LCAzNy42OTM1OTUzNDIwMjAzNF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHViMTc4XHVjNmQwXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExMTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YjE3OFx1YzZkMFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJOb3dvbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wNTI4ODQ3OTcxMDQ4NSwgMzcuNjg0MjM4NTcwODQzNDddLCBbMTI3LjA1ODAwMDc1MjIwMDkxLCAzNy42NDMxODI2Mzg3ODI3Nl0sIFsxMjcuMDQzNTg4MDA4OTU2MDksIDM3LjYyODQ4OTMxMjk4NzE1XSwgWzEyNy4wMTQ2NTkzNTg5MjQ2NiwgMzcuNjQ5NDM2ODc0OTY4MTJdLCBbMTI3LjAyMDYyMTE2MTQxMzg5LCAzNy42NjcxNzM1NzU5NzEyMDVdLCBbMTI3LjAxMDM5NjY2MDQyMDcxLCAzNy42ODE4OTQ1ODk2MDM1OTRdLCBbMTI3LjAxNzk1MDk5MjAzNDMyLCAzNy42OTgyNDQxMjc3NTY2Ml0sIFsxMjcuMDUyODg0Nzk3MTA0ODUsIDM3LjY4NDIzODU3MDg0MzQ3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIzYzRcdWJkMDlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTEwMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViM2M0XHViZDA5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkRvYm9uZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45OTM4MzkwMzQyNCwgMzcuNjc2NjgxNzYxMTk5MDg1XSwgWzEyNy4wMTAzOTY2NjA0MjA3MSwgMzcuNjgxODk0NTg5NjAzNTk0XSwgWzEyNy4wMjA2MjExNjE0MTM4OSwgMzcuNjY3MTczNTc1OTcxMjA1XSwgWzEyNy4wMTQ2NTkzNTg5MjQ2NiwgMzcuNjQ5NDM2ODc0OTY4MTJdLCBbMTI3LjA0MzU4ODAwODk1NjA5LCAzNy42Mjg0ODkzMTI5ODcxNV0sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wMzg5MjQwMDk5MjMwMSwgMzcuNjA5NzE1NjExMDIzODE2XSwgWzEyNy4wMTI4MTU0NzQ5NTIzLCAzNy42MTM2NTIyNDM0NzAyNTZdLCBbMTI2Ljk4NjcyNzA1NTEzODY5LCAzNy42MzM3NzY0MTI4ODE5Nl0sIFsxMjYuOTgxNzQ1MjY3NjU1MSwgMzcuNjUyMDk3NjkzODc3NzZdLCBbMTI2Ljk5MzgzOTAzNDI0LCAzNy42NzY2ODE3NjExOTkwODVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWMxNVx1YmQ4MVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDkwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFjMTVcdWJkODFcdWFkNmMiLCAibmFtZV9lbmciOiAiR2FuZ2J1ay1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NzcxNzU0MDY0MTYsIDM3LjYyODU5NzE1NDAwMzg4XSwgWzEyNi45ODY3MjcwNTUxMzg2OSwgMzcuNjMzNzc2NDEyODgxOTZdLCBbMTI3LjAxMjgxNTQ3NDk1MjMsIDM3LjYxMzY1MjI0MzQ3MDI1Nl0sIFsxMjcuMDM4OTI0MDA5OTIzMDEsIDM3LjYwOTcxNTYxMTAyMzgxNl0sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wNzM1MTI0MzgyNTI3OCwgMzcuNjEyODM2NjAzNDIzMTNdLCBbMTI3LjA3MzgyNzA3MDk5MjI3LCAzNy42MDQwMTkyODk4NjQxOV0sIFsxMjcuMDQyNzA1MjIyMDk0LCAzNy41OTIzOTQzNzU5MzM5MV0sIFsxMjcuMDI1MjcyNTQ1MjgwMDMsIDM3LjU3NTI0NjE2MjQ1MjQ5XSwgWzEyNi45OTM0ODI5MzM1ODMxNCwgMzcuNTg4NTY1NDU3MjE2MTU2XSwgWzEyNi45ODg3OTg2NTk5MjM4NCwgMzcuNjExODkyNzMxOTc1Nl0sIFsxMjYuOTc3MTc1NDA2NDE2LCAzNy42Mjg1OTcxNTQwMDM4OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMTMxXHViZDgxXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwODAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzEzMVx1YmQ4MVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJTZW9uZ2J1ay1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wNzM1MTI0MzgyNTI3OCwgMzcuNjEyODM2NjAzNDIzMTNdLCBbMTI3LjEwNzgyMjc3Njg4MTI5LCAzNy42MTgwNDI0NDI0MTA2OV0sIFsxMjcuMTIwMTI0NjAyMDExNCwgMzcuNjAxNzg0NTc1OTgxODhdLCBbMTI3LjEwMzA0MTc0MjQ5MjE0LCAzNy41NzA3NjM0MjI5MDk1NV0sIFsxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XSwgWzEyNy4wNzM4MjcwNzA5OTIyNywgMzcuNjA0MDE5Mjg5ODY0MTldLCBbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjOTExXHViNzkxXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNzAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzkxMVx1Yjc5MVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJKdW5nbmFuZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjUyNzI1NDUyODAwMywgMzcuNTc1MjQ2MTYyNDUyNDldLCBbMTI3LjA0MjcwNTIyMjA5NCwgMzcuNTkyMzk0Mzc1OTMzOTFdLCBbMTI3LjA3MzgyNzA3MDk5MjI3LCAzNy42MDQwMTkyODk4NjQxOV0sIFsxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA1MDA1NjAxMDgxNTY3LCAzNy41Njc1Nzc2MTI1OTA4NDZdLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdLCBbMTI3LjAyNTI3MjU0NTI4MDAzLCAzNy41NzUyNDYxNjI0NTI0OV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHViM2Q5XHViMzAwXHViYjM4XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNjAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YjNkOVx1YjMwMFx1YmIzOFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJEb25nZGFlbXVuLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZjYyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA4MDY4NTQxMjgwNDAzLCAzNy41NjkwNjQyNTUxOTAxN10sIFsxMjcuMTAzMDQxNzQyNDkyMTQsIDM3LjU3MDc2MzQyMjkwOTU1XSwgWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XSwgWzEyNy4xMTE2NzY0MjAzNjA4LCAzNy41NDA2Njk5NTUzMjQ5NjVdLCBbMTI3LjEwMDg3NTE5NzkxOTYyLCAzNy41MjQ4NDEyMjAxNjcwNTVdLCBbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl0sIFsxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA4MDY4NTQxMjgwNDAzLCAzNy41NjkwNjQyNTUxOTAxN11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZDExXHVjOWM0XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWQxMVx1YzljNFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJHd2FuZ2ppbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjU0NzI2NjM0OTk3NiwgMzcuNTY4OTQzNTUyMjM3NzM0XSwgWzEyNy4wNTAwNTYwMTA4MTU2NywgMzcuNTY3NTc3NjEyNTkwODQ2XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA1ODY3MzU5Mjg4Mzk4LCAzNy41MjYyOTk3NDkyMjU2OF0sIFsxMjcuMDIzMDI4MzE4OTA1NTksIDM3LjUzMjMxODk5NTgyNjYzXSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzEzMVx1YjNkOVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDQwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWMxMzFcdWIzZDlcdWFkNmMiLCAibmFtZV9lbmciOiAiU2Vvbmdkb25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZjYyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjAxMDcwODk0MTc3NDgyLCAzNy41NDExODA0ODk2NDc2Ml0sIFsxMjcuMDIzMDI4MzE4OTA1NTksIDM3LjUzMjMxODk5NTgyNjYzXSwgWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldLCBbMTI2Ljk4MjIzODA3OTE2MDgxLCAzNy41MDkzMTQ5NjY3NzAzMjZdLCBbMTI2Ljk1MjQ5OTkwMjk4MTU5LCAzNy41MTcyMjUwMDc0MTgxM10sIFsxMjYuOTQ1NjY3MzMwODMyMTIsIDM3LjUyNjYxNzU0MjQ1MzM2Nl0sIFsxMjYuOTY0NDg1NzA1NTMwNTUsIDM3LjU0ODcwNTY5MjAyMTYzNV0sIFsxMjYuOTg3NTI5OTY5MDMzMjgsIDM3LjU1MDk0ODE4ODA3MTM5XSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzZhOVx1YzBiMFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDMwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM2YTlcdWMwYjBcdWFkNmMiLCAibmFtZV9lbmciOiAiWW9uZ3Nhbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiM3ZmNkYmIiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjU0NzI2NjM0OTk3NiwgMzcuNTY4OTQzNTUyMjM3NzM0XSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdLCBbMTI2Ljk4NzUyOTk2OTAzMzI4LCAzNy41NTA5NDgxODgwNzEzOV0sIFsxMjYuOTY0NDg1NzA1NTMwNTUsIDM3LjU0ODcwNTY5MjAyMTYzNV0sIFsxMjYuOTYzNTgyMjY3MTA4MTIsIDM3LjU1NjA1NjM1NDc1MTU0XSwgWzEyNi45Njg3MzYzMzI3OTA3NSwgMzcuNTYzMTM2MDQ2OTA4MjddLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzkxMVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDIwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM5MTFcdWFkNmMiLCAibmFtZV9lbmciOiAiSnVuZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiMyMjVlYTgiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NzM4ODY0MTI4NzAyLCAzNy42Mjk0OTYzNDc4Njg4OF0sIFsxMjYuOTc3MTc1NDA2NDE2LCAzNy42Mjg1OTcxNTQwMDM4OF0sIFsxMjYuOTg4Nzk4NjU5OTIzODQsIDM3LjYxMTg5MjczMTk3NTZdLCBbMTI2Ljk5MzQ4MjkzMzU4MzE0LCAzNy41ODg1NjU0NTcyMTYxNTZdLCBbMTI3LjAyNTI3MjU0NTI4MDAzLCAzNy41NzUyNDYxNjI0NTI0OV0sIFsxMjcuMDI1NDcyNjYzNDk5NzYsIDM3LjU2ODk0MzU1MjIzNzczNF0sIFsxMjYuOTY4NzM2MzMyNzkwNzUsIDM3LjU2MzEzNjA0NjkwODI3XSwgWzEyNi45NTU2NTQyNTg0NjQ2MywgMzcuNTc2MDgwNzkwODgxNDU2XSwgWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTU0MjcwMTcwMDYxMjksIDM3LjYyMjAzMzQzMTMzOTQyNV0sIFsxMjYuOTczODg2NDEyODcwMiwgMzcuNjI5NDk2MzQ3ODY4ODhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1Yzg4NVx1Yjg1Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDEwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM4ODVcdWI4NWNcdWFkNmMiLCAibmFtZV9lbmciOiAiSm9uZ25vLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiIzQxYjZjNCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn1dLCAidHlwZSI6ICJGZWF0dXJlQ29sbGVjdGlvbiJ9CiAgICAgICAgICAgIAogICAgICAgICAgICApLmFkZFRvKG1hcF84MjYyNmQ2MTEzZDQ0OGIyYmM2MTkwZGYyZTJiMjZkMSk7CiAgICAgICAgZ2VvX2pzb25fMzI3ZjY5YmNiNmM4NDg1MjgwZDNkN2RhNDM3MmNmZmQuc2V0U3R5bGUoZnVuY3Rpb24oZmVhdHVyZSkge3JldHVybiBmZWF0dXJlLnByb3BlcnRpZXMuc3R5bGU7fSk7CiAgICAgICAgCiAgICAKICAgIHZhciBjb2xvcl9tYXBfYzMyNTc0MWFkMTMyNDMyMDgwZDEwOGJjODc3MjA4YTcgPSB7fTsKCiAgICAKICAgIGNvbG9yX21hcF9jMzI1NzQxYWQxMzI0MzIwODBkMTA4YmM4NzcyMDhhNy5jb2xvciA9IGQzLnNjYWxlLnRocmVzaG9sZCgpCiAgICAgICAgICAgICAgLmRvbWFpbihbMzEuNTUwNywgMzIuMzY0MTA0MDA4MDE2MDMsIDMzLjE3NzUwODAxNjAzMjA2NCwgMzMuOTkwOTEyMDI0MDQ4MDksIDM0LjgwNDMxNjAzMjA2NDEzLCAzNS42MTc3MjAwNDAwODAxNiwgMzYuNDMxMTI0MDQ4MDk2MTk0LCAzNy4yNDQ1MjgwNTYxMTIyMiwgMzguMDU3OTMyMDY0MTI4MjUsIDM4Ljg3MTMzNjA3MjE0NDI5LCAzOS42ODQ3NDAwODAxNjAzMiwgNDAuNDk4MTQ0MDg4MTc2MzUsIDQxLjMxMTU0ODA5NjE5MjM4LCA0Mi4xMjQ5NTIxMDQyMDg0MiwgNDIuOTM4MzU2MTEyMjI0NDUsIDQzLjc1MTc2MDEyMDI0MDQ3NiwgNDQuNTY1MTY0MTI4MjU2NTEsIDQ1LjM3ODU2ODEzNjI3MjU1LCA0Ni4xOTE5NzIxNDQyODg1OCwgNDcuMDA1Mzc2MTUyMzA0NjA2LCA0Ny44MTg3ODAxNjAzMjA2NCwgNDguNjMyMTg0MTY4MzM2NjcsIDQ5LjQ0NTU4ODE3NjM1MjcsIDUwLjI1ODk5MjE4NDM2ODczNiwgNTEuMDcyMzk2MTkyMzg0NzcsIDUxLjg4NTgwMDIwMDQwMDgsIDUyLjY5OTIwNDIwODQxNjgzLCA1My41MTI2MDgyMTY0MzI4NywgNTQuMzI2MDEyMjI0NDQ4ODk1LCA1NS4xMzk0MTYyMzI0NjQ5MjQsIDU1Ljk1MjgyMDI0MDQ4MDk2LCA1Ni43NjYyMjQyNDg0OTcsIDU3LjU3OTYyODI1NjUxMzAyNiwgNTguMzkzMDMyMjY0NTI5MDU0LCA1OS4yMDY0MzYyNzI1NDUwOSwgNjAuMDE5ODQwMjgwNTYxMTMsIDYwLjgzMzI0NDI4ODU3NzE1NiwgNjEuNjQ2NjQ4Mjk2NTkzMTg1LCA2Mi40NjAwNTIzMDQ2MDkyMiwgNjMuMjczNDU2MzEyNjI1MjUsIDY0LjA4Njg2MDMyMDY0MTI4LCA2NC45MDAyNjQzMjg2NTczMSwgNjUuNzEzNjY4MzM2NjczMzUsIDY2LjUyNzA3MjM0NDY4OTM3LCA2Ny4zNDA0NzYzNTI3MDU0MSwgNjguMTUzODgwMzYwNzIxNDQsIDY4Ljk2NzI4NDM2ODczNzQ3LCA2OS43ODA2ODgzNzY3NTM1MiwgNzAuNTk0MDkyMzg0NzY5NTQsIDcxLjQwNzQ5NjM5Mjc4NTU2LCA3Mi4yMjA5MDA0MDA4MDE2MSwgNzMuMDM0MzA0NDA4ODE3NjMsIDczLjg0NzcwODQxNjgzMzY3LCA3NC42NjExMTI0MjQ4NDk3LCA3NS40NzQ1MTY0MzI4NjU3MywgNzYuMjg3OTIwNDQwODgxNzYsIDc3LjEwMTMyNDQ0ODg5NzgsIDc3LjkxNDcyODQ1NjkxMzgyLCA3OC43MjgxMzI0NjQ5Mjk4NiwgNzkuNTQxNTM2NDcyOTQ1OSwgODAuMzU0OTQwNDgwOTYxOTEsIDgxLjE2ODM0NDQ4ODk3Nzk3LCA4MS45ODE3NDg0OTY5OTM5OSwgODIuNzk1MTUyNTA1MDEwMDIsIDgzLjYwODU1NjUxMzAyNjA2LCA4NC40MjE5NjA1MjEwNDIwOCwgODUuMjM1MzY0NTI5MDU4MTIsIDg2LjA0ODc2ODUzNzA3NDE1LCA4Ni44NjIxNzI1NDUwOTAxNywgODcuNjc1NTc2NTUzMTA2MjEsIDg4LjQ4ODk4MDU2MTEyMjI1LCA4OS4zMDIzODQ1NjkxMzgyNywgOTAuMTE1Nzg4NTc3MTU0MzIsIDkwLjkyOTE5MjU4NTE3MDM0LCA5MS43NDI1OTY1OTMxODYzNiwgOTIuNTU2MDAwNjAxMjAyNDEsIDkzLjM2OTQwNDYwOTIxODQ0LCA5NC4xODI4MDg2MTcyMzQ0NywgOTQuOTk2MjEyNjI1MjUwNTEsIDk1LjgwOTYxNjYzMzI2NjUzLCA5Ni42MjMwMjA2NDEyODI1NSwgOTcuNDM2NDI0NjQ5Mjk4NiwgOTguMjQ5ODI4NjU3MzE0NjIsIDk5LjA2MzIzMjY2NTMzMDY0LCA5OS44NzY2MzY2NzMzNDY3LCAxMDAuNjkwMDQwNjgxMzYyNzIsIDEwMS41MDM0NDQ2ODkzNzg3NywgMTAyLjMxNjg0ODY5NzM5NDc5LCAxMDMuMTMwMjUyNzA1NDEwODEsIDEwMy45NDM2NTY3MTM0MjY4MywgMTA0Ljc1NzA2MDcyMTQ0Mjg4LCAxMDUuNTcwNDY0NzI5NDU4OSwgMTA2LjM4Mzg2ODczNzQ3NDk2LCAxMDcuMTk3MjcyNzQ1NDkwOTgsIDEwOC4wMTA2NzY3NTM1MDcwMywgMTA4LjgyNDA4MDc2MTUyMzA1LCAxMDkuNjM3NDg0NzY5NTM5MDcsIDExMC40NTA4ODg3Nzc1NTUxLCAxMTEuMjY0MjkyNzg1NTcxMTQsIDExMi4wNzc2OTY3OTM1ODcxNywgMTEyLjg5MTEwMDgwMTYwMzIyLCAxMTMuNzA0NTA0ODA5NjE5MjQsIDExNC41MTc5MDg4MTc2MzUyNiwgMTE1LjMzMTMxMjgyNTY1MTMxLCAxMTYuMTQ0NzE2ODMzNjY3MzMsIDExNi45NTgxMjA4NDE2ODMzNSwgMTE3Ljc3MTUyNDg0OTY5OTQsIDExOC41ODQ5Mjg4NTc3MTU0MywgMTE5LjM5ODMzMjg2NTczMTQ4LCAxMjAuMjExNzM2ODczNzQ3NSwgMTIxLjAyNTE0MDg4MTc2MzUyLCAxMjEuODM4NTQ0ODg5Nzc5NTQsIDEyMi42NTE5NDg4OTc3OTU1OSwgMTIzLjQ2NTM1MjkwNTgxMTYxLCAxMjQuMjc4NzU2OTEzODI3NjYsIDEyNS4wOTIxNjA5MjE4NDM2OSwgMTI1LjkwNTU2NDkyOTg1OTcxLCAxMjYuNzE4OTY4OTM3ODc1NzYsIDEyNy41MzIzNzI5NDU4OTE3OCwgMTI4LjM0NTc3Njk1MzkwNzgsIDEyOS4xNTkxODA5NjE5MjM4NSwgMTI5Ljk3MjU4NDk2OTkzOTg3LCAxMzAuNzg1OTg4OTc3OTU1OTIsIDEzMS41OTkzOTI5ODU5NzE5NSwgMTMyLjQxMjc5Njk5Mzk4Nzk3LCAxMzMuMjI2MjAxMDAyMDA0LCAxMzQuMDM5NjA1MDEwMDIwMDQsIDEzNC44NTMwMDkwMTgwMzYwNiwgMTM1LjY2NjQxMzAyNjA1MjEsIDEzNi40Nzk4MTcwMzQwNjgxMywgMTM3LjI5MzIyMTA0MjA4NDE2LCAxMzguMTA2NjI1MDUwMTAwMiwgMTM4LjkyMDAyOTA1ODExNjIzLCAxMzkuNzMzNDMzMDY2MTMyMjUsIDE0MC41NDY4MzcwNzQxNDgzLCAxNDEuMzYwMjQxMDgyMTY0MzIsIDE0Mi4xNzM2NDUwOTAxODAzNywgMTQyLjk4NzA0OTA5ODE5NjQsIDE0My44MDA0NTMxMDYyMTI0MiwgMTQ0LjYxMzg1NzExNDIyODQ0LCAxNDUuNDI3MjYxMTIyMjQ0NSwgMTQ2LjI0MDY2NTEzMDI2MDUsIDE0Ny4wNTQwNjkxMzgyNzY1NiwgMTQ3Ljg2NzQ3MzE0NjI5MjU4LCAxNDguNjgwODc3MTU0MzA4NjMsIDE0OS40OTQyODExNjIzMjQ2NSwgMTUwLjMwNzY4NTE3MDM0MDY4LCAxNTEuMTIxMDg5MTc4MzU2NywgMTUxLjkzNDQ5MzE4NjM3Mjc1LCAxNTIuNzQ3ODk3MTk0Mzg4NzcsIDE1My41NjEzMDEyMDI0MDQ4MiwgMTU0LjM3NDcwNTIxMDQyMDg0LCAxNTUuMTg4MTA5MjE4NDM2ODYsIDE1Ni4wMDE1MTMyMjY0NTI5LCAxNTYuODE0OTE3MjM0NDY4OTQsIDE1Ny42MjgzMjEyNDI0ODQ5NiwgMTU4LjQ0MTcyNTI1MDUwMSwgMTU5LjI1NTEyOTI1ODUxNzAzLCAxNjAuMDY4NTMzMjY2NTMzMDgsIDE2MC44ODE5MzcyNzQ1NDkxLCAxNjEuNjk1MzQxMjgyNTY1MTIsIDE2Mi41MDg3NDUyOTA1ODExNywgMTYzLjMyMjE0OTI5ODU5NzIsIDE2NC4xMzU1NTMzMDY2MTMyMiwgMTY0Ljk0ODk1NzMxNDYyOTI3LCAxNjUuNzYyMzYxMzIyNjQ1MzIsIDE2Ni41NzU3NjUzMzA2NjEzLCAxNjcuMzg5MTY5MzM4Njc3MzYsIDE2OC4yMDI1NzMzNDY2OTMzOCwgMTY5LjAxNTk3NzM1NDcwOTQzLCAxNjkuODI5MzgxMzYyNzI1NDYsIDE3MC42NDI3ODUzNzA3NDE0OCwgMTcxLjQ1NjE4OTM3ODc1NzUzLCAxNzIuMjY5NTkzMzg2NzczNTUsIDE3My4wODI5OTczOTQ3ODk1NywgMTczLjg5NjQwMTQwMjgwNTYyLCAxNzQuNzA5ODA1NDEwODIxNjQsIDE3NS41MjMyMDk0MTg4Mzc3LCAxNzYuMzM2NjEzNDI2ODUzNywgMTc3LjE1MDAxNzQzNDg2OTc0LCAxNzcuOTYzNDIxNDQyODg1OCwgMTc4Ljc3NjgyNTQ1MDkwMTgsIDE3OS41OTAyMjk0NTg5MTc4MywgMTgwLjQwMzYzMzQ2NjkzMzg4LCAxODEuMjE3MDM3NDc0OTQ5OSwgMTgyLjAzMDQ0MTQ4Mjk2NTk1LCAxODIuODQzODQ1NDkwOTgxOTUsIDE4My42NTcyNDk0OTg5OTgsIDE4NC40NzA2NTM1MDcwMTQwNSwgMTg1LjI4NDA1NzUxNTAzMDA3LCAxODYuMDk3NDYxNTIzMDQ2MSwgMTg2LjkxMDg2NTUzMTA2MjExLCAxODcuNzI0MjY5NTM5MDc4MTYsIDE4OC41Mzc2NzM1NDcwOTQyMiwgMTg5LjM1MTA3NzU1NTExMDIsIDE5MC4xNjQ0ODE1NjMxMjYyNiwgMTkwLjk3Nzg4NTU3MTE0MjI4LCAxOTEuNzkxMjg5NTc5MTU4MzMsIDE5Mi42MDQ2OTM1ODcxNzQzNSwgMTkzLjQxODA5NzU5NTE5MDM3LCAxOTQuMjMxNTAxNjAzMjA2NDIsIDE5NS4wNDQ5MDU2MTEyMjI0NSwgMTk1Ljg1ODMwOTYxOTIzODQ3LCAxOTYuNjcxNzEzNjI3MjU0NTIsIDE5Ny40ODUxMTc2MzUyNzA1NCwgMTk4LjI5ODUyMTY0MzI4NjYsIDE5OS4xMTE5MjU2NTEzMDI2LCAxOTkuOTI1MzI5NjU5MzE4NjMsIDIwMC43Mzg3MzM2NjczMzQ2OSwgMjAxLjU1MjEzNzY3NTM1MDcsIDIwMi4zNjU1NDE2ODMzNjY3MywgMjAzLjE3ODk0NTY5MTM4Mjc4LCAyMDMuOTkyMzQ5Njk5Mzk4OCwgMjA0LjgwNTc1MzcwNzQxNDg1LCAyMDUuNjE5MTU3NzE1NDMwODQsIDIwNi40MzI1NjE3MjM0NDY5LCAyMDcuMjQ1OTY1NzMxNDYyOTUsIDIwOC4wNTkzNjk3Mzk0Nzg5NywgMjA4Ljg3Mjc3Mzc0NzQ5NSwgMjA5LjY4NjE3Nzc1NTUxMSwgMjEwLjQ5OTU4MTc2MzUyNzA2LCAyMTEuMzEyOTg1NzcxNTQzMSwgMjEyLjEyNjM4OTc3OTU1OTEsIDIxMi45Mzk3OTM3ODc1NzUxNiwgMjEzLjc1MzE5Nzc5NTU5MTE4LCAyMTQuNTY2NjAxODAzNjA3MjMsIDIxNS4zODAwMDU4MTE2MjMyNSwgMjE2LjE5MzQwOTgxOTYzOTI3LCAyMTcuMDA2ODEzODI3NjU1MzIsIDIxNy44MjAyMTc4MzU2NzEzNywgMjE4LjYzMzYyMTg0MzY4NzM3LCAyMTkuNDQ3MDI1ODUxNzAzNDIsIDIyMC4yNjA0Mjk4NTk3MTk0NCwgMjIxLjA3MzgzMzg2NzczNTUsIDIyMS44ODcyMzc4NzU3NTE1LCAyMjIuNzAwNjQxODgzNzY3NTMsIDIyMy41MTQwNDU4OTE3ODM1OCwgMjI0LjMyNzQ0OTg5OTc5OTYsIDIyNS4xNDA4NTM5MDc4MTU2MywgMjI1Ljk1NDI1NzkxNTgzMTY4LCAyMjYuNzY3NjYxOTIzODQ3NywgMjI3LjU4MTA2NTkzMTg2Mzc1LCAyMjguMzk0NDY5OTM5ODc5NzQsIDIyOS4yMDc4NzM5NDc4OTU4LCAyMzAuMDIxMjc3OTU1OTExODQsIDIzMC44MzQ2ODE5NjM5Mjc4NiwgMjMxLjY0ODA4NTk3MTk0Mzg5LCAyMzIuNDYxNDg5OTc5OTU5OTQsIDIzMy4yNzQ4OTM5ODc5NzU5NiwgMjM0LjA4ODI5Nzk5NTk5MiwgMjM0LjkwMTcwMjAwNDAwOCwgMjM1LjcxNTEwNjAxMjAyNDA1LCAyMzYuNTI4NTEwMDIwMDQwMSwgMjM3LjM0MTkxNDAyODA1NjEyLCAyMzguMTU1MzE4MDM2MDcyMTUsIDIzOC45Njg3MjIwNDQwODgxNywgMjM5Ljc4MjEyNjA1MjEwNDIyLCAyNDAuNTk1NTMwMDYwMTIwMjcsIDI0MS40MDg5MzQwNjgxMzYyNiwgMjQyLjIyMjMzODA3NjE1MjMsIDI0My4wMzU3NDIwODQxNjgzMywgMjQzLjg0OTE0NjA5MjE4NDM4LCAyNDQuNjYyNTUwMTAwMjAwNCwgMjQ1LjQ3NTk1NDEwODIxNjQzLCAyNDYuMjg5MzU4MTE2MjMyNDgsIDI0Ny4xMDI3NjIxMjQyNDg1LCAyNDcuOTE2MTY2MTMyMjY0NTIsIDI0OC43Mjk1NzAxNDAyODA1NywgMjQ5LjU0Mjk3NDE0ODI5NjYsIDI1MC4zNTYzNzgxNTYzMTI2NCwgMjUxLjE2OTc4MjE2NDMyODY3LCAyNTEuOTgzMTg2MTcyMzQ0NywgMjUyLjc5NjU5MDE4MDM2MDc0LCAyNTMuNjA5OTk0MTg4Mzc2NzYsIDI1NC40MjMzOTgxOTYzOTI3OCwgMjU1LjIzNjgwMjIwNDQwODgzLCAyNTYuMDUwMjA2MjEyNDI0OCwgMjU2Ljg2MzYxMDIyMDQ0MDksIDI1Ny42NzcwMTQyMjg0NTY4NywgMjU4LjQ5MDQxODIzNjQ3MjksIDI1OS4zMDM4MjIyNDQ0ODg5NywgMjYwLjExNzIyNjI1MjUwNSwgMjYwLjkzMDYzMDI2MDUyMSwgMjYxLjc0NDAzNDI2ODUzNzA2LCAyNjIuNTU3NDM4Mjc2NTUzMSwgMjYzLjM3MDg0MjI4NDU2OTE2LCAyNjQuMTg0MjQ2MjkyNTg1MTYsIDI2NC45OTc2NTAzMDA2MDEyLCAyNjUuODExMDU0MzA4NjE3MjYsIDI2Ni42MjQ0NTgzMTY2MzMyNSwgMjY3LjQzNzg2MjMyNDY0OTMsIDI2OC4yNTEyNjYzMzI2NjUzLCAyNjkuMDY0NjcwMzQwNjgxMzUsIDI2OS44NzgwNzQzNDg2OTc0LCAyNzAuNjkxNDc4MzU2NzEzNCwgMjcxLjUwNDg4MjM2NDcyOTQ0LCAyNzIuMzE4Mjg2MzcyNzQ1NSwgMjczLjEzMTY5MDM4MDc2MTU0LCAyNzMuOTQ1MDk0Mzg4Nzc3NTMsIDI3NC43NTg0OTgzOTY3OTM2LCAyNzUuNTcxOTAyNDA0ODA5NjMsIDI3Ni4zODUzMDY0MTI4MjU2LCAyNzcuMTk4NzEwNDIwODQxNywgMjc4LjAxMjExNDQyODg1NzcsIDI3OC44MjU1MTg0MzY4NzM3LCAyNzkuNjM4OTIyNDQ0ODg5OCwgMjgwLjQ1MjMyNjQ1MjkwNTc3LCAyODEuMjY1NzMwNDYwOTIxOCwgMjgyLjA3OTEzNDQ2ODkzNzg3LCAyODIuODkyNTM4NDc2OTUzOSwgMjgzLjcwNTk0MjQ4NDk2OTksIDI4NC41MTkzNDY0OTI5ODU5NiwgMjg1LjMzMjc1MDUwMTAwMiwgMjg2LjE0NjE1NDUwOTAxODA2LCAyODYuOTU5NTU4NTE3MDM0MDUsIDI4Ny43NzI5NjI1MjUwNTAxLCAyODguNTg2MzY2NTMzMDY2MTUsIDI4OS4zOTk3NzA1NDEwODIxNSwgMjkwLjIxMzE3NDU0OTA5ODIsIDI5MS4wMjY1Nzg1NTcxMTQyNSwgMjkxLjgzOTk4MjU2NTEzMDI0LCAyOTIuNjUzMzg2NTczMTQ2MywgMjkzLjQ2Njc5MDU4MTE2MjM0LCAyOTQuMjgwMTk0NTg5MTc4NCwgMjk1LjA5MzU5ODU5NzE5NDQsIDI5NS45MDcwMDI2MDUyMTA0NCwgMjk2LjcyMDQwNjYxMzIyNjQzLCAyOTcuNTMzODEwNjIxMjQyNSwgMjk4LjM0NzIxNDYyOTI1ODUzLCAyOTkuMTYwNjE4NjM3Mjc0NiwgMjk5Ljk3NDAyMjY0NTI5MDYzLCAzMDAuNzg3NDI2NjUzMzA2NiwgMzAxLjYwMDgzMDY2MTMyMjYsIDMwMi40MTQyMzQ2NjkzMzg2NywgMzAzLjIyNzYzODY3NzM1NDcsIDMwNC4wNDEwNDI2ODUzNzA3NywgMzA0Ljg1NDQ0NjY5MzM4Njc2LCAzMDUuNjY3ODUwNzAxNDAyOCwgMzA2LjQ4MTI1NDcwOTQxODg2LCAzMDcuMjk0NjU4NzE3NDM0OSwgMzA4LjEwODA2MjcyNTQ1MDksIDMwOC45MjE0NjY3MzM0NjY5LCAzMDkuNzM0ODcwNzQxNDgyOTUsIDMxMC41NDgyNzQ3NDk0OTksIDMxMS4zNjE2Nzg3NTc1MTUwNSwgMzEyLjE3NTA4Mjc2NTUzMTEsIDMxMi45ODg0ODY3NzM1NDcxLCAzMTMuODAxODkwNzgxNTYzMTUsIDMxNC42MTUyOTQ3ODk1NzkxNCwgMzE1LjQyODY5ODc5NzU5NTIsIDMxNi4yNDIxMDI4MDU2MTEyNCwgMzE3LjA1NTUwNjgxMzYyNzIzLCAzMTcuODY4OTEwODIxNjQzMywgMzE4LjY4MjMxNDgyOTY1OTMzLCAzMTkuNDk1NzE4ODM3Njc1NCwgMzIwLjMwOTEyMjg0NTY5MTQzLCAzMjEuMTIyNTI2ODUzNzA3MzcsIDMyMS45MzU5MzA4NjE3MjM0LCAzMjIuNzQ5MzM0ODY5NzM5NDcsIDMyMy41NjI3Mzg4Nzc3NTU1LCAzMjQuMzc2MTQyODg1NzcxNTcsIDMyNS4xODk1NDY4OTM3ODc1NiwgMzI2LjAwMjk1MDkwMTgwMzYsIDMyNi44MTYzNTQ5MDk4MTk2NywgMzI3LjYyOTc1ODkxNzgzNTY2LCAzMjguNDQzMTYyOTI1ODUxNywgMzI5LjI1NjU2NjkzMzg2Nzc2LCAzMzAuMDY5OTcwOTQxODgzNzUsIDMzMC44ODMzNzQ5NDk4OTk4LCAzMzEuNjk2Nzc4OTU3OTE1ODUsIDMzMi41MTAxODI5NjU5MzE5LCAzMzMuMzIzNTg2OTczOTQ3OTUsIDMzNC4xMzY5OTA5ODE5NjM5LCAzMzQuOTUwMzk0OTg5OTc5OTQsIDMzNS43NjM3OTg5OTc5OTYsIDMzNi41NzcyMDMwMDYwMTIwNCwgMzM3LjM5MDYwNzAxNDAyODEsIDMzOC4yMDQwMTEwMjIwNDQxLCAzMzkuMDE3NDE1MDMwMDYwMTQsIDMzOS44MzA4MTkwMzgwNzYyLCAzNDAuNjQ0MjIzMDQ2MDkyMiwgMzQxLjQ1NzYyNzA1NDEwODIzLCAzNDIuMjcxMDMxMDYyMTI0MiwgMzQzLjA4NDQzNTA3MDE0MDMsIDM0My44OTc4MzkwNzgxNTYzLCAzNDQuNzExMjQzMDg2MTcyNCwgMzQ1LjUyNDY0NzA5NDE4ODQsIDM0Ni4zMzgwNTExMDIyMDQzNiwgMzQ3LjE1MTQ1NTExMDIyMDQsIDM0Ny45NjQ4NTkxMTgyMzY0NiwgMzQ4Ljc3ODI2MzEyNjI1MjUsIDM0OS41OTE2NjcxMzQyNjg1NiwgMzUwLjQwNTA3MTE0MjI4NDU2LCAzNTEuMjE4NDc1MTUwMzAwNiwgMzUyLjAzMTg3OTE1ODMxNjY2LCAzNTIuODQ1MjgzMTY2MzMyNjUsIDM1My42NTg2ODcxNzQzNDg3LCAzNTQuNDcyMDkxMTgyMzY0NywgMzU1LjI4NTQ5NTE5MDM4MDc0LCAzNTYuMDk4ODk5MTk4Mzk2OCwgMzU2LjkxMjMwMzIwNjQxMjg0LCAzNTcuNzI1NzA3MjE0NDI4OSwgMzU4LjUzOTExMTIyMjQ0NDksIDM1OS4zNTI1MTUyMzA0NjA5LCAzNjAuMTY1OTE5MjM4NDc2OTMsIDM2MC45NzkzMjMyNDY0OTMsIDM2MS43OTI3MjcyNTQ1MDkwMywgMzYyLjYwNjEzMTI2MjUyNTEsIDM2My40MTk1MzUyNzA1NDExLCAzNjQuMjMyOTM5Mjc4NTU3MSwgMzY1LjA0NjM0MzI4NjU3MzIsIDM2NS44NTk3NDcyOTQ1ODkxNywgMzY2LjY3MzE1MTMwMjYwNTIsIDM2Ny40ODY1NTUzMTA2MjEyLCAzNjguMjk5OTU5MzE4NjM3MjYsIDM2OS4xMTMzNjMzMjY2NTMzLCAzNjkuOTI2NzY3MzM0NjY5MzYsIDM3MC43NDAxNzEzNDI2ODU0LCAzNzEuNTUzNTc1MzUwNzAxNCwgMzcyLjM2Njk3OTM1ODcxNzQsIDM3My4xODAzODMzNjY3MzM0NSwgMzczLjk5Mzc4NzM3NDc0OTUsIDM3NC44MDcxOTEzODI3NjU1NSwgMzc1LjYyMDU5NTM5MDc4MTU1LCAzNzYuNDMzOTk5Mzk4Nzk3NiwgMzc3LjI0NzQwMzQwNjgxMzY1LCAzNzguMDYwODA3NDE0ODI5NywgMzc4Ljg3NDIxMTQyMjg0NTcsIDM3OS42ODc2MTU0MzA4NjE3LCAzODAuNTAxMDE5NDM4ODc3NzMsIDM4MS4zMTQ0MjM0NDY4OTM4LCAzODIuMTI3ODI3NDU0OTA5ODMsIDM4Mi45NDEyMzE0NjI5MjU5LCAzODMuNzU0NjM1NDcwOTQxOSwgMzg0LjU2ODAzOTQ3ODk1NzksIDM4NS4zODE0NDM0ODY5NzM5LCAzODYuMTk0ODQ3NDk0OTksIDM4Ny4wMDgyNTE1MDMwMDYsIDM4Ny44MjE2NTU1MTEwMjIsIDM4OC42MzUwNTk1MTkwMzgwNywgMzg5LjQ0ODQ2MzUyNzA1NDEsIDM5MC4yNjE4Njc1MzUwNzAxNywgMzkxLjA3NTI3MTU0MzA4NjIsIDM5MS44ODg2NzU1NTExMDIxNSwgMzkyLjcwMjA3OTU1OTExODIsIDM5My41MTU0ODM1NjcxMzQyNSwgMzk0LjMyODg4NzU3NTE1MDMsIDM5NS4xNDIyOTE1ODMxNjYzNSwgMzk1Ljk1NTY5NTU5MTE4MjM1LCAzOTYuNzY5MDk5NTk5MTk4NCwgMzk3LjU4MjUwMzYwNzIxNDQ1LCAzOTguMzk1OTA3NjE1MjMwNDQsIDM5OS4yMDkzMTE2MjMyNDY1LCA0MDAuMDIyNzE1NjMxMjYyNTQsIDQwMC44MzYxMTk2MzkyNzg1NCwgNDAxLjY0OTUyMzY0NzI5NDYsIDQwMi40NjI5Mjc2NTUzMTA2NCwgNDAzLjI3NjMzMTY2MzMyNjcsIDQwNC4wODk3MzU2NzEzNDI3NCwgNDA0LjkwMzEzOTY3OTM1ODcsIDQwNS43MTY1NDM2ODczNzQ3LCA0MDYuNTI5OTQ3Njk1MzkwOCwgNDA3LjM0MzM1MTcwMzQwNjgsIDQwOC4xNTY3NTU3MTE0MjI5LCA0MDguOTcwMTU5NzE5NDM4ODcsIDQwOS43ODM1NjM3Mjc0NTQ5LCA0MTAuNTk2OTY3NzM1NDcwOTcsIDQxMS40MTAzNzE3NDM0ODY5NiwgNDEyLjIyMzc3NTc1MTUwMywgNDEzLjAzNzE3OTc1OTUxOSwgNDEzLjg1MDU4Mzc2NzUzNTA2LCA0MTQuNjYzOTg3Nzc1NTUxMSwgNDE1LjQ3NzM5MTc4MzU2NzE2LCA0MTYuMjkwNzk1NzkxNTgzMiwgNDE3LjEwNDE5OTc5OTU5OTIsIDQxNy45MTc2MDM4MDc2MTUyLCA0MTguNzMxMDA3ODE1NjMxMjQsIDQxOS41NDQ0MTE4MjM2NDczLCA0MjAuMzU3ODE1ODMxNjYzMzQsIDQyMS4xNzEyMTk4Mzk2NzkzNCwgNDIxLjk4NDYyMzg0NzY5NTQsIDQyMi43OTgwMjc4NTU3MTE0NCwgNDIzLjYxMTQzMTg2MzcyNzUsIDQyNC40MjQ4MzU4NzE3NDM1LCA0MjUuMjM4MjM5ODc5NzU5NSwgNDI2LjA1MTY0Mzg4Nzc3NTUsIDQyNi44NjUwNDc4OTU3OTE2LCA0MjcuNjc4NDUxOTAzODA3NiwgNDI4LjQ5MTg1NTkxMTgyMzcsIDQyOS4zMDUyNTk5MTk4Mzk2NywgNDMwLjExODY2MzkyNzg1NTcsIDQzMC45MzIwNjc5MzU4NzE3LCA0MzEuNzQ1NDcxOTQzODg3NzYsIDQzMi41NTg4NzU5NTE5MDM4LCA0MzMuMzcyMjc5OTU5OTE5ODcsIDQzNC4xODU2ODM5Njc5MzU4NiwgNDM0Ljk5OTA4Nzk3NTk1MTksIDQzNS44MTI0OTE5ODM5Njc5NiwgNDM2LjYyNTg5NTk5MTk4NCwgNDM3LjQzOTNdKQogICAgICAgICAgICAgIC5yYW5nZShbJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCddKTsKICAgIAoKICAgIGNvbG9yX21hcF9jMzI1NzQxYWQxMzI0MzIwODBkMTA4YmM4NzcyMDhhNy54ID0gZDMuc2NhbGUubGluZWFyKCkKICAgICAgICAgICAgICAuZG9tYWluKFszMS41NTA3LCA0MzcuNDM5M10pCiAgICAgICAgICAgICAgLnJhbmdlKFswLCA0MDBdKTsKCiAgICBjb2xvcl9tYXBfYzMyNTc0MWFkMTMyNDMyMDgwZDEwOGJjODc3MjA4YTcubGVnZW5kID0gTC5jb250cm9sKHtwb3NpdGlvbjogJ3RvcHJpZ2h0J30pOwogICAgY29sb3JfbWFwX2MzMjU3NDFhZDEzMjQzMjA4MGQxMDhiYzg3NzIwOGE3LmxlZ2VuZC5vbkFkZCA9IGZ1bmN0aW9uIChtYXApIHt2YXIgZGl2ID0gTC5Eb21VdGlsLmNyZWF0ZSgnZGl2JywgJ2xlZ2VuZCcpOyByZXR1cm4gZGl2fTsKICAgIGNvbG9yX21hcF9jMzI1NzQxYWQxMzI0MzIwODBkMTA4YmM4NzcyMDhhNy5sZWdlbmQuYWRkVG8obWFwXzgyNjI2ZDYxMTNkNDQ4YjJiYzYxOTBkZjJlMmIyNmQxKTsKCiAgICBjb2xvcl9tYXBfYzMyNTc0MWFkMTMyNDMyMDgwZDEwOGJjODc3MjA4YTcueEF4aXMgPSBkMy5zdmcuYXhpcygpCiAgICAgICAgLnNjYWxlKGNvbG9yX21hcF9jMzI1NzQxYWQxMzI0MzIwODBkMTA4YmM4NzcyMDhhNy54KQogICAgICAgIC5vcmllbnQoInRvcCIpCiAgICAgICAgLnRpY2tTaXplKDEpCiAgICAgICAgLnRpY2tWYWx1ZXMoWzMxLjU1MDcsIDk5LjE5ODgsIDE2Ni44NDY5LCAyMzQuNDk1LCAzMDIuMTQzMSwgMzY5Ljc5MTIsIDQzNy40MzkzXSk7CgogICAgY29sb3JfbWFwX2MzMjU3NDFhZDEzMjQzMjA4MGQxMDhiYzg3NzIwOGE3LnN2ZyA9IGQzLnNlbGVjdCgiLmxlZ2VuZC5sZWFmbGV0LWNvbnRyb2wiKS5hcHBlbmQoInN2ZyIpCiAgICAgICAgLmF0dHIoImlkIiwgJ2xlZ2VuZCcpCiAgICAgICAgLmF0dHIoIndpZHRoIiwgNDUwKQogICAgICAgIC5hdHRyKCJoZWlnaHQiLCA0MCk7CgogICAgY29sb3JfbWFwX2MzMjU3NDFhZDEzMjQzMjA4MGQxMDhiYzg3NzIwOGE3LmcgPSBjb2xvcl9tYXBfYzMyNTc0MWFkMTMyNDMyMDgwZDEwOGJjODc3MjA4YTcuc3ZnLmFwcGVuZCgiZyIpCiAgICAgICAgLmF0dHIoImNsYXNzIiwgImtleSIpCiAgICAgICAgLmF0dHIoInRyYW5zZm9ybSIsICJ0cmFuc2xhdGUoMjUsMTYpIik7CgogICAgY29sb3JfbWFwX2MzMjU3NDFhZDEzMjQzMjA4MGQxMDhiYzg3NzIwOGE3Lmcuc2VsZWN0QWxsKCJyZWN0IikKICAgICAgICAuZGF0YShjb2xvcl9tYXBfYzMyNTc0MWFkMTMyNDMyMDgwZDEwOGJjODc3MjA4YTcuY29sb3IucmFuZ2UoKS5tYXAoZnVuY3Rpb24oZCwgaSkgewogICAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgeDA6IGkgPyBjb2xvcl9tYXBfYzMyNTc0MWFkMTMyNDMyMDgwZDEwOGJjODc3MjA4YTcueChjb2xvcl9tYXBfYzMyNTc0MWFkMTMyNDMyMDgwZDEwOGJjODc3MjA4YTcuY29sb3IuZG9tYWluKClbaSAtIDFdKSA6IGNvbG9yX21hcF9jMzI1NzQxYWQxMzI0MzIwODBkMTA4YmM4NzcyMDhhNy54LnJhbmdlKClbMF0sCiAgICAgICAgICAgIHgxOiBpIDwgY29sb3JfbWFwX2MzMjU3NDFhZDEzMjQzMjA4MGQxMDhiYzg3NzIwOGE3LmNvbG9yLmRvbWFpbigpLmxlbmd0aCA/IGNvbG9yX21hcF9jMzI1NzQxYWQxMzI0MzIwODBkMTA4YmM4NzcyMDhhNy54KGNvbG9yX21hcF9jMzI1NzQxYWQxMzI0MzIwODBkMTA4YmM4NzcyMDhhNy5jb2xvci5kb21haW4oKVtpXSkgOiBjb2xvcl9tYXBfYzMyNTc0MWFkMTMyNDMyMDgwZDEwOGJjODc3MjA4YTcueC5yYW5nZSgpWzFdLAogICAgICAgICAgICB6OiBkCiAgICAgICAgICB9OwogICAgICAgIH0pKQogICAgICAuZW50ZXIoKS5hcHBlbmQoInJlY3QiKQogICAgICAgIC5hdHRyKCJoZWlnaHQiLCAxMCkKICAgICAgICAuYXR0cigieCIsIGZ1bmN0aW9uKGQpIHsgcmV0dXJuIGQueDA7IH0pCiAgICAgICAgLmF0dHIoIndpZHRoIiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC54MSAtIGQueDA7IH0pCiAgICAgICAgLnN0eWxlKCJmaWxsIiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC56OyB9KTsKCiAgICBjb2xvcl9tYXBfYzMyNTc0MWFkMTMyNDMyMDgwZDEwOGJjODc3MjA4YTcuZy5jYWxsKGNvbG9yX21hcF9jMzI1NzQxYWQxMzI0MzIwODBkMTA4YmM4NzcyMDhhNy54QXhpcykuYXBwZW5kKCJ0ZXh0IikKICAgICAgICAuYXR0cigiY2xhc3MiLCAiY2FwdGlvbiIpCiAgICAgICAgLmF0dHIoInkiLCAyMSkKICAgICAgICAudGV4dCgnJyk7Cjwvc2NyaXB0Pg==" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
df_N2 = df2[df2["재산세 수준지수(서울특별시=100)"]<130]
```


```python
map = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='Stamen Toner')
map.choropleth(geo_str, data = df_N2, columns =["지역", "재산세 수준지수(서울특별시=100)"], fill_color='YlGnBu', #PuRd, YlGnBu
              key_on='feature.id')
map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVM9ZmFsc2U7IExfTk9fVE9VQ0g9ZmFsc2U7IExfRElTQUJMRV8zRD1mYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgPHN0eWxlPiNtYXBfNTBhOTYyNTY5MzA0NDY3YzgxZDE0ZDJlZTQ0MzQ1OTYgewogICAgICAgIHBvc2l0aW9uOiByZWxhdGl2ZTsKICAgICAgICB3aWR0aDogMTAwLjAlOwogICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgdG9wOiAwLjAlOwogICAgICAgIH0KICAgIDwvc3R5bGU+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvZDMvMy41LjUvZDMubWluLmpzIj48L3NjcmlwdD4KPC9oZWFkPgo8Ym9keT4gICAgCiAgICAKICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfNTBhOTYyNTY5MzA0NDY3YzgxZDE0ZDJlZTQ0MzQ1OTYiID48L2Rpdj4KPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgCiAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAKCiAgICB2YXIgbWFwXzUwYTk2MjU2OTMwNDQ2N2M4MWQxNGQyZWU0NDM0NTk2ID0gTC5tYXAoCiAgICAgICAgJ21hcF81MGE5NjI1NjkzMDQ0NjdjODFkMTRkMmVlNDQzNDU5NicsIHsKICAgICAgICBjZW50ZXI6IFszNy41NTAyLCAxMjYuOTgyXSwKICAgICAgICB6b29tOiAxMSwKICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICBsYXllcnM6IFtdLAogICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcsCiAgICAgICAgem9vbUNvbnRyb2w6IHRydWUsCiAgICAgICAgfSk7CgogICAgCiAgICAKICAgIHZhciB0aWxlX2xheWVyX2Q5NzYwY2NhZGZhZDQ1MTE4MzBmZWY5YTQ3MTM4MmI1ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgJ2h0dHBzOi8vc3RhbWVuLXRpbGVzLXtzfS5hLnNzbC5mYXN0bHkubmV0L3RvbmVyL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgewogICAgICAgICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgICAgICAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICAgICAgICJtYXhOYXRpdmVab29tIjogMTgsCiAgICAgICAgIm1heFpvb20iOiAxOCwKICAgICAgICAibWluWm9vbSI6IDAsCiAgICAgICAgIm5vV3JhcCI6IGZhbHNlLAogICAgICAgICJzdWJkb21haW5zIjogImFiYyIKfSkuYWRkVG8obWFwXzUwYTk2MjU2OTMwNDQ2N2M4MWQxNGQyZWU0NDM0NTk2KTsKICAgIAogICAgICAgIAogICAgICAgIHZhciBnZW9fanNvbl9hZDMwYTFmYWFmYTY0Njk1OTE5YzE0OTVkZGMwOWQ3YiA9IEwuZ2VvSnNvbigKICAgICAgICAgICAgeyJmZWF0dXJlcyI6IFt7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XSwgWzEyNy4xNjY4MzE4NDM2NjEyOSwgMzcuNTc2NzI0ODczODg2MjddLCBbMTI3LjE4NDA4NzkyMzMwMTUyLCAzNy41NTgxNDI4MDM2OTU3NV0sIFsxMjcuMTY1MzA5ODQzMDc0NDcsIDM3LjU0MjIxODUxMjU4NjkzXSwgWzEyNy4xNDY3MjgwNjgyMzUwMiwgMzcuNTE0MTU2ODA2ODAyOTFdLCBbMTI3LjEyMTIzMTY1NzE5NjE1LCAzNy41MjUyODI3MDA4OV0sIFsxMjcuMTExNjc2NDIwMzYwOCwgMzcuNTQwNjY5OTU1MzI0OTY1XSwgWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFjMTVcdWIzZDlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTI1MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhYzE1XHViM2Q5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkdhbmdkb25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiIzQxYjZjNCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl0sIFsxMjcuMTAwODc1MTk3OTE5NjIsIDM3LjUyNDg0MTIyMDE2NzA1NV0sIFsxMjcuMTExNjc2NDIwMzYwOCwgMzcuNTQwNjY5OTU1MzI0OTY1XSwgWzEyNy4xMjEyMzE2NTcxOTYxNSwgMzcuNTI1MjgyNzAwODldLCBbMTI3LjE0NjcyODA2ODIzNTAyLCAzNy41MTQxNTY4MDY4MDI5MV0sIFsxMjcuMTYzNDk0NDIxNTc2NSwgMzcuNDk3NDQ1NDA2MDk3NDg0XSwgWzEyNy4xNDIwNjA1ODQxMzI3NCwgMzcuNDcwODk4MTkwOTg1MDFdLCBbMTI3LjEyNDQwNTcxMDgwODkzLCAzNy40NjI0MDQ0NTU4NzA0OF0sIFsxMjcuMTExMTcwODUyMDEyMzgsIDM3LjQ4NTcwODM4MTUxMjQ0NV0sIFsxMjcuMDcxOTE0NjAwMDcyNCwgMzcuNTAyMjQwMTM1ODc2NjldLCBbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMWExXHVkMzBjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEyNDAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzFhMVx1ZDMwY1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJTb25ncGEtZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjMGMyYzg0IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XSwgWzEyNy4wNjkwNjk4MTMwMzcyLCAzNy41MjIyNzk0MjM1MDUwMjZdLCBbMTI3LjA3MTkxNDYwMDA3MjQsIDM3LjUwMjI0MDEzNTg3NjY5XSwgWzEyNy4xMTExNzA4NTIwMTIzOCwgMzcuNDg1NzA4MzgxNTEyNDQ1XSwgWzEyNy4xMjQ0MDU3MTA4MDg5MywgMzcuNDYyNDA0NDU1ODcwNDhdLCBbMTI3LjA5ODQyNzU5MzE4NzUxLCAzNy40NTg2MjI1Mzg1NzQ2MV0sIFsxMjcuMDg2NDA0NDA1NzgxNTYsIDM3LjQ3MjY5NzkzNTE4NDY1NV0sIFsxMjcuMDU1OTE3MDQ4MTkwNCwgMzcuNDY1OTIyODkxNDA3N10sIFsxMjcuMDM2MjE5MTUwOTg3OTgsIDM3LjQ4MTc1ODAyNDI3NjAzXSwgWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldLCBbMTI3LjAyMzAyODMxODkwNTU5LCAzNy41MzIzMTg5OTU4MjY2M10sIFsxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWFjMTVcdWIwYThcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIzMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVhYzE1XHViMGE4XHVhZDZjIiwgIm5hbWVfZW5nIjogIkdhbmduYW0tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjMGMyYzg0IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjcuMDEzOTcxMTk2Njc1MTMsIDM3LjUyNTAzOTg4Mjg5NjY5XSwgWzEyNy4wMzYyMTkxNTA5ODc5OCwgMzcuNDgxNzU4MDI0Mjc2MDNdLCBbMTI3LjA1NTkxNzA0ODE5MDQsIDM3LjQ2NTkyMjg5MTQwNzddLCBbMTI3LjA4NjQwNDQwNTc4MTU2LCAzNy40NzI2OTc5MzUxODQ2NTVdLCBbMTI3LjA5ODQyNzU5MzE4NzUxLCAzNy40NTg2MjI1Mzg1NzQ2MV0sIFsxMjcuMDkwNDY5Mjg1NjU5NTEsIDM3LjQ0Mjk2ODI2MTE0MTg1XSwgWzEyNy4wNjc3ODEwNzYwNTQzMywgMzcuNDI2MTk3NDI0MDU3MzE0XSwgWzEyNy4wNDk1NzIzMjk4NzE0MiwgMzcuNDI4MDU4MzY4NDU2OTRdLCBbMTI3LjAzODgxNzgyNTk3OTIyLCAzNy40NTM4MjAzOTg1MTcxNV0sIFsxMjYuOTkwNzIwNzMxOTU0NjIsIDM3LjQ1NTMyNjE0MzMxMDAyNV0sIFsxMjYuOTgzNjc2NjgyOTE4MDIsIDM3LjQ3Mzg1NjQ5MjY5MjA4Nl0sIFsxMjYuOTgyMjM4MDc5MTYwODEsIDM3LjUwOTMxNDk2Njc3MDMyNl0sIFsxMjcuMDEzOTcxMTk2Njc1MTMsIDM3LjUyNTAzOTg4Mjg5NjY5XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWMxMWNcdWNkMDhcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIyMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjMTFjXHVjZDA4XHVhZDZjIiwgIm5hbWVfZW5nIjogIlNlb2Noby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiMwYzJjODQiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45ODM2NzY2ODI5MTgwMiwgMzcuNDczODU2NDkyNjkyMDg2XSwgWzEyNi45OTA3MjA3MzE5NTQ2MiwgMzcuNDU1MzI2MTQzMzEwMDI1XSwgWzEyNi45NjUyMDQzOTA4NTE0MywgMzcuNDM4MjQ5Nzg0MDA2MjQ2XSwgWzEyNi45NTAwMDAwMTAxMDE4MiwgMzcuNDM2MTM0NTExNjU3MTldLCBbMTI2LjkzMDg0NDA4MDU2NTI1LCAzNy40NDczODI5MjgzMzM5OTRdLCBbMTI2LjkxNjc3MjgxNDY2MDEsIDM3LjQ1NDkwNTY2NDIzNzg5XSwgWzEyNi45MDE1NjA5NDEyOTg5NSwgMzcuNDc3NTM4NDI3ODk5MDFdLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuOTQ5MjI2NjEzODk1MDgsIDM3LjQ5MTI1NDM3NDk1NjQ5XSwgWzEyNi45NzI1ODkxODUwNjYyLCAzNy40NzI1NjEzNjMyNzgxMjVdLCBbMTI2Ljk4MzY3NjY4MjkxODAyLCAzNy40NzM4NTY0OTI2OTIwODZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWQwMFx1YzU0NVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMjEwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFkMDBcdWM1NDVcdWFkNmMiLCAibmFtZV9lbmciOiAiR3dhbmFrLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2ZmZmZjYyIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk4MjIzODA3OTE2MDgxLCAzNy41MDkzMTQ5NjY3NzAzMjZdLCBbMTI2Ljk4MzY3NjY4MjkxODAyLCAzNy40NzM4NTY0OTI2OTIwODZdLCBbMTI2Ljk3MjU4OTE4NTA2NjIsIDM3LjQ3MjU2MTM2MzI3ODEyNV0sIFsxMjYuOTQ5MjI2NjEzODk1MDgsIDM3LjQ5MTI1NDM3NDk1NjQ5XSwgWzEyNi45MDUzMTk3NTgwMTgxMiwgMzcuNDgyMTgwODc1NzU0MjldLCBbMTI2LjkyMTc3ODkzMTc0ODI1LCAzNy40OTQ4ODk4Nzc0MTUxNzZdLCBbMTI2LjkyODEwNjI4ODI4Mjc5LCAzNy41MTMyOTU5NTczMjAxNV0sIFsxMjYuOTUyNDk5OTAyOTgxNTksIDM3LjUxNzIyNTAwNzQxODEzXSwgWzEyNi45ODIyMzgwNzkxNjA4MSwgMzcuNTA5MzE0OTY2NzcwMzI2XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIzZDlcdWM3OTFcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTIwMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViM2Q5XHVjNzkxXHVhZDZjIiwgIm5hbWVfZW5nIjogIkRvbmdqYWstZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjYzdlOWI0IiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuODkxODQ2NjM4NjI3NjQsIDM3LjU0NzM3Mzk3NDk5NzExNF0sIFsxMjYuOTQ1NjY3MzMwODMyMTIsIDM3LjUyNjYxNzU0MjQ1MzM2Nl0sIFsxMjYuOTUyNDk5OTAyOTgxNTksIDM3LjUxNzIyNTAwNzQxODEzXSwgWzEyNi45MjgxMDYyODgyODI3OSwgMzcuNTEzMjk1OTU3MzIwMTVdLCBbMTI2LjkyMTc3ODkzMTc0ODI1LCAzNy40OTQ4ODk4Nzc0MTUxNzZdLCBbMTI2LjkwNTMxOTc1ODAxODEyLCAzNy40ODIxODA4NzU3NTQyOV0sIFsxMjYuODk1OTQ3NzY3ODI0ODUsIDM3LjUwNDY3NTI4MTMwOTE3Nl0sIFsxMjYuODgxNTY0MDIzNTM4NjIsIDM3LjUxMzk3MDAzNDc2NTY4NF0sIFsxMjYuODg4MjU3NTc4NjAwOTksIDM3LjU0MDc5NzMzNjMwMjMyXSwgWzEyNi44OTE4NDY2Mzg2Mjc2NCwgMzcuNTQ3MzczOTc0OTk3MTE0XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWM2MDFcdWI0ZjFcdWQzZWNcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTE5MCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjNjAxXHViNGYxXHVkM2VjXHVhZDZjIiwgIm5hbWVfZW5nIjogIlllb25nZGV1bmdwby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiMyMjVlYTgiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45MDE1NjA5NDEyOTg5NSwgMzcuNDc3NTM4NDI3ODk5MDFdLCBbMTI2LjkxNjc3MjgxNDY2MDEsIDM3LjQ1NDkwNTY2NDIzNzg5XSwgWzEyNi45MzA4NDQwODA1NjUyNSwgMzcuNDQ3MzgyOTI4MzMzOTk0XSwgWzEyNi45MDI1ODMxNzExNjk3LCAzNy40MzQ1NDkzNjYzNDkxMjRdLCBbMTI2Ljg3NjgzMjcxNTAyNDI4LCAzNy40ODI1NzY1OTE2MDczMDVdLCBbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZTA4XHVjYzljXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExODAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWUwOFx1Y2M5Y1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJHZXVtY2hlb24tZ3UiLCAic3R5bGUiOiB7ImNvbG9yIjogImJsYWNrIiwgImZpbGxDb2xvciI6ICIjN2ZjZGJiIiwgImZpbGxPcGFjaXR5IjogMC42LCAib3BhY2l0eSI6IDEsICJ3ZWlnaHQiOiAxfX0sICJ0eXBlIjogIkZlYXR1cmUifSwgeyJnZW9tZXRyeSI6IHsiY29vcmRpbmF0ZXMiOiBbW1sxMjYuODI2ODgwODE1MTczMTQsIDM3LjUwNTQ4OTcyMjMyODk2XSwgWzEyNi44ODE1NjQwMjM1Mzg2MiwgMzcuNTEzOTcwMDM0NzY1Njg0XSwgWzEyNi44OTU5NDc3Njc4MjQ4NSwgMzcuNTA0Njc1MjgxMzA5MTc2XSwgWzEyNi45MDUzMTk3NTgwMTgxMiwgMzcuNDgyMTgwODc1NzU0MjldLCBbMTI2LjkwMTU2MDk0MTI5ODk1LCAzNy40Nzc1Mzg0Mjc4OTkwMV0sIFsxMjYuODc2ODMyNzE1MDI0MjgsIDM3LjQ4MjU3NjU5MTYwNzMwNV0sIFsxMjYuODQ3NjI2NzYwNTQ5NTMsIDM3LjQ3MTQ2NzIzOTM2MzIzXSwgWzEyNi44MzU0OTQ4NTA3NjE5NiwgMzcuNDc0MDk4MjM2OTc1MDk1XSwgWzEyNi44MjI2NDc5Njc5MTM0OCwgMzcuNDg3ODQ3NjQ5MjE0N10sIFsxMjYuODI1MDQ3MzYzMzE0MDYsIDM3LjUwMzAyNjEyNjQwNDQzXSwgWzEyNi44MjY4ODA4MTUxNzMxNCwgMzcuNTA1NDg5NzIyMzI4OTZdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWQ2Y1x1Yjg1Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTcwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFkNmNcdWI4NWNcdWFkNmMiLCAibmFtZV9lbmciOiAiR3Vyby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNjN2U5YjQiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi43OTU3NTc2ODU1MjkwNywgMzcuNTc4ODEwODc2MzMyMDJdLCBbMTI2LjgwNzAyMTE1MDIzNTk3LCAzNy42MDEyMzAwMTAxMzIyOF0sIFsxMjYuODIyNTE0Mzg0NzcxMDUsIDM3LjU4ODA0MzA4MTAwODJdLCBbMTI2Ljg1OTg0MTk5Mzk5NjY3LCAzNy41NzE4NDc4NTUyOTI3NDVdLCBbMTI2Ljg5MTg0NjYzODYyNzY0LCAzNy41NDczNzM5NzQ5OTcxMTRdLCBbMTI2Ljg4ODI1NzU3ODYwMDk5LCAzNy41NDA3OTczMzYzMDIzMl0sIFsxMjYuODY2Mzc0NjQzMjEyMzgsIDM3LjU0ODU5MTkxMDk0ODIzXSwgWzEyNi44NjYxMDA3MzQ3NjM5NSwgMzcuNTI2OTk5NjQxNDQ2NjldLCBbMTI2Ljg0MjU3MjkxOTQzMTUzLCAzNy41MjM3MzcwNzgwNTU5Nl0sIFsxMjYuODI0MjMzMTQyNjcyMiwgMzcuNTM3ODgwNzg3NTMyNDhdLCBbMTI2Ljc3MzI0NDE3NzE3NzAzLCAzNy41NDU5MTIzNDUwNTU0XSwgWzEyNi43Njk3OTE4MDU3OTM1MiwgMzcuNTUxMzkxODMwMDg4MDldLCBbMTI2Ljc5NTc1NzY4NTUyOTA3LCAzNy41Nzg4MTA4NzYzMzIwMl1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhYzE1XHVjMTFjXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExNjAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWMxNVx1YzExY1x1YWQ2YyIsICJuYW1lX2VuZyI6ICJHYW5nc2VvLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiIzdmY2RiYiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2LjgyNDIzMzE0MjY3MjIsIDM3LjUzNzg4MDc4NzUzMjQ4XSwgWzEyNi44NDI1NzI5MTk0MzE1MywgMzcuNTIzNzM3MDc4MDU1OTZdLCBbMTI2Ljg2NjEwMDczNDc2Mzk1LCAzNy41MjY5OTk2NDE0NDY2OV0sIFsxMjYuODY2Mzc0NjQzMjEyMzgsIDM3LjU0ODU5MTkxMDk0ODIzXSwgWzEyNi44ODgyNTc1Nzg2MDA5OSwgMzcuNTQwNzk3MzM2MzAyMzJdLCBbMTI2Ljg4MTU2NDAyMzUzODYyLCAzNy41MTM5NzAwMzQ3NjU2ODRdLCBbMTI2LjgyNjg4MDgxNTE3MzE0LCAzNy41MDU0ODk3MjIzMjg5Nl0sIFsxMjYuODI0MjMzMTQyNjcyMiwgMzcuNTM3ODgwNzg3NTMyNDhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzU5MVx1Y2M5Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTUwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM1OTFcdWNjOWNcdWFkNmMiLCAibmFtZV9lbmciOiAiWWFuZ2NoZW9uLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M3ZTliNCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2LjkwNTIyMDY1ODMxMDUzLCAzNy41NzQwOTcwMDUyMjU3NF0sIFsxMjYuOTM4OTgxNjE3OTg5NzMsIDM3LjU1MjMxMDAwMzcyODEyNF0sIFsxMjYuOTYzNTgyMjY3MTA4MTIsIDM3LjU1NjA1NjM1NDc1MTU0XSwgWzEyNi45NjQ0ODU3MDU1MzA1NSwgMzcuNTQ4NzA1NjkyMDIxNjM1XSwgWzEyNi45NDU2NjczMzA4MzIxMiwgMzcuNTI2NjE3NTQyNDUzMzY2XSwgWzEyNi44OTE4NDY2Mzg2Mjc2NCwgMzcuNTQ3MzczOTc0OTk3MTE0XSwgWzEyNi44NTk4NDE5OTM5OTY2NywgMzcuNTcxODQ3ODU1MjkyNzQ1XSwgWzEyNi44ODQzMzI4NDc3MzI4OCwgMzcuNTg4MTQzMzIyODgwNTI2XSwgWzEyNi45MDUyMjA2NTgzMTA1MywgMzcuNTc0MDk3MDA1MjI1NzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YjljOFx1ZDNlY1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTQwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWI5YzhcdWQzZWNcdWFkNmMiLCAibmFtZV9lbmciOiAiTWFwby1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiMyMjVlYTgiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTU1NjU0MjU4NDY0NjMsIDM3LjU3NjA4MDc5MDg4MTQ1Nl0sIFsxMjYuOTY4NzM2MzMyNzkwNzUsIDM3LjU2MzEzNjA0NjkwODI3XSwgWzEyNi45NjM1ODIyNjcxMDgxMiwgMzcuNTU2MDU2MzU0NzUxNTRdLCBbMTI2LjkzODk4MTYxNzk4OTczLCAzNy41NTIzMTAwMDM3MjgxMjRdLCBbMTI2LjkwNTIyMDY1ODMxMDUzLCAzNy41NzQwOTcwMDUyMjU3NF0sIFsxMjYuOTUyNDc1MjAzMDU3MiwgMzcuNjA1MDg2OTI3MzcwNDVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzExY1x1YjMwMFx1YmIzOFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMTMwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWMxMWNcdWIzMDBcdWJiMzhcdWFkNmMiLCAibmFtZV9lbmciOiAiU2VvZGFlbXVuLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiI2M3ZTliNCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI2Ljk3Mzg4NjQxMjg3MDIsIDM3LjYyOTQ5NjM0Nzg2ODg4XSwgWzEyNi45NTQyNzAxNzAwNjEyOSwgMzcuNjIyMDMzNDMxMzM5NDI1XSwgWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTA1MjIwNjU4MzEwNTMsIDM3LjU3NDA5NzAwNTIyNTc0XSwgWzEyNi44ODQzMzI4NDc3MzI4OCwgMzcuNTg4MTQzMzIyODgwNTI2XSwgWzEyNi45MDM5NjY4MTAwMzU5NSwgMzcuNTkyMjc0MDM0MTk5NDJdLCBbMTI2LjkwMzAzMDY2MTc3NjY4LCAzNy42MDk5Nzc5MTE0MDEzNDRdLCBbMTI2LjkxNDU1NDgxNDI5NjQ4LCAzNy42NDE1MDA1MDk5NjkzNV0sIFsxMjYuOTU2NDczNzk3Mzg3LCAzNy42NTI0ODA3MzczMzk0NDVdLCBbMTI2Ljk3Mzg4NjQxMjg3MDIsIDM3LjYyOTQ5NjM0Nzg2ODg4XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWM3NDBcdWQzYzlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTEyMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHVjNzQwXHVkM2M5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkV1bnB5ZW9uZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wODM4NzUyNzAzMTk1LCAzNy42OTM1OTUzNDIwMjAzNF0sIFsxMjcuMDk3MDYzOTEzMDk2OTUsIDM3LjY4NjM4MzcxOTM3MjI5NF0sIFsxMjcuMDk0NDA3NjYyOTg3MTcsIDM3LjY0NzEzNDkwNDczMDQ1XSwgWzEyNy4xMTMyNjc5NTg1NTE5OSwgMzcuNjM5NjIyOTA1MzE1OTI1XSwgWzEyNy4xMDc4MjI3NzY4ODEyOSwgMzcuNjE4MDQyNDQyNDEwNjldLCBbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM10sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wNDM1ODgwMDg5NTYwOSwgMzcuNjI4NDg5MzEyOTg3MTVdLCBbMTI3LjA1ODAwMDc1MjIwMDkxLCAzNy42NDMxODI2Mzg3ODI3Nl0sIFsxMjcuMDUyODg0Nzk3MTA0ODUsIDM3LjY4NDIzODU3MDg0MzQ3XSwgWzEyNy4wODM4NzUyNzAzMTk1LCAzNy42OTM1OTUzNDIwMjAzNF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHViMTc4XHVjNmQwXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTExMTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YjE3OFx1YzZkMFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJOb3dvbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wNTI4ODQ3OTcxMDQ4NSwgMzcuNjg0MjM4NTcwODQzNDddLCBbMTI3LjA1ODAwMDc1MjIwMDkxLCAzNy42NDMxODI2Mzg3ODI3Nl0sIFsxMjcuMDQzNTg4MDA4OTU2MDksIDM3LjYyODQ4OTMxMjk4NzE1XSwgWzEyNy4wMTQ2NTkzNTg5MjQ2NiwgMzcuNjQ5NDM2ODc0OTY4MTJdLCBbMTI3LjAyMDYyMTE2MTQxMzg5LCAzNy42NjcxNzM1NzU5NzEyMDVdLCBbMTI3LjAxMDM5NjY2MDQyMDcxLCAzNy42ODE4OTQ1ODk2MDM1OTRdLCBbMTI3LjAxNzk1MDk5MjAzNDMyLCAzNy42OTgyNDQxMjc3NTY2Ml0sIFsxMjcuMDUyODg0Nzk3MTA0ODUsIDM3LjY4NDIzODU3MDg0MzQ3XV1dLCAidHlwZSI6ICJQb2x5Z29uIn0sICJpZCI6ICJcdWIzYzRcdWJkMDlcdWFkNmMiLCAicHJvcGVydGllcyI6IHsiYmFzZV95ZWFyIjogIjIwMTMiLCAiY29kZSI6ICIxMTEwMCIsICJoaWdobGlnaHQiOiB7fSwgIm5hbWUiOiAiXHViM2M0XHViZDA5XHVhZDZjIiwgIm5hbWVfZW5nIjogIkRvYm9uZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45OTM4MzkwMzQyNCwgMzcuNjc2NjgxNzYxMTk5MDg1XSwgWzEyNy4wMTAzOTY2NjA0MjA3MSwgMzcuNjgxODk0NTg5NjAzNTk0XSwgWzEyNy4wMjA2MjExNjE0MTM4OSwgMzcuNjY3MTczNTc1OTcxMjA1XSwgWzEyNy4wMTQ2NTkzNTg5MjQ2NiwgMzcuNjQ5NDM2ODc0OTY4MTJdLCBbMTI3LjA0MzU4ODAwODk1NjA5LCAzNy42Mjg0ODkzMTI5ODcxNV0sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wMzg5MjQwMDk5MjMwMSwgMzcuNjA5NzE1NjExMDIzODE2XSwgWzEyNy4wMTI4MTU0NzQ5NTIzLCAzNy42MTM2NTIyNDM0NzAyNTZdLCBbMTI2Ljk4NjcyNzA1NTEzODY5LCAzNy42MzM3NzY0MTI4ODE5Nl0sIFsxMjYuOTgxNzQ1MjY3NjU1MSwgMzcuNjUyMDk3NjkzODc3NzZdLCBbMTI2Ljk5MzgzOTAzNDI0LCAzNy42NzY2ODE3NjExOTkwODVdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YWMxNVx1YmQ4MVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDkwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWFjMTVcdWJkODFcdWFkNmMiLCAibmFtZV9lbmciOiAiR2FuZ2J1ay1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NzcxNzU0MDY0MTYsIDM3LjYyODU5NzE1NDAwMzg4XSwgWzEyNi45ODY3MjcwNTUxMzg2OSwgMzcuNjMzNzc2NDEyODgxOTZdLCBbMTI3LjAxMjgxNTQ3NDk1MjMsIDM3LjYxMzY1MjI0MzQ3MDI1Nl0sIFsxMjcuMDM4OTI0MDA5OTIzMDEsIDM3LjYwOTcxNTYxMTAyMzgxNl0sIFsxMjcuMDUyMDkzNzM1Njg2MTksIDM3LjYyMTY0MDY1NDg3NzgyXSwgWzEyNy4wNzM1MTI0MzgyNTI3OCwgMzcuNjEyODM2NjAzNDIzMTNdLCBbMTI3LjA3MzgyNzA3MDk5MjI3LCAzNy42MDQwMTkyODk4NjQxOV0sIFsxMjcuMDQyNzA1MjIyMDk0LCAzNy41OTIzOTQzNzU5MzM5MV0sIFsxMjcuMDI1MjcyNTQ1MjgwMDMsIDM3LjU3NTI0NjE2MjQ1MjQ5XSwgWzEyNi45OTM0ODI5MzM1ODMxNCwgMzcuNTg4NTY1NDU3MjE2MTU2XSwgWzEyNi45ODg3OTg2NTk5MjM4NCwgMzcuNjExODkyNzMxOTc1Nl0sIFsxMjYuOTc3MTc1NDA2NDE2LCAzNy42Mjg1OTcxNTQwMDM4OF1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjMTMxXHViZDgxXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwODAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzEzMVx1YmQ4MVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJTZW9uZ2J1ay1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNjN2U5YjQiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wNzM1MTI0MzgyNTI3OCwgMzcuNjEyODM2NjAzNDIzMTNdLCBbMTI3LjEwNzgyMjc3Njg4MTI5LCAzNy42MTgwNDI0NDI0MTA2OV0sIFsxMjcuMTIwMTI0NjAyMDExNCwgMzcuNjAxNzg0NTc1OTgxODhdLCBbMTI3LjEwMzA0MTc0MjQ5MjE0LCAzNy41NzA3NjM0MjI5MDk1NV0sIFsxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XSwgWzEyNy4wNzM4MjcwNzA5OTIyNywgMzcuNjA0MDE5Mjg5ODY0MTldLCBbMTI3LjA3MzUxMjQzODI1Mjc4LCAzNy42MTI4MzY2MDM0MjMxM11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVjOTExXHViNzkxXHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNzAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YzkxMVx1Yjc5MVx1YWQ2YyIsICJuYW1lX2VuZyI6ICJKdW5nbmFuZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiNmZmZmY2MiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjUyNzI1NDUyODAwMywgMzcuNTc1MjQ2MTYyNDUyNDldLCBbMTI3LjA0MjcwNTIyMjA5NCwgMzcuNTkyMzk0Mzc1OTMzOTFdLCBbMTI3LjA3MzgyNzA3MDk5MjI3LCAzNy42MDQwMTkyODk4NjQxOV0sIFsxMjcuMDgwNjg1NDEyODA0MDMsIDM3LjU2OTA2NDI1NTE5MDE3XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA1MDA1NjAxMDgxNTY3LCAzNy41Njc1Nzc2MTI1OTA4NDZdLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdLCBbMTI3LjAyNTI3MjU0NTI4MDAzLCAzNy41NzUyNDYxNjI0NTI0OV1dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHViM2Q5XHViMzAwXHViYjM4XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNjAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YjNkOVx1YjMwMFx1YmIzOFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJEb25nZGFlbXVuLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiIzdmY2RiYiIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjA4MDY4NTQxMjgwNDAzLCAzNy41NjkwNjQyNTUxOTAxN10sIFsxMjcuMTAzMDQxNzQyNDkyMTQsIDM3LjU3MDc2MzQyMjkwOTU1XSwgWzEyNy4xMTUxOTU4NDk4MTYwNiwgMzcuNTU3NTMzMTgwNzA0OTE1XSwgWzEyNy4xMTE2NzY0MjAzNjA4LCAzNy41NDA2Njk5NTUzMjQ5NjVdLCBbMTI3LjEwMDg3NTE5NzkxOTYyLCAzNy41MjQ4NDEyMjAxNjcwNTVdLCBbMTI3LjA2OTA2OTgxMzAzNzIsIDM3LjUyMjI3OTQyMzUwNTAyNl0sIFsxMjcuMDU4NjczNTkyODgzOTgsIDM3LjUyNjI5OTc0OTIyNTY4XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA4MDY4NTQxMjgwNDAzLCAzNy41NjkwNjQyNTUxOTAxN11dXSwgInR5cGUiOiAiUG9seWdvbiJ9LCAiaWQiOiAiXHVhZDExXHVjOWM0XHVhZDZjIiwgInByb3BlcnRpZXMiOiB7ImJhc2VfeWVhciI6ICIyMDEzIiwgImNvZGUiOiAiMTEwNTAiLCAiaGlnaGxpZ2h0Ijoge30sICJuYW1lIjogIlx1YWQxMVx1YzljNFx1YWQ2YyIsICJuYW1lX2VuZyI6ICJHd2FuZ2ppbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiM3ZmNkYmIiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjU0NzI2NjM0OTk3NiwgMzcuNTY4OTQzNTUyMjM3NzM0XSwgWzEyNy4wNTAwNTYwMTA4MTU2NywgMzcuNTY3NTc3NjEyNTkwODQ2XSwgWzEyNy4wNzQyMTA1MzAyNDM2MiwgMzcuNTU3MjQ3Njk3MTIwODVdLCBbMTI3LjA1ODY3MzU5Mjg4Mzk4LCAzNy41MjYyOTk3NDkyMjU2OF0sIFsxMjcuMDIzMDI4MzE4OTA1NTksIDM3LjUzMjMxODk5NTgyNjYzXSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzEzMVx1YjNkOVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDQwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWMxMzFcdWIzZDlcdWFkNmMiLCAibmFtZV9lbmciOiAiU2Vvbmdkb25nLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiIzFkOTFjMCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn0sIHsiZ2VvbWV0cnkiOiB7ImNvb3JkaW5hdGVzIjogW1tbMTI3LjAxMDcwODk0MTc3NDgyLCAzNy41NDExODA0ODk2NDc2Ml0sIFsxMjcuMDIzMDI4MzE4OTA1NTksIDM3LjUzMjMxODk5NTgyNjYzXSwgWzEyNy4wMTM5NzExOTY2NzUxMywgMzcuNTI1MDM5ODgyODk2NjldLCBbMTI2Ljk4MjIzODA3OTE2MDgxLCAzNy41MDkzMTQ5NjY3NzAzMjZdLCBbMTI2Ljk1MjQ5OTkwMjk4MTU5LCAzNy41MTcyMjUwMDc0MTgxM10sIFsxMjYuOTQ1NjY3MzMwODMyMTIsIDM3LjUyNjYxNzU0MjQ1MzM2Nl0sIFsxMjYuOTY0NDg1NzA1NTMwNTUsIDM3LjU0ODcwNTY5MjAyMTYzNV0sIFsxMjYuOTg3NTI5OTY5MDMzMjgsIDM3LjU1MDk0ODE4ODA3MTM5XSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzZhOVx1YzBiMFx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDMwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM2YTlcdWMwYjBcdWFkNmMiLCAibmFtZV9lbmciOiAiWW9uZ3Nhbi1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiMwYzJjODQiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNy4wMjU0NzI2NjM0OTk3NiwgMzcuNTY4OTQzNTUyMjM3NzM0XSwgWzEyNy4wMTA3MDg5NDE3NzQ4MiwgMzcuNTQxMTgwNDg5NjQ3NjJdLCBbMTI2Ljk4NzUyOTk2OTAzMzI4LCAzNy41NTA5NDgxODgwNzEzOV0sIFsxMjYuOTY0NDg1NzA1NTMwNTUsIDM3LjU0ODcwNTY5MjAyMTYzNV0sIFsxMjYuOTYzNTgyMjY3MTA4MTIsIDM3LjU1NjA1NjM1NDc1MTU0XSwgWzEyNi45Njg3MzYzMzI3OTA3NSwgMzcuNTYzMTM2MDQ2OTA4MjddLCBbMTI3LjAyNTQ3MjY2MzQ5OTc2LCAzNy41Njg5NDM1NTIyMzc3MzRdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1YzkxMVx1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDIwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM5MTFcdWFkNmMiLCAibmFtZV9lbmciOiAiSnVuZy1ndSIsICJzdHlsZSI6IHsiY29sb3IiOiAiYmxhY2siLCAiZmlsbENvbG9yIjogIiMwYzJjODQiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJvcGFjaXR5IjogMSwgIndlaWdodCI6IDF9fSwgInR5cGUiOiAiRmVhdHVyZSJ9LCB7Imdlb21ldHJ5IjogeyJjb29yZGluYXRlcyI6IFtbWzEyNi45NzM4ODY0MTI4NzAyLCAzNy42Mjk0OTYzNDc4Njg4OF0sIFsxMjYuOTc3MTc1NDA2NDE2LCAzNy42Mjg1OTcxNTQwMDM4OF0sIFsxMjYuOTg4Nzk4NjU5OTIzODQsIDM3LjYxMTg5MjczMTk3NTZdLCBbMTI2Ljk5MzQ4MjkzMzU4MzE0LCAzNy41ODg1NjU0NTcyMTYxNTZdLCBbMTI3LjAyNTI3MjU0NTI4MDAzLCAzNy41NzUyNDYxNjI0NTI0OV0sIFsxMjcuMDI1NDcyNjYzNDk5NzYsIDM3LjU2ODk0MzU1MjIzNzczNF0sIFsxMjYuOTY4NzM2MzMyNzkwNzUsIDM3LjU2MzEzNjA0NjkwODI3XSwgWzEyNi45NTU2NTQyNTg0NjQ2MywgMzcuNTc2MDgwNzkwODgxNDU2XSwgWzEyNi45NTI0NzUyMDMwNTcyLCAzNy42MDUwODY5MjczNzA0NV0sIFsxMjYuOTU0MjcwMTcwMDYxMjksIDM3LjYyMjAzMzQzMTMzOTQyNV0sIFsxMjYuOTczODg2NDEyODcwMiwgMzcuNjI5NDk2MzQ3ODY4ODhdXV0sICJ0eXBlIjogIlBvbHlnb24ifSwgImlkIjogIlx1Yzg4NVx1Yjg1Y1x1YWQ2YyIsICJwcm9wZXJ0aWVzIjogeyJiYXNlX3llYXIiOiAiMjAxMyIsICJjb2RlIjogIjExMDEwIiwgImhpZ2hsaWdodCI6IHt9LCAibmFtZSI6ICJcdWM4ODVcdWI4NWNcdWFkNmMiLCAibmFtZV9lbmciOiAiSm9uZ25vLWd1IiwgInN0eWxlIjogeyJjb2xvciI6ICJibGFjayIsICJmaWxsQ29sb3IiOiAiIzBjMmM4NCIsICJmaWxsT3BhY2l0eSI6IDAuNiwgIm9wYWNpdHkiOiAxLCAid2VpZ2h0IjogMX19LCAidHlwZSI6ICJGZWF0dXJlIn1dLCAidHlwZSI6ICJGZWF0dXJlQ29sbGVjdGlvbiJ9CiAgICAgICAgICAgIAogICAgICAgICAgICApLmFkZFRvKG1hcF81MGE5NjI1NjkzMDQ0NjdjODFkMTRkMmVlNDQzNDU5Nik7CiAgICAgICAgZ2VvX2pzb25fYWQzMGExZmFhZmE2NDY5NTkxOWMxNDk1ZGRjMDlkN2Iuc2V0U3R5bGUoZnVuY3Rpb24oZmVhdHVyZSkge3JldHVybiBmZWF0dXJlLnByb3BlcnRpZXMuc3R5bGU7fSk7CiAgICAgICAgCiAgICAKICAgIHZhciBjb2xvcl9tYXBfNzQ1OGY0OWJiNDA0NDg3ZWFkNjNhMDA2MTEzOWY3M2QgPSB7fTsKCiAgICAKICAgIGNvbG9yX21hcF83NDU4ZjQ5YmI0MDQ0ODdlYWQ2M2EwMDYxMTM5ZjczZC5jb2xvciA9IGQzLnNjYWxlLnRocmVzaG9sZCgpCiAgICAgICAgICAgICAgLmRvbWFpbihbMzQuNzcyNSwgMzQuOTI3MzM5Njc5MzU4NzIsIDM1LjA4MjE3OTM1ODcxNzQzLCAzNS4yMzcwMTkwMzgwNzYxNTYsIDM1LjM5MTg1ODcxNzQzNDg3LCAzNS41NDY2OTgzOTY3OTM1OSwgMzUuNzAxNTM4MDc2MTUyMywgMzUuODU2Mzc3NzU1NTExMDI2LCAzNi4wMTEyMTc0MzQ4Njk3NCwgMzYuMTY2MDU3MTE0MjI4NDYsIDM2LjMyMDg5Njc5MzU4NzE3NCwgMzYuNDc1NzM2NDcyOTQ1ODksIDM2LjYzMDU3NjE1MjMwNDYxLCAzNi43ODU0MTU4MzE2NjMzMywgMzYuOTQwMjU1NTExMDIyMDQ1LCAzNy4wOTUwOTUxOTAzODA3NiwgMzcuMjQ5OTM0ODY5NzM5NDgsIDM3LjQwNDc3NDU0OTA5ODIsIDM3LjU1OTYxNDIyODQ1NjkxNSwgMzcuNzE0NDUzOTA3ODE1NjMsIDM3Ljg2OTI5MzU4NzE3NDM1LCAzOC4wMjQxMzMyNjY1MzMwNywgMzguMTc4OTcyOTQ1ODkxNzg2LCAzOC4zMzM4MTI2MjUyNTA1LCAzOC40ODg2NTIzMDQ2MDkyMiwgMzguNjQzNDkxOTgzOTY3OTQsIDM4Ljc5ODMzMTY2MzMyNjY2LCAzOC45NTMxNzEzNDI2ODUzNywgMzkuMTA4MDExMDIyMDQ0MDksIDM5LjI2Mjg1MDcwMTQwMjgwNSwgMzkuNDE3NjkwMzgwNzYxNTMsIDM5LjU3MjUzMDA2MDEyMDI0LCAzOS43MjczNjk3Mzk0Nzg5NiwgMzkuODgyMjA5NDE4ODM3Njc1LCA0MC4wMzcwNDkwOTgxOTYzOSwgNDAuMTkxODg4Nzc3NTU1MTE0LCA0MC4zNDY3Mjg0NTY5MTM4MywgNDAuNTAxNTY4MTM2MjcyNTQ2LCA0MC42NTY0MDc4MTU2MzEyNiwgNDAuODExMjQ3NDk0OTg5OTg1LCA0MC45NjYwODcxNzQzNDg3LCA0MS4xMjA5MjY4NTM3MDc0MiwgNDEuMjc1NzY2NTMzMDY2MTMsIDQxLjQzMDYwNjIxMjQyNDg1LCA0MS41ODU0NDU4OTE3ODM1NywgNDEuNzQwMjg1NTcxMTQyMjksIDQxLjg5NTEyNTI1MDUwMSwgNDIuMDQ5OTY0OTI5ODU5NzIsIDQyLjIwNDgwNDYwOTIxODQ0LCA0Mi4zNTk2NDQyODg1NzcxNiwgNDIuNTE0NDgzOTY3OTM1ODc0LCA0Mi42NjkzMjM2NDcyOTQ1OSwgNDIuODI0MTYzMzI2NjUzMzA2LCA0Mi45NzkwMDMwMDYwMTIwMywgNDMuMTMzODQyNjg1MzcwNzQ1LCA0My4yODg2ODIzNjQ3Mjk0NiwgNDMuNDQzNTIyMDQ0MDg4MTgsIDQzLjU5ODM2MTcyMzQ0NjksIDQzLjc1MzIwMTQwMjgwNTYxNSwgNDMuOTA4MDQxMDgyMTY0MzMsIDQ0LjA2Mjg4MDc2MTUyMzA1LCA0NC4yMTc3MjA0NDA4ODE3NiwgNDQuMzcyNTYwMTIwMjQwNDg2LCA0NC41MjczOTk3OTk1OTkyLCA0NC42ODIyMzk0Nzg5NTc5MiwgNDQuODM3MDc5MTU4MzE2NjQsIDQ0Ljk5MTkxODgzNzY3NTM2LCA0NS4xNDY3NTg1MTcwMzQwNywgNDUuMzAxNTk4MTk2MzkyNzksIDQ1LjQ1NjQzNzg3NTc1MTUwNCwgNDUuNjExMjc3NTU1MTEwMjIsIDQ1Ljc2NjExNzIzNDQ2ODk0LCA0NS45MjA5NTY5MTM4Mjc2NiwgNDYuMDc1Nzk2NTkzMTg2Mzc1LCA0Ni4yMzA2MzYyNzI1NDUxLCA0Ni4zODU0NzU5NTE5MDM4MTQsIDQ2LjU0MDMxNTYzMTI2MjUzLCA0Ni42OTUxNTUzMTA2MjEyNDYsIDQ2Ljg0OTk5NDk4OTk3OTk2LCA0Ny4wMDQ4MzQ2NjkzMzg2OCwgNDcuMTU5Njc0MzQ4Njk3MzksIDQ3LjMxNDUxNDAyODA1NjEyLCA0Ny40NjkzNTM3MDc0MTQ4MywgNDcuNjI0MTkzMzg2NzczNTUsIDQ3Ljc3OTAzMzA2NjEzMjI3LCA0Ny45MzM4NzI3NDU0OTA5OSwgNDguMDg4NzEyNDI0ODQ5NywgNDguMjQzNTUyMTA0MjA4NDIsIDQ4LjM5ODM5MTc4MzU2NzEzNSwgNDguNTUzMjMxNDYyOTI1ODUsIDQ4LjcwODA3MTE0MjI4NDU3NCwgNDguODYyOTEwODIxNjQzMjksIDQ5LjAxNzc1MDUwMTAwMjAwNiwgNDkuMTcyNTkwMTgwMzYwNzMsIDQ5LjMyNzQyOTg1OTcxOTQ0NCwgNDkuNDgyMjY5NTM5MDc4MTYsIDQ5LjYzNzEwOTIxODQzNjg3NiwgNDkuNzkxOTQ4ODk3Nzk1NTksIDQ5Ljk0Njc4ODU3NzE1NDMxLCA1MC4xMDE2MjgyNTY1MTMwMywgNTAuMjU2NDY3OTM1ODcxNzUsIDUwLjQxMTMwNzYxNTIzMDQ2LCA1MC41NjYxNDcyOTQ1ODkxODYsIDUwLjcyMDk4Njk3Mzk0NzksIDUwLjg3NTgyNjY1MzMwNjYyLCA1MS4wMzA2NjYzMzI2NjUzMzQsIDUxLjE4NTUwNjAxMjAyNDA1LCA1MS4zNDAzNDU2OTEzODI3NjUsIDUxLjQ5NTE4NTM3MDc0MTQ4LCA1MS42NTAwMjUwNTAxMDAyMDQsIDUxLjgwNDg2NDcyOTQ1ODkyLCA1MS45NTk3MDQ0MDg4MTc2NCwgNTIuMTE0NTQ0MDg4MTc2MzYsIDUyLjI2OTM4Mzc2NzUzNTA3NSwgNTIuNDI0MjIzNDQ2ODkzNzksIDUyLjU3OTA2MzEyNjI1MjUxLCA1Mi43MzM5MDI4MDU2MTEyMiwgNTIuODg4NzQyNDg0OTY5OTQsIDUzLjA0MzU4MjE2NDMyODY2LCA1My4xOTg0MjE4NDM2ODczOCwgNTMuMzUzMjYxNTIzMDQ2MSwgNTMuNTA4MTAxMjAyNDA0ODE2LCA1My42NjI5NDA4ODE3NjM1MywgNTMuODE3NzgwNTYxMTIyMjUsIDUzLjk3MjYyMDI0MDQ4MDk2NCwgNTQuMTI3NDU5OTE5ODM5NjgsIDU0LjI4MjI5OTU5OTE5ODM5NiwgNTQuNDM3MTM5Mjc4NTU3MTIsIDU0LjU5MTk3ODk1NzkxNTgzNSwgNTQuNzQ2ODE4NjM3Mjc0NTYsIDU0LjkwMTY1ODMxNjYzMzI3NCwgNTUuMDU2NDk3OTk1OTkxOTksIDU1LjIxMTMzNzY3NTM1MDcwNSwgNTUuMzY2MTc3MzU0NzA5NDIsIDU1LjUyMTAxNzAzNDA2ODE0LCA1NS42NzU4NTY3MTM0MjY4NSwgNTUuODMwNjk2MzkyNzg1NTc2LCA1NS45ODU1MzYwNzIxNDQyOSwgNTYuMTQwMzc1NzUxNTAzMDE1LCA1Ni4yOTUyMTU0MzA4NjE3MywgNTYuNDUwMDU1MTEwMjIwNDUsIDU2LjYwNDg5NDc4OTU3OTE2LCA1Ni43NTk3MzQ0Njg5Mzc4OCwgNTYuOTE0NTc0MTQ4Mjk2NTk1LCA1Ny4wNjk0MTM4Mjc2NTUzMSwgNTcuMjI0MjUzNTA3MDE0MDMsIDU3LjM3OTA5MzE4NjM3Mjc1LCA1Ny41MzM5MzI4NjU3MzE0NywgNTcuNjg4NzcyNTQ1MDkwMTksIDU3Ljg0MzYxMjIyNDQ0ODkwNCwgNTcuOTk4NDUxOTAzODA3NjIsIDU4LjE1MzI5MTU4MzE2NjMzNiwgNTguMzA4MTMxMjYyNTI1MDUsIDU4LjQ2Mjk3MDk0MTg4Mzc3LCA1OC42MTc4MTA2MjEyNDI0OSwgNTguNzcyNjUwMzAwNjAxMjEsIDU4LjkyNzQ4OTk3OTk1OTkzLCA1OS4wODIzMjk2NTkzMTg2NDYsIDU5LjIzNzE2OTMzODY3NzM2LCA1OS4zOTIwMDkwMTgwMzYwOCwgNTkuNTQ2ODQ4Njk3Mzk0NzksIDU5LjcwMTY4ODM3Njc1MzUxLCA1OS44NTY1MjgwNTYxMTIyMjUsIDYwLjAxMTM2NzczNTQ3MDk0LCA2MC4xNjYyMDc0MTQ4Mjk2NjQsIDYwLjMyMTA0NzA5NDE4ODM5LCA2MC40NzU4ODY3NzM1NDcxLCA2MC42MzA3MjY0NTI5MDU4MiwgNjAuNzg1NTY2MTMyMjY0NTM1LCA2MC45NDA0MDU4MTE2MjMyNSwgNjEuMDk1MjQ1NDkwOTgxOTY2LCA2MS4yNTAwODUxNzAzNDA2OCwgNjEuNDA0OTI0ODQ5Njk5NCwgNjEuNTU5NzY0NTI5MDU4MTMsIDYxLjcxNDYwNDIwODQxNjg0NCwgNjEuODY5NDQzODg3Nzc1NTYsIDYyLjAyNDI4MzU2NzEzNDI3NiwgNjIuMTc5MTIzMjQ2NDkyOTksIDYyLjMzMzk2MjkyNTg1MTcxLCA2Mi40ODg4MDI2MDUyMTA0MjQsIDYyLjY0MzY0MjI4NDU2OTE0LCA2Mi43OTg0ODE5NjM5Mjc4NTYsIDYyLjk1MzMyMTY0MzI4NjU4NiwgNjMuMTA4MTYxMzIyNjQ1MywgNjMuMjYzMDAxMDAyMDA0MDIsIDYzLjQxNzg0MDY4MTM2MjczLCA2My41NzI2ODAzNjA3MjE0NSwgNjMuNzI3NTIwMDQwMDgwMTY1LCA2My44ODIzNTk3MTk0Mzg4OCwgNjQuMDM3MTk5Mzk4Nzk3NiwgNjQuMTkyMDM5MDc4MTU2MzEsIDY0LjM0Njg3ODc1NzUxNTA0LCA2NC41MDE3MTg0MzY4NzM3NiwgNjQuNjU2NTU4MTE2MjMyNDcsIDY0LjgxMTM5Nzc5NTU5MTE5LCA2NC45NjYyMzc0NzQ5NDk5LCA2NS4xMjEwNzcxNTQzMDg2MiwgNjUuMjc1OTE2ODMzNjY3MzQsIDY1LjQzMDc1NjUxMzAyNjA1LCA2NS41ODU1OTYxOTIzODQ3NywgNjUuNzQwNDM1ODcxNzQzNSwgNjUuODk1Mjc1NTUxMTAyMjIsIDY2LjA1MDExNTIzMDQ2MDkzLCA2Ni4yMDQ5NTQ5MDk4MTk2NSwgNjYuMzU5Nzk0NTg5MTc4MzYsIDY2LjUxNDYzNDI2ODUzNzA4LCA2Ni42Njk0NzM5NDc4OTU4LCA2Ni44MjQzMTM2MjcyNTQ1MywgNjYuOTc5MTUzMzA2NjEzMjMsIDY3LjEzMzk5Mjk4NTk3MTk2LCA2Ny4yODg4MzI2NjUzMzA2NiwgNjcuNDQzNjcyMzQ0Njg5MzksIDY3LjU5ODUxMjAyNDA0ODEsIDY3Ljc1MzM1MTcwMzQwNjgyLCA2Ny45MDgxOTEzODI3NjU1NCwgNjguMDYzMDMxMDYyMTI0MjUsIDY4LjIxNzg3MDc0MTQ4Mjk3LCA2OC4zNzI3MTA0MjA4NDE2OCwgNjguNTI3NTUwMTAwMjAwNDEsIDY4LjY4MjM4OTc3OTU1OTEyLCA2OC44MzcyMjk0NTg5MTc4NSwgNjguOTkyMDY5MTM4Mjc2NTUsIDY5LjE0NjkwODgxNzYzNTI4LCA2OS4zMDE3NDg0OTY5OTQwMSwgNjkuNDU2NTg4MTc2MzUyNzEsIDY5LjYxMTQyNzg1NTcxMTQ0LCA2OS43NjYyNjc1MzUwNzAxNCwgNjkuOTIxMTA3MjE0NDI4ODcsIDcwLjA3NTk0Njg5Mzc4NzU3LCA3MC4yMzA3ODY1NzMxNDYzLCA3MC4zODU2MjYyNTI1MDUwMiwgNzAuNTQwNDY1OTMxODYzNzQsIDcwLjY5NTMwNTYxMTIyMjQ1LCA3MC44NTAxNDUyOTA1ODExNywgNzEuMDA0OTg0OTY5OTM5ODgsIDcxLjE1OTgyNDY0OTI5ODYsIDcxLjMxNDY2NDMyODY1NzMzLCA3MS40Njk1MDQwMDgwMTYwMywgNzEuNjI0MzQzNjg3Mzc0NzYsIDcxLjc3OTE4MzM2NjczMzQ2LCA3MS45MzQwMjMwNDYwOTIyLCA3Mi4wODg4NjI3MjU0NTA5MiwgNzIuMjQzNzAyNDA0ODA5NjIsIDcyLjM5ODU0MjA4NDE2ODM1LCA3Mi41NTMzODE3NjM1MjcwNiwgNzIuNzA4MjIxNDQyODg1NzksIDcyLjg2MzA2MTEyMjI0NDQ5LCA3My4wMTc5MDA4MDE2MDMyMiwgNzMuMTcyNzQwNDgwOTYxOTMsIDczLjMyNzU4MDE2MDMyMDY1LCA3My40ODI0MTk4Mzk2NzkzNywgNzMuNjM3MjU5NTE5MDM4MDgsIDczLjc5MjA5OTE5ODM5NjgsIDczLjk0NjkzODg3Nzc1NTUxLCA3NC4xMDE3Nzg1NTcxMTQyNCwgNzQuMjU2NjE4MjM2NDcyOTUsIDc0LjQxMTQ1NzkxNTgzMTY4LCA3NC41NjYyOTc1OTUxOTAzOCwgNzQuNzIxMTM3Mjc0NTQ5MTEsIDc0Ljg3NTk3Njk1MzkwNzgyLCA3NS4wMzA4MTY2MzMyNjY1NCwgNzUuMTg1NjU2MzEyNjI1MjcsIDc1LjM0MDQ5NTk5MTk4Mzk3LCA3NS40OTUzMzU2NzEzNDI3LCA3NS42NTAxNzUzNTA3MDE0LCA3NS44MDUwMTUwMzAwNjAxMywgNzUuOTU5ODU0NzA5NDE4ODUsIDc2LjExNDY5NDM4ODc3NzU2LCA3Ni4yNjk1MzQwNjgxMzYyOCwgNzYuNDI0MzczNzQ3NDk1LCA3Ni41NzkyMTM0MjY4NTM3MSwgNzYuNzM0MDUzMTA2MjEyNDMsIDc2Ljg4ODg5Mjc4NTU3MTE2LCA3Ny4wNDM3MzI0NjQ5Mjk4NiwgNzcuMTk4NTcyMTQ0Mjg4NTksIDc3LjM1MzQxMTgyMzY0NzMsIDc3LjUwODI1MTUwMzAwNjAyLCA3Ny42NjMwOTExODIzNjQ3NCwgNzcuODE3OTMwODYxNzIzNDUsIDc3Ljk3Mjc3MDU0MTA4MjE4LCA3OC4xMjc2MTAyMjA0NDA4OSwgNzguMjgyNDQ5ODk5Nzk5NjIsIDc4LjQzNzI4OTU3OTE1ODMyLCA3OC41OTIxMjkyNTg1MTcwNSwgNzguNzQ2OTY4OTM3ODc1NzYsIDc4LjkwMTgwODYxNzIzNDQ4LCA3OS4wNTY2NDgyOTY1OTMyLCA3OS4yMTE0ODc5NzU5NTE5MSwgNzkuMzY2MzI3NjU1MzEwNjMsIDc5LjUyMTE2NzMzNDY2OTM0LCA3OS42NzYwMDcwMTQwMjgwNywgNzkuODMwODQ2NjkzMzg2NzcsIDc5Ljk4NTY4NjM3Mjc0NTUsIDgwLjE0MDUyNjA1MjEwNDIyLCA4MC4yOTUzNjU3MzE0NjI5NCwgODAuNDUwMjA1NDEwODIxNjUsIDgwLjYwNTA0NTA5MDE4MDM3LCA4MC43NTk4ODQ3Njk1MzkxLCA4MC45MTQ3MjQ0NDg4OTc4LCA4MS4wNjk1NjQxMjgyNTY1MywgODEuMjI0NDAzODA3NjE1MjMsIDgxLjM3OTI0MzQ4Njk3Mzk2LCA4MS41MzQwODMxNjYzMzI2OCwgODEuNjg4OTIyODQ1NjkxNCwgODEuODQzNzYyNTI1MDUwMTEsIDgxLjk5ODYwMjIwNDQwODgzLCA4Mi4xNTM0NDE4ODM3Njc1NCwgODIuMzA4MjgxNTYzMTI2MjYsIDgyLjQ2MzEyMTI0MjQ4NDk5LCA4Mi42MTc5NjA5MjE4NDM2OSwgODIuNzcyODAwNjAxMjAyNDIsIDgyLjkyNzY0MDI4MDU2MTE0LCA4My4wODI0Nzk5NTk5MTk4NSwgODMuMjM3MzE5NjM5Mjc4NTcsIDgzLjM5MjE1OTMxODYzNzI4LCA4My41NDY5OTg5OTc5OTYwMSwgODMuNzAxODM4Njc3MzU0NzEsIDgzLjg1NjY3ODM1NjcxMzQ1LCA4NC4wMTE1MTgwMzYwNzIxNSwgODQuMTY2MzU3NzE1NDMwODgsIDg0LjMyMTE5NzM5NDc4OTU4LCA4NC40NzYwMzcwNzQxNDgzMSwgODQuNjMwODc2NzUzNTA3MDIsIDg0Ljc4NTcxNjQzMjg2NTc0LCA4NC45NDA1NTYxMTIyMjQ0NiwgODUuMDk1Mzk1NzkxNTgzMTcsIDg1LjI1MDIzNTQ3MDk0MTg5LCA4NS40MDUwNzUxNTAzMDA2LCA4NS41NTk5MTQ4Mjk2NTkzMywgODUuNzE0NzU0NTA5MDE4MDUsIDg1Ljg2OTU5NDE4ODM3Njc3LCA4Ni4wMjQ0MzM4Njc3MzU0OCwgODYuMTc5MjczNTQ3MDk0MiwgODYuMzM0MTEzMjI2NDUyOTMsIDg2LjQ4ODk1MjkwNTgxMTYzLCA4Ni42NDM3OTI1ODUxNzAzNiwgODYuNzk4NjMyMjY0NTI5MDYsIDg2Ljk1MzQ3MTk0Mzg4Nzc5LCA4Ny4xMDgzMTE2MjMyNDY1LCA4Ny4yNjMxNTEzMDI2MDUyMiwgODcuNDE3OTkwOTgxOTYzOTQsIDg3LjU3MjgzMDY2MTMyMjY2LCA4Ny43Mjc2NzAzNDA2ODEzNywgODcuODgyNTEwMDIwMDQwMDksIDg4LjAzNzM0OTY5OTM5ODgsIDg4LjE5MjE4OTM3ODc1NzUyLCA4OC4zNDcwMjkwNTgxMTYyNSwgODguNTAxODY4NzM3NDc0OTYsIDg4LjY1NjcwODQxNjgzMzY4LCA4OC44MTE1NDgwOTYxOTI0LCA4OC45NjYzODc3NzU1NTExMSwgODkuMTIxMjI3NDU0OTA5ODQsIDg5LjI3NjA2NzEzNDI2ODU0LCA4OS40MzA5MDY4MTM2MjcyNywgODkuNTg1NzQ2NDkyOTg1OTgsIDg5Ljc0MDU4NjE3MjM0NDcsIDg5Ljg5NTQyNTg1MTcwMzQxLCA5MC4wNTAyNjU1MzEwNjIxNCwgOTAuMjA1MTA1MjEwNDIwODUsIDkwLjM1OTk0NDg4OTc3OTU3LCA5MC41MTQ3ODQ1NjkxMzgyOSwgOTAuNjY5NjI0MjQ4NDk3LCA5MC44MjQ0NjM5Mjc4NTU3MiwgOTAuOTc5MzAzNjA3MjE0NDMsIDkxLjEzNDE0MzI4NjU3MzE2LCA5MS4yODg5ODI5NjU5MzE4OCwgOTEuNDQzODIyNjQ1MjkwNiwgOTEuNTk4NjYyMzI0NjQ5MzEsIDkxLjc1MzUwMjAwNDAwODAzLCA5MS45MDgzNDE2ODMzNjY3NiwgOTIuMDYzMTgxMzYyNzI1NDYsIDkyLjIxODAyMTA0MjA4NDE5LCA5Mi4zNzI4NjA3MjE0NDI4OSwgOTIuNTI3NzAwNDAwODAxNjIsIDkyLjY4MjU0MDA4MDE2MDMyLCA5Mi44MzczNzk3NTk1MTkwNSwgOTIuOTkyMjE5NDM4ODc3NzcsIDkzLjE0NzA1OTExODIzNjQ4LCA5My4zMDE4OTg3OTc1OTUyLCA5My40NTY3Mzg0NzY5NTM5MiwgOTMuNjExNTc4MTU2MzEyNjMsIDkzLjc2NjQxNzgzNTY3MTM1LCA5My45MjEyNTc1MTUwMzAwOCwgOTQuMDc2MDk3MTk0Mzg4OCwgOTQuMjMwOTM2ODczNzQ3NTEsIDk0LjM4NTc3NjU1MzEwNjIzLCA5NC41NDA2MTYyMzI0NjQ5NCwgOTQuNjk1NDU1OTExODIzNjYsIDk0Ljg1MDI5NTU5MTE4MjM3LCA5NS4wMDUxMzUyNzA1NDExLCA5NS4xNTk5NzQ5NDk4OTk4LCA5NS4zMTQ4MTQ2MjkyNTg1NCwgOTUuNDY5NjU0MzA4NjE3MjQsIDk1LjYyNDQ5Mzk4Nzk3NTk3LCA5NS43NzkzMzM2NjczMzQ2OCwgOTUuOTM0MTczMzQ2NjkzNCwgOTYuMDg5MDEzMDI2MDUyMTEsIDk2LjI0Mzg1MjcwNTQxMDgzLCA5Ni4zOTg2OTIzODQ3Njk1NSwgOTYuNTUzNTMyMDY0MTI4MjYsIDk2LjcwODM3MTc0MzQ4Njk5LCA5Ni44NjMyMTE0MjI4NDU3MSwgOTcuMDE4MDUxMTAyMjA0NDIsIDk3LjE3Mjg5MDc4MTU2MzE0LCA5Ny4zMjc3MzA0NjA5MjE4NiwgOTcuNDgyNTcwMTQwMjgwNTcsIDk3LjYzNzQwOTgxOTYzOTI5LCA5Ny43OTIyNDk0OTg5OTgwMiwgOTcuOTQ3MDg5MTc4MzU2NzIsIDk4LjEwMTkyODg1NzcxNTQ1LCA5OC4yNTY3Njg1MzcwNzQxNSwgOTguNDExNjA4MjE2NDMyODgsIDk4LjU2NjQ0Nzg5NTc5MTYsIDk4LjcyMTI4NzU3NTE1MDMxLCA5OC44NzYxMjcyNTQ1MDkwNCwgOTkuMDMwOTY2OTMzODY3NzUsIDk5LjE4NTgwNjYxMzIyNjQ4LCA5OS4zNDA2NDYyOTI1ODUxOCwgOTkuNDk1NDg1OTcxOTQzOSwgOTkuNjUwMzI1NjUxMzAyNjEsIDk5LjgwNTE2NTMzMDY2MTM0LCA5OS45NjAwMDUwMTAwMjAwNCwgMTAwLjExNDg0NDY4OTM3ODc3LCAxMDAuMjY5Njg0MzY4NzM3NDcsIDEwMC40MjQ1MjQwNDgwOTYyLCAxMDAuNTc5MzYzNzI3NDU0OTMsIDEwMC43MzQyMDM0MDY4MTM2MywgMTAwLjg4OTA0MzA4NjE3MjM2LCAxMDEuMDQzODgyNzY1NTMxMDcsIDEwMS4xOTg3MjI0NDQ4ODk4LCAxMDEuMzUzNTYyMTI0MjQ4NSwgMTAxLjUwODQwMTgwMzYwNzIzLCAxMDEuNjYzMjQxNDgyOTY1OTMsIDEwMS44MTgwODExNjIzMjQ2NiwgMTAxLjk3MjkyMDg0MTY4MzM5LCAxMDIuMTI3NzYwNTIxMDQyMDksIDEwMi4yODI2MDAyMDA0MDA4MiwgMTAyLjQzNzQzOTg3OTc1OTUyLCAxMDIuNTkyMjc5NTU5MTE4MjUsIDEwMi43NDcxMTkyMzg0NzY5NiwgMTAyLjkwMTk1ODkxNzgzNTY5LCAxMDMuMDU2Nzk4NTk3MTk0MzksIDEwMy4yMTE2MzgyNzY1NTMxMiwgMTAzLjM2NjQ3Nzk1NTkxMTgyLCAxMDMuNTIxMzE3NjM1MjcwNTUsIDEwMy42NzYxNTczMTQ2MjkyOCwgMTAzLjgzMDk5Njk5Mzk4ODAxLCAxMDMuOTg1ODM2NjczMzQ2NzEsIDEwNC4xNDA2NzYzNTI3MDU0NCwgMTA0LjI5NTUxNjAzMjA2NDE0LCAxMDQuNDUwMzU1NzExNDIyODcsIDEwNC42MDUxOTUzOTA3ODE1NywgMTA0Ljc2MDAzNTA3MDE0MDMsIDEwNC45MTQ4NzQ3NDk0OTksIDEwNS4wNjk3MTQ0Mjg4NTc3NCwgMTA1LjIyNDU1NDEwODIxNjQ0LCAxMDUuMzc5MzkzNzg3NTc1MTcsIDEwNS41MzQyMzM0NjY5MzM4NywgMTA1LjY4OTA3MzE0NjI5MjYsIDEwNS44NDM5MTI4MjU2NTEzMywgMTA1Ljk5ODc1MjUwNTAxMDAzLCAxMDYuMTUzNTkyMTg0MzY4NzYsIDEwNi4zMDg0MzE4NjM3Mjc0NiwgMTA2LjQ2MzI3MTU0MzA4NjIsIDEwNi42MTgxMTEyMjI0NDQ5LCAxMDYuNzcyOTUwOTAxODAzNjMsIDEwNi45Mjc3OTA1ODExNjIzMywgMTA3LjA4MjYzMDI2MDUyMTA2LCAxMDcuMjM3NDY5OTM5ODc5NzYsIDEwNy4zOTIzMDk2MTkyMzg0OSwgMTA3LjU0NzE0OTI5ODU5NzIyLCAxMDcuNzAxOTg4OTc3OTU1OTIsIDEwNy44NTY4Mjg2NTczMTQ2NSwgMTA4LjAxMTY2ODMzNjY3MzM1LCAxMDguMTY2NTA4MDE2MDMyMDgsIDEwOC4zMjEzNDc2OTUzOTA3OCwgMTA4LjQ3NjE4NzM3NDc0OTUxLCAxMDguNjMxMDI3MDU0MTA4MjIsIDEwOC43ODU4NjY3MzM0NjY5NSwgMTA4Ljk0MDcwNjQxMjgyNTY1LCAxMDkuMDk1NTQ2MDkyMTg0MzgsIDEwOS4yNTAzODU3NzE1NDMxMSwgMTA5LjQwNTIyNTQ1MDkwMTg0LCAxMDkuNTYwMDY1MTMwMjYwNTQsIDEwOS43MTQ5MDQ4MDk2MTkyNywgMTA5Ljg2OTc0NDQ4ODk3Nzk3LCAxMTAuMDI0NTg0MTY4MzM2NywgMTEwLjE3OTQyMzg0NzY5NTQsIDExMC4zMzQyNjM1MjcwNTQxMywgMTEwLjQ4OTEwMzIwNjQxMjg0LCAxMTAuNjQzOTQyODg1NzcxNTcsIDExMC43OTg3ODI1NjUxMzAyNywgMTEwLjk1MzYyMjI0NDQ4OSwgMTExLjEwODQ2MTkyMzg0NzcsIDExMS4yNjMzMDE2MDMyMDY0MywgMTExLjQxODE0MTI4MjU2NTE2LCAxMTEuNTcyOTgwOTYxOTIzODYsIDExMS43Mjc4MjA2NDEyODI1OSwgMTExLjg4MjY2MDMyMDY0MTI5LCAxMTIuMDM3NTAwMDAwMDAwMDJdKQogICAgICAgICAgICAgIC5yYW5nZShbJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyNjN2U5YjQnLCAnI2M3ZTliNCcsICcjYzdlOWI0JywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjN2ZjZGJiJywgJyM3ZmNkYmInLCAnIzdmY2RiYicsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzQxYjZjNCcsICcjNDFiNmM0JywgJyM0MWI2YzQnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMxZDkxYzAnLCAnIzFkOTFjMCcsICcjMWQ5MWMwJywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMjI1ZWE4JywgJyMyMjVlYTgnLCAnIzIyNWVhOCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCcsICcjMGMyYzg0JywgJyMwYzJjODQnLCAnIzBjMmM4NCddKTsKICAgIAoKICAgIGNvbG9yX21hcF83NDU4ZjQ5YmI0MDQ0ODdlYWQ2M2EwMDYxMTM5ZjczZC54ID0gZDMuc2NhbGUubGluZWFyKCkKICAgICAgICAgICAgICAuZG9tYWluKFszNC43NzI1LCAxMTIuMDM3NTAwMDAwMDAwMDJdKQogICAgICAgICAgICAgIC5yYW5nZShbMCwgNDAwXSk7CgogICAgY29sb3JfbWFwXzc0NThmNDliYjQwNDQ4N2VhZDYzYTAwNjExMzlmNzNkLmxlZ2VuZCA9IEwuY29udHJvbCh7cG9zaXRpb246ICd0b3ByaWdodCd9KTsKICAgIGNvbG9yX21hcF83NDU4ZjQ5YmI0MDQ0ODdlYWQ2M2EwMDYxMTM5ZjczZC5sZWdlbmQub25BZGQgPSBmdW5jdGlvbiAobWFwKSB7dmFyIGRpdiA9IEwuRG9tVXRpbC5jcmVhdGUoJ2RpdicsICdsZWdlbmQnKTsgcmV0dXJuIGRpdn07CiAgICBjb2xvcl9tYXBfNzQ1OGY0OWJiNDA0NDg3ZWFkNjNhMDA2MTEzOWY3M2QubGVnZW5kLmFkZFRvKG1hcF81MGE5NjI1NjkzMDQ0NjdjODFkMTRkMmVlNDQzNDU5Nik7CgogICAgY29sb3JfbWFwXzc0NThmNDliYjQwNDQ4N2VhZDYzYTAwNjExMzlmNzNkLnhBeGlzID0gZDMuc3ZnLmF4aXMoKQogICAgICAgIC5zY2FsZShjb2xvcl9tYXBfNzQ1OGY0OWJiNDA0NDg3ZWFkNjNhMDA2MTEzOWY3M2QueCkKICAgICAgICAub3JpZW50KCJ0b3AiKQogICAgICAgIC50aWNrU2l6ZSgxKQogICAgICAgIC50aWNrVmFsdWVzKFszNC43NzI1LCA0Ny42NTAwMDAwMDAwMDAwMDYsIDYwLjUyNzUsIDczLjQwNSwgODYuMjgyNTAwMDAwMDAwMDEsIDk5LjE2LCAxMTIuMDM3NTAwMDAwMDAwMDJdKTsKCiAgICBjb2xvcl9tYXBfNzQ1OGY0OWJiNDA0NDg3ZWFkNjNhMDA2MTEzOWY3M2Quc3ZnID0gZDMuc2VsZWN0KCIubGVnZW5kLmxlYWZsZXQtY29udHJvbCIpLmFwcGVuZCgic3ZnIikKICAgICAgICAuYXR0cigiaWQiLCAnbGVnZW5kJykKICAgICAgICAuYXR0cigid2lkdGgiLCA0NTApCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDQwKTsKCiAgICBjb2xvcl9tYXBfNzQ1OGY0OWJiNDA0NDg3ZWFkNjNhMDA2MTEzOWY3M2QuZyA9IGNvbG9yX21hcF83NDU4ZjQ5YmI0MDQ0ODdlYWQ2M2EwMDYxMTM5ZjczZC5zdmcuYXBwZW5kKCJnIikKICAgICAgICAuYXR0cigiY2xhc3MiLCAia2V5IikKICAgICAgICAuYXR0cigidHJhbnNmb3JtIiwgInRyYW5zbGF0ZSgyNSwxNikiKTsKCiAgICBjb2xvcl9tYXBfNzQ1OGY0OWJiNDA0NDg3ZWFkNjNhMDA2MTEzOWY3M2QuZy5zZWxlY3RBbGwoInJlY3QiKQogICAgICAgIC5kYXRhKGNvbG9yX21hcF83NDU4ZjQ5YmI0MDQ0ODdlYWQ2M2EwMDYxMTM5ZjczZC5jb2xvci5yYW5nZSgpLm1hcChmdW5jdGlvbihkLCBpKSB7CiAgICAgICAgICByZXR1cm4gewogICAgICAgICAgICB4MDogaSA/IGNvbG9yX21hcF83NDU4ZjQ5YmI0MDQ0ODdlYWQ2M2EwMDYxMTM5ZjczZC54KGNvbG9yX21hcF83NDU4ZjQ5YmI0MDQ0ODdlYWQ2M2EwMDYxMTM5ZjczZC5jb2xvci5kb21haW4oKVtpIC0gMV0pIDogY29sb3JfbWFwXzc0NThmNDliYjQwNDQ4N2VhZDYzYTAwNjExMzlmNzNkLngucmFuZ2UoKVswXSwKICAgICAgICAgICAgeDE6IGkgPCBjb2xvcl9tYXBfNzQ1OGY0OWJiNDA0NDg3ZWFkNjNhMDA2MTEzOWY3M2QuY29sb3IuZG9tYWluKCkubGVuZ3RoID8gY29sb3JfbWFwXzc0NThmNDliYjQwNDQ4N2VhZDYzYTAwNjExMzlmNzNkLngoY29sb3JfbWFwXzc0NThmNDliYjQwNDQ4N2VhZDYzYTAwNjExMzlmNzNkLmNvbG9yLmRvbWFpbigpW2ldKSA6IGNvbG9yX21hcF83NDU4ZjQ5YmI0MDQ0ODdlYWQ2M2EwMDYxMTM5ZjczZC54LnJhbmdlKClbMV0sCiAgICAgICAgICAgIHo6IGQKICAgICAgICAgIH07CiAgICAgICAgfSkpCiAgICAgIC5lbnRlcigpLmFwcGVuZCgicmVjdCIpCiAgICAgICAgLmF0dHIoImhlaWdodCIsIDEwKQogICAgICAgIC5hdHRyKCJ4IiwgZnVuY3Rpb24oZCkgeyByZXR1cm4gZC54MDsgfSkKICAgICAgICAuYXR0cigid2lkdGgiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLngxIC0gZC54MDsgfSkKICAgICAgICAuc3R5bGUoImZpbGwiLCBmdW5jdGlvbihkKSB7IHJldHVybiBkLno7IH0pOwoKICAgIGNvbG9yX21hcF83NDU4ZjQ5YmI0MDQ0ODdlYWQ2M2EwMDYxMTM5ZjczZC5nLmNhbGwoY29sb3JfbWFwXzc0NThmNDliYjQwNDQ4N2VhZDYzYTAwNjExMzlmNzNkLnhBeGlzKS5hcHBlbmQoInRleHQiKQogICAgICAgIC5hdHRyKCJjbGFzcyIsICJjYXB0aW9uIikKICAgICAgICAuYXR0cigieSIsIDIxKQogICAgICAgIC50ZXh0KCcnKTsKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
df_econ = df2[['지역','수준지수(서울특별시=100)','재산세 수준지수(서울특별시=100)']]
```


```python
df_econ.to_csv("data/economy_target.csv", encoding="UTF-8")
```


```python
total=pd.merge(df,df_econ, on="지역" )
```


```python
total.to_csv("data/economy_total_data.csv", encoding="UTF-8")
```


```python
corr = df.corr()
corr
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1인가구비율</th>
      <th>1인당 자동차 등록대수</th>
      <th>EQ-5D지표</th>
      <th>가구수</th>
      <th>건강보험 적용인구 현황</th>
      <th>고령인구비율</th>
      <th>교원1인당 학생수</th>
      <th>남녀성비</th>
      <th>노인 천명당 노인여가복지시설수</th>
      <th>대학교 수</th>
      <th>...</th>
      <th>cctv대수</th>
      <th>단순직비율</th>
      <th>전문직비율</th>
      <th>서비스.사무직</th>
      <th>1차산업비율</th>
      <th>2차산업비율</th>
      <th>3차산업비율</th>
      <th>체육시설</th>
      <th>유치원 교원비율</th>
      <th>초등학교 교원비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1인가구비율</th>
      <td>1.000000</td>
      <td>-0.023354</td>
      <td>-0.211930</td>
      <td>-0.299514</td>
      <td>-0.517826</td>
      <td>0.465624</td>
      <td>0.289308</td>
      <td>0.318409</td>
      <td>-0.246952</td>
      <td>0.161400</td>
      <td>...</td>
      <td>0.024950</td>
      <td>0.083416</td>
      <td>-0.070904</td>
      <td>-0.031107</td>
      <td>-0.240484</td>
      <td>0.287560</td>
      <td>-0.287308</td>
      <td>-0.209136</td>
      <td>0.257311</td>
      <td>0.611372</td>
    </tr>
    <tr>
      <th>1인당 자동차 등록대수</th>
      <td>-0.023354</td>
      <td>1.000000</td>
      <td>0.396053</td>
      <td>-0.198103</td>
      <td>-0.085428</td>
      <td>-0.208875</td>
      <td>-0.336957</td>
      <td>-0.078884</td>
      <td>0.359054</td>
      <td>-0.378171</td>
      <td>...</td>
      <td>0.183395</td>
      <td>-0.454541</td>
      <td>0.519313</td>
      <td>-0.189766</td>
      <td>0.335844</td>
      <td>0.175264</td>
      <td>-0.175615</td>
      <td>0.136316</td>
      <td>0.224541</td>
      <td>0.191329</td>
    </tr>
    <tr>
      <th>EQ-5D지표</th>
      <td>-0.211930</td>
      <td>0.396053</td>
      <td>1.000000</td>
      <td>0.057654</td>
      <td>0.124259</td>
      <td>-0.261232</td>
      <td>-0.160260</td>
      <td>-0.027076</td>
      <td>0.552838</td>
      <td>-0.015065</td>
      <td>...</td>
      <td>0.197363</td>
      <td>-0.268048</td>
      <td>0.287185</td>
      <td>-0.060403</td>
      <td>0.086602</td>
      <td>0.000142</td>
      <td>-0.000233</td>
      <td>0.201795</td>
      <td>0.100532</td>
      <td>-0.017419</td>
    </tr>
    <tr>
      <th>가구수</th>
      <td>-0.299514</td>
      <td>-0.198103</td>
      <td>0.057654</td>
      <td>1.000000</td>
      <td>0.962372</td>
      <td>-0.701991</td>
      <td>-0.234332</td>
      <td>-0.204123</td>
      <td>-0.054716</td>
      <td>-0.035535</td>
      <td>...</td>
      <td>0.416848</td>
      <td>-0.319290</td>
      <td>0.390141</td>
      <td>-0.201808</td>
      <td>0.187379</td>
      <td>-0.504774</td>
      <td>0.504576</td>
      <td>0.584218</td>
      <td>-0.049699</td>
      <td>-0.570560</td>
    </tr>
    <tr>
      <th>건강보험 적용인구 현황</th>
      <td>-0.517826</td>
      <td>-0.085428</td>
      <td>0.124259</td>
      <td>0.962372</td>
      <td>1.000000</td>
      <td>-0.773707</td>
      <td>-0.285306</td>
      <td>-0.324780</td>
      <td>0.010375</td>
      <td>-0.084839</td>
      <td>...</td>
      <td>0.381981</td>
      <td>-0.395403</td>
      <td>0.449922</td>
      <td>-0.160143</td>
      <td>0.264045</td>
      <td>-0.550530</td>
      <td>0.550251</td>
      <td>0.616281</td>
      <td>-0.083785</td>
      <td>-0.671339</td>
    </tr>
    <tr>
      <th>고령인구비율</th>
      <td>0.465624</td>
      <td>-0.208875</td>
      <td>-0.261232</td>
      <td>-0.701991</td>
      <td>-0.773707</td>
      <td>1.000000</td>
      <td>0.335224</td>
      <td>0.208236</td>
      <td>-0.185215</td>
      <td>0.250769</td>
      <td>...</td>
      <td>-0.231993</td>
      <td>0.424493</td>
      <td>-0.576849</td>
      <td>0.425465</td>
      <td>-0.288486</td>
      <td>0.287406</td>
      <td>-0.287103</td>
      <td>-0.672231</td>
      <td>0.149504</td>
      <td>0.526685</td>
    </tr>
    <tr>
      <th>교원1인당 학생수</th>
      <td>0.289308</td>
      <td>-0.336957</td>
      <td>-0.160260</td>
      <td>-0.234332</td>
      <td>-0.285306</td>
      <td>0.335224</td>
      <td>1.000000</td>
      <td>-0.119623</td>
      <td>0.068874</td>
      <td>0.823140</td>
      <td>...</td>
      <td>-0.181528</td>
      <td>0.065839</td>
      <td>-0.262258</td>
      <td>0.532906</td>
      <td>-0.368982</td>
      <td>0.062631</td>
      <td>-0.062245</td>
      <td>-0.071870</td>
      <td>0.266460</td>
      <td>-0.005489</td>
    </tr>
    <tr>
      <th>남녀성비</th>
      <td>0.318409</td>
      <td>-0.078884</td>
      <td>-0.027076</td>
      <td>-0.204123</td>
      <td>-0.324780</td>
      <td>0.208236</td>
      <td>-0.119623</td>
      <td>1.000000</td>
      <td>-0.148124</td>
      <td>-0.183950</td>
      <td>...</td>
      <td>-0.130360</td>
      <td>0.708268</td>
      <td>-0.556582</td>
      <td>-0.386932</td>
      <td>0.165044</td>
      <td>0.703606</td>
      <td>-0.703775</td>
      <td>-0.399692</td>
      <td>-0.017568</td>
      <td>0.452540</td>
    </tr>
    <tr>
      <th>노인 천명당 노인여가복지시설수</th>
      <td>-0.246952</td>
      <td>0.359054</td>
      <td>0.552838</td>
      <td>-0.054716</td>
      <td>0.010375</td>
      <td>-0.185215</td>
      <td>0.068874</td>
      <td>-0.148124</td>
      <td>1.000000</td>
      <td>0.083009</td>
      <td>...</td>
      <td>0.106801</td>
      <td>-0.242698</td>
      <td>0.226323</td>
      <td>0.036383</td>
      <td>-0.184694</td>
      <td>0.103948</td>
      <td>-0.103754</td>
      <td>-0.012442</td>
      <td>0.128368</td>
      <td>0.136981</td>
    </tr>
    <tr>
      <th>대학교 수</th>
      <td>0.161400</td>
      <td>-0.378171</td>
      <td>-0.015065</td>
      <td>-0.035535</td>
      <td>-0.084839</td>
      <td>0.250769</td>
      <td>0.823140</td>
      <td>-0.183950</td>
      <td>0.083009</td>
      <td>1.000000</td>
      <td>...</td>
      <td>0.095789</td>
      <td>-0.004649</td>
      <td>-0.163065</td>
      <td>0.453054</td>
      <td>-0.366506</td>
      <td>-0.083042</td>
      <td>0.083425</td>
      <td>0.146566</td>
      <td>0.122763</td>
      <td>-0.113270</td>
    </tr>
    <tr>
      <th>대학교 학생수</th>
      <td>0.370252</td>
      <td>-0.419633</td>
      <td>-0.105035</td>
      <td>-0.102912</td>
      <td>-0.196344</td>
      <td>0.331689</td>
      <td>0.890386</td>
      <td>-0.067889</td>
      <td>-0.012305</td>
      <td>0.926908</td>
      <td>...</td>
      <td>0.049649</td>
      <td>0.028563</td>
      <td>-0.179173</td>
      <td>0.407908</td>
      <td>-0.390064</td>
      <td>0.026151</td>
      <td>-0.025743</td>
      <td>0.035285</td>
      <td>0.155828</td>
      <td>-0.014170</td>
    </tr>
    <tr>
      <th>도로포장률</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>도시지역면적</th>
      <td>-0.374822</td>
      <td>0.207307</td>
      <td>0.240399</td>
      <td>0.620576</td>
      <td>0.692416</td>
      <td>-0.489283</td>
      <td>-0.457293</td>
      <td>-0.567843</td>
      <td>0.006928</td>
      <td>-0.144609</td>
      <td>...</td>
      <td>0.561120</td>
      <td>-0.605640</td>
      <td>0.635399</td>
      <td>-0.100050</td>
      <td>0.228179</td>
      <td>-0.594446</td>
      <td>0.594204</td>
      <td>0.579132</td>
      <td>-0.223188</td>
      <td>-0.479369</td>
    </tr>
    <tr>
      <th>등록외국인 현황</th>
      <td>0.418908</td>
      <td>0.212814</td>
      <td>0.029925</td>
      <td>-0.009980</td>
      <td>-0.147181</td>
      <td>0.098287</td>
      <td>-0.036972</td>
      <td>0.446262</td>
      <td>0.272139</td>
      <td>-0.001728</td>
      <td>...</td>
      <td>0.023319</td>
      <td>0.080468</td>
      <td>0.014335</td>
      <td>-0.253572</td>
      <td>-0.084268</td>
      <td>0.305609</td>
      <td>-0.305519</td>
      <td>-0.160083</td>
      <td>0.204922</td>
      <td>0.436593</td>
    </tr>
    <tr>
      <th>비만율</th>
      <td>0.161545</td>
      <td>-0.206943</td>
      <td>-0.286453</td>
      <td>-0.267542</td>
      <td>-0.343454</td>
      <td>0.366672</td>
      <td>-0.161184</td>
      <td>0.438920</td>
      <td>-0.160696</td>
      <td>-0.224048</td>
      <td>...</td>
      <td>-0.119278</td>
      <td>0.635497</td>
      <td>-0.531784</td>
      <td>-0.259654</td>
      <td>-0.088605</td>
      <td>0.444339</td>
      <td>-0.444244</td>
      <td>-0.341596</td>
      <td>0.020998</td>
      <td>0.348064</td>
    </tr>
    <tr>
      <th>사망률</th>
      <td>0.278474</td>
      <td>-0.317175</td>
      <td>-0.160387</td>
      <td>-0.656168</td>
      <td>-0.707015</td>
      <td>0.877737</td>
      <td>0.353616</td>
      <td>0.341343</td>
      <td>-0.150321</td>
      <td>0.259522</td>
      <td>...</td>
      <td>-0.309920</td>
      <td>0.686299</td>
      <td>-0.835703</td>
      <td>0.425972</td>
      <td>-0.229455</td>
      <td>0.372678</td>
      <td>-0.372436</td>
      <td>-0.568577</td>
      <td>0.195033</td>
      <td>0.460253</td>
    </tr>
    <tr>
      <th>사망자수</th>
      <td>-0.514810</td>
      <td>-0.462595</td>
      <td>0.069266</td>
      <td>0.828339</td>
      <td>0.826882</td>
      <td>-0.432412</td>
      <td>-0.091958</td>
      <td>-0.169262</td>
      <td>-0.040716</td>
      <td>0.123917</td>
      <td>...</td>
      <td>0.281789</td>
      <td>0.027709</td>
      <td>-0.048286</td>
      <td>0.056502</td>
      <td>0.062643</td>
      <td>-0.452263</td>
      <td>0.452196</td>
      <td>0.403748</td>
      <td>-0.046902</td>
      <td>-0.611052</td>
    </tr>
    <tr>
      <th>상수도보급률</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>소년·소녀가정현황</th>
      <td>-0.229774</td>
      <td>0.119330</td>
      <td>0.283959</td>
      <td>0.085161</td>
      <td>0.135177</td>
      <td>-0.208209</td>
      <td>-0.255686</td>
      <td>-0.095325</td>
      <td>0.049212</td>
      <td>-0.283654</td>
      <td>...</td>
      <td>-0.161435</td>
      <td>-0.002632</td>
      <td>0.043439</td>
      <td>-0.110357</td>
      <td>0.080335</td>
      <td>-0.140733</td>
      <td>0.140648</td>
      <td>0.012967</td>
      <td>0.234696</td>
      <td>-0.130243</td>
    </tr>
    <tr>
      <th>순이동인구</th>
      <td>0.273594</td>
      <td>0.064515</td>
      <td>0.136303</td>
      <td>-0.337577</td>
      <td>-0.367332</td>
      <td>0.340627</td>
      <td>0.112531</td>
      <td>-0.105502</td>
      <td>0.183720</td>
      <td>0.047065</td>
      <td>...</td>
      <td>-0.163665</td>
      <td>0.067128</td>
      <td>-0.152993</td>
      <td>0.234204</td>
      <td>-0.458370</td>
      <td>0.151532</td>
      <td>-0.151052</td>
      <td>-0.084981</td>
      <td>0.547832</td>
      <td>0.270130</td>
    </tr>
    <tr>
      <th>스트레스 인지율</th>
      <td>0.004342</td>
      <td>0.090132</td>
      <td>-0.389560</td>
      <td>0.147948</td>
      <td>0.166277</td>
      <td>-0.110761</td>
      <td>0.115991</td>
      <td>-0.413282</td>
      <td>-0.184112</td>
      <td>0.039562</td>
      <td>...</td>
      <td>0.352805</td>
      <td>-0.273663</td>
      <td>0.279018</td>
      <td>-0.023342</td>
      <td>-0.165012</td>
      <td>-0.155043</td>
      <td>0.155215</td>
      <td>0.396096</td>
      <td>0.265197</td>
      <td>-0.393167</td>
    </tr>
    <tr>
      <th>아파트매매가격지수</th>
      <td>0.052387</td>
      <td>-0.405117</td>
      <td>-0.210493</td>
      <td>-0.562128</td>
      <td>-0.567590</td>
      <td>0.628127</td>
      <td>0.367539</td>
      <td>0.258989</td>
      <td>-0.187500</td>
      <td>0.260665</td>
      <td>...</td>
      <td>-0.315464</td>
      <td>0.664674</td>
      <td>-0.697717</td>
      <td>0.110838</td>
      <td>-0.258244</td>
      <td>0.490638</td>
      <td>-0.490366</td>
      <td>-0.418798</td>
      <td>-0.103436</td>
      <td>0.178695</td>
    </tr>
    <tr>
      <th>아파트월세통합가격지수</th>
      <td>-0.266480</td>
      <td>0.154535</td>
      <td>-0.021186</td>
      <td>-0.032663</td>
      <td>0.076776</td>
      <td>-0.156746</td>
      <td>-0.122934</td>
      <td>-0.247288</td>
      <td>-0.124016</td>
      <td>-0.113156</td>
      <td>...</td>
      <td>0.128053</td>
      <td>-0.311338</td>
      <td>0.276023</td>
      <td>0.085338</td>
      <td>0.300778</td>
      <td>-0.230452</td>
      <td>0.230137</td>
      <td>0.084337</td>
      <td>-0.525076</td>
      <td>-0.279902</td>
    </tr>
    <tr>
      <th>유아 천명당 보육시설수</th>
      <td>-0.207788</td>
      <td>-0.399570</td>
      <td>0.159451</td>
      <td>-0.053728</td>
      <td>-0.074107</td>
      <td>0.111103</td>
      <td>0.109689</td>
      <td>0.484733</td>
      <td>0.095203</td>
      <td>0.208075</td>
      <td>...</td>
      <td>-0.113605</td>
      <td>0.662893</td>
      <td>-0.680389</td>
      <td>0.068769</td>
      <td>0.084544</td>
      <td>0.227426</td>
      <td>-0.227513</td>
      <td>-0.116929</td>
      <td>-0.045089</td>
      <td>0.113819</td>
    </tr>
    <tr>
      <th>음주율</th>
      <td>0.227528</td>
      <td>-0.050806</td>
      <td>0.166307</td>
      <td>0.043922</td>
      <td>0.009579</td>
      <td>-0.109250</td>
      <td>0.325612</td>
      <td>0.156724</td>
      <td>-0.225005</td>
      <td>0.220727</td>
      <td>...</td>
      <td>-0.140156</td>
      <td>-0.060405</td>
      <td>0.065636</td>
      <td>-0.016092</td>
      <td>0.167782</td>
      <td>0.194036</td>
      <td>-0.194210</td>
      <td>0.054691</td>
      <td>0.010797</td>
      <td>-0.057064</td>
    </tr>
    <tr>
      <th>흡연율</th>
      <td>0.611769</td>
      <td>-0.098146</td>
      <td>-0.389013</td>
      <td>-0.426485</td>
      <td>-0.552234</td>
      <td>0.666227</td>
      <td>0.011777</td>
      <td>0.257828</td>
      <td>-0.367052</td>
      <td>0.007377</td>
      <td>...</td>
      <td>0.026919</td>
      <td>0.423327</td>
      <td>-0.450149</td>
      <td>0.086204</td>
      <td>-0.223898</td>
      <td>0.269616</td>
      <td>-0.269380</td>
      <td>-0.317007</td>
      <td>0.208882</td>
      <td>0.575612</td>
    </tr>
    <tr>
      <th>인구 십만명당 문화기반시설수</th>
      <td>0.352513</td>
      <td>0.252521</td>
      <td>-0.060720</td>
      <td>-0.585440</td>
      <td>-0.566996</td>
      <td>0.506862</td>
      <td>0.193417</td>
      <td>0.039299</td>
      <td>-0.005567</td>
      <td>0.144158</td>
      <td>...</td>
      <td>-0.056810</td>
      <td>-0.033666</td>
      <td>-0.078200</td>
      <td>0.301195</td>
      <td>0.116997</td>
      <td>0.161446</td>
      <td>-0.161567</td>
      <td>-0.294410</td>
      <td>0.036833</td>
      <td>0.529618</td>
    </tr>
    <tr>
      <th>인구 십만명당 사회복지시설수</th>
      <td>-0.020727</td>
      <td>-0.435650</td>
      <td>-0.226415</td>
      <td>-0.253873</td>
      <td>-0.291608</td>
      <td>0.418085</td>
      <td>-0.020333</td>
      <td>0.491671</td>
      <td>-0.406318</td>
      <td>-0.010519</td>
      <td>...</td>
      <td>-0.307609</td>
      <td>0.735820</td>
      <td>-0.770469</td>
      <td>0.117486</td>
      <td>0.178596</td>
      <td>0.197686</td>
      <td>-0.197872</td>
      <td>-0.238648</td>
      <td>-0.004122</td>
      <td>0.143509</td>
    </tr>
    <tr>
      <th>인구 십만명당 자살률</th>
      <td>0.080499</td>
      <td>-0.392301</td>
      <td>-0.077771</td>
      <td>-0.279178</td>
      <td>-0.334487</td>
      <td>0.482472</td>
      <td>0.141749</td>
      <td>0.403513</td>
      <td>0.025399</td>
      <td>-0.063754</td>
      <td>...</td>
      <td>-0.237529</td>
      <td>0.623530</td>
      <td>-0.718444</td>
      <td>0.276696</td>
      <td>-0.116899</td>
      <td>0.262750</td>
      <td>-0.262626</td>
      <td>-0.498733</td>
      <td>0.076297</td>
      <td>0.288240</td>
    </tr>
    <tr>
      <th>인구 천명당 사설학원수</th>
      <td>-0.290660</td>
      <td>0.553090</td>
      <td>0.201854</td>
      <td>0.295530</td>
      <td>0.429074</td>
      <td>-0.588470</td>
      <td>-0.248719</td>
      <td>-0.496439</td>
      <td>0.144646</td>
      <td>-0.247734</td>
      <td>...</td>
      <td>0.433962</td>
      <td>-0.743916</td>
      <td>0.770635</td>
      <td>-0.096318</td>
      <td>0.335209</td>
      <td>-0.415512</td>
      <td>0.415160</td>
      <td>0.596287</td>
      <td>0.008052</td>
      <td>-0.376686</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>전입인구</th>
      <td>-0.327074</td>
      <td>-0.063028</td>
      <td>0.041248</td>
      <td>0.946771</td>
      <td>0.950191</td>
      <td>-0.731750</td>
      <td>-0.305826</td>
      <td>-0.380852</td>
      <td>-0.097455</td>
      <td>-0.143899</td>
      <td>...</td>
      <td>0.428737</td>
      <td>-0.488736</td>
      <td>0.542366</td>
      <td>-0.160765</td>
      <td>0.238044</td>
      <td>-0.587941</td>
      <td>0.587689</td>
      <td>0.605713</td>
      <td>-0.063661</td>
      <td>-0.603959</td>
    </tr>
    <tr>
      <th>전출인구</th>
      <td>-0.354970</td>
      <td>-0.070518</td>
      <td>0.014135</td>
      <td>0.946034</td>
      <td>0.954569</td>
      <td>-0.745476</td>
      <td>-0.306213</td>
      <td>-0.337284</td>
      <td>-0.124094</td>
      <td>-0.143026</td>
      <td>...</td>
      <td>0.430339</td>
      <td>-0.469144</td>
      <td>0.534701</td>
      <td>-0.192360</td>
      <td>0.304837</td>
      <td>-0.577064</td>
      <td>0.576742</td>
      <td>0.581752</td>
      <td>-0.157783</td>
      <td>-0.613314</td>
    </tr>
    <tr>
      <th>조이혼율</th>
      <td>0.161269</td>
      <td>-0.156466</td>
      <td>-0.182353</td>
      <td>-0.432344</td>
      <td>-0.487747</td>
      <td>0.517604</td>
      <td>-0.060436</td>
      <td>0.634772</td>
      <td>-0.268071</td>
      <td>-0.197827</td>
      <td>...</td>
      <td>-0.225325</td>
      <td>0.893741</td>
      <td>-0.814235</td>
      <td>-0.185870</td>
      <td>0.064418</td>
      <td>0.684702</td>
      <td>-0.684766</td>
      <td>-0.454371</td>
      <td>0.150067</td>
      <td>0.447357</td>
    </tr>
    <tr>
      <th>조혼인율</th>
      <td>0.431603</td>
      <td>0.296598</td>
      <td>0.054629</td>
      <td>0.160139</td>
      <td>0.035328</td>
      <td>-0.172497</td>
      <td>-0.114342</td>
      <td>0.103174</td>
      <td>0.222115</td>
      <td>-0.193014</td>
      <td>...</td>
      <td>-0.075244</td>
      <td>-0.172904</td>
      <td>0.234452</td>
      <td>-0.171923</td>
      <td>-0.095351</td>
      <td>0.127472</td>
      <td>-0.127372</td>
      <td>-0.069613</td>
      <td>0.182140</td>
      <td>0.265362</td>
    </tr>
    <tr>
      <th>주관적건강수준 인지율</th>
      <td>-0.130528</td>
      <td>0.111269</td>
      <td>0.270997</td>
      <td>-0.062278</td>
      <td>0.025893</td>
      <td>0.016116</td>
      <td>0.008717</td>
      <td>-0.496326</td>
      <td>0.207681</td>
      <td>0.042085</td>
      <td>...</td>
      <td>-0.027527</td>
      <td>-0.500360</td>
      <td>0.419331</td>
      <td>0.202740</td>
      <td>-0.068896</td>
      <td>-0.375067</td>
      <td>0.375137</td>
      <td>0.087290</td>
      <td>-0.173168</td>
      <td>0.002125</td>
    </tr>
    <tr>
      <th>주민등록인구</th>
      <td>-0.527168</td>
      <td>-0.136019</td>
      <td>0.117716</td>
      <td>0.962130</td>
      <td>0.997824</td>
      <td>-0.753502</td>
      <td>-0.266898</td>
      <td>-0.322588</td>
      <td>-0.005768</td>
      <td>-0.063790</td>
      <td>...</td>
      <td>0.372445</td>
      <td>-0.359327</td>
      <td>0.406314</td>
      <td>-0.138618</td>
      <td>0.245462</td>
      <td>-0.554920</td>
      <td>0.554661</td>
      <td>0.604170</td>
      <td>-0.090895</td>
      <td>-0.679227</td>
    </tr>
    <tr>
      <th>주택월세통합가격지수</th>
      <td>-0.226593</td>
      <td>0.179921</td>
      <td>-0.137007</td>
      <td>0.134553</td>
      <td>0.211264</td>
      <td>-0.370775</td>
      <td>-0.173509</td>
      <td>-0.062059</td>
      <td>0.011458</td>
      <td>-0.225509</td>
      <td>...</td>
      <td>0.032596</td>
      <td>-0.348474</td>
      <td>0.339590</td>
      <td>0.012707</td>
      <td>0.342097</td>
      <td>-0.246285</td>
      <td>0.245926</td>
      <td>0.010243</td>
      <td>-0.393530</td>
      <td>-0.188342</td>
    </tr>
    <tr>
      <th>지가변동률</th>
      <td>-0.246010</td>
      <td>0.263553</td>
      <td>-0.003115</td>
      <td>0.593670</td>
      <td>0.645426</td>
      <td>-0.760614</td>
      <td>-0.207786</td>
      <td>-0.387064</td>
      <td>0.007831</td>
      <td>-0.157281</td>
      <td>...</td>
      <td>0.369698</td>
      <td>-0.509050</td>
      <td>0.580944</td>
      <td>-0.210777</td>
      <td>0.345238</td>
      <td>-0.340811</td>
      <td>0.340449</td>
      <td>0.652508</td>
      <td>-0.041621</td>
      <td>-0.437940</td>
    </tr>
    <tr>
      <th>초등학교수</th>
      <td>-0.628716</td>
      <td>-0.028689</td>
      <td>0.332675</td>
      <td>0.820723</td>
      <td>0.905222</td>
      <td>-0.720914</td>
      <td>-0.141735</td>
      <td>-0.346176</td>
      <td>0.191075</td>
      <td>0.085169</td>
      <td>...</td>
      <td>0.376775</td>
      <td>-0.322877</td>
      <td>0.320893</td>
      <td>-0.005106</td>
      <td>0.275366</td>
      <td>-0.476543</td>
      <td>0.476252</td>
      <td>0.609540</td>
      <td>-0.012063</td>
      <td>-0.604410</td>
    </tr>
    <tr>
      <th>출생아수</th>
      <td>-0.486807</td>
      <td>0.006220</td>
      <td>0.142592</td>
      <td>0.926536</td>
      <td>0.958137</td>
      <td>-0.779958</td>
      <td>-0.299156</td>
      <td>-0.312109</td>
      <td>0.126339</td>
      <td>-0.109704</td>
      <td>...</td>
      <td>0.316159</td>
      <td>-0.404815</td>
      <td>0.469345</td>
      <td>-0.187501</td>
      <td>0.232764</td>
      <td>-0.475514</td>
      <td>0.475269</td>
      <td>0.523391</td>
      <td>-0.081515</td>
      <td>-0.590901</td>
    </tr>
    <tr>
      <th>토지거래 면적</th>
      <td>-0.434260</td>
      <td>0.161485</td>
      <td>0.061410</td>
      <td>0.541315</td>
      <td>0.615124</td>
      <td>-0.556967</td>
      <td>-0.424470</td>
      <td>-0.389443</td>
      <td>-0.038959</td>
      <td>-0.230103</td>
      <td>...</td>
      <td>0.365929</td>
      <td>-0.492949</td>
      <td>0.552730</td>
      <td>-0.177523</td>
      <td>0.111934</td>
      <td>-0.453907</td>
      <td>0.453788</td>
      <td>0.370006</td>
      <td>-0.322871</td>
      <td>-0.657670</td>
    </tr>
    <tr>
      <th>토지거래현황</th>
      <td>-0.434260</td>
      <td>0.161485</td>
      <td>0.061410</td>
      <td>0.541315</td>
      <td>0.615124</td>
      <td>-0.556967</td>
      <td>-0.424470</td>
      <td>-0.389443</td>
      <td>-0.038959</td>
      <td>-0.230103</td>
      <td>...</td>
      <td>0.365929</td>
      <td>-0.492949</td>
      <td>0.552730</td>
      <td>-0.177523</td>
      <td>0.111934</td>
      <td>-0.453907</td>
      <td>0.453788</td>
      <td>0.370006</td>
      <td>-0.322871</td>
      <td>-0.657670</td>
    </tr>
    <tr>
      <th>폐수배출업소수</th>
      <td>0.076780</td>
      <td>0.687858</td>
      <td>0.298482</td>
      <td>-0.370852</td>
      <td>-0.304967</td>
      <td>0.082507</td>
      <td>-0.159523</td>
      <td>0.281265</td>
      <td>0.248332</td>
      <td>-0.191252</td>
      <td>...</td>
      <td>-0.027994</td>
      <td>0.029401</td>
      <td>0.001488</td>
      <td>-0.082514</td>
      <td>0.239114</td>
      <td>0.556200</td>
      <td>-0.556447</td>
      <td>-0.180259</td>
      <td>0.155770</td>
      <td>0.365109</td>
    </tr>
    <tr>
      <th>하수도보급률</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>합계출산율</th>
      <td>-0.547604</td>
      <td>0.119828</td>
      <td>0.345852</td>
      <td>0.134752</td>
      <td>0.211597</td>
      <td>-0.283919</td>
      <td>-0.174352</td>
      <td>0.161000</td>
      <td>0.541234</td>
      <td>-0.067129</td>
      <td>...</td>
      <td>-0.079310</td>
      <td>0.226905</td>
      <td>-0.151279</td>
      <td>-0.197005</td>
      <td>-0.028126</td>
      <td>0.235345</td>
      <td>-0.235315</td>
      <td>-0.129273</td>
      <td>-0.050945</td>
      <td>-0.135860</td>
    </tr>
    <tr>
      <th>총합계</th>
      <td>-0.459826</td>
      <td>-0.104203</td>
      <td>0.115907</td>
      <td>0.972355</td>
      <td>0.995038</td>
      <td>-0.745518</td>
      <td>-0.220192</td>
      <td>-0.338410</td>
      <td>0.009031</td>
      <td>-0.015120</td>
      <td>...</td>
      <td>0.415351</td>
      <td>-0.411349</td>
      <td>0.450597</td>
      <td>-0.119392</td>
      <td>0.233273</td>
      <td>-0.560188</td>
      <td>0.559941</td>
      <td>0.626279</td>
      <td>-0.051325</td>
      <td>-0.661015</td>
    </tr>
    <tr>
      <th>공원율</th>
      <td>-0.053805</td>
      <td>-0.413343</td>
      <td>-0.273860</td>
      <td>-0.189276</td>
      <td>-0.184328</td>
      <td>0.459313</td>
      <td>-0.038076</td>
      <td>-0.091760</td>
      <td>-0.375968</td>
      <td>0.141100</td>
      <td>...</td>
      <td>0.097159</td>
      <td>0.231259</td>
      <td>-0.314013</td>
      <td>0.231116</td>
      <td>-0.125606</td>
      <td>-0.123599</td>
      <td>0.123730</td>
      <td>-0.079753</td>
      <td>-0.253342</td>
      <td>-0.105935</td>
    </tr>
    <tr>
      <th>다문화학생수</th>
      <td>-0.206098</td>
      <td>-0.134791</td>
      <td>-0.021816</td>
      <td>0.115865</td>
      <td>0.132842</td>
      <td>0.090483</td>
      <td>-0.181207</td>
      <td>-0.064413</td>
      <td>-0.022190</td>
      <td>-0.131707</td>
      <td>...</td>
      <td>0.074809</td>
      <td>0.066905</td>
      <td>-0.123750</td>
      <td>0.155776</td>
      <td>-0.207064</td>
      <td>-0.127284</td>
      <td>0.127500</td>
      <td>-0.212424</td>
      <td>-0.029140</td>
      <td>-0.095100</td>
    </tr>
    <tr>
      <th>아파트비율</th>
      <td>-0.605081</td>
      <td>0.413111</td>
      <td>0.613812</td>
      <td>0.318579</td>
      <td>0.469361</td>
      <td>-0.476255</td>
      <td>-0.091407</td>
      <td>-0.324035</td>
      <td>0.537408</td>
      <td>0.083264</td>
      <td>...</td>
      <td>0.330675</td>
      <td>-0.437367</td>
      <td>0.402865</td>
      <td>0.079055</td>
      <td>0.261731</td>
      <td>-0.265775</td>
      <td>0.265500</td>
      <td>0.406984</td>
      <td>-0.029017</td>
      <td>-0.459250</td>
    </tr>
    <tr>
      <th>주택보급율</th>
      <td>-0.165184</td>
      <td>-0.031952</td>
      <td>0.200441</td>
      <td>-0.293790</td>
      <td>-0.238333</td>
      <td>0.215746</td>
      <td>0.264122</td>
      <td>0.036915</td>
      <td>0.143661</td>
      <td>0.118297</td>
      <td>...</td>
      <td>-0.110242</td>
      <td>0.260650</td>
      <td>-0.330736</td>
      <td>0.197840</td>
      <td>-0.380337</td>
      <td>0.284139</td>
      <td>-0.283739</td>
      <td>-0.193372</td>
      <td>0.265910</td>
      <td>-0.156287</td>
    </tr>
    <tr>
      <th>cctv대수</th>
      <td>0.024950</td>
      <td>0.183395</td>
      <td>0.197363</td>
      <td>0.416848</td>
      <td>0.381981</td>
      <td>-0.231993</td>
      <td>-0.181528</td>
      <td>-0.130360</td>
      <td>0.106801</td>
      <td>0.095789</td>
      <td>...</td>
      <td>1.000000</td>
      <td>-0.260059</td>
      <td>0.378344</td>
      <td>-0.328065</td>
      <td>0.072416</td>
      <td>-0.088741</td>
      <td>0.088665</td>
      <td>0.479473</td>
      <td>-0.040936</td>
      <td>-0.114148</td>
    </tr>
    <tr>
      <th>단순직비율</th>
      <td>0.083416</td>
      <td>-0.454541</td>
      <td>-0.268048</td>
      <td>-0.319290</td>
      <td>-0.395403</td>
      <td>0.424493</td>
      <td>0.065839</td>
      <td>0.708268</td>
      <td>-0.242698</td>
      <td>-0.004649</td>
      <td>...</td>
      <td>-0.260059</td>
      <td>1.000000</td>
      <td>-0.930768</td>
      <td>-0.154662</td>
      <td>-0.049392</td>
      <td>0.632874</td>
      <td>-0.632819</td>
      <td>-0.427170</td>
      <td>0.006835</td>
      <td>0.352635</td>
    </tr>
    <tr>
      <th>전문직비율</th>
      <td>-0.070904</td>
      <td>0.519313</td>
      <td>0.287185</td>
      <td>0.390141</td>
      <td>0.449922</td>
      <td>-0.576849</td>
      <td>-0.262258</td>
      <td>-0.556582</td>
      <td>0.226323</td>
      <td>-0.163065</td>
      <td>...</td>
      <td>0.378344</td>
      <td>-0.930768</td>
      <td>1.000000</td>
      <td>-0.217257</td>
      <td>0.122285</td>
      <td>-0.465451</td>
      <td>0.465321</td>
      <td>0.502931</td>
      <td>-0.082536</td>
      <td>-0.297040</td>
    </tr>
    <tr>
      <th>서비스.사무직</th>
      <td>-0.031107</td>
      <td>-0.189766</td>
      <td>-0.060403</td>
      <td>-0.201808</td>
      <td>-0.160143</td>
      <td>0.425465</td>
      <td>0.532906</td>
      <td>-0.386932</td>
      <td>0.036383</td>
      <td>0.453054</td>
      <td>...</td>
      <td>-0.328065</td>
      <td>-0.154662</td>
      <td>-0.217257</td>
      <td>1.000000</td>
      <td>-0.198576</td>
      <td>-0.431898</td>
      <td>0.432104</td>
      <td>-0.218572</td>
      <td>0.204785</td>
      <td>-0.138797</td>
    </tr>
    <tr>
      <th>1차산업비율</th>
      <td>-0.240484</td>
      <td>0.335844</td>
      <td>0.086602</td>
      <td>0.187379</td>
      <td>0.264045</td>
      <td>-0.288486</td>
      <td>-0.368982</td>
      <td>0.165044</td>
      <td>-0.184694</td>
      <td>-0.366506</td>
      <td>...</td>
      <td>0.072416</td>
      <td>-0.049392</td>
      <td>0.122285</td>
      <td>-0.198576</td>
      <td>1.000000</td>
      <td>0.004035</td>
      <td>-0.005081</td>
      <td>0.081811</td>
      <td>-0.238282</td>
      <td>0.078385</td>
    </tr>
    <tr>
      <th>2차산업비율</th>
      <td>0.287560</td>
      <td>0.175264</td>
      <td>0.000142</td>
      <td>-0.504774</td>
      <td>-0.550530</td>
      <td>0.287406</td>
      <td>0.062631</td>
      <td>0.703606</td>
      <td>0.103948</td>
      <td>-0.083042</td>
      <td>...</td>
      <td>-0.088741</td>
      <td>0.632874</td>
      <td>-0.465451</td>
      <td>-0.431898</td>
      <td>0.004035</td>
      <td>1.000000</td>
      <td>-0.999999</td>
      <td>-0.379907</td>
      <td>0.080486</td>
      <td>0.580726</td>
    </tr>
    <tr>
      <th>3차산업비율</th>
      <td>-0.287308</td>
      <td>-0.175615</td>
      <td>-0.000233</td>
      <td>0.504576</td>
      <td>0.550251</td>
      <td>-0.287103</td>
      <td>-0.062245</td>
      <td>-0.703775</td>
      <td>-0.103754</td>
      <td>0.083425</td>
      <td>...</td>
      <td>0.088665</td>
      <td>-0.632819</td>
      <td>0.465321</td>
      <td>0.432104</td>
      <td>-0.005081</td>
      <td>-0.999999</td>
      <td>1.000000</td>
      <td>0.379820</td>
      <td>-0.080237</td>
      <td>-0.580805</td>
    </tr>
    <tr>
      <th>체육시설</th>
      <td>-0.209136</td>
      <td>0.136316</td>
      <td>0.201795</td>
      <td>0.584218</td>
      <td>0.616281</td>
      <td>-0.672231</td>
      <td>-0.071870</td>
      <td>-0.399692</td>
      <td>-0.012442</td>
      <td>0.146566</td>
      <td>...</td>
      <td>0.479473</td>
      <td>-0.427170</td>
      <td>0.502931</td>
      <td>-0.218572</td>
      <td>0.081811</td>
      <td>-0.379907</td>
      <td>0.379820</td>
      <td>1.000000</td>
      <td>0.165132</td>
      <td>-0.517711</td>
    </tr>
    <tr>
      <th>유치원 교원비율</th>
      <td>0.257311</td>
      <td>0.224541</td>
      <td>0.100532</td>
      <td>-0.049699</td>
      <td>-0.083785</td>
      <td>0.149504</td>
      <td>0.266460</td>
      <td>-0.017568</td>
      <td>0.128368</td>
      <td>0.122763</td>
      <td>...</td>
      <td>-0.040936</td>
      <td>0.006835</td>
      <td>-0.082536</td>
      <td>0.204785</td>
      <td>-0.238282</td>
      <td>0.080486</td>
      <td>-0.080237</td>
      <td>0.165132</td>
      <td>1.000000</td>
      <td>0.130214</td>
    </tr>
    <tr>
      <th>초등학교 교원비율</th>
      <td>0.611372</td>
      <td>0.191329</td>
      <td>-0.017419</td>
      <td>-0.570560</td>
      <td>-0.671339</td>
      <td>0.526685</td>
      <td>-0.005489</td>
      <td>0.452540</td>
      <td>0.136981</td>
      <td>-0.113270</td>
      <td>...</td>
      <td>-0.114148</td>
      <td>0.352635</td>
      <td>-0.297040</td>
      <td>-0.138797</td>
      <td>0.078385</td>
      <td>0.580726</td>
      <td>-0.580805</td>
      <td>-0.517711</td>
      <td>0.130214</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
<p>71 rows × 71 columns</p>
</div>




```python
# df =df.fillna(0)
df = df.drop(["하수도보급률","도로포장률","상수도보급률"],1)
```


```python
import seaborn as sns
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
%matplotlib inline
sns.set(style = 'darkgrid') #
import os
from pylab import rcParams
rcParams['figure.figsize'] = 25, 12.5
```


```python
plt.figure(figsize=(100, 100))
# Heatmap 설정
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap="coolwarm",
            linecolor='white', annot=True)

# 렌더링
plt.show()
```


![png](output_23_0.png)



```python
df.columns
```




    Index(['지역', '1인가구비율', '1인당 자동차 등록대수', 'EQ-5D지표', '가구수', '건강보험 적용인구 현황',
           '고령인구비율', '교원1인당 학생수', '남녀성비', '노인 천명당 노인여가복지시설수', '대학교 수', '대학교 학생수',
           '도시지역면적', '등록외국인 현황', '비만율', '사망률', '사망자수', '소년·소녀가정현황', '순이동인구',
           '스트레스 인지율', '아파트매매가격지수', '아파트월세통합가격지수', '유아 천명당 보육시설수', '음주율', '흡연율',
           '인구 십만명당 문화기반시설수', '인구 십만명당 사회복지시설수', '인구 십만명당 자살률', '인구 천명당 사설학원수',
           '인구 천명당 사업체수', '인구 천명당 외국인수', '인구 천명당 의료기관병상수', '인구 천명당 의료기관종사의사수',
           '인구 천명당 종사자수', '인구증가율', '일반회계중 사회복지예산비중', '일반회계중 일반공공행정예산비중',
           '자동차 천대당 교통사고발생건수', '장애인고용률', '재정자주도', '전입인구', '전출인구', '조이혼율', '조혼인율',
           '주관적건강수준 인지율', '주민등록인구', '주택월세통합가격지수', '지가변동률', '초등학교수', '출생아수',
           '토지거래 면적', '토지거래현황', '폐수배출업소수', '합계출산율', '총합계', '공원율', '다문화학생수',
           '한부모가구수', '아파트비율', '주택보급율', ' cctv대수', '단순직비율', '전문직비율', '서비스.사무직',
           '1차산업비율', '2차산업비율', '3차산업비율', '체육시설', '강력범죄발생건수', '유치원 교원비율',
           '초등학교 교원비율'],
          dtype='object')




```python
type(df['한부모가구수'][1])
```




    float




```python
df.select_dtypes(include=['object'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>한부모가구수</th>
      <th>강력범죄발생건수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>1278</td>
      <td>8,617</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>1589</td>
      <td>5,244</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>2568</td>
      <td>4,257</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>2805</td>
      <td>5,585</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>1830</td>
      <td>6,345</td>
    </tr>
    <tr>
      <th>5</th>
      <td>광진구</td>
      <td>1511</td>
      <td>5,909</td>
    </tr>
    <tr>
      <th>6</th>
      <td>구로구</td>
      <td>1460</td>
      <td>5,646</td>
    </tr>
    <tr>
      <th>7</th>
      <td>금천구</td>
      <td>1575</td>
      <td>3,781</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노원구</td>
      <td>3075</td>
      <td>5,130</td>
    </tr>
    <tr>
      <th>9</th>
      <td>도봉구</td>
      <td>1978</td>
      <td>2,664</td>
    </tr>
    <tr>
      <th>10</th>
      <td>동대문구</td>
      <td>1515</td>
      <td>4,720</td>
    </tr>
    <tr>
      <th>11</th>
      <td>동작구</td>
      <td>1268</td>
      <td>4,074</td>
    </tr>
    <tr>
      <th>12</th>
      <td>마포구</td>
      <td>1132</td>
      <td>5,854</td>
    </tr>
    <tr>
      <th>13</th>
      <td>서대문구</td>
      <td>1245</td>
      <td>4,029</td>
    </tr>
    <tr>
      <th>14</th>
      <td>서초구</td>
      <td>787</td>
      <td>5,444</td>
    </tr>
    <tr>
      <th>15</th>
      <td>성동구</td>
      <td>1011</td>
      <td>3,358</td>
    </tr>
    <tr>
      <th>16</th>
      <td>성북구</td>
      <td>1798</td>
      <td>4,154</td>
    </tr>
    <tr>
      <th>17</th>
      <td>송파구</td>
      <td>1783</td>
      <td>6,778</td>
    </tr>
    <tr>
      <th>18</th>
      <td>양천구</td>
      <td>1837</td>
      <td>4,528</td>
    </tr>
    <tr>
      <th>19</th>
      <td>영등포구</td>
      <td>890</td>
      <td>6,867</td>
    </tr>
    <tr>
      <th>20</th>
      <td>용산구</td>
      <td>728</td>
      <td>3,820</td>
    </tr>
    <tr>
      <th>21</th>
      <td>은평구</td>
      <td>2622</td>
      <td>4,745</td>
    </tr>
    <tr>
      <th>22</th>
      <td>종로구</td>
      <td>480</td>
      <td>4,705</td>
    </tr>
    <tr>
      <th>23</th>
      <td>중구</td>
      <td>417</td>
      <td>4,954</td>
    </tr>
    <tr>
      <th>24</th>
      <td>중랑구</td>
      <td>2730</td>
      <td>5,193</td>
    </tr>
  </tbody>
</table>
</div>




```python
for i in range(0,25) :
    df["강력범죄발생건수"][i] = df["강력범죄발생건수"][i].replace(",","")
    df["강력범죄발생건수"][i] = float(df["강력범죄발생건수"][i])
```

    C:\Python\Anaconda3-52\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    C:\Python\Anaconda3-52\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until
    


```python
df.select_dtypes(include=['object'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>한부모가구수</th>
      <th>강력범죄발생건수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>1278</td>
      <td>8617</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>1589</td>
      <td>5244</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>2568</td>
      <td>4257</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>2805</td>
      <td>5585</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>1830</td>
      <td>6345</td>
    </tr>
    <tr>
      <th>5</th>
      <td>광진구</td>
      <td>1511</td>
      <td>5909</td>
    </tr>
    <tr>
      <th>6</th>
      <td>구로구</td>
      <td>1460</td>
      <td>5646</td>
    </tr>
    <tr>
      <th>7</th>
      <td>금천구</td>
      <td>1575</td>
      <td>3781</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노원구</td>
      <td>3075</td>
      <td>5130</td>
    </tr>
    <tr>
      <th>9</th>
      <td>도봉구</td>
      <td>1978</td>
      <td>2664</td>
    </tr>
    <tr>
      <th>10</th>
      <td>동대문구</td>
      <td>1515</td>
      <td>4720</td>
    </tr>
    <tr>
      <th>11</th>
      <td>동작구</td>
      <td>1268</td>
      <td>4074</td>
    </tr>
    <tr>
      <th>12</th>
      <td>마포구</td>
      <td>1132</td>
      <td>5854</td>
    </tr>
    <tr>
      <th>13</th>
      <td>서대문구</td>
      <td>1245</td>
      <td>4029</td>
    </tr>
    <tr>
      <th>14</th>
      <td>서초구</td>
      <td>787</td>
      <td>5444</td>
    </tr>
    <tr>
      <th>15</th>
      <td>성동구</td>
      <td>1011</td>
      <td>3358</td>
    </tr>
    <tr>
      <th>16</th>
      <td>성북구</td>
      <td>1798</td>
      <td>4154</td>
    </tr>
    <tr>
      <th>17</th>
      <td>송파구</td>
      <td>1783</td>
      <td>6778</td>
    </tr>
    <tr>
      <th>18</th>
      <td>양천구</td>
      <td>1837</td>
      <td>4528</td>
    </tr>
    <tr>
      <th>19</th>
      <td>영등포구</td>
      <td>890</td>
      <td>6867</td>
    </tr>
    <tr>
      <th>20</th>
      <td>용산구</td>
      <td>728</td>
      <td>3820</td>
    </tr>
    <tr>
      <th>21</th>
      <td>은평구</td>
      <td>2622</td>
      <td>4745</td>
    </tr>
    <tr>
      <th>22</th>
      <td>종로구</td>
      <td>480</td>
      <td>4705</td>
    </tr>
    <tr>
      <th>23</th>
      <td>중구</td>
      <td>417</td>
      <td>4954</td>
    </tr>
    <tr>
      <th>24</th>
      <td>중랑구</td>
      <td>2730</td>
      <td>5193</td>
    </tr>
  </tbody>
</table>
</div>




```python
x_data = df[['1인가구비율', '1인당 자동차 등록대수', 'EQ-5D지표', '가구수', '건강보험 적용인구 현황',
       '고령인구비율', '교원1인당 학생수', '남녀성비', '노인 천명당 노인여가복지시설수', '대학교 수', '대학교 학생수',
       '도시지역면적', '등록외국인 현황', '비만율', '사망률', '사망자수', '소년·소녀가정현황', '순이동인구',
       '스트레스 인지율', '아파트매매가격지수', '아파트월세통합가격지수', '유아 천명당 보육시설수', '음주율', '흡연율',
       '인구 십만명당 문화기반시설수', '인구 십만명당 사회복지시설수', '인구 십만명당 자살률', '인구 천명당 사설학원수',
       '인구 천명당 사업체수', '인구 천명당 외국인수', '인구 천명당 의료기관병상수', '인구 천명당 의료기관종사의사수',
       '인구 천명당 종사자수', '인구증가율', '일반회계중 사회복지예산비중', '일반회계중 일반공공행정예산비중',
       '자동차 천대당 교통사고발생건수', '장애인고용률', '재정자주도', '전입인구', '전출인구', '조이혼율', '조혼인율',
       '주관적건강수준 인지율', '주민등록인구', '주택월세통합가격지수', '지가변동률', '초등학교수', '출생아수',
       '토지거래 면적', '토지거래현황', '폐수배출업소수', '합계출산율', '총합계', '공원율', '다문화학생수',
       '한부모가구수', '아파트비율', '주택보급율', ' cctv대수', '단순직비율', '전문직비율', '서비스.사무직',
       '1차산업비율', '2차산업비율', '3차산업비율', '체육시설', '강력범죄발생건수', '유치원 교원비율',
       '초등학교 교원비율']]
```


```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_data)
x_data_scaled = scaler.transform(x_data)    
```


```python
end=pd.DataFrame(x_data_scaled)
end.columns
```




    RangeIndex(start=0, stop=70, step=1)




```python
end.columns =['1인가구비율', '1인당 자동차 등록대수', 'EQ-5D지표', '가구수', '건강보험 적용인구 현황',
       '고령인구비율', '교원1인당 학생수', '남녀성비', '노인 천명당 노인여가복지시설수', '대학교 수', '대학교 학생수',
       '도시지역면적', '등록외국인 현황', '비만율', '사망률', '사망자수', '소년·소녀가정현황', '순이동인구',
       '스트레스 인지율', '아파트매매가격지수', '아파트월세통합가격지수', '유아 천명당 보육시설수', '음주율', '흡연율',
       '인구 십만명당 문화기반시설수', '인구 십만명당 사회복지시설수', '인구 십만명당 자살률', '인구 천명당 사설학원수',
       '인구 천명당 사업체수', '인구 천명당 외국인수', '인구 천명당 의료기관병상수', '인구 천명당 의료기관종사의사수',
       '인구 천명당 종사자수', '인구증가율', '일반회계중 사회복지예산비중', '일반회계중 일반공공행정예산비중',
       '자동차 천대당 교통사고발생건수', '장애인고용률', '재정자주도', '전입인구', '전출인구', '조이혼율', '조혼인율',
       '주관적건강수준 인지율', '주민등록인구', '주택월세통합가격지수', '지가변동률', '초등학교수', '출생아수',
       '토지거래 면적', '토지거래현황', '폐수배출업소수', '합계출산율', '총합계', '공원율', '다문화학생수',
       '한부모가구수', '아파트비율', '주택보급율', ' cctv대수', '단순직비율', '전문직비율', '서비스.사무직',
       '1차산업비율', '2차산업비율', '3차산업비율', '체육시설', '강력범죄발생건수', '유치원 교원비율',
       '초등학교 교원비율']
```


```python
end.index = df["지역"]
end
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1인가구비율</th>
      <th>1인당 자동차 등록대수</th>
      <th>EQ-5D지표</th>
      <th>가구수</th>
      <th>건강보험 적용인구 현황</th>
      <th>고령인구비율</th>
      <th>교원1인당 학생수</th>
      <th>남녀성비</th>
      <th>노인 천명당 노인여가복지시설수</th>
      <th>대학교 수</th>
      <th>...</th>
      <th>단순직비율</th>
      <th>전문직비율</th>
      <th>서비스.사무직</th>
      <th>1차산업비율</th>
      <th>2차산업비율</th>
      <th>3차산업비율</th>
      <th>체육시설</th>
      <th>강력범죄발생건수</th>
      <th>유치원 교원비율</th>
      <th>초등학교 교원비율</th>
    </tr>
    <tr>
      <th>지역</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>0.389121</td>
      <td>1.000000</td>
      <td>0.517241</td>
      <td>0.869933</td>
      <td>0.864842</td>
      <td>0.021239</td>
      <td>0.184996</td>
      <td>0.000000</td>
      <td>0.479532</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.043294</td>
      <td>0.929255</td>
      <td>0.366377</td>
      <td>0.704676</td>
      <td>0.021875</td>
      <td>0.977683</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.385598</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>0.179916</td>
      <td>0.368421</td>
      <td>0.275862</td>
      <td>0.608510</td>
      <td>0.607484</td>
      <td>0.173451</td>
      <td>0.134697</td>
      <td>0.604613</td>
      <td>0.216374</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.587930</td>
      <td>0.313199</td>
      <td>0.493997</td>
      <td>0.862016</td>
      <td>0.241523</td>
      <td>0.757919</td>
      <td>0.113360</td>
      <td>0.433395</td>
      <td>0.000000</td>
      <td>0.434276</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>0.355649</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.392685</td>
      <td>0.350888</td>
      <td>0.982301</td>
      <td>0.167945</td>
      <td>0.406919</td>
      <td>0.081871</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.863530</td>
      <td>0.000000</td>
      <td>0.562783</td>
      <td>0.000000</td>
      <td>0.368732</td>
      <td>0.631580</td>
      <td>0.145749</td>
      <td>0.267596</td>
      <td>0.544277</td>
      <td>0.483389</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>0.259414</td>
      <td>0.473684</td>
      <td>0.620690</td>
      <td>0.900969</td>
      <td>0.839668</td>
      <td>0.210619</td>
      <td>0.157715</td>
      <td>0.288303</td>
      <td>0.520468</td>
      <td>0.166667</td>
      <td>...</td>
      <td>0.522093</td>
      <td>0.305983</td>
      <td>0.714281</td>
      <td>0.194817</td>
      <td>0.107386</td>
      <td>0.892688</td>
      <td>0.522267</td>
      <td>0.490677</td>
      <td>0.974622</td>
      <td>0.328900</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>1.000000</td>
      <td>0.052632</td>
      <td>0.448276</td>
      <td>1.000000</td>
      <td>0.706803</td>
      <td>0.419469</td>
      <td>0.001705</td>
      <td>0.822900</td>
      <td>0.000000</td>
      <td>0.166667</td>
      <td>...</td>
      <td>0.545098</td>
      <td>0.466145</td>
      <td>0.182424</td>
      <td>0.247080</td>
      <td>0.175012</td>
      <td>0.825023</td>
      <td>0.489879</td>
      <td>0.618344</td>
      <td>0.527639</td>
      <td>0.585963</td>
    </tr>
    <tr>
      <th>광진구</th>
      <td>0.698745</td>
      <td>0.210526</td>
      <td>0.379310</td>
      <td>0.544293</td>
      <td>0.431054</td>
      <td>0.148673</td>
      <td>0.700767</td>
      <td>0.352554</td>
      <td>0.228070</td>
      <td>0.500000</td>
      <td>...</td>
      <td>0.564153</td>
      <td>0.363532</td>
      <td>0.420794</td>
      <td>0.000000</td>
      <td>0.385112</td>
      <td>0.615202</td>
      <td>0.825911</td>
      <td>0.545103</td>
      <td>0.714629</td>
      <td>0.466526</td>
    </tr>
    <tr>
      <th>구로구</th>
      <td>0.259414</td>
      <td>0.526316</td>
      <td>0.275862</td>
      <td>0.628386</td>
      <td>0.566464</td>
      <td>0.401770</td>
      <td>0.416880</td>
      <td>0.602142</td>
      <td>0.754386</td>
      <td>0.500000</td>
      <td>...</td>
      <td>0.648989</td>
      <td>0.297160</td>
      <td>0.355292</td>
      <td>0.173111</td>
      <td>0.485077</td>
      <td>0.515086</td>
      <td>0.259109</td>
      <td>0.500924</td>
      <td>0.627489</td>
      <td>0.488497</td>
    </tr>
    <tr>
      <th>금천구</th>
      <td>0.560669</td>
      <td>0.631579</td>
      <td>0.551724</td>
      <td>0.259654</td>
      <td>0.201417</td>
      <td>0.476106</td>
      <td>0.037511</td>
      <td>1.000000</td>
      <td>0.239766</td>
      <td>0.000000</td>
      <td>...</td>
      <td>1.000000</td>
      <td>0.051750</td>
      <td>0.000000</td>
      <td>0.430994</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.206478</td>
      <td>0.187636</td>
      <td>0.713895</td>
      <td>0.844315</td>
    </tr>
    <tr>
      <th>노원구</th>
      <td>0.104603</td>
      <td>0.210526</td>
      <td>1.000000</td>
      <td>0.821804</td>
      <td>0.798622</td>
      <td>0.293805</td>
      <td>0.553282</td>
      <td>0.240527</td>
      <td>0.701754</td>
      <td>1.000000</td>
      <td>...</td>
      <td>0.522324</td>
      <td>0.287411</td>
      <td>0.767170</td>
      <td>0.250983</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.801619</td>
      <td>0.414245</td>
      <td>0.578324</td>
      <td>0.291038</td>
    </tr>
    <tr>
      <th>도봉구</th>
      <td>0.079498</td>
      <td>0.210526</td>
      <td>0.655172</td>
      <td>0.384444</td>
      <td>0.402148</td>
      <td>0.619469</td>
      <td>0.276215</td>
      <td>0.409390</td>
      <td>0.421053</td>
      <td>0.166667</td>
      <td>...</td>
      <td>0.705029</td>
      <td>0.098227</td>
      <td>0.759543</td>
      <td>0.702481</td>
      <td>0.209568</td>
      <td>0.790026</td>
      <td>0.186235</td>
      <td>0.000000</td>
      <td>0.491846</td>
      <td>0.347561</td>
    </tr>
    <tr>
      <th>동대문구</th>
      <td>0.673640</td>
      <td>0.210526</td>
      <td>0.655172</td>
      <td>0.534033</td>
      <td>0.415911</td>
      <td>0.745133</td>
      <td>1.000000</td>
      <td>0.686161</td>
      <td>0.345029</td>
      <td>0.666667</td>
      <td>...</td>
      <td>0.627759</td>
      <td>0.154077</td>
      <td>0.832484</td>
      <td>0.196464</td>
      <td>0.497766</td>
      <td>0.502375</td>
      <td>0.085020</td>
      <td>0.345372</td>
      <td>0.779502</td>
      <td>0.411159</td>
    </tr>
    <tr>
      <th>동작구</th>
      <td>0.564854</td>
      <td>0.105263</td>
      <td>0.275862</td>
      <td>0.606857</td>
      <td>0.505768</td>
      <td>0.532743</td>
      <td>0.637681</td>
      <td>0.337727</td>
      <td>0.350877</td>
      <td>0.500000</td>
      <td>...</td>
      <td>0.381973</td>
      <td>0.467389</td>
      <td>0.673046</td>
      <td>0.000000</td>
      <td>0.059564</td>
      <td>0.940693</td>
      <td>0.008097</td>
      <td>0.236855</td>
      <td>0.733299</td>
      <td>0.339013</td>
    </tr>
    <tr>
      <th>마포구</th>
      <td>0.577406</td>
      <td>0.368421</td>
      <td>0.310345</td>
      <td>0.568273</td>
      <td>0.482375</td>
      <td>0.380531</td>
      <td>0.536232</td>
      <td>0.049423</td>
      <td>0.643275</td>
      <td>0.333333</td>
      <td>...</td>
      <td>0.329932</td>
      <td>0.466097</td>
      <td>0.834439</td>
      <td>0.000000</td>
      <td>0.126059</td>
      <td>0.874210</td>
      <td>0.238866</td>
      <td>0.535864</td>
      <td>0.566137</td>
      <td>0.560401</td>
    </tr>
    <tr>
      <th>서대문구</th>
      <td>0.552301</td>
      <td>0.157895</td>
      <td>0.379310</td>
      <td>0.380062</td>
      <td>0.333044</td>
      <td>0.805310</td>
      <td>0.720375</td>
      <td>0.231466</td>
      <td>0.228070</td>
      <td>1.000000</td>
      <td>...</td>
      <td>0.475282</td>
      <td>0.256114</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.079965</td>
      <td>0.920296</td>
      <td>0.429150</td>
      <td>0.229296</td>
      <td>0.877765</td>
      <td>0.481747</td>
    </tr>
    <tr>
      <th>서초구</th>
      <td>0.179916</td>
      <td>0.894737</td>
      <td>0.793103</td>
      <td>0.552266</td>
      <td>0.616382</td>
      <td>0.122124</td>
      <td>0.000000</td>
      <td>0.035420</td>
      <td>0.368421</td>
      <td>0.166667</td>
      <td>...</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.293404</td>
      <td>0.137739</td>
      <td>0.098413</td>
      <td>0.901716</td>
      <td>0.684211</td>
      <td>0.466991</td>
      <td>0.272094</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>성동구</th>
      <td>0.447699</td>
      <td>0.473684</td>
      <td>0.827586</td>
      <td>0.345958</td>
      <td>0.307463</td>
      <td>0.438938</td>
      <td>0.397272</td>
      <td>0.546129</td>
      <td>1.000000</td>
      <td>0.333333</td>
      <td>...</td>
      <td>0.603471</td>
      <td>0.388155</td>
      <td>0.230623</td>
      <td>0.000000</td>
      <td>0.966831</td>
      <td>0.033586</td>
      <td>0.068826</td>
      <td>0.116580</td>
      <td>0.502561</td>
      <td>0.824309</td>
    </tr>
    <tr>
      <th>성북구</th>
      <td>0.410042</td>
      <td>0.105263</td>
      <td>0.241379</td>
      <td>0.672406</td>
      <td>0.601362</td>
      <td>0.607080</td>
      <td>0.809889</td>
      <td>0.321252</td>
      <td>0.333333</td>
      <td>1.000000</td>
      <td>...</td>
      <td>0.598762</td>
      <td>0.280704</td>
      <td>0.554946</td>
      <td>0.000000</td>
      <td>0.473378</td>
      <td>0.526952</td>
      <td>0.502024</td>
      <td>0.250294</td>
      <td>0.696917</td>
      <td>0.310910</td>
    </tr>
    <tr>
      <th>송파구</th>
      <td>0.133891</td>
      <td>0.526316</td>
      <td>0.517241</td>
      <td>0.980119</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.195226</td>
      <td>0.273476</td>
      <td>0.204678</td>
      <td>0.166667</td>
      <td>...</td>
      <td>0.293479</td>
      <td>0.633685</td>
      <td>0.461294</td>
      <td>1.000000</td>
      <td>0.148872</td>
      <td>0.850418</td>
      <td>0.449393</td>
      <td>0.691080</td>
      <td>0.542165</td>
      <td>0.392688</td>
    </tr>
    <tr>
      <th>양천구</th>
      <td>0.000000</td>
      <td>0.421053</td>
      <td>0.689655</td>
      <td>0.603762</td>
      <td>0.659893</td>
      <td>0.010619</td>
      <td>0.236999</td>
      <td>0.495881</td>
      <td>0.660819</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.479214</td>
      <td>0.403187</td>
      <td>0.563698</td>
      <td>0.000000</td>
      <td>0.167765</td>
      <td>0.832511</td>
      <td>0.485830</td>
      <td>0.313119</td>
      <td>0.865608</td>
      <td>0.184137</td>
    </tr>
    <tr>
      <th>영등포구</th>
      <td>0.535565</td>
      <td>0.842105</td>
      <td>0.827586</td>
      <td>0.584285</td>
      <td>0.495283</td>
      <td>0.550442</td>
      <td>0.049446</td>
      <td>0.661450</td>
      <td>0.795322</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.443226</td>
      <td>0.464354</td>
      <td>0.496228</td>
      <td>0.436881</td>
      <td>0.500591</td>
      <td>0.499315</td>
      <td>0.182186</td>
      <td>0.706031</td>
      <td>0.842156</td>
      <td>0.815011</td>
    </tr>
    <tr>
      <th>용산구</th>
      <td>0.602510</td>
      <td>0.526316</td>
      <td>0.689655</td>
      <td>0.223084</td>
      <td>0.185206</td>
      <td>0.854867</td>
      <td>0.316283</td>
      <td>0.169687</td>
      <td>0.532164</td>
      <td>0.166667</td>
      <td>...</td>
      <td>0.413431</td>
      <td>0.481994</td>
      <td>0.535594</td>
      <td>0.000000</td>
      <td>0.133847</td>
      <td>0.866424</td>
      <td>0.000000</td>
      <td>0.194188</td>
      <td>0.739713</td>
      <td>0.836409</td>
    </tr>
    <tr>
      <th>은평구</th>
      <td>0.184100</td>
      <td>0.105263</td>
      <td>0.448276</td>
      <td>0.688822</td>
      <td>0.665013</td>
      <td>0.647788</td>
      <td>0.167945</td>
      <td>0.261944</td>
      <td>0.210526</td>
      <td>0.166667</td>
      <td>...</td>
      <td>0.604043</td>
      <td>0.185598</td>
      <td>0.813378</td>
      <td>0.000000</td>
      <td>0.098903</td>
      <td>0.901361</td>
      <td>0.052632</td>
      <td>0.349572</td>
      <td>0.569468</td>
      <td>0.325091</td>
    </tr>
    <tr>
      <th>종로구</th>
      <td>0.711297</td>
      <td>0.473684</td>
      <td>0.413793</td>
      <td>0.070516</td>
      <td>0.047389</td>
      <td>1.000000</td>
      <td>0.512361</td>
      <td>0.450577</td>
      <td>0.397661</td>
      <td>0.500000</td>
      <td>...</td>
      <td>0.514099</td>
      <td>0.294714</td>
      <td>0.771017</td>
      <td>0.475800</td>
      <td>0.393669</td>
      <td>0.606180</td>
      <td>0.028340</td>
      <td>0.342852</td>
      <td>0.532540</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>중구</th>
      <td>0.728033</td>
      <td>1.000000</td>
      <td>0.482759</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.549020</td>
      <td>0.602142</td>
      <td>0.280702</td>
      <td>0.333333</td>
      <td>...</td>
      <td>0.592735</td>
      <td>0.160070</td>
      <td>0.921300</td>
      <td>0.293797</td>
      <td>0.701077</td>
      <td>0.299005</td>
      <td>0.036437</td>
      <td>0.384680</td>
      <td>0.998858</td>
      <td>0.708808</td>
    </tr>
    <tr>
      <th>중랑구</th>
      <td>0.364017</td>
      <td>0.210526</td>
      <td>0.413793</td>
      <td>0.570494</td>
      <td>0.513228</td>
      <td>0.483186</td>
      <td>0.311168</td>
      <td>0.613674</td>
      <td>0.146199</td>
      <td>0.166667</td>
      <td>...</td>
      <td>0.945731</td>
      <td>0.049657</td>
      <td>0.170456</td>
      <td>0.475109</td>
      <td>0.684944</td>
      <td>0.314957</td>
      <td>0.311741</td>
      <td>0.424828</td>
      <td>0.774180</td>
      <td>0.552632</td>
    </tr>
  </tbody>
</table>
<p>25 rows × 70 columns</p>
</div>




```python
end.to_csv("data/economy_normalize.csv", encoding="UTF-8")
```


```python
end.drop(['총합계'],1,inplace=True)
```


```python
end.columns
```




    Index(['1인가구비율', '1인당 자동차 등록대수', 'EQ-5D지표', '가구수', '건강보험 적용인구 현황', '고령인구비율',
           '교원1인당 학생수', '남녀성비', '노인 천명당 노인여가복지시설수', '대학교 수', '대학교 학생수', '도시지역면적',
           '등록외국인 현황', '비만율', '사망률', '사망자수', '소년·소녀가정현황', '순이동인구', '스트레스 인지율',
           '아파트매매가격지수', '아파트월세통합가격지수', '유아 천명당 보육시설수', '음주율', '흡연율',
           '인구 십만명당 문화기반시설수', '인구 십만명당 사회복지시설수', '인구 십만명당 자살률', '인구 천명당 사설학원수',
           '인구 천명당 사업체수', '인구 천명당 외국인수', '인구 천명당 의료기관병상수', '인구 천명당 의료기관종사의사수',
           '인구 천명당 종사자수', '인구증가율', '일반회계중 사회복지예산비중', '일반회계중 일반공공행정예산비중',
           '자동차 천대당 교통사고발생건수', '장애인고용률', '재정자주도', '전입인구', '전출인구', '조이혼율', '조혼인율',
           '주관적건강수준 인지율', '주민등록인구', '주택월세통합가격지수', '지가변동률', '초등학교수', '출생아수',
           '토지거래 면적', '토지거래현황', '폐수배출업소수', '합계출산율', '총합계', '공원율', '다문화학생수',
           '한부모가구수', '아파트비율', '주택보급율', ' cctv대수', '단순직비율', '전문직비율', '서비스.사무직',
           '1차산업비율', '2차산업비율', '3차산업비율', '체육시설', '강력범죄발생건수', '유치원 교원비율',
           '초등학교 교원비율'],
          dtype='object')




```python
end["인구"]=(end[ '고령인구비율'] +end['남녀성비']+end['등록외국인 현황']+end['순이동인구']+end[ '인구 천명당 외국인수']+end['인구증가율']+end[ '전입인구']+end['전출인구']+end['조이혼율']+end['조혼인율']+end['주민등록인구']+end['출생아수']+end['합계출산율'])/13
end["가족"]=(end['1인가구비율']+end['가구수']+end['소년·소녀가정현황']+end[ '다문화학생수']+end['한부모가구수'])/5
end["건강"]=(end['EQ-5D지표'] +end['비만율']+end['사망률']+end[ '사망자수']+end[ '스트레스 인지율']+end['음주율']+end[ '흡연율']+end['인구 천명당 의료기관병상수']+end['인구 천명당 의료기관종사의사수']+end['주관적건강수준 인지율']+end['체육시설'])/11
end["교육"]=(end['교원1인당 학생수']+ end[ '대학교 수']+end['대학교 학생수']+end[ '유아 천명당 보육시설수']+end['인구 천명당 사설학원수']+end['초등학교수']+end['유치원 교원비율']+end['초등학교 교원비율'])/8
end["주거와 교통"]=(end['1인당 자동차 등록대수'] +end['건강보험 적용인구 현황']+ end['도시지역면적']+end['아파트매매가격지수']+end['아파트월세통합가격지수']+end['주택월세통합가격지수']+end['지가변동률']+end['토지거래 면적']+end['토지거래현황']+end['아파트비율']+end[ '주택보급율']+end['단순직비율']+end[ '전문직비율']+end['서비스.사무직']+end['1차산업비율']+end['2차산업비율']+end['3차산업비율'])/17
end["성장과 안정"]=(end[ '인구 천명당 사업체수']+end['인구 천명당 종사자수']+end['재정자주도'])/3
end["안전"]=(end[ ' cctv대수']+end['강력범죄발생건수'])/2
end["환경"]=(end['폐수배출업소수']+end['공원율'])/2
end["문화"]=end['인구 십만명당 문화기반시설수']
end["사회통합"]=(end['노인 천명당 노인여가복지시설수']+end[ '인구 십만명당 사회복지시설수']+end[ '인구 십만명당 자살률']+end['일반회계중 사회복지예산비중']+end['일반회계중 일반공공행정예산비중']+end['장애인고용률'])/6

```


```python
df_normal = end[["인구","가족","건강","교육","주거와 교통","성장과 안정","안전","환경","문화","사회통합"]]
```


```python
df_normal.to_csv("data/economy_normalize_sum.csv", encoding="UTF-8")
```


```python
plt.figure(figsize=(25, 25))
# Heatmap 설정
sns.heatmap(df_normal.corr(), linewidths=0.1, vmax=0.5, cmap="coolwarm",
            linecolor='white', annot=True)

# 렌더링
plt.show()
```


![png](output_40_0.png)

