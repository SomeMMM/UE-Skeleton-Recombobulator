import unreal
from importlib import reload    

#thank you.

#this script can_________
#delete skel mesh bones
#regenerate skeletal mesh lods
#save/load skel mesh LOD settings

#please read the readme.txt for instructions on how to setup & use this script.
#message Some_7 on discord if you need help.

def listAssetPaths():

	EAL = unreal.EditorAssetLibrary
	
	assetPaths = EAL.list_assets('/Game')
	
	for assetPath in assetPaths: print (assetPath)
    
def getSelectionContentBrowser(): #working

    EUL = unreal.EditorUtilityLibrary
    
    selectedAssets = EUL.get_selected_assets()
    
    for selectedAsset in selectedAssets: 
        return (selectedAssets)
    
def getAllActors():

    EAS = unreal.EditorActorSubsystem()
    
    actors = EAS.get_all_level_actors()
    
    for actor in actors: print (actor)
    
def getSelectedActors():

    EAS = unreal.EditorActorSubsystem()
    
    selectedActors = EAS.get_selected_level_actors()
    
    for selectedActor in selectedActors: print (selectedActor)
    
def getAssetNames(classType): #returns all asset names in /game/ of class type in positional

    EAL = unreal.EditorAssetLibrary
    assetPaths = EAL.list_assets('/Game')
    
    assets = []
    
    for assetPath in assetPaths:
        assetData = EAL.find_asset_data(assetPath)
        assetClass = assetData.asset_class_path.asset_name
        if assetClass == classType:
            assets.append(assetData.get_asset())
            
    for asset in assets: print (asset)
    return assets 
        
def getAssetClass(assetName): #returns the class of the asset name in positional

    EAL = unreal.EditorAssetLibrary
    assetPaths = EAL.list_assets('/Game')
    
    assets = []
    
    for assetPath in assetPaths:
        assetData = EAL.find_asset_data(assetPath)
        assetString = assetData.asset_name
        if assetString == assetName:
            assets.append(assetData.asset_class_path.asset_name)
            
    for asset in assets: print (asset)
    return assets
    
def getAssetPath(assetName): #returns the class of the asset name in positional

    EAL = unreal.EditorAssetLibrary
    assetPaths = EAL.list_assets('/Game')
    
    assets = []
    
    for assetPath in assetPaths:
        assetData = EAL.find_asset_data(assetPath)
        assetString = assetData.asset_name
        if assetString == assetName:
            assets.append(assetData.package_name)
            
    return assets
    
def getSkeletonObject(assetName):

    EAL = unreal.EditorAssetLibrary
    
    assetPath = " ".join(str(x) for x in getAssetPath(assetName))
    skeletonObject = unreal.load_asset(assetPath)
    
    #print (skeletonObject)
    return skeletonObject
    
def getSkeletalMeshObject(assetName):

    EAL = unreal.EditorAssetLibrary
    
    assetPath = " ".join(str(x) for x in getAssetPath(assetName))
    skeletalMeshObject = unreal.load_asset(assetPath)
    
    #print (skeletalMeshObject)
    return skeletalMeshObject
    
def deleteBone(skeletalMeshName, boneName): #DEPRECIATED
    
    SKLMOD = unreal.SkeletonModifier() #stores in skeleton modifier class into a variable
    skeletalMesh = (getSkeletalMeshObject(skeletalMeshName)) #gets the object of the skeletal mesh name from positional
    
    SKLMOD.set_skeletal_mesh(skeletalMesh) #select the skeletal mesh used by the skeleton modifier
    
    print ("Attempting SkeletonModifier.remove_bone on " + boneName)
    SKLMOD.remove_bone(boneName, False) #deletes the bone in positional
    
    print ("Attempting SkeletonModifier.commit_skeleton_to_skeletal_mesh()")
    SKLMOD.commit_skeleton_to_skeletal_mesh() #saves the changes to the Skeletal Mesh
    
