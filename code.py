import os,json,zipfile

def read_zip_file(filepath):
    zfile = zipfile.ZipFile(filepath)
    if os.path.exists("output"):
        pass
    else:
        os.mkdir("output") # creates the output directory
    for index,finfo in enumerate(zfile.infolist()):

        txt = read_json(json.load(zfile.open(finfo)))

        if txt is not None:
            f=open("output/outfile"+str(index+1)+".txt","w")
            f.write(json.dumps(txt,sort_keys=True,indent=4,separators=(",",":"))+"\n")
            f.close()

        else:
            print("File "+str(index+1)+" doesn't have BGP data")


def read_json(data):

    dict_tree=json.loads(json.dumps(data))["featureConfigs"]["features"]

    for k in range(len(dict_tree)):
        for i in dict_tree[k]:
            if i=="bgp":
                return dict_tree[k][i]


read_zip_file("nsx-1.zip")
