# -*- coding: utf-8 -*
from pyfbsdk_additions import *
from pyfbsdk import *

#Create a null for constrained
nullConsed = FBModelNull("nullConstrained")
nullConsed.SetVector( FBVector3d( 0, 0, 0 ), FBModelTransformationType.kModelTranslation, True)
nullConsed.Show = True

#Create a null for rotation source
nullMain = FBModelNull("nullMain")
nullMain.Selected = True

#Create a null for aim
nullAimAt = FBModelNull("nullAimAt")
nullAimAt.SetVector( FBVector3d( 0, 0, 10 ), FBModelTransformationType.kModelTranslation, True)
nullAimAt.Parent = nullMain

#Create a null for up vector
nullUpVec = FBModelNull("nullUpVec")
nullUpVec.SetVector( FBVector3d( 0, 10, 0 ), FBModelTransformationType.kModelTranslation, True)
nullUpVec.Parent = nullMain

#Create a contraint
CM = FBConstraintManager()
cons = CM.TypeCreateConstraint("Aim")
cons.ReferenceAdd(0,nullConsed)
cons.ReferenceAdd(1,nullAimAt)
cons.ReferenceAdd(2,nullUpVec)
cons.Active = True

#Check PropertyList
for prp in cons.PropertyList:
    print prp.Name
print "---"
#see each property
print cons.PropertyList.Find("WorldUpType").Data
print cons.PropertyList.Find("AimVector").Data
print cons.PropertyList.Find("UpVector").Data

#use each property
cons.PropertyList.Find("WorldUpType").Data = 1
cons.PropertyList.Find("AimVector").Data = FBVector3d(1, 0, 0)
cons.PropertyList.Find("UpVector").Data = FBVector3d(0, 1, 0)
