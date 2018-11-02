# 9일차



# 1. Pandas Basic

https://pandas.pydata.org/pandas-docs/stable/10min.html

## pandas

> - 고수준의 자료구조와 파이썬을 통한 통한 빠르고 쉬운 데이터 분석도구를 포함하는 라이브러리
> - NumPy 기반에서 개발되었다.
> - Series와 DataFrame은 로컬 네임스페이스로 import하는 것이 훨씬 편하다.



```python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
```





## 1. Introduction to pandas data structures

> pandas 자료 구조 소개
>
> - Series와 DataFrame 이 두가지 자료구소게에 대해 익숙해지도록 하자.
> - 이 두가지 자료구조가 모든 문제를 해결할 수는 없지만, 대부분의 애플리케이션에서 사용하기 쉽고 탄탄한 기반을 제공한다.



### Series

> - Series는 일련의 객체를 담을 수 있는 1차원 배열 같은 자료 구조
> - Index라고 하는 배열의 데이터에 연관된 일므을 가지고 있다.

In [2]:

```python
obj = Series([4, 7, -5, 3])
obj
```

Out[2]:

```python
0    4
1    7
2   -5
3    3
dtype: int64
```

In [3]:

```python
obj.index
```

Out[3]:

```python
RangeIndex(start=0, stop=4, step=1)
```

In [4]:

```python
obj.values
```

Out[4]:

```python
array([ 4,  7, -5,  3], dtype=int64)
```

In [5]:

```python
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
```

Out[5]:

```python
d    4
b    7
a   -5
c    3
dtype: int64
```

In [6]:

```python
obj2.index
```

Out[6]:

```python
Index(['d', 'b', 'a', 'c'], dtype='object')
```

In [7]:

```python
obj2['a']
```

Out[7]:

```python
-5
```

In [8]:

```python
obj2['d'] = 6
obj2[['c', 'a', 'd']]
```

Out[8]:

```python
c    3
a   -5
d    6
dtype: int64
```

In [9]:

```python
obj2[obj2 > 0]
```

Out[9]:

```python
d    6
b    7
c    3
dtype: int64
```

In [10]:

```python
obj2 * 2
```

Out[10]:

```python
d    12
b    14
a   -10
c     6
dtype: int64
```

In [11]:

```python
np.exp(obj2) # 지수승을 나타내는 함수 e^n 을 나타내는 것
```

Out[11]:

```python
d     403.428793
b    1096.633158
a       0.006738
c      20.085537
dtype: float64
```

In [12]:

```python
'b' in obj2
```

Out[12]:

```python
True
```

In [13]:

```python
'e' in obj2
```

Out[13]:

```python
False
```

In [14]:

```python
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3
```

Out[14]:

```python
Ohio      35000
Oregon    16000
Texas     71000
Utah       5000
dtype: int64
```

In [15]:

```python
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4
```

Out[15]:

```python
California        NaN	# NaN : Null값이나 무한대 값
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
```

In [16]:

```python
pd.isnull(obj4)
```

Out[16]:

```python
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
```

In [17]:

```python
pd.notnull(obj4)
```

Out[17]:

```python
California    False
Ohio           True
Oregon         True
Texas          True
dtype: bool
```

In [18]:

```python
obj4.isnull()
```

Out[18]:

```python
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
```

In [19]:

```python
obj3
```

Out[19]:

```python
Ohio      35000
Oregon    16000
Texas     71000
Utah       5000
dtype: int64
```

In [20]:

```python
obj4
```

Out[20]:

```python
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
```

In [21]:

```python
obj3 + obj4
```

Out[21]:

```python
California         NaN
Ohio           70000.0
Oregon         32000.0
Texas         142000.0
Utah               NaN
dtype: float64
```

In [22]:

```python
obj4.name = 'population'
obj4.index.name = 'state'
obj4
```

Out[22]:

```python
state
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
Name: population, dtype: float64
```

In [23]:

```python
obj
```

Out[23]:

```python
0    4
1    7
2   -5
3    3
dtype: int64
```

In [24]:

```python
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj
```

Out[24]:

```python
Bob      4
Steve    7
Jeff    -5
Ryan     3
dtype: int64
```



### DataFrame

> - 표 같은 스프레드시트 형식의 자료구조로 여러개의 칼럼을 가진다.
> - 각 칼럼은 서로 다른 종류의 값(숫자, 문자, 불리언 등)을 담을 수 있다.
> - 로우와 칼럼에 대한 Index가 있는데, Index의 모양이 같은 Series 객체를 담고 있는 파이썬 사전으로 생각하자.
> - Dataframe은 데이터를 내부적으로 2차원 형식으로 저장고차원의 표 형식 데이터를 계층적 색인(Hierarchical Indexing)을 통해 쉽게 표현할 수 있다. </font>







In [25]:

```python
# DataFrame 객체 생성1
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year' : [2000, 2001, 2002, 2001, 2002],
        'pop'  : [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
```

In [26]:

```python
frame
```

Out[26]:

|      | pop  | state  | year |
| ---- | ---- | ------ | ---- |
| 0    | 1.5  | Ohio   | 2000 |
| 1    | 1.7  | Ohio   | 2001 |
| 2    | 3.6  | Ohio   | 2002 |
| 3    | 2.4  | Nevada | 2001 |
| 4    | 2.9  | Nevada | 2002 |