def metaGetOffendingBones(skeletalMeshName, bonesWeightedThreshold):#DEPRECIATED, returns list of bones and how many times they were involved in being weighted to a vertex along with more than x amount of bones total.
    #print ("Running: metaTestVertices on " + skeletalMeshName + ".")
    #print ("The following bones have offended the bones weighted per vertex threshold of >= " + str(bonesWeightedThreshold) + " ammount of times:")
    
    boneIdOffendCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
    skeletalMesh = (getSkeletalMeshObject(skeletalMeshName)) #gets the object of the skeletal mesh name from positional
    SKIN_WT_MOD = unreal.SkinWeightModifier() #instance bone weight modifier
    SKIN_WT_MOD.set_skeletal_mesh(skeletalMesh) #set the skeletal mesh to be focused on
    
    vertexCount = SKIN_WT_MOD.get_num_vertices()
    boneNamesArray = SKIN_WT_MOD.get_all_bone_names() # "root"
    
    loopCountB = 0
    for _ in range(vertexCount):
        vertexWeightMap = SKIN_WT_MOD.get_vertex_weights(loopCountB)        #use loop count instead of vertex count because vertex count starts at 1 and we will always miss a vertex in the loop
        vertexWeightTupleList = [(k, v) for k, v in vertexWeightMap.items()]
        boneOffenderNameList = [] #empty the bone offender list before checking how many bones weighted to vertex
        loopCountB += 1
        loopCountC = 0
        for vertexWeight in vertexWeightTupleList: #loop per bone in weight map
            boneWeight = ((vertexWeightTupleList[loopCountC])[1]) #get bone weight of current weighted bone in question
            boneName = ((vertexWeightTupleList[loopCountC])[0])
            boneOffenderNameList.append(boneName) 
            loopCountC += 1
        if loopCountC >= bonesWeightedThreshold: #if the vertex has specified number of bones weighted to it
            for boneOffenderName in boneOffenderNameList: #for every bone currently weighted to vertex above # of bones weighted threshold
                boneId = boneNamesArray.index(str(boneOffenderName))
                boneIdOffendCountList[boneId] += 1 #increment the number of times the bone is involved in specified number of weighted bones per vertex threshold in bone index list
                
    masterBoneOffenderList = [] #make a list of tuples to be filled with findings of bone weight offense counting
    for bone in boneNamesArray: #loop through every bone in the skeleton, they will return in order of id starting with 0 for root
        boneNameIndex = (boneNamesArray.index(bone))
        masterBoneOffenderList.append((bone, boneIdOffendCountList[boneNameIndex])) #add each bones count of bone weight offenses to the list of tuples
             
        #sorts and prints list of bone offenders with count of offenses over the threshold
    masterBoneOffenderList.sort(key = lambda x:x[1], reverse = True) # sort the list of tuples by number of bone offese occurences
    outputList = []
    for sortedOffender in masterBoneOffenderList: #prevents printing un-deletable bones from offender list
        if not str(sortedOffender[0]) in "root, pelvis, spine_01, spine_02, spine_03, spine_04, spine_05, clavicle_l, upperarm_l, lowerarm_l, hand_l, index_metacarpal_l, index_01_l, index_02_l, index_03_l, pinky_metacarpal_l, pinky_01_l, pinky_02_l, pinky_03_l, ring_metacarpal_l, ring_01_l, ring_02_l, ring_03_l, index_01_r, index_02_r, index_03_r, pinky_metacarpal_r, pinky_01_r, pinky_02_r, pinky_03_r, ring_metacarpal_r, ring_01_r, ring_02_r, ring_03_r, middle_metacarpal_l, middle_01_l, middle_02_l, middle_03_l, thumb_01_l, thumb_02_l, thumb_03_l, clavicle_r, upperarm_r, lowerarm_r, hand_r, middle_metacarpal_r, middle_01_r, middle_02_r, middle_03_r, thumb_01_r, thumb_02_r, thumb_03_r, neck_01, neck_02, head, thigh_l, calf_l, foot_l, ball_l, thigh_r, calf_r, foot_r, ball_r":
            if not sortedOffender[1] == 0: #if offenses do not equal zero
                outputList.append((sortedOffender[1], sortedOffender[0]))
    return (outputList)
                 
