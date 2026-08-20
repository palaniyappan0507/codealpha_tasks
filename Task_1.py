import requests
from bs4 import BeautifulSoup
import pandas as pd

# --------------------------------------------------
# 1. Website URL
# --------------------------------------------------

url = "https://books.toscrape.com/"

# --------------------------------------------------
# 2. Request the webpage
# --------------------------------------------------

response = requests.get(url)

print("Website Status Code:", response.status_code)

# Check whether website was accessed successfully
if response.status_code != 200:
    print("Unable to access the website.")
    exit()

# --------------------------------------------------
# 3. Parse HTML
# --------------------------------------------------

soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

print("Number of books found:", len(books))

# --------------------------------------------------
# 4. Create empty list
# --------------------------------------------------

data = []

# --------------------------------------------------
# 5. Extract book information
# --------------------------------------------------

for book in books:

    # Book name
    title = book.h3.a["title"]

    # Price
    price = book.find(
        "p",
        class_="price_color"
    ).text.strip()

    # Availability
    availability = book.find(
        "p",
        class_="instock availability"
    ).text.strip()

    # Rating
    rating = book.find(
        "p",
        class_="star-rating"
    )["class"][1]

    # Add information to list
    data.append({
        "Book Name": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating
    })

# --------------------------------------------------
# 6. Convert data into DataFrame
# --------------------------------------------------

df = pd.DataFrame(data)

print("\nRaw Dataset:")
print(df.head())

# --------------------------------------------------
# 7. Clean Price
# --------------------------------------------------

# Remove Â and £ symbols
df["Price"] = (
    df["Price"]
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
)

# Convert Price into numeric format
df["Price"] = pd.to_numeric(df["Price"])

# --------------------------------------------------
# 8. Convert Rating into numbers
# --------------------------------------------------

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# --------------------------------------------------
# 9. Display cleaned dataset
# --------------------------------------------------

print("\nCleaned Dataset:")
print(df.head())

# --------------------------------------------------
# 10. Display dataset information
# --------------------------------------------------

print("\nDataset Information:")
print(df.info())

# --------------------------------------------------
# 11. Display statistical summary
# --------------------------------------------------

print("\nStatistical Summary:")
print(df.describe())

# --------------------------------------------------
# 12. Save raw dataset
# --------------------------------------------------

df.to_csv(
    "clean_books_dataset.csv",
    index=False
)

# --------------------------------------------------
# 13. Success message
# --------------------------------------------------

print("\n----------------------------------------")
print("Web scraping completed successfully!")
print("Clean dataset saved as:")
print("clean_books_dataset.csv")
print("----------------------------------------")