In [27]:

```
# 순서를 지정
DataFrame(data, columns=['year', 'state', 'pop'])
```

Out[27]:

|      | year | state  | pop  |
| ---- | ---- | ------ | ---- |
| 0    | 2000 | Ohio   | 1.5  |
| 1    | 2001 | Ohio   | 1.7  |
| 2    | 2002 | Ohio   | 3.6  |
| 3    | 2001 | Nevada | 2.4  |
| 4    | 2002 | Nevada | 2.9  |

In [28]:

```python
# DataFrame 객체 생성2
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame2
```

Out[28]:

|       | year | state  | pop  | debt |
| ----- | ---- | ------ | ---- | ---- |
| one   | 2000 | Ohio   | 1.5  | NaN  |
| two   | 2001 | Ohio   | 1.7  | NaN  |
| three | 2002 | Ohio   | 3.6  | NaN  |
| four  | 2001 | Nevada | 2.4  | NaN  |
| five  | 2002 | Nevada | 2.9  | NaN  |

In [29]:

```python
frame2.columns
```

Out[29]:

```python
Index(['year', 'state', 'pop', 'debt'], dtype='object')
```

In [30]:

```python
frame2['state']
```

Out[30]:

```python
one        Ohio
two        Ohio
three      Ohio
four     Nevada
five     Nevada
Name: state, dtype: object
```

In [31]:

```python
frame2.year
```

Out[31]:

```python
one      2000
two      2001
three    2002
four     2001
five     2002
Name: year, dtype: int64
```

In [32]:

```python
# 로우는 위치나 ix 메소드를 통해 접근
frame2.ix['three']
```

Out[32]:

```python
year     2002
state    Ohio
pop       3.6
debt      NaN
Name: three, dtype: object
```



* 추가

  * 경고문이 발생하는데 이제 ix는 잘 안쓰게되고 loc으로 라벨명, iloc으로 인덱스 숫자로 간다.

  * frame2.ix[3]

    * ```python
      C:\Python\Anaconda3-52\lib\site-packages\ipykernel_launcher.py:1: DeprecationWarning: 
      .ix is deprecated. Please use
      .loc for label based indexing or
      .iloc for positional indexing
      
      See the documentation here:
      http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
        """Entry point for launching an IPython kernel.
        
      year       2001
      state    Nevada
      pop         2.4
      debt        NaN
      Name: four, dtype: object
      ```

  * frame2.loc['three']

    * ```python
      year     2002
      state    Ohio
      pop       3.6
      debt      NaN
      Name: three, dtype: object
      ```

  * frame2.iloc[2]

    * ```Python
      year     2002
      state    Ohio
      pop       3.6
      debt      NaN
      Name: three, dtype: object
      ```



In [33]:

```python
frame2['debt'] = 16.5
frame2
```

Out[33]:

|       | year | state  | pop  | debt |
| ----- | ---- | ------ | ---- | ---- |
| one   | 2000 | Ohio   | 1.5  | 16.5 |
| two   | 2001 | Ohio   | 1.7  | 16.5 |
| three | 2002 | Ohio   | 3.6  | 16.5 |
| four  | 2001 | Nevada | 2.4  | 16.5 |
| five  | 2002 | Nevada | 2.9  | 16.5 |

In [34]:

```python
frame2['debt'] = np.arange(5.)
frame2
```

Out[34]:

|       | year | state  | pop  | debt |
| ----- | ---- | ------ | ---- | ---- |
| one   | 2000 | Ohio   | 1.5  | 0.0  |
| two   | 2001 | Ohio   | 1.7  | 1.0  |
| three | 2002 | Ohio   | 3.6  | 2.0  |
| four  | 2001 | Nevada | 2.4  | 3.0  |
| five  | 2002 | Nevada | 2.9  | 4.0  |

In [35]:

```python
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2
```

Out[35]:

|       | year | state  | pop  | debt |
| ----- | ---- | ------ | ---- | ---- |
| one   | 2000 | Ohio   | 1.5  | NaN  |
| two   | 2001 | Ohio   | 1.7  | -1.2 |
| three | 2002 | Ohio   | 3.6  | NaN  |
| four  | 2001 | Nevada | 2.4  | -1.5 |
| five  | 2002 | Nevada | 2.9  | -1.7 |

In [36]:

```python
frame2['eastern'] = frame2.state == 'Ohio'
frame2
```

Out[36]:

|       | year | state  | pop  | debt | eastern |
| ----- | ---- | ------ | ---- | ---- | ------- |
| one   | 2000 | Ohio   | 1.5  | NaN  | True    |
| two   | 2001 | Ohio   | 1.7  | -1.2 | True    |
| three | 2002 | Ohio   | 3.6  | NaN  | True    |
| four  | 2001 | Nevada | 2.4  | -1.5 | False   |
| five  | 2002 | Nevada | 2.9  | -1.7 | False   |

In [37]:

```python
# 칼럼을 삭제
del frame2['eastern']
frame2.columns
```

Out[37]:

```python
Index(['year', 'state', 'pop', 'debt'], dtype='object')
```

In [38]:

```python
frame2
```

Out[38]:

