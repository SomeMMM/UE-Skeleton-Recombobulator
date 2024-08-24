*The following Python Statement examples will need to be edited depending on your UE Python folder settings.
*My python location was in UE settings @ ../UnrealProjects/Python/Skeleton1.py

SETUP:
1. Enable Plugins:
	Edit > Plugins
		Python Editor Script Plugin
		Skeletal Mesh Editor
	
2. Add Python Startup Scripts:
	Edit > Project Settings > Python > Startup Scripts
		"from importlib import reload"
		"import Skeleton1 as skel"

3. Set Python Path:
	Edit > Project Settings > Python > Additional Paths	../../../../../../Users/Some/Documents/Unreal Projects/python

METHODS:

deleteBones(skeletalMeshNames, boneNames, loneBoneNames) #Delete bones function, remove comments at beginning & end to automate loading settings & LOD regeneration.
	read attached file "bone deletion order.txt" for specifics.
		*lone bones are bones that, when deleted, will leave behind vertecies with no weight. This causes UE to normalize them (1,1,1) to the Root bone.
		*lone bones have their vertex skin weights copied to the closest parent bone not being deleted.

deleteLODs(skeletalMeshNames, LODs) #deletes LODs on the skeletal mesh names. LODs positional is count, not index.
	"skel.deleteLODs("f_med_nrw_body", [1, 2, 3, 4])"	
		
regenerateLODs(skeletalMeshNames, LODs) #regenerates LODs on the skeletal mesh names. LODs positional is count, not index.
	"skel.regenerateLODs("f_med_nrw_body", [1, 2, 3, 4])"
	
flushLODs(skeletalMeshNames, LODs) #deletes & regenerates LODs on the skeletal mesh names. LODs positional is count, not index.
	"skel.flushLODs("f_med_nrw_body", [1, 2, 3, 4])"
	
saveLODSettings() #saves selected LOD Data Asset into .txt file.
	"skel.saveLODSettings()"
	
loadLODSettings() #loads .txt file into selected LOD Data Asset. May trigger forced LOD regeneration.
	"skel.loadLODSettings()"
	
loadLODSettingsListOnly() #loads .txt file into selected LOD Data Asset. Only the bone list & bones to prioritize to avoid forced LOD regeneration.
	"skel.loadLODSettingsListOnly()"	
