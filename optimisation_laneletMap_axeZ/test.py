import xml.dom.minidom as xmldom


def parse_xml(fn):
    xml_file = xmldom.parse(fn)
    eles = xml_file.documentElement
    print(eles.tagName)
    xmin = eles.getElementsByTagName("xmin")[0].firstChild.data
    xmax = eles.getElementsByTagName("xmax")[0].firstChild.data
    ymin = eles.getElementsByTagName("ymin")[0].firstChild.data
    ymax = eles.getElementsByTagName("ymax")[0].firstChild.data
    print(xmin, xmax, ymin, ymax)
    return xmin, xmax, ymin, ymax


def test_parse_xml():
    parse_xml('loiv3.xml')


if __name__ == "__main__":
    test_parse_xml()
    


# -----------------------------------------------------------------------------
# ======================================================================================
 
import xml.etree.ElementTree as xee
 
def osmProcess():
    # 读取文件
    domTree = xee.parse("osm.osm")
 
    # 获得所有节点的内容
    root = domTree.getroot()
 
    # 获得所选区域的经纬度范围
    bound = root.findall("bounds")
    maxLat = float(bound[0].get("maxlat"))
    maxLon = float(bound[0].get("maxlon"))
    minLat = float(bound[0].get("minlat"))
    minLon = float(bound[0].get("minlon"))
    # 输出所选区域的经纬度范围
    print('Bounds:' + '\n' + 'minLat: ' + str(minLat) + '\n' + 'maxLat: ' + str(maxLat) + '\n' + 
    'minLon: ' + str(minLon) + '\n' + 'maxLon: ' + str(maxLon) + '\n' +'Nodes: ')
 
    # 存储不在所选区域内的node ID
    IDlist = []
 
    # 逐个检查node
    nodes = root.findall("node")
    for node in nodes:
        # 当前节点的经纬度和ID
        Lat = float(node.get("lat"))
        Lon = float(node.get("lon"))
        ID = node.get("id")
        #输出node信息
        print('nodeID:' + ID + ', Lat:' + str(Lat) + ', Lon:' + str(Lon) + ', Bound: ' , end='')
        # 判断
        if Lat < minLat or Lat > maxLat or Lon < minLon or Lon > maxLon:
            root.remove(node)
            IDlist.append(ID)
            #输出bound比对情况，若Lat和Lon均不符合则只输出Lat
            if Lat < minLat:
                print('Lat < min')
            elif Lat > maxLat:
                print('Lat > max')
            elif Lon < minLon:
                print('Lon < min')
            elif Lon > maxLon:
                print('Lon > max')
        else:
            print('Satisfied')
 
    # 删除不在所选区域内的node在后续道路的参照行
    ways = root.findall("way")
    for ID in IDlist:
        for way in ways:
            refnodes = way.findall("nd")
            for node in refnodes:
                if node.get("ref") == ID:
                    way.remove(node)
 
    # 输出文件
    domTree.write("out.osm",encoding="utf8")
 
if __name__=="__main__":
    osmProcess()