|       | year | state  | pop  | debt |
| ----- | ---- | ------ | ---- | ---- |
| one   | 2000 | Ohio   | 1.5  | NaN  |
| two   | 2001 | Ohio   | 1.7  | -1.2 |
| three | 2002 | Ohio   | 3.6  | NaN  |
| four  | 2001 | Nevada | 2.4  | -1.5 |
| five  | 2002 | Nevada | 2.9  | -1.7 |



[Tip] DataFrame의 색인을 이용해서 생성된 칼럼은 내부 데이터에 대한 뷰(View)이며 복사가 이루어지지 않는다.

이렇게 얻은 Series 객체에 대한 변경은 실제 DataFrame에 반영된다.복사본이 필요할 때는 Series의 copy 메소드를 이용





In [39]:

```python
# DataFrame 객체 생성3  
# 중첩된 dict, 바깥 사전의 키값이 칼럼이 되고 안의 키는 로우가 된다.
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio'  : {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
```

In [40]:

```
frame3
```

Out[40]:

|      | Nevada | Ohio |
| ---- | ------ | ---- |
| 2000 | NaN    | 1.5  |
| 2001 | 2.4    | 1.7  |
| 2002 | 2.9    | 3.6  |

In [41]:

```
# NumPy에서 처럼 결과값의 순서 뒤집기
frame3.T
```

Out[41]:

|        | 2000 | 2001 | 2002 |
| ------ | ---- | ---- | ---- |
| Nevada | NaN  | 2.4  | 2.9  |
| Ohio   | 1.5  | 1.7  | 3.6  |

In [42]:

```python
DataFrame(pop, index=[2001, 2002, 2003])
```

Out[42]:

|      | Nevada | Ohio |
| ---- | ------ | ---- |
| 2001 | 2.4    | 1.7  |
| 2002 | 2.9    | 3.6  |
| 2003 | NaN    | NaN  |

In [43]:

```python
frame3
```

Out[43]:

|      | Nevada | Ohio |
| ---- | ------ | ---- |
| 2000 | NaN    | 1.5  |
| 2001 | 2.4    | 1.7  |
| 2002 | 2.9    | 3.6  |

In [44]:

```
pdata = {'Ohio'  : frame3['Ohio'][:-1], # Ohio 맨 마지막 행 값(3.6)은 제외한다.
         'Nevada': frame3['Nevada'][:2]} # Nevada의 첫번째 두번째 행 값은 포함한다.
DataFrame(pdata)
```

Out[44]:

|      | Nevada | Ohio |
| ---- | ------ | ---- |
| 2000 | NaN    | 1.5  |
| 2001 | 2.4    | 1.7  |

In [45]:

```python
frame3.index.name = 'year'; frame3.columns.name = 'state'
frame3
```

Out[45]:

| state | Nevada | Ohio |
| ----- | ------ | ---- |
| year  |        |      |
| 2000  | NaN    | 1.5  |
| 2001  | 2.4    | 1.7  |
| 2002  | 2.9    | 3.6  |

In [46]:

```python
frame3.values
```

Out[46]:

```python
array([[nan, 1.5],
       [2.4, 1.7],
       [2.9, 3.6]])
```

In [47]:

```python
frame2.values
```

Out[47]:

```python
array([[2000, 'Ohio', 1.5, nan],
       [2001, 'Ohio', 1.7, -1.2],
       [2002, 'Ohio', 3.6, nan],
       [2001, 'Nevada', 2.4, -1.5],
       [2002, 'Nevada', 2.9, -1.7]], dtype=object)
```

In [48]:

```python
frame2
```

Out[48]:

|       | year | state  | pop  | debt |
| ----- | ---- | ------ | ---- | ---- |
| one   | 2000 | Ohio   | 1.5  | NaN  |
| two   | 2001 | Ohio   | 1.7  | -1.2 |
| three | 2002 | Ohio   | 3.6  | NaN  |
| four  | 2001 | Nevada | 2.4  | -1.5 |
| five  | 2002 | Nevada | 2.9  | -1.7 |

In [49]:

```python
# DataFrame 생성자에서 사용 가능한 입력 데이터 
Image(bpc.Table5_1)
```

Out[49]:





### Index objects

> pandas의 색인 객체
>
> - 표 형식의 데이터에서 각 로우와 칼럼에 대한 이름과 다른 메타데이터(축의 이름 등)을 저장하는 객체
> - Series나 DataFrame 객체를 생성할 때 사용되는 배열이나 혹은 다른 순차적인 이름은 내부적으로 색인으로 변환
> - 색인 객체는 변경할 수 없다. 그래서~~~ 자료구조사이에서 안전하게 공유될 수 있다.^^

In [50]:

```
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
index
```

Out[50]:

```
Index(['a', 'b', 'c'], dtype='object')
```

In [51]:

```
index[1:]
```

Out[51]:

```
Index(['b', 'c'], dtype='object')
```

In [52]:

```
# 색인객체 변경시 TypeError 발생!!
# index[1] = 'd'
```

In [53]:

```
index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
obj2.index is index
```

Out[53]:

```
True
```

In [54]:

```
frame3
```

Out[54]:

| state | Nevada | Ohio |
| ----- | ------ | ---- |
| year  |        |      |
| 2000  | NaN    | 1.5  |
| 2001  | 2.4    | 1.7  |
| 2002  | 2.9    | 3.6  |

In [55]:

```
'Ohio' in frame3.columns
```

Out[55]:

```
True
```

In [56]:

```
2003 in frame3.index
```

