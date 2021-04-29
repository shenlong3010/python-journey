import re
import pandas as pd

top10books = "Pride and Prejudice by Jane Austen (1448), Alices Adventures in Wonderland by Lewis Carroll (1005), The Adventures of Sherlock Holmes by Arthur Conan Doyle (764), The Yellow Wallpaper by Charlotte Perkins Gilman (704), Moby Dick; Or, The Whale by Herman Melville (632), Ion by Plato (617), Frankenstein; Or, The Modern Prometheus by Mary Wollstonecraft Shelley (584), The Strange Case of Dr. Jekyll and Mr. Hyde by Robert Louis Stevenson (525), Treasure Island by Robert Louis Stevenson (503)"

downloads = re.findall(r'([\d+]+)', top10books)
# breakdown: r for raw string
# ( open bracket
# [\d+]+ means any digits 0-9 repeated one or more times multiple times
# ) close bracket
print(downloads)

books = re.findall(r'[\w][\w\s]*?(?=by)', top10books)
# [\w] a letter character
# [\w\s]* any qty of words and spaces
# ?(?=by) look behind until the word 'by'
print(books)

authors = re.findall(r'(?<=by).[\D]*[\s]', top10books)
# (?<=by) look after the word 'by'
# . dot means find any character
# [\D]*: 0 or more non-digits
# [\s] space
print(authors)
books.pop(5)
authors[5] = "Herman Melville"

top10_df = pd.DataFrame(
	{'Book_Title': books, 
	'Author': authors, 
	'Downloads': downloads,
	})

print(top10_df)