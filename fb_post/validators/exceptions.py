
class Error(Exception):
    pass


class InvalidUserException(Exception):
    pass


class InvalidPostException(Exception):
    pass

class InvalidCommentException(Exception):
    pass


class InvalidPostContent(Exception):
    pass


class InvalidCommentContent(Exception):
    pass


class InvalidReplyContent(Error):
    pass


class UserCannotDeletePostException(Error):
    pass


class InvalidReactionTypeException(Error):
    pass