Out[56]:

```
False
```

In [57]:

```
# pandas의 주요 Index 객체
Image(bpc.Table5_2)
```

```
# Index 메소드와 속성
Image(bpc.Table5_3)
```





# 2. Pandas Basic 2

In [1]:

```
from images import bigpycraft_bda as bpc
from IPython.display import Image 

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
```



## 2. Essential functionality

> 핵심 기능
>
> - Series나 DataFrame에 저장된 데이터를 다루는 방법



### Reindexing

In [2]:

```
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj
```

Out[2]:

```
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64
```

In [3]:

```
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2
```

Out[3]:

```
a   -5.3
b    7.2
c    3.6
d    4.5
e    NaN
dtype: float64
```

In [4]:

```
obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
```

Out[4]:

```
a   -5.3
b    7.2
c    3.6
d    4.5
e    0.0
dtype: float64
```

In [5]:

```
# reindex 메소드(보간) 옵션
Image(bpc.Table5_4, width=300)
```



In [6]:

```
# ffill 메소드 : 앞의 값으로 누락된 값을 채워 넣기
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6), method='ffill')
```

Out[6]:

```
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
```

In [7]:

```
# bfill 메소드 : 뒤의 값으로 누락된 값을 채워 넣기
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6), method='bfill')
```

Out[7]:

```
0      blue
1    purple
2    purple
3    yellow
4    yellow
5       NaN
dtype: object
```

In [8]:

- arange는 numpy에 있는 내장함수로 arange(1,9,1)이라하면 1부터 9까지 1씩 올리는 것
- reshape는 행렬 3x3

```
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])
frame
```

Out[8]:

|      | Ohio | Texas | California |
| ---- | ---- | ----- | ---------- |
| a    | 0    | 1     | 2          |
| c    | 3    | 4     | 5          |
| d    | 6    | 7     | 8          |

In [9]:

```
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame2
```

Out[9]:

|      | Ohio | Texas | California |
| ---- | ---- | ----- | ---------- |
| a    | 0.0  | 1.0   | 2.0        |
| b    | NaN  | NaN   | NaN        |
| c    | 3.0  | 4.0   | 5.0        |
| d    | 6.0  | 7.0   | 8.0        |

\# Question. 음~ 왜 float 형으로 바뀌지???

In [10]:

```
states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)
```

Out[10]:

|      | Texas | Utah | California |
| ---- | ----- | ---- | ---------- |
| a    | 1     | NaN  | 2          |
| c    | 4     | NaN  | 5          |
| d    | 7     | NaN  | 8          |

In [11]:

```
frame.reindex(index=['a', 'b', 'c', 'd'], columns=states)
```

Out[11]:

|      | Texas | Utah | California |
| ---- | ----- | ---- | ---------- |
| a    | 1.0   | NaN  | 2.0        |
| b    | NaN   | NaN  | NaN        |
| c    | 4.0   | NaN  | 5.0        |
| d    | 7.0   | NaN  | 8.0        |

In [12]:

```
frame.loc[['a', 'b', 'c', 'd'], states]
```

Out[12]:

|      | Texas | Utah | California |
| ---- | ----- | ---- | ---------- |
| a    | 1.0   | NaN  | 2.0        |
| b    | NaN   | NaN  | NaN        |
| c    | 4.0   | NaN  | 5.0        |
| d    | 7.0   | NaN  | 8.0        |

In [13]:

```
# 재색인 함수 인자
Image(bpc.Table5_5, width=600)
```



### Dropping entries from an axis

> 하나의 로우 또는 칼럼 삭제하기
>
> - 색인 배열 또는 삭제하려는 로우나 칼럼이 제외된 리스트를 이미 가지고 있다면 쉽게 삭제 가능한데...
> - 이 방법은 데이터의 모양을 변경하는 작업이 필요하다.
> - drop 메소드를 사용하면 선택한 값이 삭제된 새로운 객체를 얻을 수 있다.
> - 칼럼 삭제 : drop( [칼럼명], axis=1)로우 삭제 : drop( [로우명], axis=0) or drop( [로우명] ) </font>



In [14]:

```
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
new_obj
```

Out[14]:

```
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
```

In [15]:

```
obj.drop(['d', 'c']) # del는 완전히 삭제하는 것이지만, drop은 일시적으로 없애는 것이라는 것!
# del obj['d', 'c']
```

Out[15]:

```
a    0.0
b    1.0
e    4.0
dtype: float64
```

In [16]:

```
obj
```

Out[16]:

```
a    0.0
b    1.0
c    2.0
d    3.0
e    4.0
dtype: float64
```

In [17]:

```
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data
```

Out[17]:

|          | one  | two  | three | four |
| -------- | ---- | ---- | ----- | ---- |
| Ohio     | 0    | 1    | 2     | 3    |
| Colorado | 4    | 5    | 6     | 7    |
| Utah     | 8    | 9    | 10    | 11   |
| New York | 12   | 13   | 14    | 15   |

In [18]:

```
data.drop(['Colorado', 'Ohio'])
```

Out[18]:

|          | one  | two  | three | four |
| -------- | ---- | ---- | ----- | ---- |
| Utah     | 8    | 9    | 10    | 11   |
| New York | 12   | 13   | 14    | 15   |



#### [Note] axis=1 denotes that we are referring to a column, not a row 

In [19]:

