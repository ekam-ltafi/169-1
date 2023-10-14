class Bookshelf :
    def __ini__(self , name , author , price , publishing_year):
        self.book_name = name
        self.book_author = author 
        self.book_price = price
        self.book_publishing_year = publishing_year
        
    def add_book(self):
        print("Book Name : " + self.book_name)
        print("Author Name : " + self.book_author)
        print("Book Price : " + self.book_price)
        print(" Publishing Date : " + self.book_publishing_date)
        print("Book has been added to the library ")
    
    def years_since_publish(self):
        years_ago_published = 2023 - self.book_publishing_year
        print("This book was published in " + str(years_ago_published))
        
        
Book1 = Bookshelf("Harry Potter and Philosopher's Stone ", "J.K Rowling ",2000 , 1997)
Book1.add_book()
Book1.years_since_publish()

Book2 = Bookshelf("Diary of the Whimpy Kid ", " Jeffery Kinney ",1000 , 2017)
Book2.add_book()
Book2.years_since_publish()