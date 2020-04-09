from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


def create_wrapper_html(genre,max_page:int):

    page = 1

    while page != max_page + 1:
        print('start create {} page'.format(page))
        if page == 1: 
            url = 'https://www.imdb.com/search/title/?genres={}&view=simple&explore=title_type,genres&ref_=adv_prv'.format(genre)
            html = requests.get(url)
            with open('imdb_page_{}_genre_{}'.format(page,genre), 'w') as output_file:
                output_file.write(html.text)
        else:
            page_part = page + 50
            url = 'https://www.imdb.com/search/title/?genres={}&view=simple&start={}&explore=title_type,genres&ref_=adv_nxt'.format(genre, page_part)
            html = requests.get(url)
            with open('imdb_page_{}_genre_{}'.format(page,genre), 'w') as output_file:
                    output_file.write(html.text)
        page += 1



def create_dict(genre,max_page:int):
    films_name = []
    films_raiting = []
    films_year = []

    page = 1

    while page != max_page + 1:

        with open('imdb_page_{}_genre_{}'.format(page,genre), 'r') as input_file:
            soup = BeautifulSoup(input_file,'lxml')

            for x in soup.findAll(attrs={'class':'col-title' }):
                films_name.append(x.find('a').string)
                print('add films name for {} page'.format(page))
            
            # Some films doesn't have mark (it will be in future, for example),
            # so this part i made with try\except const)
            for x in soup.findAll(attrs={'class':'col-imdb-rating' }):
                try:
                    films_raiting.append(x.find('strong').string.replace(' ','').replace('\n',''))
                except:
                    print('Dont have a mark')
                    films_raiting.append('Doesnt have a mark')
                print('add films raiting for {} page'.format(page))

            for x in soup.findAll(attrs={'class':'col-title', 'class':'lister-item-year text-muted unbold'}):
                films_year.append(x.string.replace('(','').replace(')',''))
                print('add films year for {} page'.format(page))
        
        page += 1

    dict = {'films_name':films_name,'films_raiting':films_raiting,'films_year':films_year }

    for page in range (1,max_page + 1):
        html_page = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'imdb_page_{}_genre_{}'.format(page,genre))
        os.remove(html_page)



    
    

    return dict


def create_csv(dict, genre):
    FILENAME = 'parsing_imdb_for_{}.csv'.format(genre)
    df = pd.DataFrame(dict) 
    df.to_csv(FILENAME, index=False)



#Parsing genre film from iMDB

if __name__ == "__main__":

    ch = input('''Выбери жанр/choose the genre >>>
    1. Comedy, 2.Sci-Fi, 3.Horror, 
    4.Romance, 5.Action, 6.Thriller,
    7.Drama, 8.Mystery, 9.Crime
    10.Animation, 11.Fantasy, 12.Superhero
    ''')
    if ch == '1':
        genre = 'comedy'
    if ch == '2':
        genre = 'sci-fi'
    if ch == '3':
        genre = 'horror'
    if ch == '4':
        genre = 'romance'
    if ch == '5':
        genre = 'action'
    if ch == '6':
        genre = 'thriller' 
    if ch == '7':
        genre = 'drama'
    if ch == '8':
        genre = 'mystery'
    if ch == '9':
        genre = 'crime'
    if ch == '10':
        genre = 'animation'
    if ch == '11':
        genre = 'fantasy'
    if ch == '12':
        genre = 'superhero'
    if ch not in ['1','2','3','4','5','6','7','8','9','10','11','12']:
        raise KeyboardInterrupt

    print('ваш выбор/your choise: {}'.format(genre))

    max_page = int(input('''Введи число страниц (1 стр = 50 фильмов)/
                            Type number of page(1 page = 50 films)>>>'''))

    create_wrapper_html(genre,max_page)
    f = create_dict(genre,max_page)
    create_csv(f,genre)
        