def optimizeV1(skeletalMeshName, bonesWeightedThreshold):#DEPRECIATED, unfinished, plans to include weight copying and enfore bones weighted per vertex thresholds extremely, see "deleteBones" above for completed idea
    print ("Running: optimizeV1 " + skeletalMeshName + "...")
    
    boneIdOffendCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
    skeletalMesh = (getSkeletalMeshObject(skeletalMeshName)) #gets the object of the skeletal mesh name from positional
    SKIN_WT_MOD = unreal.SkinWeightModifier() #instance bone weight modifier
    SKIN_WT_MOD.set_skeletal_mesh(skeletalMesh) #set the skeletal mesh to be focused on
    
    vertexCount = SKIN_WT_MOD.get_num_vertices()
    boneNamesArray = SKIN_WT_MOD.get_all_bone_names() # "root"
    
    loopCountB = 0
    for _ in range(vertexCount):
        vertexWeightMap = SKIN_WT_MOD.get_vertex_weights(loopCountB)        #use loop count instead of vertex count because vertex count starts at 1 and we will always miss a vertex in the loop
        vertexWeightTupleList = [(k, v) for k, v in vertexWeightMap.items()]
        boneOffenderNameList = [] #empty the bone offender list before checking how many bones weighted to vertex
        loopCountB += 1
        loopCountC = 0
        for vertexWeight in vertexWeightTupleList: #loop per bone in weight map
            boneWeight = ((vertexWeightTupleList[loopCountC])[1]) #get bone weight of current weighted bone in question
            boneName = ((vertexWeightTupleList[loopCountC])[0])
            boneOffenderNameList.append(boneName) 
            loopCountC += 1
        if loopCountC >= bonesWeightedThreshold: #if the vertex has specified number of bones weighted to it
            for boneOffenderName in boneOffenderNameList: #for every bone currently weighted to vertex above # of bones weighted threshold
                boneId = boneNamesArray.index(str(boneOffenderName))
                boneIdOffendCountList[boneId] += 1
            #find lowest weighted bone
            #remove from weight influence or add weight to parent? or most weighted bone?
            #commit changes
    SKIN_WT_MOD.prune_all_weights(.05)
    SKIN_WT_MOD.commit_weights_to_skeletal_mesh()#----------------------# REAL SCRIPTS BELOW: #---------------------------------#    

#Real Scripts Below
    
