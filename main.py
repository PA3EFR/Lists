# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'


# Add your code after this line

# Opdracht 1
def alphabetical_order(film_names):
    sorted_list = sorted(film_names)
    print("sorted_list", sorted_list)
    return


# Opdracht 2
def won_golden_globe(film_name):
    #    print (film_name)
    film_name_lower = film_name.lower()
    print(film_name_lower)
    if film_name_lower == "fiddler on the roof":
        print("won golden globe")
        x = 1
    elif film_name_lower == "cinderella liberty":
        print("nominated")
        x = 0
    elif film_name_lower == "valley of the dolls":
        print("nominated")
        x = 0
    elif film_name_lower == "jaws":
        print("won golden globe")
        x = 1
    return x


film_names = ["Fiddler on the Roof", "Valley of the Dolls", "Cinderella Liberty", "Jaws"]
alphabetical_order(film_names)
if won_golden_globe(film_names[0]) == True:
    print("True")
else:
    print("False")
print()
print()
print("----")


# Opdracht 3
def remove_toto_albums(total_old_list):
    print(total_old_list)
    remove_item = list_toto[0]
    total_old_list.remove(remove_item)
    remove_item = list_toto[1]
    total_old_list.remove(remove_item)
    remove_item = list_toto[2]
    total_old_list.remove(remove_item)
    remove_item = list_toto[3]
    total_old_list.remove(remove_item)
    remove_item = list_toto[4]
    total_old_list.remove(remove_item)
    remove_item = list_toto[5]
    total_old_list.remove(remove_item)
    total_new_list = total_old_list
    return total_new_list


list_toto = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between", "Toto XIV", "Old Is New"]
list_williams = ["Joseph Williams", "I Am Alive", "3", "Early Years", "Vertigo", "Two of Us", "Vertigo 2",
                 "Smiles and Tears", "This Fall"]
# print (list_toto[0])
total_old_list = ["Joseph Williams", "I Am Alive", "3", "Early Years", "Vertigo", "Two of Us", "Vertigo 2",
                  "Smiles and Tears", "This Fall", "Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between",
                  "Toto XIV", "Old Is New"]
toto_free_new_list = remove_toto_albums(total_old_list)
print(toto_free_new_list)

