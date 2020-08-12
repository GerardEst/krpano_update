import os, shutil

# ✅ Borrar .html i .js
# ✅ Borrar carpeta skin
# ✅ Editar xml

def clean():
    pano_folders = [f.path for f in os.scandir('panos/') if f.is_dir()]
    for folder in pano_folders:

        pano_name = folder[6:]

        print ("Working on "+pano_name)
        print ("In folder: "+folder)

        deleteUnnecesary(folder,pano_name)
        deleteSkin(folder,pano_name)
        updateXml(folder,pano_name)

        print ("Done!")
        print (" ")

    print("{} panos were affected".format(len(pano_folders)))

#Borramos el js y el html viejos
def deleteUnnecesary(folder,name):
    print("- Removing unnecesary files (js,html)...")

    os.remove(folder+'/pano.js')
    os.remove(folder+'/'+name+'.html')

#Borramos skin
def deleteSkin(folder,name):
    print("- Removing skin folder...")

    shutil.rmtree(folder+'/skin')

#Quitar la version y display en el xml
def updateXml(folder,name):
    print("- Updating xml...")
    xml = open(folder+"/"+name+".xml", "rt")
    data = xml.read()
    data = data.replace('<include url="skin/flatskin.xml" />', '<include url="/panos/skin/flatskin.xml" />')
    xml.close()
    xml = open(folder+"/"+name+".xml", "wt")
    #overrite the input file with the resulting data
    xml.write(data)
    xml.close()


clean()