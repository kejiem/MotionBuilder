# -*- coding: utf-8 -*-

import sys
libPath = "PATH"  #your module.py file's directory path
if not libPath in sys.path : sys.path.append(libPath)
import testmod
reload(testmod)
import testmod

testmod.testclass()

testmod.testclass().testmethod()
