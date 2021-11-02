# News API App
#### 1/11/2021
#### By **Annalis Kirwa**  
## Description

News API App is a web appliction that displays a list of news sources ranging from sports to technology and entertainment. 
The user will be able to view news from various sources.
The user can click on the article to read more about the news.  
## Behaviour Driven Development(BDD)  
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |
  
 ## Features  
 As a user, you will be able to:   
* View the news sources according to categories
* View all news sources from the source selected.
* View the description (image and time created) of the article.
* Click on an article and read it fully from the news source  
## Setup/Installation Requirements
### To interact with the News API web application:   
* Have the latest version of browser installed  
* Click on this <a href = "https://ann-news-api.herokuapp.com/">link</a> to read news/articles from various sources  

### To contribute to the web application project:  
Make sure you have the following installed:  
```
Pip
Python version 3.6
Flask
virtualenv
```  
* Create an account on Github
* Fork the repository from Github with this <a href = "https://github.com/Annaliskirwa/_News_API.git" >link </a>
* Clone the repository
* Open the project cloned project  
* Go to this <a href = "https://newsapi.org/">link</a> and register for an API key  
* Create ```start.sh``` file at the root folder and in it write the following lines:
```
 export NEWS_API_KEY='<Your-Api-Key>'
 python3.6 manage.py server
```
* Run ```chmod +x start.sh``` follwoed by ``` ./start.sh ``` on the terminal to start the project.
* View the project on your localhost using the address: ``` localhost:5000 ```.  
## Known Bugs
There are no known bugs so far
## Technologies Used  
* Python v3.6  
* HTML
* Bootstrap
* Flask  
* NewsAPI  
## Support and contact details
In case of any problem while interacting with the web application, reach out to me at annalis.kirwa@student.moringaschool.com
### License.
MIT Copyright (c) 2021 **[MITlicense](LICENSE)**
