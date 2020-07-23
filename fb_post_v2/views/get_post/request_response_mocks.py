


RESPONSE_200_JSON = """
{
    "post_id": 1,
    "posted_by": {
        "user_id": 1,
        "name": "string",
        "profile_pic": "string"
    },
    "posted_at": "string",
    "post_content": "string",
    "reactions": {
        "count": 1,
        "type": [
            "WOW"
        ]
    },
    "comments": [
        {
            "comment_id": 1,
            "commenter": {
                "user_id": 1,
                "name": "string",
                "profile_pic": "string"
            },
            "commented_at": "string",
            "comment_content": "string",
            "reactions": {
                "count": 1,
                "type": [
                    "WOW"
                ]
            },
            "replies_count": 1,
            "replies": [
                {
                    "comment_id": 1,
                    "commenter": {
                        "user_id": 1,
                        "name": "string",
                        "profile_pic": "string"
                    },
                    "commented_at": "string",
                    "comment_content": "string",
                    "reactions": {
                        "count": 1,
                        "type": [
                            "WOW"
                        ]
                    }
                }
            ]
        }
    ],
    "comments_count": 1
}
"""