def deleteBones(skeletalMeshNames, boneNames, loneBoneNames): #Delete bones function, remove comments at beginning & end to automate loading settings & LOD regeneration.

    #deleteLODs(skeletalMeshNames, LODs) #deletes LODs before modifying skin weights.

    SKLMOD = unreal.SkeletonModifier() #instances skeleton modifier class
    SKIN_WT_MOD = unreal.SkinWeightModifier() #instance bone weight modifier
    skeletalMeshList = skeletalMeshNames.split() #puts inputted meshes into list
    boneNameList = boneNames.split() #puts inputted bones into list
    loneBoneNameList = loneBoneNames.split() #puts inputted lone bones into list
    
    for skeletalMesh in skeletalMeshList: #loop skeleteal meshes > all
        print ("Modifying skeletal mesh: " + skeletalMesh)
        skeletalMeshObject = (getSkeletalMeshObject(skeletalMesh))  #pulls mesh from list & gets object
        SKIN_WT_MOD.set_skeletal_mesh(skeletalMeshObject) #load skeletal mesh
        vertexCount = SKIN_WT_MOD.get_num_vertices() #save vertex count
        print ("Number of vertices: " + str(vertexCount))
        loneVertexTupleList = []
        vertexCountLoop = 0
        
        for _ in range(vertexCount): #loop vertices > edit weights
            vertexWeightsMap = SKIN_WT_MOD.get_vertex_weights(vertexCountLoop) #vertex bone weights data > current vertex
            vertexWeightsTupleList = [(k, v) for k, v in vertexWeightsMap.items()] #organize data > current vertex > vertex bone weights
            weightedBoneCount = 0
            for vertexWeightsTuple in vertexWeightsTupleList: #loop weighted bones > current vertex
                boneWeight = (vertexWeightsTuple[1]) #bone weight > current weighted bone > current vertex
                weightedBoneName = (vertexWeightsTuple[0]) #bone name > current weighted bone > current vertex
                if weightedBoneName in loneBoneNameList: #if weighted bone = lone bone
                    loneVertexTupleList.append((vertexCountLoop, weightedBoneName, boneWeight)) #add data to list of tuples > ((vertex1, bone1, weight1), (vertex2, bone2, weight2))
                    break
                weightedBoneCount += 1
            vertexCountLoop += 1
        SKIN_WT_MOD.commit_weights_to_skeletal_mesh() #save skeletal mesh
        
        SKLMOD.set_skeletal_mesh(skeletalMeshObject) #load skeletal mesh
        loop1Index = 0
        print ("Finding lone bone vertex weights' nearest valid parent bone")
        for loneVertexTuple in loneVertexTupleList: #loop lone vertices > get target parent
            parentBoneName = SKLMOD.get_parent_name(loneVertexTuple[1]) #save parent bone of weighted bone
            while parentBoneName in loneBoneNameList or parentBoneName in boneNameList: #if parent bone is planned to be deleted
                parentBoneName = SKLMOD.get_parent_name(parentBoneName) #update parent bone of weighted bone
            loneVertexTupleList[loop1Index] = ((loneVertexTupleList[loop1Index])[0], parentBoneName, (loneVertexTupleList[loop1Index])[2]) #change bone name in tuple list of lone vertices 
            loop1Index += 1
        SKLMOD.commit_skeleton_to_skeletal_mesh() #save skeletal mesh mod
        
        SKIN_WT_MOD.set_skeletal_mesh(skeletalMeshObject) #load skeletal mesh
        loop2Index = 0
        print ("Replacing lone bone vertex weights with nearest valid parent bone")
        for loneVertexTuple in loneVertexTupleList: #loop lone vertices > replace lone bone
            weightDict = SKIN_WT_MOD.get_vertex_weights(loneVertexTuple[0]) #get bone:weight dict > current vertex
            weightDict.clear() #REDUNDANT? 
            weightDict.update({loneVertexTuple[1] : loneVertexTuple[2]}) #add parent bone
            SKIN_WT_MOD.set_vertex_weights(loneVertexTuple[0], weightDict, False) #replace bone:weight dict > current vertex
            loop2Index += 1
        SKIN_WT_MOD.commit_weights_to_skeletal_mesh() #save skeletal mesh
            
        for boneName in boneNameList: #loop bones > delete bones
            print ("Removing bone: " + boneName + " from: " + skeletalMesh)
            SKLMOD.set_skeletal_mesh(skeletalMeshObject) #load skeletal mesh
            SKLMOD.remove_bone(boneName, False) #delete bone
            SKLMOD.commit_skeleton_to_skeletal_mesh() #save skeletal mesh
            
        print ("Normalizing vertex weights for " + skeletalMesh)
        SKIN_WT_MOD.set_skeletal_mesh(skeletalMeshObject) #load skeletal mesh
        SKIN_WT_MOD.normalize_all_weights() #normalizes vertex bone weights
        SKIN_WT_MOD.commit_weights_to_skeletal_mesh() #save skeletal mesh
        #loadLODSettings()#updates LOD file with preferred settings
        #generateLODs(skeletalMeshNames, LODs) #deletes LODs before modifying skin weights.
        print ("Finished modifying skeletal mesh: " + skeletalMesh)
    