```
data.drop('two', axis=1)
```

Out[19]:

|          | one  | three | four |
| -------- | ---- | ----- | ---- |
| Ohio     | 0    | 2     | 3    |
| Colorado | 4    | 6     | 7    |
| Utah     | 8    | 10    | 11   |
| New York | 12   | 14    | 15   |

In [20]:

```
data.drop(['two', 'four'], axis=1)
```

Out[20]:

|          | one  | three |
| -------- | ---- | ----- |
| Ohio     | 0    | 2     |
| Colorado | 4    | 6     |
| Utah     | 8    | 10    |
| New York | 12   | 14    |



### Indexing, selection, and filtering

> 색인하기, 선택하기, 거르기
>
> - Series의 색인(obj[...])은 NumPy 배열의 색인과 유사하게 동작하는데,
> - Series의 색인은 정수가 아니어도 된다는 점이 다르다.
> - 또한 라벨이름으로 슬라이싱하는 것은 시작점과 끝점을 포함한다는 것이 파이썬과 다른점이다.

In [21]:

```
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj
```

Out[21]:

```
a    0.0
b    1.0
c    2.0
d    3.0
dtype: float64
```

In [22]:

```
obj['b']
```

Out[22]:

```
1.0
```

In [23]:

```
obj[1]
```

Out[23]:

```
1.0
```

In [24]:

```
obj[2:4]
```

Out[24]:

```
c    2.0
d    3.0
dtype: float64
```

In [25]:

```
obj[['b', 'a', 'd']]
```

Out[25]:

```
b    1.0
a    0.0
d    3.0
dtype: float64
```

In [26]:

```
obj[[1, 3]]
```

Out[26]:

```
b    1.0
d    3.0
dtype: float64
```

In [27]:

```
obj[obj < 2]
```

Out[27]:

```
a    0.0
b    1.0
dtype: float64
```



#### 라벨이름으로 슬라이싱 할 경우, 끝점도 포함한다.

In [28]:

```
obj['b':'c']
```

Out[28]:

```
b    1.0
c    2.0
dtype: float64
```

In [29]:

```
obj['b':'c'] = 5
obj
```

Out[29]:

```
a    0.0
b    5.0
c    5.0
d    3.0
dtype: float64
```

In [30]:

```
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data
```

Out[30]:

|          | one  | two  | three | four |
| -------- | ---- | ---- | ----- | ---- |
| Ohio     | 0    | 1    | 2     | 3    |
| Colorado | 4    | 5    | 6     | 7    |
| Utah     | 8    | 9    | 10    | 11   |
| New York | 12   | 13   | 14    | 15   |

In [31]:

```
data['two']
```

Out[31]:

```
Ohio         1
Colorado     5
Utah         9
New York    13
Name: two, dtype: int32
```

In [32]:

```
data[['three', 'one']]
```

Out[32]:

|          | three | one  |
| -------- | ----- | ---- |
| Ohio     | 2     | 0    |
| Colorado | 6     | 4    |
| Utah     | 10    | 8    |
| New York | 14    | 12   |

In [33]:

```
data[:2]
```

Out[33]:

|          | one  | two  | three | four |
| -------- | ---- | ---- | ----- | ---- |
| Ohio     | 0    | 1    | 2     | 3    |
| Colorado | 4    | 5    | 6     | 7    |

In [34]:

```
data[data['three'] > 5]
```

Out[34]:

|          | one  | two  | three | four |
| -------- | ---- | ---- | ----- | ---- |
| Colorado | 4    | 5    | 6     | 7    |
| Utah     | 8    | 9    | 10    | 11   |
| New York | 12   | 13   | 14    | 15   |

In [35]:

```
# 요건 문법적으로 모순이 있으나, 실용성에 기인한 것일뿐
data < 5
```

Out[35]:

|          | one   | two   | three | four  |
| -------- | ----- | ----- | ----- | ----- |
| Ohio     | True  | True  | True  | True  |
| Colorado | True  | False | False | False |
| Utah     | False | False | False | False |
| New York | False | False | False | False |

In [36]:

```
data[data < 5] = 0
```

In [37]:

```
data
```

Out[37]:

|          | one  | two  | three | four |
| -------- | ---- | ---- | ----- | ---- |
| Ohio     | 0    | 0    | 0     | 0    |
| Colorado | 0    | 5    | 6     | 7    |
| Utah     | 8    | 9    | 10    | 11   |
| New York | 12   | 13   | 14    | 15   |

In [38]:

```
data.loc['Colorado', ['two', 'three']]
```

Out[38]:

```
two      5
three    6
Name: Colorado, dtype: int32
```

In [39]:

```
data.ix[['Colorado', 'Utah'], [3, 0, 1]]
```



```
C:\Python\Anaconda3-50\lib\site-packages\ipykernel_launcher.py:1: DeprecationWarning: 
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

See the documentation here:
http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
  """Entry point for launching an IPython kernel.
```

Out[39]:

|          | four | one  | two  |
| -------- | ---- | ---- | ---- |
| Colorado | 7    | 0    | 5    |
| Utah     | 11   | 8    | 9    |

In [40]:

```
data.ix[2]
```

Out[40]:

```
one       8
two       9
three    10
four     11
Name: Utah, dtype: int32
```

In [41]:

```
data.ix[:'Utah', 'two']
```

Out[41]:

