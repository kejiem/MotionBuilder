# -*- coding: utf-8 -*
import os
import traceback

print os.path.normpath(traceback.extract_stack()[-1][0])
