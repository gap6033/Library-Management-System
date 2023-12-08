from abstract_classes import AdminAbstractClass, CustomerAbstractClass, LibrarianAbstractClass
from book_addition_strategy import BookAdditionStrategy
from notification_strategy import NotificationStrategy



class Customer(CustomerAbstractClass):
    def search_books(self):
       #dynamic query using Q object in Django
        pass

class Librarian(LibrarianAbstractClass):
    def register_member(self, name, email, phone, subscription_plan):
        #add member to CustomerTable and return customer id
        #add record to customer subscription plan table
        pass

    def renew_customer_membership(self, customer_id, updated_membership_end_date):
        #update membership end date in customer subscription plan table for the given customer_id
        pass

    def update_customer_membership(self, customer_id, new_subscription_plan, new_membership_start_date):
        #get customer id from customer table
        #update the end date of customers current subscription plan in customer subscription plan column and set it to a day prior to membership start date
        #add a new record to customer subscription plan table
        pass

    def check_in(self, customer_id, book_copy_id):
        #check for fine through the Checkedout Table, looking if the return date exceeds the due date
        #if fine to pay add a new record to Fines Table
        #update book copy status in the BookCopies Table for the given book as available
        #remove the record from the checked_out table
        #update CustomerHistory Table and add books to past checkouts and if required update finespaid and delayedreturns count
        pass

    def check_out(self, customer_id, book_copy_id):
        #check customers history from customer history table
        #update book copy status to checked out
        #add record to checked_out table
        #add record to BookCopyHistory Table 
        #update customer Table and add the book to customer's checkedout Books 
        pass
    
    def add_book(self, BookAdditionStrategy: BookAdditionStrategy):
        BookAdditionStrategy.add_book()

    def create_subscription_plan(self):
        #add a new row subcription plan table
        pass

    def get_overdue_books(self):
        #get all the books from checked out table
        #filter these fetched copies and compare the duedate with current date
        pass

    def get_due_books(self):
        #get all the books from checked out table
        #filter these fetched copies and compare the duedate with current date
        pass

    def remove_books(self, book_copy_id):
        #fetch the book_copy from book_copies table. update its status to removed
        pass

    def get_book_history(self, book_copy_id):
        #fetch the data from BookCopyhistory table for the given book_copy_id
        pass


class NotificationSheduler:

    def three_day_overdue_notification(self):
        #filter data from checked out table and send it to all customers who are three day overdue
        pass

    def one_day_left_notification(self):
        #filter data from checked out table and send it to all customers who have one day left to return
        pass