```
Ohio        0
Colorado    5
Utah        9
Name: two, dtype: int32
```

In [42]:

```
data.ix[data.three > 5, :3]
```

Out[42]:

|          | one  | two  | three |
| -------- | ---- | ---- | ----- |
| Colorado | 0    | 5    | 6     |
| Utah     | 8    | 9    | 10    |
| New York | 12   | 13   | 14    |

In [43]:

```
# DataFrame의 값 선택하기
Image(bpc.Table5_6, width=600)
```



### Arithmetic and data alignment

> 산술연산과 데이터 정렬
>
> - pandas 에서 중요한 기능은 색인이 다른 객체 간의 산술연산이다.
> - 객체를 더할 때 짝이 맞지 않는 색인이 있다면 결과에 두 색인이 통합된다.

In [44]:

```
s1 = Series([ 7.3, -2.5, 3.4, 1.5],    index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
```

In [45]:

```
s1
```

Out[45]:

```
a    7.3
c   -2.5
d    3.4
e    1.5
dtype: float64
```

In [46]:

```
s2
```

Out[46]:

```
a   -2.1
c    3.6
e   -1.5
f    4.0
g    3.1
dtype: float64
```

In [47]:

```
s1 + s2
```

Out[47]:

```
a    5.2
c    1.1
d    NaN
e    0.0
f    NaN
g    NaN
dtype: float64
```

In [48]:

```
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])
```

In [49]:

```
df1
```

Out[49]:

|          | b    | c    | d    |
| -------- | ---- | ---- | ---- |
| Ohio     | 0.0  | 1.0  | 2.0  |
| Texas    | 3.0  | 4.0  | 5.0  |
| Colorado | 6.0  | 7.0  | 8.0  |

In [50]:

```
df2
```

Out[50]:

|        | b    | d    | e    |
| ------ | ---- | ---- | ---- |
| Utah   | 0.0  | 1.0  | 2.0  |
| Ohio   | 3.0  | 4.0  | 5.0  |
| Texas  | 6.0  | 7.0  | 8.0  |
| Oregon | 9.0  | 10.0 | 11.0 |

In [51]:

```
df1 + df2
```

Out[51]:

|          | b    | c    | d    | e    |
| -------- | ---- | ---- | ---- | ---- |
| Colorado | NaN  | NaN  | NaN  | NaN  |
| Ohio     | 3.0  | NaN  | 6.0  | NaN  |
| Oregon   | NaN  | NaN  | NaN  | NaN  |
| Texas    | 9.0  | NaN  | 12.0 | NaN  |
| Utah     | NaN  | NaN  | NaN  | NaN  |



#### Arithmetic methods with fill values

> 산술연산 메소드에 채워 넣을 값 지정하기

In [52]:

```
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
```

In [53]:

```
df1
```

Out[53]:

|      | a    | b    | c    | d    |
| ---- | ---- | ---- | ---- | ---- |
| 0    | 0.0  | 1.0  | 2.0  | 3.0  |
| 1    | 4.0  | 5.0  | 6.0  | 7.0  |
| 2    | 8.0  | 9.0  | 10.0 | 11.0 |

In [54]:

```
df2
```

Out[54]:

|      | a    | b    | c    | d    | e    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | 0.0  | 1.0  | 2.0  | 3.0  | 4.0  |
| 1    | 5.0  | 6.0  | 7.0  | 8.0  | 9.0  |
| 2    | 10.0 | 11.0 | 12.0 | 13.0 | 14.0 |
| 3    | 15.0 | 16.0 | 17.0 | 18.0 | 19.0 |

In [55]:

```
df1 + df2
```

Out[55]:

|      | a    | b    | c    | d    | e    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | 0.0  | 2.0  | 4.0  | 6.0  | NaN  |
| 1    | 9.0  | 11.0 | 13.0 | 15.0 | NaN  |
| 2    | 18.0 | 20.0 | 22.0 | 24.0 | NaN  |
| 3    | NaN  | NaN  | NaN  | NaN  | NaN  |

In [56]:

```
df1.add(df2, fill_value=0)
```

Out[56]:

|      | a    | b    | c    | d    | e    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | 0.0  | 2.0  | 4.0  | 6.0  | 4.0  |
| 1    | 9.0  | 11.0 | 13.0 | 15.0 | 9.0  |
| 2    | 18.0 | 20.0 | 22.0 | 24.0 | 14.0 |
| 3    | 15.0 | 16.0 | 17.0 | 18.0 | 19.0 |

In [57]:

```
df1.reindex(columns=df2.columns, fill_value=0)
```

Out[57]:

|      | a    | b    | c    | d    | e    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | 0.0  | 1.0  | 2.0  | 3.0  | 0    |
| 1    | 4.0  | 5.0  | 6.0  | 7.0  | 0    |
| 2    | 8.0  | 9.0  | 10.0 | 11.0 | 0    |

In [58]:

```
# 산술연산 메소드
Image(bpc.Table5_7, width=250)
```



#### Operations between DataFrame and Series

> DataFrame과 Series 간의 연산

In [59]:

```
arr = np.arange(12.).reshape((3, 4))
arr
```

Out[59]:

```
array([[ 0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.],
       [ 8.,  9., 10., 11.]])
```

In [60]:

```
arr[0]
```

Out[60]:

```
array([0., 1., 2., 3.])
```

