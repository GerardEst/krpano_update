import os
import shutil

# ✅ En el html, quitar el swf
# ✅ Borrar archivo js y poner el nuevo js
# ✅ Borrar el archivo swf
# ✅ En el xml, quitar la version y el display
# ✅ Hacer esto recursivamente para todas las carpetas en "panos"
# ✅ Informar de lo que ocurre en consola porque es mas guay

def convert():
    pano_folders = [f.path for f in os.scandir('panos/') if f.is_dir()]
    for folder in pano_folders:

        pano_name = folder[6:]

        print ("Working on "+pano_name)
        print ("In folder: "+folder)

        deleteOldStuff(folder,pano_name)
        newJs(folder)
        generateHtml(folder,pano_name)
        updateXml(folder,pano_name)

        print ("Done!")
        print (" ")

    print("{} panos were affected".format(len(pano_folders)))

#Borramos el swf, el js y el html viejos
def deleteOldStuff(folder,name):
    print("- Removing old files (swf,js,html)...")

    try:
        os.remove(folder+'/'+name+'.swf')
    except:
        print("! No swf file to delete !")

    try:
        os.remove(folder+'/'+name+'.js')
    except:
        print("! No js file to delete !")

    try:
        os.remove(folder+'/'+name+'.html')
    except:
        print("! No html file to delete !")

#Creamos el nuevo js copiando el modelo
def newJs(folder):
    print("- Copying new js file...")
    shutil.copyfile('pano.js', folder+'/pano.js') 

#Generamos el nuevo html con valores personalizados
def generateHtml(folder,name):
    print("- Generating new html...")
    f = open(folder+'/'+name+'.html','w')
    message = """<!DOCTYPE html>
    <html>
    <head>
        <title>{name}</title>
        <meta name="viewport" content="target-densitydpi=device-dpi, width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
        <style>
            html {{ height:100%; }}
            body {{ height:100%; overflow: hidden; margin:0; padding:0; font-family:Arial, Helvetica, sans-serif; font-size:16px; color:#FFFFFF; background-color:#000000; }}
            a{{ color:#AAAAAA; text-decoration:underline; }}
            a:hover{{ color:#FFFFFF; text-decoration:underline; }}
        </style>
    </head>
    <body>

    <script src="pano.js"></script>

    <div id="pano" style="width:100%; height:100%;">
        <noscript><table style="width:100%;height:100%;"><tr style="valign:middle;"><td><div style="text-align:center;">ERROR:<br/><br/>Javascript not activated<br/><br/></div></td></tr></table></noscript>
        <script>
            embedpano({{xml:'{name}.xml', target:"pano"}});
        </script>
    </div>

    </body>
    </html>"""
    f.write(message.format(name=name))
    f.close()

#Quitar la version y display en el xml
def updateXml(folder,name):
    print("- Updating xml...")
    xml = open(folder+"/"+name+".xml", "rt")
    data = xml.read()
    data = data.replace('<krpano version="1.0.8">', '<krpano>')
    data = data.replace('<display flash10="on" movequality="LOW" stillquality="HIGHSHARP" movequality10="HIGH" stillquality10="HIGH" />', '')
    xml.close()
    xml = open(folder+"/"+name+".xml", "wt")
    #overrite the input file with the resulting data
    xml.write(data)
    xml.close()


convert()