from usp.tree import sitemap_tree_for_homepage

def save():
    with open('2.txt', 'a', encoding="utf-8") as file:
        file.write(f'{tree} end=", \n"')
def sav():
    with open('3.txt', 'a', encoding="utf-8") as file:
        file.write(f'{page} end=", \n"')

with open("1.txt", "r", encoding="utf-8") as file:
    for line in file:
        URL = line.strip()
        tree = sitemap_tree_for_homepage(URL)
        print(tree)
        save()
        for page in tree.all_pages():
            print(page)
            sav()
