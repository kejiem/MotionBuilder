# -*- coding: utf-8 -*-

from pyfbsdk import*
from pyfbsdk_additions import*

#デフォルトでロードされるツール群を除外
expFilter = {"Python Tool Manager", "Batch Tool (scripted)", "Character Selection/Key Controls", "FBX Export"}

#Regionの名前は検索できない。前もって決定しておく。
for obj in FBSystem().Scene.Components:
    if obj.ClassName() == "FBTool":
        if not obj.Name in expFilter:
            print "----------------------------------------------------"
            print obj.Name
            print obj
            print obj.GetControl("content")                                 #コントロールが存在しないと　None を返す
            print obj.GetControl("content").Content                         #コントロールが存在しないと　None を返す
            print obj.GetControl("content").Content.GetControl("items")     #コントロールが存在しないと　None を返す
#            obj.GetControl("content").Content.GetControl("items").RemoveAll()  #内容を全削除したりできる
