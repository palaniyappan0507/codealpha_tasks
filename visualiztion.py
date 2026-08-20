import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================================================
# TASK 3 - DATA VISUALIZATION
# =========================================================

print("==========================================")
print("       TASK 3 - DATA VISUALIZATION")
print("==========================================")

# ---------------------------------------------------------
# 1. Find the folder where this Python file is located
# ---------------------------------------------------------

folder = os.path.dirname(os.path.abspath(__file__))

print("\nProject folder:")
print(folder)

# ---------------------------------------------------------
# 2. Find the CSV file
# ---------------------------------------------------------

csv_file = os.path.join(folder, "clean_books_dataset.csv")

print("\nChecking CSV file...")

if not os.path.exists(csv_file):
    print("ERROR: clean_books_dataset.csv was not found!")
    print("Put the CSV file in the same folder as Task_3.py")
    input("\nPress Enter to exit...")
    exit()

print("CSV file found!")

# ---------------------------------------------------------
# 3. Load the dataset
# ---------------------------------------------------------

df = pd.read_csv(csv_file)

print("\nDataset loaded successfully!")

print("\nFirst 5 rows:")
print(df.head())

# ---------------------------------------------------------
# 4. Check columns
# ---------------------------------------------------------

print("\nColumns in dataset:")
print(df.columns.tolist())

# ---------------------------------------------------------
# 5. Convert Price to number
# ---------------------------------------------------------

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

# ---------------------------------------------------------
# 6. Convert Rating to number if necessary
# ---------------------------------------------------------

if df["Rating"].dtype == "object":

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["Rating"] = df["Rating"].map(rating_map)

df["Rating"] = pd.to_numeric(
    df["Rating"],
    errors="coerce"
)

# Remove rows with missing values
df = df.dropna(subset=["Price", "Rating"])

print("\nClean data:")
print(df.head())

# ---------------------------------------------------------
# 7. Set chart style
# ---------------------------------------------------------

sns.set_theme(style="whitegrid")

# =========================================================
# CHART 1 - BOOKS BY RATING
# =========================================================

print("\nCreating Chart 1...")

rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

plt.bar(
    rating_counts.index.astype(str),
    rating_counts.values
)

plt.title("Number of Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()

file1 = os.path.join(
    folder,
    "01_books_by_rating.png"
)

plt.savefig(
    file1,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()

print("Chart 1 saved:")
print(file1)

# =========================================================
# CHART 2 - PRICE DISTRIBUTION
# =========================================================

print("\nCreating Chart 2...")

plt.figure(figsize=(8, 5))

plt.hist(
    df["Price"],
    bins=10
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Number of Books")

plt.tight_layout()

file2 = os.path.join(
    folder,
    "02_price_distribution.png"
)

plt.savefig(
    file2,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()

print("Chart 2 saved:")
print(file2)

# =========================================================
# CHART 3 - PRICE VS RATING
# =========================================================

print("\nCreating Chart 3...")

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Price"],
    df["Rating"]
)

plt.title("Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Rating")

plt.tight_layout()

file3 = os.path.join(
    folder,
    "03_price_vs_rating.png"
)

plt.savefig(
    file3,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()

print("Chart 3 saved:")
print(file3)

# =========================================================
# CHART 4 - PRICE BY RATING
# =========================================================

print("\nCreating Chart 4...")

plt.figure(figsize=(8, 5))

df.boxplot(
    column="Price",
    by="Rating"
)

plt.title("Book Price Distribution by Rating")
plt.suptitle("")

plt.xlabel("Rating")
plt.ylabel("Price")

plt.tight_layout()

file4 = os.path.join(
    folder,
    "04_price_by_rating.png"
)

plt.savefig(
    file4,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()

print("Chart 4 saved:")
print(file4)

# =========================================================
# CHART 5 - RATING PERCENTAGE
# =========================================================

print("\nCreating Chart 5...")

plt.figure(figsize=(7, 7))

plt.pie(
    rating_counts.values,
    labels=rating_counts.index.astype(str),
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Percentage of Books by Rating")

plt.tight_layout()

file5 = os.path.join(
    folder,
    "05_rating_percentage.png"
)

plt.savefig(
    file5,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()

print("Chart 5 saved:")
print(file5)

# =========================================================
# 8. DISPLAY DATA INSIGHTS
# =========================================================

print("\n==========================================")
print("             DATA INSIGHTS")
print("==========================================")

print(
    "\nTotal books analyzed:",
    len(df)
)

print(
    "Average book price: £",
    round(df["Price"].mean(), 2)
)

print(
    "Minimum book price: £",
    round(df["Price"].min(), 2)
)

print(
    "Maximum book price: £",
    round(df["Price"].max(), 2)
)

print(
    "Most common rating:",
    int(df["Rating"].mode()[0]),
    "stars"
)

# ---------------------------------------------------------
# Average price by rating
# ---------------------------------------------------------

average_price = df.groupby("Rating")["Price"].mean()

print("\nAverage price by rating:")

print(average_price)

# ---------------------------------------------------------
# 9. Save processed dataset
# ---------------------------------------------------------

output_csv = os.path.join(
    folder,
    "visualization_ready_dataset.csv"
)

df.to_csv(
    output_csv,
    index=False
)

print("\nProcessed dataset saved:")
print(output_csv)

# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n==========================================")
print("      ALL TASKS COMPLETED SUCCESSFULLY")
print("==========================================")

print("\nYour image files are located here:")
print(folder)

input("\nPress Enter to close...")