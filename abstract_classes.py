from abc import ABC, abstractmethod


class CustomerAbstractClass(ABC):
    @abstractmethod
    def search_books(self):
        pass


class LibrarianAbstractClass(ABC):
    @abstractmethod
    def register_member(self, name: str, email: str, phone: str, subscription_plan: str):
        pass

    @abstractmethod
    def renew_customer_membership(self, customer_id: str, updated_membership_end_date):
        pass

    @abstractmethod
    def update_customer_membership(self, customer_id, subscription_plan: str, membership_start_date):
        pass

    @abstractmethod
    def check_in(self, customer_id, book_copy_id):
        pass

    @abstractmethod
    def check_out(self, customer_id, book_copy_id):
        pass

    @abstractmethod
    def add_books(self, book_addition_strategy):
        pass
    
    @abstractmethod
    def create_subscription(self):
        pass

    @abstractmethod
    def get_overdue_books(self):
        pass
    
    @abstractmethod
    def get_due_books(self):
        pass

    @abstractmethod
    def remove_book(self, book_copy_id):
        pass

    @abstractmethod
    def get_book_history(self, book_copy_id):
        pass

