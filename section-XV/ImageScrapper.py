import bs4
import os
import requests

req = requests.get("https://en.wikipedia.org/wiki/Avatar:_The_Last_Airbender")
soup = bs4.BeautifulSoup(req.text, 'lxml')
path_downloads = "D://Computer Science//Courses//Udemy//jose portila-python//python programs//section-XV"

# if not os.path.exists(path_downloads):
#     os.chdir(path_downloads)
#     os.mkdir("dwn")

# img_goal = soup.select('.infobox-image .mw-file-element')[0]
# source = img_goal['src'] 
# print(type(img_goal)) # special element tag object -> <class 'bs4.element.Tag'>
# print(img_goal['src'])

# img_req = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Avatar_The_Last_Airbender_logo.svg/220px-Avatar_The_Last_Airbender_logo.svg.png")
# f = open("D://Computer Science//Courses//Udemy//jose portila-python//python programs//section-XV//dwn//avatar-logo.jpg", "wb")
# # write binary as img_req.content is in binary
# f.write(img_req.content)
# f.close()

def get_img(pathdir, pathimg, imgname):
    try:
        req_image = requests.get(pathimg)
        new_path = f"{pathdir}//{imgname}"
        f = open(new_path, "wb")
        f.write(req_image.content)
        f.close()
    except:
        print("something went wrong! ")
        
path_toC_downloads = "C://Users//RAVIRAJ//Downloads"
path_toWorldMap = "https://upload.wikimedia.org/wikipedia/en/thumb/3/39/Avatar_world_map.jpg/220px-Avatar_world_map.jpg"

get_img(pathdir=path_toC_downloads, pathimg=path_toWorldMap,imgname="world-map.jpg"  )