# Restaurant Crawler

### Scapres zomato for basic info about restaurants, also displays scraped items on google map.
---

* Uses Scrapy to create spider and manage pipline.

* Uses Django to store scraped data using Django Models, ORM and create website to display scraped data.

Execution Instructions:
1. Clone the repository to your local file system
2. create a virtual environment using "venv" module :
    
    `python -m venv your_venv`
3. activate the venv and install dependencies using pip:
    
    `pip install django`
    
    `pip install scrapy`
    
4. Now, we need to run migrations to save our Django models in Database (move to mapsite folder )

  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
  
5. Run the spider to fetch data from the website,
the fetched data will be stored as Django models as we are using **django items** to hold the fetched data
(cd web_scraper/web_scraper)

```
pip install scrapy-djangoitem 
scrapy crawl zom_scraper
```

*Note: you can check the data in the admin page*

6. Run django internal server to see results on map

` python manage.py runserver`

---

#### Output:

the web page looks something like this:
![image](https://user-images.githubusercontent.com/5194508/41259574-b62f7b82-6df1-11e8-939f-cd8387de37c8.png)


