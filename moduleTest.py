# -*- coding: utf-8 -*- 
from pyfbsdk_additions import *
from pyfbsdk import *

exception = ["FBAnimationLayer"]

def IntoList(obj):
    returnVal = []
    if "list" in str(type(obj)):
        returnVal = obj
    else:
        returnVal.append(obj)
    return returnVal

class PrintList:
    def __init__(self, obj, flag):
        objList = IntoList(obj)
        for obj in objList:
            if flag == "Class": print obj.ClassName()
            if flag == "Name": print obj.Name
            if flag == "LongName": print obj.LongName
            if flag == None: print obj

#選択関連
class Selection:
    selList = []
    #Selectedフラグが立っているコンポーネントを全て取得
    #以降のメソッドではself.selListからオブジェクトを取得する
    def __init__(self):
        for obj in FBSystem().Scene.Components:
            if obj.Selected == True:
                self.selList.append(obj)
    #フィルタリングしたコンポーネントを除外
    def Get(self):
        returnVal = []
        returnVal = selList
        return returnVal
    def Filtered(self):
        returnVal = []
        for obj in self.selList:
            if not obj.ClassName() in exception:
                returnVal.append(obj)
        return returnVal
    #選択を全解除
    def Clear(self):
        for obj in self.selList:
            if obj.Selected:
                obj.Selected = False
    #指定したオブジェクトだけを選択
    def Change(self, obj):
        objList = IntoList(obj)
        Selection().Clear()
        for o in FBSystem().Scene.Components:
            if o in objList:
                o.Selected = True
    #LongNameで検索してオブジェクトを取得＆選択
    def ByLongName(self, name, isSelect):
        if "str" in str(type(name)):
            for obj in FBSystem().Scene.Components:
                if obj.LongName == name:
                    break
            if obj.LongName == name and isSelect: 
                Selection().Clear()
                obj.Selected = True
            elif obj.LongName != name:
                obj = None
            return obj
