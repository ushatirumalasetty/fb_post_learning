from .enums import ReactionTypeEnum

DEFAULT_DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

REACTION_TYPE_ENUMS = [
    reaction_type.value for reaction_type in ReactionTypeEnum
    ]

POSITIVE_REACTIONS_ENUMS = [
    ReactionTypeEnum.WOW.value,
    ReactionTypeEnum.LIT.value,
    ReactionTypeEnum.HAHA.value,
    ReactionTypeEnum.LOVE.value,
    ReactionTypeEnum.THUMBS_UP.value
]

NEGATIVE_REACTIONS_ENUMS = [
    ReactionTypeEnum.THUMBS_DOWN.value,
    ReactionTypeEnum.ANGRY.value,
    ReactionTypeEnum.SAD.value
]