import os
import shutil

if not os.path.isdir('./ItemsAdder'):
    os.mkdir('./ItemsAdder') 
    os.mkdir('./ItemsAdder/contents') 
    print("Please put the ItemsAdder folder in the same directory as this file.")
    exit()
if os.path.exists("./Output"):
    shutil.rmtree('./Output')

itemadder = './ItemsAdder/contents'
for get_namespace in os.listdir(itemadder):
    print(get_namespace)
    if not os.path.exists("./Output"):
        os.mkdir('./Output') 
    if not os.path.exists("./Output/ItemsAdder"):
        os.mkdir('./Output/ItemsAdder') 
    if not os.path.exists("./Output/ItemsAdder/data"):
        os.mkdir('./Output/ItemsAdder/data') 
        os.mkdir('./Output/ItemsAdder/data/resource_pack') 
        os.mkdir('./Output/ItemsAdder/data/items_packs') 
    # coopy rp
 
    shutil.copytree('./ItemsAdder/contents/'+get_namespace+'/configs','./Output/ItemsAdder/data/items_packs/'+get_namespace)
    shutil.copytree('./ItemsAdder/contents/'+get_namespace+'/resourcepack/assets','./Output/ItemsAdder/data/resource_pack/assets')
    
    print("convert "+get_namespace)    
