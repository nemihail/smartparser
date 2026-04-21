
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Book categories')
root.geometry('300x300')
root.resizable(width=False, height=False)

categories = {
    'All Books': 'books_1',
    'Travel': 'travel_2',
    'Mystery': 'mystery_3',
    'Historical Fiction': 'historical-fiction_4',
    'Sequential Art': 'sequential-art_5',
    'Classics': 'classics_6',
    'Philosophy': 'philosophy_7',
    'Romance': 'romance_8',
    'Womens Fiction': 'womens-fiction_9',
    'Fiction': 'fiction_10',
    'Childrens': 'childrens_11',
    'Religion': 'religion_12',
    'Nonfiction': 'nonfiction_13',
    'Music': 'music_14',
    'Default': 'default_15',
    'Science Fiction': 'science-fiction_16',
    'Sports and Games': 'sports-and-games_17',
    'Add a comment': 'add-a-comment_18',
    'Fantasy': 'fantasy_19',
    'New Adult': 'new-adult_20',
    'Young Adult': 'young-adult_21',
    'Science': 'science_22',
    'Poetry': 'poetry_23',
    'Paranormal': 'paranormal_24',
    'Art': 'art_25',
    'Psychology': 'psychology_26',
    'Autobiography': 'autobiography_27',
    'Parenting': 'parenting_28',
    'Adult Fiction': 'adult-fiction_29',
    'Humor': 'humor_30',
    'Horror': 'horror_31',
    'History': 'history_32',
    'Food and Drink':'food-and-drink_33',
    'Christian Fiction': 'christian-fiction_34',
    'Business': 'business_35',
    'Biography': 'biography_36',
    'Thriller': 'thriller_37',
    'Contemporary': 'contemporary_38',
    'Spirituality': 'spirituality_39',
    'Academic': 'academic_40',
    'Self Help': 'self-help_41',
    'Historical': 'historical_42',
    'Christian': 'christian_43',
    'Suspense': 'suspense_44',
    'Short Stories': 'short-stories_45',
    'Novels': 'novels_46',
    'Health': 'health_47',
    'Politics': 'politics_48',
    'Cultural': 'cultural_49',
    'Erotica': 'erotica_50',    # the best of my projects
    'Crime': 'crime_51'
}

tk.Label(root, text='Select one of the book categories:',
         font=('Arial', 12)).place(relx=0.5, rely=0.1, anchor='center')

cat_ask = ttk.Combobox(root, values=list(categories.keys()), state='readonly', font=('Arial', 12))
cat_ask.current(0)
cat_ask.place(relx=0.5, rely=0.3, anchor='center')

selected = None
def write_selected(option):
    """this func is completely костыль"""
    global selected
    selected = categories[option]
    root.destroy()


select_button = tk.Button(root, text='Select', font=('Arial', 12),
                          command=write_selected(cat_ask.get()))
select_button.place(relx=0.5, rely=0.7, anchor='center')

root.mainloop()
