{
    "swagger": "2.0",
    "host": "127.0.0.1:8080",
    "basePath": "/fb_post/",
    "info": {
        "version": "1.0.0",
        "title": "fb_post API",
        "description": "fb_post OpenAPI Specification"
    },
    "schemes": [
        "https",
        "http"
    ],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "securityDefinitions": {
        "oauth": {
            "tokenUrl": "http://auth.ibtspl.com/oauth2/",
            "flow": "password",
            "scopes": {
                "read": "read users",
                "write": "create users",
                "update": "update users",
                "delete": "delete users",
                "superuser": "super user permission"
            },
            "type": "oauth2"
        }
    },
    "definitions": {
        "UserWithContent": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string"
                }
            },
            "required": [
                "content"
            ]
        },
        "BaseCommentDetails": {
            "type": "object",
            "properties": {
                "comment_id": {
                    "type": "integer",
                    "format": "int64"
                },
                "commenter": {
                    "$ref": "#/definitions/User"
                },
                "commented_at": {
                    "type": "string",
                    "format": "datetime"
                },
                "comment_content": {
                    "type": "string"
                }
            },
            "required": [
                "comment_id",
                "commenter",
                "commented_at",
                "comment_content"
            ]
        },
        "User": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "integer",
                    "format": "int64"
                },
                "name": {
                    "type": "string"
                },
                "profile_pic": {
                    "type": "string"
                }
            },
            "required": [
                "user_id",
                "name",
                "profile_pic"
            ]
        },
        "Reply": {
            "allOf": [{
                    "$ref": "#/definitions/BaseCommentDetails"
                },
                {
                    "type": "object",
                    "properties": {
                        "reactions": {
                            "$ref": "#/definitions/ReactionsDict"
                        }
                    },
                    "required": [
                        "reactions"
                    ]
                }
            ]
        },
        "Comment": {
            "allOf": [{
                    "$ref": "#/definitions/BaseCommentDetails"
                },
                {
                    "type": "object",
                    "properties": {
                        "reactions": {
                            "$ref": "#/definitions/ReactionsDict"
                        }
                    },
                    "required": [
                        "reactions"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "replies_count": {
                            "type": "integer",
                            "format": "int64"
                        },
                        "replies": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Reply"
                            }
                        }
                    },
                    "required": [
                        "replies_count",
                        "replies"
                    ]
                }

            ]
        },
        "Post": {
            "type": "object",
            "properties": {
                "post_id": {
                    "type": "integer",
                    "format": "int64"
                },
                "posted_by": {
                    "$ref": "#/definitions/User"
                },
                "posted_at": {
                    "type": "string",
                    "format": "datetime"
                },
                "post_content": {
                    "type": "string"
                },
                "reactions": {
                    "$ref": "#/definitions/ReactionsDict"
                },
                "comments": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Comment"
                    }
                },
                "comments_count": {
                    "type": "integer",
                    "format": "int64"
                }
            },
            "required": [
                "post_id",
                "posted_by",
                "posted_at",
                "post_content",
                "reactions",
                "comments",
                "comments_count"
            ]
        },
        "ReactionsDict": {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                    "format": "int64"
                },
                "type": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            "WOW", "LIT",
                            "LOVE", "HAHA",
                            "THUMBS-UP", "THUMBS-DOWN",
                            "ANGRY", "SAD"
                        ]
                    }
                }
            },
            "required": [
                "count",
                "type"
            ]
        },
        "UseridPostidAndContent": {
            "allOf": [{
                    "$ref": "#/definitions/UserWithContent"
                },
                {
                    "type": "object",
                    "properties": {
                        "post_id": {
                            "type": "integer",
                            "format": "int64"
                        }
                    },
                    "required": [
                        "post_id"
                    ]
                }
            ]
        },
        "CommentId": {
            "type": "object",
            "properties": {
                "comment_id": {
                    "type": "integer",
                    "format": "int64"
                }
            },
            "required": [
                "comment_id"
            ]
        },
        "ReactionTypes": {
            "type": "object",
            "properties": {
                "reaction_type": {
                    "type": "string",
                    "enum": [
                        "WOW", "LIT",
                        "LOVE", "HAHA",
                        "THUMBS-UP", "THUMBS-DOWN",
                        "ANGRY", "SAD"
                    ]

                }
            },
            "required": [
                "reaction_type"
            ]
        },
        "ReactionToPost": {
            "allOf": [{
                    "$ref": "#/definitions/User"
                },
                {
                    "type": "object",
                    "properties": {
                        "reaction": {
                            "type": "string",
                            "enum": [
                                "WOW", "LIT",
                                "LOVE", "HAHA",
                                "THUMBS-UP", "THUMBS-DOWN",
                                "ANGRY", "SAD"
                            ]
                        }
                    },
                    "required": [
                        "reaction"
                    ]
                }
            ]
        },
        "ReactionMetrics": {
            "type": "object",
            "properties": {
                "reaction_type": {
                    "type": "string",
                    "enum": [
                        "WOW", "LIT",
                        "LOVE", "HAHA",
                        "THUMBS-UP", "THUMBS-DOWN",
                        "ANGRY", "SAD"
                    ]
                },
                "count": {
                    "type": "integer",
                    "format": "int64"
                }
            },
            "required": [
                "reaction_type",
                "count"
            ]
        }


    },

    "parameters": {
        "CreateNewPostParameter": {
            "name": "post",
            "in": "body",
            "description": "Post to create",
            "schema": {
                "$ref": "#/definitions/UserWithContent"
            }
        },
        "CreateNewCommentParameters": {
            "name": "comment",
            "in": "body",
            "description": "Create comment",
            "schema": {
                "$ref": "#/definitions/UseridPostidAndContent"
            }
        },
        "CreateNewReplyParameters": {
            "name": "comment",
            "in": "body",
            "description": "Create comment",
            "schema": {
                "$ref": "#/definitions/UserWithContent"
            }
        },
        "ReactToPostParameters": {
            "name": "post",
            "in": "body",
            "description": "React to Post",
            "schema": {
                "$ref": "#/definitions/ReactionTypes"
            }
        },
        "ReactToCommentParameters": {
            "name": "comment",
            "in": "body",
            "required": true,
            "description": "react to comment",
            "schema": {
                "$ref": "#/definitions/ReactionTypes"
            }

        },
        "PostIdPathParameters": {
            "name": "post_id",
            "in": "path",
            "description": " post's post_id",
            "required": true,
            "type": "integer",
            "format": "int64"
        },
        "CommentIdPathParameters": {
            "name": "comment_id",
            "in": "path",
            "description": " comment's comment_id",
            "required": true,
            "type": "integer",
            "format": "int64"
        },
        "MinimumValueQueryParameter": {
            "name": "offset",
            "in": "query",
            "description": "MiniumValue",
            "type": "integer"
        },
        "MaximumValueQueryParameter": {
            "name": "limit",
            "in": "query",
            "required": true,
            "description": "MaximumValue",
            "type": "integer",
            "format": "int64"
        }


    },

    "responses": {
        "CreatePostResponse": {
            "description": "Post created",
            "schema": {
                "type": "object",
                "properties": {
                    "post_id": {
                        "type": "integer",
                        "format": "int64"
                    }
                },
                "required": [
                    "post_id"
                ]
            }
        },
        "CreateCommentResponse": {
            "description": "Comment created successfully",
            "schema": {
                "$ref": "#/definitions/CommentId"
            }
        },
        "GetTotalReactionCountResponse": {
            "description": "OK",
            "schema": {
                "type": "object",
                "properties": {
                    "count": {
                        "type": "integer",
                        "format": "int64"
                    }
                },
                "required": [
                    "count"
                ]
            }
        },
        "GetPostWithPositiveReactionsResponse": {
            "description": "OK",
            "schema": {
                "type": "array",
                "items": {
                    "type": "integer",
                    "format": "int64"
                }
            }

        },
        "GetPostReactionsResponse": {
            "description": "OK",
            "schema": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/ReactionToPost"
                }

            }
        },
        "GetPostsReactedByUserResponse": {
            "description": "OK",
            "schema": {
                "type": "array",
                "items": {
                    "type": "integer",
                    "format": "int64"
                }
            }
        },
        "GetPostResponse": {
            "description": "OK",
            "schema": {
                "$ref": "#/definitions/Post"
            }
        },
        "GetUserPostsResponse": {
            "description": "OK",
            "schema": {
                "type": "object",
                "properties": {
                    "posts": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/Post"
                        }
                    },
                    "total_count": {
                        "type": "integer",
                        "format": "int64"
                    }
                }
            }
        },
        "GetReactionMetricsOfPostResponse": {
            "description": "OK",
            "schema": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/ReactionMetrics"
                }
            }
        },
        "GetRepliesForCommentResponse": {
            "description": "OK",
            "schema": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/BaseCommentDetails"
                }

            }
        }

    },

    "paths": {
        "/posts/create/v1/": {
            "post": {
                "operationId": "create_post",
                "summary": "Create New Post",
                "description": "Create new post and returns post_id",
                "security": [{
                    "oauth": [
                        "superuser"
                    ]
                }],
                "parameters": [{
                    "$ref": "#/parameters/CreateNewPostParameter"
                }],
                "responses": {
                    "201": {
                        "$ref": "#/responses/CreatePostResponse"
                    },
                    "404": {
                        "description": "User does not exists"
                    },
                    "400": {
                        "description": "Invalid content"
                    }
                }
            }
        },
        "/comments/create/v1/": {
            "post": {
                "operationId": "create_comment",
                "summary": "Create New Comment",
                "description": "Create new comment and returns comment_id",
                "security": [{
                    "oauth": [
                        "superuser"
                    ]
                }],
                "parameters": [{
                    "$ref": "#/parameters/CreateNewCommentParameters"
                }],
                "responses": {
                    "201": {
                        "$ref": "#/responses/CreateCommentResponse"
                    },
                    "404": {
                        "description": "User or Post does not exists"
                    },
                    "400": {
                        "description": "Invalid comment content"
                    }
                }
            }

        },
        "/comments/{comment_id}/reply/v1/": {
            "post": {
                "operationId": "reply_to_comment",
                "summary": "Create Reply to Comment",
                "description": "Create reply to comment and returns reply_id",
                "security": [{
                    "oauth": [
                        "superuser"
                    ]
                }],
                "parameters": [{
                        "$ref": "#/parameters/CommentIdPathParameters"
                    },
                    {
                        "$ref": "#/parameters/CreateNewReplyParameters"
                    }
                ],
                "responses": {
                    "201": {
                        "$ref": "#/responses/CreateCommentResponse"
                    },
                    "404": {
                        "description": "User or Comment does not exists"
                    },
                    "400": {
                        "description": "Invalid comment content"
                    }
                }
            }

        },
        "/posts/{post_id}/react/v1/": {
            "post": {
                "operationId": "react_to_post",
                "summary": "Reacting to Post",
                "description": "Reacting to post ",
                "security": [{
                    "oauth": [
                        "superuser"
                    ]
                }],
                "parameters": [{
                        "$ref": "#/parameters/PostIdPathParameters"
                    },
                    {
                        "$ref": "#/parameters/ReactToPostParameters"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    },
                    "404": {
                        "description": "User or Comment does not exists"
                    },
                    "400": {
                        "description": "Invalid reaction type"
                    }
                }
            }

        },
        "/comments/{comment_id}/react/v1/": {
            "post": {
                "operationId": "react_to_comment",
                "summary": "Reacting to comment",
                "description": "Reacting to comment  and based on existing reacting we can update or delete or create new reaction ",
                "security": [{
                    "oauth": [
                        "superuser"
                    ]
                }],
                "parameters": [{
                        "$ref": "#/parameters/CommentIdPathParameters"
                    },
                    {
                        "$ref": "#/parameters/ReactToCommentParameters"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    },
                    "404": {
                        "description": "User or Comment does not exists"
                    },
                    "400": {
                        "description": "Invalid reaction type"
                    }
                }
            }

        },
        "/reactions/count/v1/": {
            "get": {
                "operationId": "get_total_reaction_count",
                "summary": "getting count of total reaction",
                "description": "getting total count of reaction",
                "parameters": [],
                "responses": {
                    "200": {
                        "$ref": "#/responses/GetTotalReactionCountResponse"
                    }
                }
            }

        },
        "/posts/{post_id}/v1/": {
            "delete": {
                "operationId": "delete_post",
                "summary": "Delete Post",
                "description": "deleting the post ",
                "security": [{
                    "oauth": [
                        "superuser"
                    ]
                }],
                "parameters": [{
                        "$ref": "#/parameters/PostIdPathParameters"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    },
                    "404": {
                        "description": "User or Post does not exists"
                    },
                    "403": {
                        "description": "User cannot delete post"
                    }
                }
            },
            "get": {
                "operationId": "get_post",
                "summary": "Get Post",
                "description": "get details of post in dict ",
                "parameters": [{
                    "$ref": "#/parameters/PostIdPathParameters"
                }],
                "responses": {
                    "200": {
                        "$ref": "#/responses/GetPostResponse"
                    },
                    "404": {
                        "description": "Post does not exists"
                    }
                }


            }

        },
        "/posts/more_positive_reactions/v1/": {
            "get": {
                "operationId": "get_posts_with_more_positive_reactions",
                "summary": "posts with having more positive reactions",
                "description": "we are getting post ids which having more positive reactions",
                "responses": {
                    "200": {
                        "$ref": "#/responses/GetPostWithPositiveReactionsResponse"
                    }
                }
            }

        },
        "/posts/{post_id}/reactions/v1/": {
            "get": {
                "operationId": "get_reactions_to_post",
                "summary": "reaction to post",
                "description": " reacttion to post",
                "parameters": [{
                    "$ref": "#/parameters/PostIdPathParameters"
                }],
                "responses": {
                    "200": {
                        "$ref": "#/responses/GetPostReactionsResponse"
                    },
                    "404": {
                        "description": "Post does not exists"
                    }
                }
            }

        },
        "/users/posts/reacted/v1/": {
            "get": {
                "operationId": "get_posts_reacted_by_user",
                "summary": "posts reacted by user",
                "description": " returns list of posts ids",
                "parameters": [],
                "responses": {
                    "200": {
                        "$ref": "#/responses/GetPostsReactedByUserResponse"
                    },
                    "404": {
                        "description": "User does not exists"
                    }
                }
            }

        },
        "/users/posts/v1/": {
            "get": {
                "operationId": "get_user_posts",
                "summary": "get posts of user",
                "description": " returns list of post details in dict",
                "parameters": [
                    {
                        "$ref": "#/parameters/MinimumValueQueryParameter"
                    },
                    {
                        "$ref": "#/parameters/MaximumValueQueryParameter"
                    }
                ],
                "responses": {
                    "200": {
                        "$ref": "#/responses/GetUserPostsResponse"
                    },
                    "404": {
                        "description": "User does not exists"
                    }
                }
            }

        },
        "/posts/{post_id}/metrics/v1/": {
            "get": {
                "operationId": "get_reaction_metrics",
                "summary": "get reaction metrics of post",
                "description": " return list of reaction metrics",
                "parameters": [{
                    "$ref": "#/parameters/PostIdPathParameters"
                }],
                "responses": {
                    "200": {
                        "$ref": "#/responses/GetReactionMetricsOfPostResponse"
                    },
                    "404": {
                        "description": "Post does not exists"
                    }
                }
            }

        },
        "/comments/{comment_id}/replies/v1/": {
            "get": {
                "operationId": "get_replies_for_comment",
                "summary": "get replies",
                "description": " get replies",
                "parameters": [{
                    "$ref": "#/parameters/CommentIdPathParameters"
                }],
                "responses": {
                    "200": {
                        "$ref": "#/responses/GetRepliesForCommentResponse"
                    },
                    "404": {
                        "description": "Comment does not exists"
                    }
                }
            }

        }

    }
}
