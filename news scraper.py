#!/usr/bin/env python
# coding: utf-8

# In[111]:

#This is the program designed to scrape the required information from the website

import  requests, os, bs4, openpyxl
os.chdir('/Users/daniellynch/Downloads/News Bias Files/Right')

url = "https://mediabiasfactcheck.com/right/"
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
table = soup.select_one('#mbfc-table')
get_links = table.find_all('a')
x = 0
for link in get_links:
    link = link.get("href")
    try:
        res = requests.get(link)
        if res.status_code == 404:
            print('404 for: ' + link)
        else:
            link_soup = bs4.BeautifulSoup(res.text, 'html.parser')
            print('Here is a link: ' + link)
            try:
                Biased = link_soup.find_all('p')
                #Only selects links in the relevant table
                title = link_soup.select_one('#mh-mobile > div.container.mh-mobile > div.wrapper.clearfix')
                organisation = title.find('h1')
                organisation = organisation.text
                #stops python thinking title is a directory
                if '/' in organisation:
                    print (organisation)
                    organisation = organisation.replace('/', " ")
            except AttributeError:
                print('dead link')
                continue
        for i in Biased:
            if 'Factual Reporting:'  in i.text:
                #Creates text files to store the data
                new_file = open((organisation) +'.txt', 'w')
                new_file.write(organisation)
                new_file.write('\n' + i.text)
                new_file.close()
                continue
            
    except requests.exceptions.MissingSchema:
        continue
print('Finished')
        


# In[112]:


for foldername, subfolders, filenames in os.walk('/Users/daniellynch/Downloads/News Bias Files/Right'):
    for file in filenames:
        if file.endswith('.txt'):
            f = open(file, 'r')
            read_text = f.readlines()
            file_name_list.append(read_text)

#Sorts the list into alphabetical order for organisational purposes           
sorted_list = sorted(file_name_list)

        
wb = openpyxl.load_workbook('/Users/daniellynch/Downloads/News Bias Files/Media Bias Fact Check.xlsx')

sheet = wb['Right']

for content in sorted_list:
    sheet.append(content)
    
wb.save('/Users/daniellynch/Downloads/News Bias Files/Media Bias Fact Check.xlsx')
wb.close()
print('Finished')

        


# In[18]:






# In[ ]:




