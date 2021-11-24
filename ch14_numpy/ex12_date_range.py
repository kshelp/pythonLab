# 날짜 자동 생성: date_range
# pd.data_range(start_None, end=None, periods=None, feq='D')
import pandas as pd

print(pd.date_range(start='2019-01-01', end='2019-01-07'))
'''
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07'],
              dtype='datetime64[ns]', freq='D')
'''

print(pd.date_range(start='2019/01/01', end='2019.01.07'))
'''
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07'],
              dtype='datetime64[ns]', freq='D')
'''

print(pd.date_range(start='2019-01-01', periods=7))
'''
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07'],
              dtype='datetime64[ns]', freq='D')
'''

print(pd.date_range(start='2019-01-01', periods=4, freq='2D'))
'''
DatetimeIndex(['2019-01-01', '2019-01-03', '2019-01-05', '2019-01-07'], dtype='datetime64[ns]', freq='2D')
'''

print(pd.date_range(start='2019-01-01', periods=4, freq='W'))
'''
DatetimeIndex(['2019-01-06', '2019-01-13', '2019-01-20', '2019-01-27'], dtype='datetime64[ns]', freq='W-SUN')
'''

print(pd.date_range(start='2019-01-01', periods=12, freq='2BM'))
'''
DatetimeIndex(['2019-01-31', '2019-03-29', '2019-05-31', '2019-07-31',
               '2019-09-30', '2019-11-29', '2020-01-31', '2020-03-31',
               '2020-05-29', '2020-07-31', '2020-09-30', '2020-11-30'],
              dtype='datetime64[ns]', freq='2BM')
'''

print(pd.date_range(start='2019-01-01', periods=4, freq='QS'))
'''
DatetimeIndex(['2019-01-01', '2019-04-01', '2019-07-01', '2019-10-01'], dtype='datetime64[ns]', freq='QS-JAN')
'''

print(pd.date_range(start='2019-01-01', periods=3, freq='AS'))
'''
DatetimeIndex(['2019-01-01', '2020-01-01', '2021-01-01'], dtype='datetime64[ns]', freq='AS-JAN')
'''

print(pd.date_range(start='2019-01-01 08:00', periods=10, freq='H'))
'''
DatetimeIndex(['2019-01-01 08:00:00', '2019-01-01 09:00:00',
               '2019-01-01 10:00:00', '2019-01-01 11:00:00',
               '2019-01-01 12:00:00', '2019-01-01 13:00:00',
               '2019-01-01 14:00:00', '2019-01-01 15:00:00',
               '2019-01-01 16:00:00', '2019-01-01 17:00:00'],
'''

print(pd.date_range(start='2019-01-01 08:00', periods=4, freq='30min'))
'''
DatetimeIndex(['2019-01-01 08:00:00', '2019-01-01 08:30:00',
               '2019-01-01 09:00:00', '2019-01-01 09:30:00'],
              dtype='datetime64[ns]', freq='30T')
'''

print(pd.date_range(start='2019-01-01', periods=4, freq='D'))
'''
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04'], dtype='datetime64[ns]', freq='D')
'''