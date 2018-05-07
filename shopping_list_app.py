# make a list to hold onto our itmes
shopping_list = []

def show_help():
    # print instructions
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help
Enter 'SHOW' to see your current list.     
""")
    
def show_list():
    # print list
    print("Here's your list:")

    for item in shopping_list:
        print(item)
        
def add_to_list(new_item):
    # add new items
    shopping_list.append(new_item)
    print("Added {}, list now has {} items.".format(new_item, len(shopping_list)))
    
show_help()
    
while True:
    # ask for new items
    new_item = input("> ")
    
    # to be able to quit the app
    if new_item == "DONE":
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)
  
show_list()