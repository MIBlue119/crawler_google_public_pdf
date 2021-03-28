'''
This script is for downloading the google public pdf  from this site: https://storage.googleapis.com/pub-tools-public-publication-data
Step to download the pdf files:
1. Download the xml from the url https://storage.googleapis.com/pub-tools-public-publication-data
2. Parse the url and extract the parts about pdf 
3. Download the pdf files 
'''

# 0. Config the path and url 
xml_path = "pub-tools-public-publication-data.xml"
google_pub_tools_url  = "https://storage.googleapis.com/pub-tools-public-publication-data"
download_pdf_dir_path = "./download_pdf"




# 1. Download the xml from the url https://storage.googleapis.com/pub-tools-public-publication-data 
import urllib
import os 

def download_xml(src_url, xml_path_to_saved):
    urllib.request.urlretrieve(src_url,xml_path_to_saved)


is_xml_Exists = os.path.exists(xml_path)
if not is_xml_Exists:
    # Download the xml about pub-tools-public-publication-data
    print("Download the xml about pub-tools-public-publication-data")
    download_xml(google_pub_tools_url , xml_path)
else:
    # Imply the xml exists
    print ("pub-tools-public-publication-data.xml: already exists")



# 2. Parse the url and extract the parts about pdf
import xml.etree.ElementTree as ET

def parse_xml_extract_pdf_info(xml_path):
    
    pdf_list = []
    tree = ET.parse(xml_path)
    root = tree.getroot()
    print("Start parse.")
    
    
    for content in root.findall('{http://doc.s3.amazonaws.com/2006-03-01}Contents'):
        key = content.find('{http://doc.s3.amazonaws.com/2006-03-01}Key')
        last_modified = content.find('{http://doc.s3.amazonaws.com/2006-03-01}LastModified')
        pdf_dict = {}
        if 'pdf/' in key.text:
           pdf_dict['pdf_name']= key.text                  # Extract the pdf_name, ex: "pdf/00b43d8596ac0da1d78089ebb57c8b244f60926e.pdf"
           pdf_dict['pdf_time']= last_modified.text[0:10]  # Extract the edited time of the pdf, ex: "2018-09-03"
           pdf_list.append(pdf_dict) 
        
    return pdf_list



pdf_list_from_xml = parse_xml_extract_pdf_info(xml_path)
print(pdf_list_from_xml[0:3]) #print three element to check 


# 3. Download the pdf files 

def mkdir(path):
    import os
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符號
    path=path.rstrip("\\")
 
    # 判斷路徑是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判斷結果
    if not isExists:
        # 如果不存在則建立目錄
        print("path")
        # 建立目錄操作函式
        os.makedirs(path)
        return True
    else:
        # 如果目錄存在則不建立，並提示目錄已存在
        print ("目錄已存在")
        return False



def download_pdf_file(saved_dir ,file_name, download_url): 
    import urllib
    import os 
    saved_path = os.path.join(saved_dir,file_name + ".pdf" )
    urllib.request.urlretrieve(download_url,saved_path)
    print("Download file {file_name} Completed.".format(file_name = file_name)) 

# Construct the directory to save the result
mkdir(download_pdf_dir_path)

# Start to download the pdf  
saved_dir = download_pdf_dir_path

for ele in pdf_list_from_xml:
    if ele['pdf_name'] !='pdf/':
        url_param = ele['pdf_name'].split('.pdf')[0].split('pdf/')[1]
        name_of_pdf=ele['pdf_time']+'_'+url_param
        print(name_of_pdf)
        download_url = "https://storage.googleapis.com/pub-tools-public-publication-data"+'/pdf/'+url_param+'.pdf'
        download_pdf_file(saved_dir,name_of_pdf,download_url)