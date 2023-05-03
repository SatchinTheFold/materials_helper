import csv

# file containing title of every product on BigComm store
file = open(r"C:\Users\Satchin Mistry\The Fold Dropbox\Satchin Mistry\PC\Documents\materials.csv")
csvreader = csv.reader(file)
header = []
header = next(csvreader)

# puts every product from file into list
rows = []
for row in csvreader:
    rows.append(row[0])

primary_materials = ['merino', 'denim', 'jersey', 'silk', 'leather', 'cotton', 'suede', 'velvet', 'linen', 'satin', 'crepe', 'chiffon', 'wool', 'twill', 'tweed', 'cashmere', 'jacquard', 'jersey', 'georgette']
secondary_materials = {
    'belt': 'leather',
    'stretch': 'crepe',
    'knitted': 'viscose blend',
    'viscose': 'viscose blend',
    'tights': 'nylon',
    'socks': 'nylon',
    'alpaca': 'alpaca wool',
}
specific_products = {
		'como 80 metallic nappa sandal': 'leather',
		'lerici 80 mahogany high heels': 'leather',
		'san casciano 45 silver glitter': 'metallic fabric',
		'sleeveless camelot dress blush pink': 'fabric blend',
		'delphi dress light sand fern print': 'georgette',
		'rosemount dress multicolour confetti print': 'silk',
		'vieste dress navy and toffee shell print': 'georgette',
		'keswick sweater oyster and sapphire blue': 'viscose blend',
		'lisson sweater ivory and navy': 'viscose blend',
		'lisson sweater khaki and ivory': 'viscose blend',
		'elstead reversible quilted jacket olive green and navy': 'padded',
		'ec1 pencil skirt black': 'crepe',
		'rivelli slim-leg elasticated trousers burnt orange': 'stretch crepe',
		'miramere slim-leg elasticated trousers eucalyptus': 'stretch crepe',
        'tirano blouse multicolour': 'viscose',
        'vinca rain mac taupe': 'water repellent blend',
        'altea top white lace': 'lace'
}

# open file for products that have a matching material
matched_materials = open(r"C:\Users\Satchin Mistry\The Fold Dropbox\Satchin Mistry\PC\Documents\matched_materials.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(matched_materials)
writer.writerow(['Product Name', 'Main Material'])

temp = rows.copy()
for product_name in temp:
    for material in primary_materials:
        if material in product_name.lower():
            writer.writerow([product_name, material])
            rows.remove(product_name)
            break

matched_materials.close()

# open file for products that have a secondary matching material
matched_secondary_materials = open(r"C:\Users\Satchin Mistry\The Fold Dropbox\Satchin Mistry\PC\Documents\matched_secondary_materials.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(matched_secondary_materials)
writer.writerow(['Product Name', 'Secondary Material', 'Corresponding Material'])

temp = rows.copy()
for product_name in temp:
    for material in secondary_materials:
        if material in product_name.lower():
            writer.writerow([product_name, material, secondary_materials[material]])
            rows.remove(product_name)
            break

matched_secondary_materials.close()

# open file for products that have been hardcoded to have a specific material
specific_product_materials = open(r"C:\Users\Satchin Mistry\The Fold Dropbox\Satchin Mistry\PC\Documents\specific_product_materials.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(specific_product_materials)
writer.writerow(['Product Name', 'Corresponding Material'])

temp = rows.copy()
for product_name in temp:
    for material in specific_products:
        if material in product_name.lower():
            writer.writerow([product_name, specific_products[material]])
            rows.remove(product_name)
            break

specific_product_materials.close()

# open file for any products that don't match at all
unmatched_products = open(r"C:\Users\Satchin Mistry\The Fold Dropbox\Satchin Mistry\PC\Documents\unmatched_products.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(unmatched_products)
writer.writerow(['Unmatched Products'])

for product_name in rows:
    writer.writerow([product_name])

unmatched_products.close()
