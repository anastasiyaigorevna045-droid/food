# Скрипт поиска рецептов по названию
recipes = ["Борщ", "Салат Цезарь", "Плов", "Блины", "Компот"]

def search(query):
    results = [r for r in recipes if query.lower() in r.lower()]
    return results

if __name__ == "__main__":
    user_query = input("Введите название рецепта: ")
    found = search(user_query)
    if found:
        print("Найдено:", ", ".join(found))
    else:
        print("Ничего не найдено.")
