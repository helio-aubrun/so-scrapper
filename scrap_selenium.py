from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # ou URI Atlas
db = client["stack_scraper"]
collection = db["questions"]

driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/questions")

time.sleep(3)

questions = driver.find_elements(By.CSS_SELECTOR, "div.s-post-summary")

for q in questions:
    try:
        # Titre et lien
        title_element = q.find_element(By.CSS_SELECTOR, "h3 a")
        title = title_element.text
        link = title_element.get_attribute("href")
        
        # Résumé de la question
        try:
            excerpt = q.find_element(By.CLASS_NAME, "s-post-summary--content-excerpt").text.strip()
        except:
            excerpt = "Aucun résumé"

        # Tags
        try:
            tags = [tag.text for tag in q.find_elements(By.CSS_SELECTOR, "li.js-post-tag-list-item a.post-tag")]
        except:
            tags = []

        # Auteur
        try:
            author = q.find_element(By.CSS_SELECTOR, ".s-user-card--link").text
        except:
            author = "Auteur inconnu"

        # Date de publication
        try:
            date_element = q.find_element(By.CSS_SELECTOR, ".relativetime")
            date = date_element.get_attribute("title")
        except:
            date = "Date inconnue"

        # Affichage
        print(f"Titre: {title}")
        print(f"Lien: {link}")
        print(f"Résumé: {excerpt}")
        print(f"Tags: {tags}")
        print(f"Auteur: {author}")
        print(f"Date: {date}")
        print("-" * 50)
        
    except Exception as e:
        print("Erreur:", e)

# Conseil : inspecter la page pour savoir quel markdown chercher

driver.quit()