def deleteLODs(skeletalMeshNames, LODs): #deletes LODs on the skeletal mesh names. LODs positional is count, not index.
    
    skeletalMeshList = skeletalMeshNames.split() #puts inputted meshes into list
    for skeletalMesh in skeletalMeshList:
        skeletalMeshObject = (getSkeletalMeshObject(skeletalMesh))
        print ("Removing LOD " + str(LODs) + " : " + skeletalMesh)
        skeletalMeshObject.remove_lo_ds(LODs) #remove select LODs

def regenerateLODs(skeletalMeshNames, LODs): #regenerates LODs on the skeletal mesh names. LODs positional is count, not index.
    
    skeletalMeshList = skeletalMeshNames.split() #puts inputted meshes into list
    for skeletalMesh in skeletalMeshList:
        skeletalMeshObject = (getSkeletalMeshObject(skeletalMesh))
        print ("Regenerating LOD " + str(LODs) + " in: " + skeletalMesh)
        skeletalMeshObject.regenerate_lod(len(LODs)) #regenerates LODs

def flushLODs(skeletalMeshNames, LODs): #deletes & regenerates LODs on the skeletal mesh names. LODs positional is count, not index.

    skeletalMeshList = skeletalMeshNames.split() #puts inputted meshes into list
    for skeletalMesh in skeletalMeshList:
        skeletalMeshObject = (getSkeletalMeshObject(skeletalMesh))
        print ("Regenerating LOD " + str(LODs) + " in: " + skeletalMesh)
        skeletalMeshObject.remove_lo_ds(LODs)#remove select LODs
        skeletalMeshObject.regenerate_lod(len(LODs)) #regenerates LODs
        
def saveLODSettings(): #saves selected LOD Data Asset into .txt file
    
    selectLODs = getSelectionContentBrowser() #select LOD data asset in browser
    
    for selectLOD in selectLODs:
        with open(r"C:\Users/Some/Documents/Unreal Projects/python\LODsettings.txt", "w") as txt:
            propertyArray1 = selectLOD.get_editor_property("lod_groups")
            propertyLoop = 0
            for property in propertyArray1:
                boneListArray = property.get_editor_property("bone_list") #unreal.BoneFilter
                txt.write("Bone list " + str(propertyLoop) +" =\n")
                for boneFilter in boneListArray: #for all LOD groups
                    if not "None" in (str(boneFilter.get_editor_property("bone_name"))):
                        txt.write(str(boneFilter.get_editor_property("bone_name")) + "\n") #save list of bones
                bonePrioArray = property.get_editor_property("bones_to_prioritize")
                txt.write("Prio list =\n")
                for bonePrio in bonePrioArray:
                    txt.write(str(bonePrio) + "\n") #save  prio bones
                reductSettings = property.get_editor_property("reduction_settings")
                txt.write("max_bones_per_vertex = \n")
                txt.write((str(reductSettings.get_editor_property("max_bones_per_vertex"))) + "\n")
                txt.write("max_num_of_verts = \n")
                txt.write((str(reductSettings.get_editor_property("max_num_of_verts"))) + "\n")
                txt.write("num_of_vert_percentage = \n")
                print
                txt.write((str(reductSettings.get_editor_property("num_of_vert_percentage"))) + "\n")
                propertyLoop += 1
            print ("LODsettings saved to file.\n")

