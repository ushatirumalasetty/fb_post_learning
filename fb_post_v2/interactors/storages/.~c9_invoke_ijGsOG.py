from abc import ABC, abstractmethod

class StorageInterface(ABC):

    @abstractmethod
    def create_post(self, user_id: int, post_content: str) ->int:
        pass
    
    @abstractmethod
    def create_comment(self, user_id: int, post_id: int,
                       comment_content: str) ->int:
        pass

    @abstractmethod
    def is_valid_post_id(self, post_id: int):
        pass
    
    @abstractmethod
    def is_valid_comment_id(self, comment_id):
        pass
    
    @abstractmethod
    def reply_to_comment(self, user_id: int,
                         comment_id: int,
                         reply_content: str) ->int:
        pass
    














