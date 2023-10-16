from bs4 import BeautifulSoup 
 import requests 
  
 response=requests.get("https://news.ycombinator.com/") 
  
 headings_list=[] 
 score_list=[] 
 link_list=[] 
  
 soup=BeautifulSoup(response.text, "html.parser") 
  
 
 a_tags=soup.find_all('a') 
 for a_tag in a_tags: 
     link_text=a_tag.text 
     headings_list.append(link_text) 
 print(headings_list) 
  
 
 score=soup.find_all(class_="score") 
 for scores in score: 
     score_text=scores.text 
     score_list.append(score_text) 
 print(score_list) 
  

 for link in soup.find_all('a'): 
     links=link.get('href') 
     link_list.append(links) 
 print(link_list)