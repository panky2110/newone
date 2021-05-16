from abc import abstractmethod,ABC

class ContactService(ABC):

    @abstractmethod
    def add_contact(self):
        pass

    @abstractmethod
    def delete_contact(self):
        pass

    @abstractmethod
    def update_contact(self):
        pass

    @abstractmethod
    def get_all_contact(self):
        pass

    @abstractmethod
    def get_contact(self):
        pass

    @abstractmethod
    def get_contact_byname(self):
        pass

    @abstractmethod
    def get_contact_bymail(self):
        pass