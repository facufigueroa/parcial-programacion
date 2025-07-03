from utils import loadLibraryItems, checkoutItems, countItems, findByTitle

libraryItems = loadLibraryItems("library.csv")

# print("Items")
# for i in libraryItems :
#     print(i)

checkoutLibraryItems = checkoutItems(libraryItems, "Facu")

# for i in checkoutLibraryItems :
#     print(i)

totalItems = countItems(libraryItems)

# print(totalItems)

filteredItems = findByTitle(libraryItems, "harry")

# for i in filteredItems :
#     print(i)