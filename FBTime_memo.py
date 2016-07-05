# -*- coding: utf-8 -*-
from pyfbsdk_additions import *
from pyfbsdk import *

#一秒をFBTimeで表示するとこういう感じ
print FBTime.OneSecond
#> FBTime(46186158000)

#スタートフレームの取得（0に設定して実施）
print FBSystem().CurrentTake.LocalTimeSpan.GetStart()
#> FBTime(0)

#ストップフレームの取得（50に設定して実施）
print FBSystem().CurrentTake.LocalTimeSpan.GetStop()
#> FBTime(92372316000)

#FBTimeとフレームの行き来
t = FBSystem().CurrentTake.LocalTimeSpan.GetStop()
print t
print t.GetFrame()
print FBTime( 0, 0, 0, t.GetFrame(), 0 )
#> FBTime(92372316000)
#> 50
#> FBTime(92372316000)

# t.GetFrame(True)
#という記述をしているサイトもあるが、私の環境ではエラーが出る。よくわからん。
## ---Error---
##Traceback (most recent call last):
##  File "C:/Users/user/Desktop/test.py", line 41, in <module>
##    t.GetFrame(True)
##Boost.Python.ArgumentError: Python argument types in
##    FBTime.GetFrame(FBTime, bool)
##did not match C++ signature:
##    GetFrame(class PYFBSDK::FBTime_Wrapper {lvalue})
##    GetFrame(class PYFBSDK::FBTime_Wrapper {lvalue}, enum ORSDK2015::FBTimeMode)

#タイムスパンの変更
FBSystem().CurrentTake.LocalTimeSpan = FBTimeSpan( FBTime(0, 0, 0, 10, 0), FBTime(0, 0, 0, 20, 0) )
#10fから20fの範囲に変更する