def loadLODSettings(): #loads .txt file into selected LOD Data Asset. May trigger forced LOD regeneration.
    
    EAL = unreal.EditorAssetLibrary
    selectLODs = getSelectionContentBrowser() #select LOD data asset in browser
    for selectLOD in selectLODs:
        LODGroupSettingsArray = selectLOD.get_editor_property("lod_groups")
        copyLODGroupSettingsArray = selectLOD.get_editor_property("lod_groups")
        with open(r"C:\Users/Some/Documents/Unreal Projects/python\LODsettings.txt") as txt:
            lines = txt.readlines()
            boneListArray = []
            prioListArray = []
            maxBonesArray = []
            maxVertsArray = []
            percentVArray = []
            boneListBool = False
            prioListBool = False
            maxBonesBool = False
            maxVertsBool = False
            percentVBool = False
            boneList = []
            prioList = []
            maxBones = 8
            maxVerts = 1.0
            percentV = 1.0
            for line in lines:
                if percentVBool and "Bone list" not in line:
                    percentV = float(line)
                if "num_of_vert_percentage" in line:
                    maxVertsBool = False
                    maxVertsArray.append(maxVerts)
                    maxVerts = int(30000)
                    percentVBool = True
                if maxVertsBool:
                    maxVerts = int(line)
                if "max_num_of_verts" in line:
                    maxBonesBool = False
                    maxBonesArray.append(maxBones)
                    maxBones = int(8)
                    maxVertsBool = True
                if maxBonesBool:
                    maxBones = int(line)
                if "max_bones_per_vertex" in line:
                    prioListBool = False
                    prioListArray.append(prioList)
                    prioList = []
                    maxBonesBool = True
                if prioListBool:
                    prioList.append(line.rstrip("\n"))
                if "Prio list" in line:
                    boneListBool = False
                    boneListArray.append(boneList)
                    boneList = []
                    prioListBool = True
                if boneListBool:
                    boneList.append(line.rstrip("\n"))
                if "Bone list" in line:
                    percentVBool = False
                    if "0" not in line:
                        percentVArray.append(percentV)
                    percentV = 1.0
                    boneListBool = True
            percentVArray.append(percentV)
            LODCount = len(boneListArray)
            copyLODGroupSettingsArray.resize(LODCount) #Cap LOD
            for count in range(LODCount): #Loop LOD
                copyLODGroupSettings = LODGroupSettingsArray[count]
                copyBoneFilter = unreal.BoneFilter() #blank unreal.BoneFilter
                copyFilterArray = copyLODGroupSettings.get_editor_property("bone_list")
                copyFilterArray.resize(0)
                copyPrioArray = copyLODGroupSettings.get_editor_property("bones_to_prioritize")
                copyPrioArray.resize(0)
                for boneNameOUT in boneListArray[count]: # names list, loop bone names
                    copyBoneFilter.set_editor_property("bone_name", boneNameOUT) #might need to cast to name type first
                    copyBoneFilter.set_editor_property("exclude_self", False) #required or the program will not recognize bone name as valid
                    copyFilterArray.append(copyBoneFilter) #1 Array of Bone Filters in
                copyLODGroupSettings.set_editor_property("bone_list", copyFilterArray)
                for prioNameOUT in prioListArray[count]:
                    copyPrioArray.append(prioNameOUT)
                copyLODGroupSettings.set_editor_property("bones_to_prioritize", copyPrioArray)
                copyOptimizeSettings = copyLODGroupSettings.get_editor_property("reduction_settings")
                copyTerminateCrit = copyOptimizeSettings.get_editor_property("termination_criterion") #unreal.SkeletalMeshTerminationCriterion()
                #copyOptimizeSettings.set_editor_property("termination_criterion", (copyTerminateCrit.SMTC_ABS_NUM_OF_VERTS)) #termination criteria settings, paste the ALL_CAPS words from https://docs.unrealengine.com/4.26/en-US/PythonAPI/class/SkeletalMeshTerminationCriterion.html
                copyOptimizeSettings.set_editor_property("termination_criterion", (copyTerminateCrit.SMTC_NUM_OF_VERTS)) #replace ^ this line, to use % of verts instead of # of verts for LOD settings.
                copyOptimizeSettings.set_editor_property("max_bones_per_vertex", maxBonesArray[count])
                maxVertsIn = maxVertsArray[count]
                percentVIn = percentVArray[count]
                copyOptimizeSettings.set_editor_property("num_of_vert_percentage", percentVIn)
                copyOptimizeSettings.set_editor_property("max_num_of_verts", maxVertsIn) #not going in at all
                copyLODGroupSettings.set_editor_property("reduction_settings", copyOptimizeSettings)
                copyLODGroupSettingsArray[count] = copyLODGroupSettings
        selectLOD.set_editor_property("lod_groups", copyLODGroupSettingsArray)
    print (str(LODCount) + " LOD settings loaded from file.\n")