In [61]:

```
arr - arr[0]
```

Out[61]:

```
array([[0., 0., 0., 0.],
       [4., 4., 4., 4.],
       [8., 8., 8., 8.]])
```

In [62]:

```
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
```

Out[62]:

|        | b    | d    | e    |
| ------ | ---- | ---- | ---- |
| Utah   | 0.0  | 1.0  | 2.0  |
| Ohio   | 3.0  | 4.0  | 5.0  |
| Texas  | 6.0  | 7.0  | 8.0  |
| Oregon | 9.0  | 10.0 | 11.0 |

In [63]:

```
series = frame.iloc[0]
series
```

Out[63]:

```
b    0.0
d    1.0
e    2.0
Name: Utah, dtype: float64
```

In [64]:

```
frame - series
```

Out[64]:

|        | b    | d    | e    |
| ------ | ---- | ---- | ---- |
| Utah   | 0.0  | 0.0  | 0.0  |
| Ohio   | 3.0  | 3.0  | 3.0  |
| Texas  | 6.0  | 6.0  | 6.0  |
| Oregon | 9.0  | 9.0  | 9.0  |

In [65]:

```
series2 = Series(range(3), index=['b', 'e', 'f'])
series2
```

Out[65]:

```
b    0
e    1
f    2
dtype: int32
```

In [66]:

```
frame + series2
```

Out[66]:

|        | b    | d    | e    | f    |
| ------ | ---- | ---- | ---- | ---- |
| Utah   | 0.0  | NaN  | 3.0  | NaN  |
| Ohio   | 3.0  | NaN  | 6.0  | NaN  |
| Texas  | 6.0  | NaN  | 9.0  | NaN  |
| Oregon | 9.0  | NaN  | 12.0 | NaN  |

In [67]:

```
series3 = frame['d']
series3
```

Out[67]:

```
Utah       1.0
Ohio       4.0
Texas      7.0
Oregon    10.0
Name: d, dtype: float64
```

In [68]:

```
frame
```

Out[68]:

|        | b    | d    | e    |
| ------ | ---- | ---- | ---- |
| Utah   | 0.0  | 1.0  | 2.0  |
| Ohio   | 3.0  | 4.0  | 5.0  |
| Texas  | 6.0  | 7.0  | 8.0  |
| Oregon | 9.0  | 10.0 | 11.0 |

In [69]:

```
frame.sub(series3, axis=0)
```

Out[69]:

|        | b    | d    | e    |
| ------ | ---- | ---- | ---- |
| Utah   | -1.0 | 0.0  | 1.0  |
| Ohio   | -1.0 | 0.0  | 1.0  |
| Texas  | -1.0 | 0.0  | 1.0  |
| Oregon | -1.0 | 0.0  | 1.0  |



### Function application and mapping 

> 함수 적용과 매핑
>
> - pandas 객체에도 NumPy의 유니버설 함수를 적용할 수 있다.
> - 유니버설 함수 : 배열의 각 원소에 적용되는 메소드

In [70]:

```
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
```

In [71]:

```
frame
```

Out[71]:

|        | b         | d         | e         |
| ------ | --------- | --------- | --------- |
| Utah   | 1.056115  | 0.867512  | 1.370779  |
| Ohio   | -0.535711 | -1.246486 | -2.185357 |
| Texas  | -0.386328 | -1.228566 | -1.601029 |
| Oregon | 1.574897  | 0.457937  | -0.790390 |

In [72]:

```
np.abs(frame)
```

Out[72]:

|        | b        | d        | e        |
| ------ | -------- | -------- | -------- |
| Utah   | 1.056115 | 0.867512 | 1.370779 |
| Ohio   | 0.535711 | 1.246486 | 2.185357 |
| Texas  | 0.386328 | 1.228566 | 1.601029 |
| Oregon | 1.574897 | 0.457937 | 0.790390 |

In [73]:

```
f = lambda x: x.max() - x.min()
```

In [74]:

```
frame.apply(f)
```

Out[74]:

```
b    2.110608
d    2.113998
e    3.556136
dtype: float64
```

In [75]:

```
frame.apply(f, axis=1)
```

Out[75]:

```
Utah      0.503267
Ohio      1.649647
Texas     1.214701
Oregon    2.365287
dtype: float64
```

In [76]:

```
def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])

frame.apply(f)
```

Out[76]:

|      | b         | d         | e         |
| ---- | --------- | --------- | --------- |
| min  | -0.535711 | -1.246486 | -2.185357 |
| max  | 1.574897  | 0.867512  | 1.370779  |

In [77]:

```
# 실수값을 문자열 포맷으로 변환
format = lambda x: '%.2f' % x
frame.applymap(format)
```

Out[77]:

|        | b     | d     | e     |
| ------ | ----- | ----- | ----- |
| Utah   | 1.06  | 0.87  | 1.37  |
| Ohio   | -0.54 | -1.25 | -2.19 |
| Texas  | -0.39 | -1.23 | -1.60 |
| Oregon | 1.57  | 0.46  | -0.79 |

In [78]:

```
frame['e'].map(format)
```

Out[78]:

```
Utah       1.37
Ohio      -2.19
Texas     -1.60
Oregon    -0.79
Name: e, dtype: object
```



### Sorting and ranking 

> 정렬과 순위

In [79]:

```
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()
```

Out[79]:

