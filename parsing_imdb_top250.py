from bs4 import BeautifulSoup
import requests
import pandas as pd


def create_wrapper_html():

    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    html = requests.get(url)

    with open('imdb_page_top_250.html', 'w') as output_file:
        output_file.write(html.text)
        
    
    return output_file

def create_dict():
    films_name = []
    films_raiting = []
    films_year = []

    with open('imdb_page_top_250.html', 'r') as input_file:
        soup = BeautifulSoup(input_file,'lxml')

    for x in soup.table.findAll('a')[1::2]:
        films_name.append(x.string)

    for y in soup.table.findAll('span',attrs={'name':'ir'}):
        films_raiting.append(str(y)[18:25])

    for z in soup.table.findAll('span',attrs={'class':'secondaryInfo'}):
        films_year.append(z.string[1:5])

    top250 = {'films_name':films_name,'films_raiting':films_raiting,'films_year':films_year }

    return top250

def create_csv(dict):
    FILENAME = 'parsing.csv'
    df = pd.DataFrame(dict) 
    df.to_csv(FILENAME, index=False)


#Parsing 250top film from iMDB

if __name__ == "__main__":
    create_wrapper_html()
    f = create_dict()
    create_csv(f)








# html = requests.get(url)

# with open('imdb_page_top_250.html', 'w') as output_file:
#     output_file.write(html.text)

# films_name = []
# films_raiting = []
# films_year = []

# with open('imdb_page_top_250.html', 'r') as input_file:
#     soup = BeautifulSoup(input_file,'lxml')


# for x in soup.table.findAll('a')[1::2]:
#     films_name.append(x.string)

# for y in soup.table.findAll('span',attrs={'name':'ir'}):
#     films_raiting.append(str(y)[18:25])

# for z in soup.table.findAll('span',attrs={'class':'secondaryInfo'}):
#     films_year.append(z.string[1:5])

# dict = {'films_name':films_name,'films_raiting':films_raiting,'films_year':films_year }


# FILENAME = 'parsing.csv'

# df = pd.DataFrame(dict) 
  

# df.to_csv(FILENAME, index=False) 








# with open(FILENAME, 'w', newline='') as file:
#     wr = csv.writer(file, quoting=csv.QUOTE_ALL)
#     wr.writerow(films_name)






# collect = [[n1,n2,n3,n4] for n1 in range(1,len(films_year)) for n2 in films_name for n3 in films_year for n4 in films_year]

# print(collect[0])



# for x in soup.table.findAll('a')[1::2]:
#     print(x.string)

# soup.table.findAll('span',attrs={'name':'ir'}) #raiting

# print(soup.table.findAll('span',attrs={'class':'secondaryInfo'})) #years





# print(soup.table.findAll('a')[1::2])

# <td class="titleColumn">
#       1.
#       <a href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&amp;pf_rd_r=TKGAZ9H438ZAN3WR0VCV&amp;pf_rd_s=center-1&amp;pf_rd_t=15506&amp;pf_rd_i=top&amp;ref_=chttp_tt_1" title="Frank Darabont (dir.), Tim Robbins, Morgan Freeman">Побег из Шоушенка</a>
#         <span class="secondaryInfo">(1994)</span>
#     </td>

# table class="chart full-width"

# title_names_and_years = tag.find_all("td", attrs={"class": "titleColumn"})
# imdb_raitings = tag.find_all("td", attrs={"class": "ratingColumn imdbRating"})

# list_s = str(title_names_and_years).split('\n')

# OKAY = []

# for x in list_s:
#     z = re.split('<span', str(x))
#     for l in z:
#         n1 = re.split(r'">',str(l))
#         n2 = re.split(r'</a>',str(n1))

#         OKAY.append(n2)
# del OKAY[0]

# n3 = OKAY[1::5]


# print(n3[0][0].split(',')[])
    
 
# print(str(title_names_and_years).split('\n'))