def loadLODSettingsListOnly(): #loads .txt file into selected LOD Data Asset. Only the bone list & bones to prioritize to avoid forced LOD regeneration.
    
    EAL = unreal.EditorAssetLibrary
    selectLODs = getSelectionContentBrowser() #select LOD data asset in browser
    for selectLOD in selectLODs:
        LODGroupSettingsArray = selectLOD.get_editor_property("lod_groups")
        copyLODGroupSettingsArray = selectLOD.get_editor_property("lod_groups")
        with open(r"C:\Users/Some/Documents/Unreal Projects/python\LODsettings.txt") as txt:
            lines = txt.readlines()
            boneListArray = []
            prioListArray = []
            maxBonesArray = []
            maxVertsArray = []
            percentVArray = []
            boneListBool = False
            prioListBool = False
            maxBonesBool = False
            maxVertsBool = False
            percentVBool = False
            boneList = []
            prioList = []
            maxBones = 8
            maxVerts = 1.0
            percentV = 1.0
            for line in lines:
                if percentVBool and "Bone list" not in line:
                    percentV = float(line)
                if "num_of_vert_percentage" in line:
                    maxVertsBool = False
                    maxVertsArray.append(maxVerts)
                    maxVerts = int(30000)
                    percentVBool = True
                if maxVertsBool:
                    maxVerts = int(line)
                if "max_num_of_verts" in line:
                    maxBonesBool = False
                    maxBonesArray.append(maxBones)
                    maxBones = int(8)
                    maxVertsBool = True
                if maxBonesBool:
                    maxBones = int(line)
                if "max_bones_per_vertex" in line:
                    prioListBool = False
                    prioListArray.append(prioList)
                    prioList = []
                    maxBonesBool = True
                if prioListBool:
                    prioList.append(line.rstrip("\n"))
                if "Prio list" in line:
                    boneListBool = False
                    boneListArray.append(boneList)
                    boneList = []
                    prioListBool = True
                if boneListBool:
                    boneList.append(line.rstrip("\n"))
                if "Bone list" in line:
                    percentVBool = False
                    if "0" not in line:
                        percentVArray.append(percentV)
                    percentV = 1.0
                    boneListBool = True
            percentVArray.append(percentV)
            LODCount = len(boneListArray)
            copyLODGroupSettingsArray.resize(LODCount) #Cap LOD
            for count in range(LODCount): #Loop LOD
                copyLODGroupSettings = LODGroupSettingsArray[count]
                copyBoneFilter = unreal.BoneFilter() #blank unreal.BoneFilter
                copyFilterArray = copyLODGroupSettings.get_editor_property("bone_list")
                copyFilterArray.resize(0)
                copyPrioArray = copyLODGroupSettings.get_editor_property("bones_to_prioritize")
                copyPrioArray.resize(0)
                for boneNameOUT in boneListArray[count]: # names list, loop bone names
                    copyBoneFilter.set_editor_property("bone_name", boneNameOUT) #might need to cast to name type first
                    copyBoneFilter.set_editor_property("exclude_self", False) #required or the program will not recognize bone name as valid
                    copyFilterArray.append(copyBoneFilter) #1 Array of Bone Filters in
                for prioNameOUT in prioListArray[count]: #TOGGLE COMMENT - bone list going into prio list, change prioNameOUT to boneNameOUT
                    copyPrioArray.append(prioNameOUT)
                copyLODGroupSettings.set_editor_property("bone_list", copyFilterArray)
                copyLODGroupSettings.set_editor_property("bones_to_prioritize", copyPrioArray)
                copyLODGroupSettingsArray[count] = copyLODGroupSettings
        selectLOD.set_editor_property("lod_groups", copyLODGroupSettingsArray)
    print (str(LODCount) + " LOD settings loaded from file.\n")
