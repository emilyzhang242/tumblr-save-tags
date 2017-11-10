import sys
import os
import shutil

from selenium import webdriver # pip install selenium

driver = webdriver.Firefox()
blog_name = sys.argv[1]
tag_name = sys.argv[2]
total_pages = int(sys.argv[3])+1

def main():
    folder_name = parse_name(tag_name)
    url = "http://"+blog_name+".tumblr.com/tagged/"+tag_name
    
    create_folders(folder_name)
    #write the rest 
    for count in range(1,total_pages):
        page_url = generate_url(url, count)
        file_name = folder_name+str(count)
        create_and_write_to_file(page_url, file_name, folder_name)
    driver.quit()

def create_folders(folder_name):
    #if base folder doesn't exist, create it  
    if not os.path.isdir(blog_name):
        os.mkdir(blog_name)
        
    #now create the actual tag folder
    tag_folder = blog_name+"/"+folder_name
    if not os.path.isdir(tag_folder):
        os.mkdir(tag_folder)
    else:
        shutil.rmtree(tag_folder)
        os.mkdir(tag_folder)

def create_and_write_to_file(url, file_name, folder_name):
    full_file_name = blog_name+"/"+folder_name+"/"+file_name+".html"
    html = get_url_contents(url).encode('utf-8')  
    with open(full_file_name, 'w') as f:
        f.write(html)

def generate_url(base_url, page_num):
    return base_url+"/page/"+str(page_num)

def get_url_contents(url):
    # use firefox to get page with javascript generated content
    driver.get(url)
    driver.implicitly_wait(5)
    html = driver.page_source
    return html
    
def parse_name(tag_name):
    return tag_name.replace("+", "")

if  __name__ =='__main__':
    main()