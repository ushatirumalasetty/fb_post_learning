
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface

from fb_post_v2.interactors.storages.post_storage_interface import \
    PostStorageInterface
from fb_post_v2.interactors.storages.comment_storage_interface import \
    CommentStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
    ReactionStorageInterface

__all__ = [
    'StorageInterface',
    "PostStorageInterface",
    "CommentStorageInterface",
    "ReactionStorageInterface"
]