```
a    1
b    2
c    3
d    0
dtype: int32
```

In [80]:

```
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])
frame.sort_index()
```

Out[80]:

|       | d    | a    | b    | c    |
| ----- | ---- | ---- | ---- | ---- |
| one   | 4    | 5    | 6    | 7    |
| three | 0    | 1    | 2    | 3    |

In [81]:

```
frame.sort_index(axis=1)
```

Out[81]:

|       | a    | b    | c    | d    |
| ----- | ---- | ---- | ---- | ---- |
| three | 1    | 2    | 3    | 0    |
| one   | 5    | 6    | 7    | 4    |

In [82]:

```
frame.sort_index(axis=1, ascending=False)
```

Out[82]:

|       | d    | c    | b    | a    |
| ----- | ---- | ---- | ---- | ---- |
| three | 0    | 3    | 2    | 1    |
| one   | 4    | 7    | 6    | 5    |

In [83]:

```
obj = Series([4, 7, -3, 2])
# obj.order()
obj.sort_values()
```

Out[83]:

```
2   -3
3    2
0    4
1    7
dtype: int64
```

In [84]:

```
obj = Series([4, np.nan, 7, np.nan, -3, 2])
obj.sort_values()
```

Out[84]:

```
4   -3.0
5    2.0
0    4.0
2    7.0
1    NaN
3    NaN
dtype: float64
```

In [85]:

```
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame
```

Out[85]:

|      | a    | b    |
| ---- | ---- | ---- |
| 0    | 0    | 4    |
| 1    | 1    | 7    |
| 2    | 0    | -3   |
| 3    | 1    | 2    |

In [86]:

```
# frame.sort_index(by='b')
frame.sort_values(by='b')
```

Out[86]:

|      | a    | b    |
| ---- | ---- | ---- |
| 2    | 0    | -3   |
| 3    | 1    | 2    |
| 0    | 0    | 4    |
| 1    | 1    | 7    |

In [87]:

```
frame.sort_values(by=['a', 'b'])
```

Out[87]:

|      | a    | b    |
| ---- | ---- | ---- |
| 2    | 0    | -3   |
| 0    | 0    | 4    |
| 3    | 1    | 2    |
| 1    | 1    | 7    |

In [88]:

```
obj = Series([7, -5, 7, 4, 2, 0, 4])
obj
```

Out[88]:

```
0    7
1   -5
2    7
3    4
4    2
5    0
6    4
dtype: int64
```

In [89]:

```
obj.rank()
```

Out[89]:

```
0    6.5
1    1.0
2    6.5
3    4.5
4    3.0
5    2.0
6    4.5
dtype: float64
```

In [90]:

```
obj.rank(method='first')
```

Out[90]:

```
0    6.0
1    1.0
2    7.0
3    4.0
4    3.0
5    2.0
6    5.0
dtype: float64
```

In [91]:

```
obj.rank(ascending=False, method='max')
```

Out[91]:

```
0    2.0
1    7.0
2    2.0
3    4.0
4    5.0
5    6.0
6    4.0
dtype: float64
```

In [92]:

```
frame = DataFrame({'b': [4.3, 7, -3, 2], 
                   'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})
frame
```

Out[92]:

|      | a    | b    | c    |
| ---- | ---- | ---- | ---- |
| 0    | 0    | 4.3  | -2.0 |
| 1    | 1    | 7.0  | 5.0  |
| 2    | 0    | -3.0 | 8.0  |
| 3    | 1    | 2.0  | -2.5 |

In [93]:

```
frame.rank(axis=1)
```

Out[93]:

|      | a    | b    | c    |
| ---- | ---- | ---- | ---- |
| 0    | 2.0  | 3.0  | 1.0  |
| 1    | 1.0  | 3.0  | 2.0  |
| 2    | 2.0  | 1.0  | 3.0  |
| 3    | 2.0  | 3.0  | 1.0  |

In [94]:

```
# 순위의 동률을 처리하는 메소드
Image(bpc.Table5_8, width=450)
```



### Axis indexes with duplicate values 

> 중복 색인
>
> - pandas의 많은 함수(reindex 같은)에서 색인 값은 유일해야 하지만, 강제 사항은 아니다.
> - 허걱~~~ 중복된 색인값이 있다는 말인데..ㅠ

In [95]:

```
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj
```

Out[95]:

```
a    0
a    1
b    2
b    3
c    4
dtype: int32
```

In [96]:

```
obj.index.is_unique
```

Out[96]:

```
False
```

In [97]:

```
obj['a']
```

Out[97]:

```
a    0
a    1
dtype: int32
```

In [98]:

```
obj['c']
```

Out[98]:

```
4
```

In [99]:

```
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df
```

Out[99]:

|      | 0         | 1         | 2         |
| ---- | --------- | --------- | --------- |
| a    | -0.181906 | 0.959783  | -0.353869 |
| a    | 1.001838  | 0.650528  | -2.024275 |
| b    | 0.475098  | -0.227254 | -0.103425 |
| b    | -0.078228 | -0.144226 | 0.892488  |

In [100]:

```
df.loc['b']
```

Out[100]:

|      | 0         | 1         | 2         |
| ---- | --------- | --------- | --------- |
| b    | 0.475098  | -0.227254 | -0.103425 |
| b    | -0.078228 | -0.144226 | 0.892488  |