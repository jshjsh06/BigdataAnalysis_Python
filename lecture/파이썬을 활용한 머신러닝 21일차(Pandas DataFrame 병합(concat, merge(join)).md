# Pandas DataFrame 병합(concat, merge(join))

section-C의 3-1. Seoul Stat 1

https://htmlpreview.github.io/?https://github.com/bigpycraft/iitp18-multicampus/blob/master/section-C/html/PD_DA_331_OpenGov_Seoul_CCTV_in2018_ver3.html

### Tip. DataFrame 병합

In [25]:

```
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])
```

In [26]:

```
df1
```

Out[26]:

|      | A    | B    | C    | D    |
| ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | C0   | D0   |
| 1    | A1   | B1   | C1   | D1   |
| 2    | A2   | B2   | C2   | D2   |
| 3    | A3   | B3   | C3   | D3   |

In [27]:

```
df2
```

Out[27]:

|      | A    | B    | C    | D    |
| ---- | ---- | ---- | ---- | ---- |
| 4    | A4   | B4   | C4   | D4   |
| 5    | A5   | B5   | C5   | D5   |
| 6    | A6   | B6   | C6   | D6   |
| 7    | A7   | B7   | C7   | D7   |

In [28]:

```
df3
```

Out[28]:

|      | A    | B    | C    | D    |
| ---- | ---- | ---- | ---- | ---- |
| 8    | A8   | B8   | C8   | D8   |
| 9    | A9   | B9   | C9   | D9   |
| 10   | A10  | B10  | C10  | D10  |
| 11   | A11  | B11  | C11  | D11  |

In [29]:

```
result = pd.concat([df1, df2, df3])    # default axis=0
result
```

Out[29]:

|      | A    | B    | C    | D    |
| ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | C0   | D0   |
| 1    | A1   | B1   | C1   | D1   |
| 2    | A2   | B2   | C2   | D2   |
| 3    | A3   | B3   | C3   | D3   |
| 4    | A4   | B4   | C4   | D4   |
| 5    | A5   | B5   | C5   | D5   |
| 6    | A6   | B6   | C6   | D6   |
| 7    | A7   | B7   | C7   | D7   |
| 8    | A8   | B8   | C8   | D8   |
| 9    | A9   | B9   | C9   | D9   |
| 10   | A10  | B10  | C10  | D10  |
| 11   | A11  | B11  | C11  | D11  |

In [30]:

```
result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
result
```

Out[30]:

|      |      | A    | B    | C    | D    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| x    | 0    | A0   | B0   | C0   | D0   |
| 1    | A1   | B1   | C1   | D1   |      |
| 2    | A2   | B2   | C2   | D2   |      |
| 3    | A3   | B3   | C3   | D3   |      |
| y    | 4    | A4   | B4   | C4   | D4   |
| 5    | A5   | B5   | C5   | D5   |      |
| 6    | A6   | B6   | C6   | D6   |      |
| 7    | A7   | B7   | C7   | D7   |      |
| z    | 8    | A8   | B8   | C8   | D8   |
| 9    | A9   | B9   | C9   | D9   |      |
| 10   | A10  | B10  | C10  | D10  |      |
| 11   | A11  | B11  | C11  | D11  |      |

In [31]:

```
result.index
```

Out[31]:

```
MultiIndex(levels=[['x', 'y', 'z'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]],
           labels=[[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]])
```

In [32]:

```
result.index.get_level_values(0)
```

Out[32]:

```
Index(['x', 'x', 'x', 'x', 'y', 'y', 'y', 'y', 'z', 'z', 'z', 'z'], dtype='object')
```

In [33]:

```
result.index.get_level_values(1)
```

Out[33]:

```
Int64Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dtype='int64')
```

In [34]:

```
result
```

Out[34]:

|      |      | A    | B    | C    | D    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| x    | 0    | A0   | B0   | C0   | D0   |
| 1    | A1   | B1   | C1   | D1   |      |
| 2    | A2   | B2   | C2   | D2   |      |
| 3    | A3   | B3   | C3   | D3   |      |
| y    | 4    | A4   | B4   | C4   | D4   |
| 5    | A5   | B5   | C5   | D5   |      |
| 6    | A6   | B6   | C6   | D6   |      |
| 7    | A7   | B7   | C7   | D7   |      |
| z    | 8    | A8   | B8   | C8   | D8   |
| 9    | A9   | B9   | C9   | D9   |      |
| 10   | A10  | B10  | C10  | D10  |      |
| 11   | A11  | B11  | C11  | D11  |      |

In [35]:

```
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'], 
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])

result = pd.concat([df1, df4], axis=1)
```

In [36]:

```
df1
```

Out[36]:

|      | A    | B    | C    | D    |
| ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | C0   | D0   |
| 1    | A1   | B1   | C1   | D1   |
| 2    | A2   | B2   | C2   | D2   |
| 3    | A3   | B3   | C3   | D3   |

In [37]:

```
df4
```

Out[37]:

|      | B    | D    | F    |
| ---- | ---- | ---- | ---- |
| 2    | B2   | D2   | F2   |
| 3    | B3   | D3   | F3   |
| 6    | B6   | D6   | F6   |
| 7    | B7   | D7   | F7   |

In [38]:

```
result
```

Out[38]:

|      | A    | B    | C    | D    | B    | D    | F    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | C0   | D0   | NaN  | NaN  | NaN  |
| 1    | A1   | B1   | C1   | D1   | NaN  | NaN  | NaN  |
| 2    | A2   | B2   | C2   | D2   | B2   | D2   | F2   |
| 3    | A3   | B3   | C3   | D3   | B3   | D3   | F3   |
| 6    | NaN  | NaN  | NaN  | NaN  | B6   | D6   | F6   |
| 7    | NaN  | NaN  | NaN  | NaN  | B7   | D7   | F7   |

In [39]:

```
result = pd.concat([df1, df4], axis=1, join='inner')
result
```

Out[39]:

|      | A    | B    | C    | D    | B    | D    | F    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 2    | A2   | B2   | C2   | D2   | B2   | D2   | F2   |
| 3    | A3   | B3   | C3   | D3   | B3   | D3   | F3   |

In [40]:

```
result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
result
```

Out[40]:

|      | A    | B    | C    | D    | B    | D    | F    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | C0   | D0   | NaN  | NaN  | NaN  |
| 1    | A1   | B1   | C1   | D1   | NaN  | NaN  | NaN  |
| 2    | A2   | B2   | C2   | D2   | B2   | D2   | F2   |
| 3    | A3   | B3   | C3   | D3   | B3   | D3   | F3   |

In [41]:

```
result = pd.concat([df1, df4], ignore_index=True)
result
```

Out[41]:

|      | A    | B    | C    | D    | F    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | C0   | D0   | NaN  |
| 1    | A1   | B1   | C1   | D1   | NaN  |
| 2    | A2   | B2   | C2   | D2   | NaN  |
| 3    | A3   | B3   | C3   | D3   | NaN  |
| 4    | NaN  | B2   | NaN  | D2   | F2   |
| 5    | NaN  | B3   | NaN  | D3   | F3   |
| 6    | NaN  | B6   | NaN  | D6   | F6   |
| 7    | NaN  | B7   | NaN  | D7   | F7   |

In [42]:

```
left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
```

In [43]:

```
left
```

Out[43]:

|      | A    | B    | key  |
| ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | K0   |
| 1    | A1   | B1   | K4   |
| 2    | A2   | B2   | K2   |
| 3    | A3   | B3   | K3   |

In [44]:

```
right
```

Out[44]:

|      | C    | D    | key  |
| ---- | ---- | ---- | ---- |
| 0    | C0   | D0   | K0   |
| 1    | C1   | D1   | K1   |
| 2    | C2   | D2   | K2   |
| 3    | C3   | D3   | K3   |

In [45]:

```
pd.merge(left, right, on='key')
```

Out[45]:

|      | A    | B    | key  | C    | D    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | K0   | C0   | D0   |
| 1    | A2   | B2   | K2   | C2   | D2   |
| 2    | A3   | B3   | K3   | C3   | D3   |

In [46]:

```
pd.merge(left, right, how='left', on='key')
```

Out[46]:

|      | A    | B    | key  | C    | D    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | K0   | C0   | D0   |
| 1    | A1   | B1   | K4   | NaN  | NaN  |
| 2    | A2   | B2   | K2   | C2   | D2   |
| 3    | A3   | B3   | K3   | C3   | D3   |

In [47]:

```
pd.merge(left, right, how='right', on='key')
```

Out[47]:

|      | A    | B    | key  | C    | D    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | K0   | C0   | D0   |
| 1    | A2   | B2   | K2   | C2   | D2   |
| 2    | A3   | B3   | K3   | C3   | D3   |
| 3    | NaN  | NaN  | K1   | C1   | D1   |

In [48]:

```
pd.merge(left, right, how='outer', on='key')
```

Out[48]:

|      | A    | B    | key  | C    | D    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | K0   | C0   | D0   |
| 1    | A1   | B1   | K4   | NaN  | NaN  |
| 2    | A2   | B2   | K2   | C2   | D2   |
| 3    | A3   | B3   | K3   | C3   | D3   |
| 4    | NaN  | NaN  | K1   | C1   | D1   |

In [49]:

```
pd.merge(left, right, how='inner', on='key')
```

Out[49]:

|      | A    | B    | key  | C    | D    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | A0   | B0   | K0   | C0   | D0   |
| 1    | A2   | B2   | K2   | C2   | D2   |
| 2    | A3   | B3   | K3   | C3   | D3   |