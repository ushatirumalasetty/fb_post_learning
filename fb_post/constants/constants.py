from enum import Enum

class ReactionChoices(Enum):
    WOW = 'WOW'
    LIT = 'LIT'
    LOVE = 'LOVE'
    HAHA = 'HAHA'
    THUMBS_UP = 'THUMBS-UP'
    THUMBS_DOWN = 'THUMBS-DOWN'
    ANGRY = 'ANGRY'
    SAD = 'SAD'



users_list=[
        {'name':'sulthan',      'profile_pic':'sulthan_babu/profile_pic'},
        {'name':'randy orton',  'profile_pic':'randyorton/profile_pic'},
        {'name':'elon musk',     'profile_pic':'elonmusk/profile_pic'},
        {'name':'sravani',      'profile_pic':'sravani/profile_pic'},
        {'name':'che quevara',  'profile_pic':'chequeara/profile_pic'},
        {'name':'shajahan',     'profile_pic':'shajahan/profile_pic'}
    ]

posts_list=[
        {'posted_by_id':1, 'content':'empty'},
        {'posted_by_id':1, 'content':'empty'},
        {'posted_by_id':2, 'content':'empty3'},
        {'posted_by_id':2, 'content':'empty4'},
        {'posted_by_id':3, 'content':'empty5'},
        {'posted_by_id':3, 'content':'empty6'},
        {'posted_by_id':4, 'content':'empty7'},
        {'posted_by_id':4, 'content':'empty8'},
        {'posted_by_id':5, 'content':'empty9'},
        {'posted_by_id':1, 'content':'empty'}
    
    ]

comments_list=[
        {'commented_by_id':3,'post_id':1,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':1,'post_id':1,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':3,'post_id':1,'content':'this is comment','parent_comment_id':2},
        {'commented_by_id':4,'post_id':1,'content':'this is comment','parent_comment_id':1},
        {'commented_by_id':5,'post_id':3,'content':'this is comment','parent_comment_id':1},
        {'commented_by_id':2,'post_id':3,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':3,'post_id':4,'content':'this is comment','parent_comment_id':5},
        {'commented_by_id':5,'post_id':2,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':5,'post_id':2,'content':'this is comment','parent_comment_id':8}
    ]
    
reactions_list=[
    {'reacted_by_id':1,'post_id':1,'comment_id':None,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':5,'post_id':1,'comment_id':None,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':3,'post_id':1,'comment_id':None,'reaction':ReactionChoices.LOVE.value},
    {'reacted_by_id':4,'post_id':1,'comment_id':None,'reaction':ReactionChoices.SAD.value},
    
    {'reacted_by_id':3,'post_id':2,'comment_id':None,'reaction':ReactionChoices.ANGRY.value},
    {'reacted_by_id':4,'post_id':3,'comment_id':None,'reaction':ReactionChoices.SAD.value},
    
    {'reacted_by_id':5,'post_id':4,'comment_id':None,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':5,'post_id':4,'comment_id':None,'reaction':ReactionChoices.WOW.value},
    
    {'reacted_by_id':3,'post_id':7,'comment_id':None,'reaction':ReactionChoices.THUMBS_UP.value},
    
    {'reacted_by_id':6,'post_id':9,'comment_id':None,'reaction':ReactionChoices.HAHA.value},
    {'reacted_by_id':4,'post_id':9,'comment_id':None,'reaction':ReactionChoices.THUMBS_DOWN.value},
    
    
    
    {'reacted_by_id':1,'post_id':None,'comment_id':1,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':5,'post_id':None,'comment_id':1,'reaction':ReactionChoices.LOVE.value},
    {'reacted_by_id':3,'post_id':None,'comment_id':1,'reaction':ReactionChoices.LOVE.value},
    {'reacted_by_id':4,'post_id':None,'comment_id':1,'reaction':ReactionChoices.SAD.value},
    
    {'reacted_by_id':3,'post_id':None,'comment_id':2,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':4,'post_id':None,'comment_id':3,'reaction':ReactionChoices.ANGRY.value},
    {'reacted_by_id':5,'post_id':None,'comment_id':4,'reaction':ReactionChoices.LIT.value},
]


class ConstantDicts(Enum):
    actual_post = {
                   "post_id": 1,
                   "posted_by": {
                      "name": "sulthan",
                      "user_id": 1,
                      "profile_pic": "sulthan_babu/profile_pic"
                   },
                   "posted_at": "2012-01-14 00:00:00.000000",
                   "post_content": "empty",
                   "reactions": {
                      "count": 4,
                      "type": [
                         "LOVE",
                         "SAD",
                         "WOW"
                      ]
                   },
                   "comments": [
                      {
                         "comment_id": 1,
                         "commenter": {
                            "user_id": 3,
                            "name": "elon musk",
                            "profile_pic": "elonmusk/profile_pic"
                         },
                         "commented_at": "2012-01-14 00:00:00.000000",
                         "comment_content": "this is comment",
                         "reactions": {
                            "count": 4,
                            "type": [
                               "LOVE",
                               "SAD",
                               "WOW"
                            ]
                         },
                         "replies_count": 1,
                         "replies": [
                            {
                               "comment_id": 4,
                               "commenter": {
                                  "user_id": 4,
                                  "name": "sravani",
                                  "profile_pic": "sravani/profile_pic"
                               },
                               "commented_at": "2012-01-14 00:00:00.000000",
                               "comment_content": "this is comment",
                               "reactions": {
                                  "count": 1,
                                  "type": [
                                     "LIT"
                                  ]
                               }
                            }
                         ]
                      },
                      {
                         "comment_id": 2,
                         "commenter": {
                            "user_id": 1,
                            "name": "sulthan",
                            "profile_pic": "sulthan_babu/profile_pic"
                         },
                         "commented_at": "2012-01-14 00:00:00.000000",
                         "comment_content": "this is comment",
                         "reactions": {
                            "count": 1,
                            "type": [
                               "WOW"
                            ]
                         },
                         "replies_count": 1,
                         "replies": [
                            {
                               "comment_id": 3,
                               "commenter": {
                                  "user_id": 3,
                                  "name": "elon musk",
                                  "profile_pic": "elonmusk/profile_pic"
                               },
                               "commented_at": "2012-01-14 00:00:00.000000",
                               "comment_content": "this is comment",
                               "reactions": {
                                  "count": 1,
                                  "type": [
                                     "ANGRY"
                                  ]
                               }
                            }
                         ]
                      }
                   ],
                   "comments_count": 2
        }
    user_original_posts = [
               {
                  "post_id": 1,
                  "posted_by": {
                     "name": "sulthan",
                     "user_id": 1,
                     "profile_pic": "sulthan_babu/profile_pic"
                  },
                  "posted_at": "2012-01-14 00:00:00.000000",
                  "post_content": "empty",
                  "reactions": {
                     "count": 4,
                     "type": [
                        "LOVE",
                        "SAD",
                        "WOW"
                     ]
                  },
                  "comments": [
                     {
                        "comment_id": 1,
                        "commenter": {
                           "user_id": 3,
                           "name": "elon musk",
                           "profile_pic": "elonmusk/profile_pic"
                        },
                        "commented_at": "2012-01-14 00:00:00.000000",
                        "comment_content": "this is comment",
                        "reactions": {
                           "count": 4,
                           "type": [
                              "LOVE",
                              "SAD",
                              "WOW"
                           ]
                        },
                        "replies_count": 1,
                        "replies": [
                           {
                              "comment_id": 4,
                              "commenter": {
                                 "user_id": 4,
                                 "name": "sravani",
                                 "profile_pic": "sravani/profile_pic"
                              },
                              "commented_at": "2012-01-14 00:00:00.000000",
                              "comment_content": "this is comment",
                              "reactions": {
                                 "count": 1,
                                 "type": [
                                    "LIT"
                                 ]
                              }
                           }
                        ]
                     },
                     {
                        "comment_id": 2,
                        "commenter": {
                           "user_id": 1,
                           "name": "sulthan",
                           "profile_pic": "sulthan_babu/profile_pic"
                        },
                        "commented_at": "2012-01-14 00:00:00.000000",
                        "comment_content": "this is comment",
                        "reactions": {
                           "count": 1,
                           "type": [
                              "WOW"
                           ]
                        },
                        "replies_count": 1,
                        "replies": [
                           {
                              "comment_id": 3,
                              "commenter": {
                                 "user_id": 3,
                                 "name": "elon musk",
                                 "profile_pic": "elonmusk/profile_pic"
                              },
                              "commented_at": "2012-01-14 00:00:00.000000",
                              "comment_content": "this is comment",
                              "reactions": {
                                 "count": 1,
                                 "type": [
                                    "ANGRY"
                                 ]
                              }
                           }
                        ]
                     }
                  ],
                  "comments_count": 2
               },
               {
                  "post_id": 2,
                  "posted_by": {
                     "name": "sulthan",
                     "user_id": 1,
                     "profile_pic": "sulthan_babu/profile_pic"
                  },
                  "posted_at": "2012-01-14 00:00:00.000000",
                  "post_content": "empty",
                  "reactions": {
                     "count": 1,
                     "type": [
                        "ANGRY"
                     ]
                  },
                  "comments": [
                     {
                        "comment_id": 8,
                        "commenter": {
                           "user_id": 5,
                           "name": "che quevara",
                           "profile_pic": "chequeara/profile_pic"
                        },
                        "commented_at": "2012-01-14 00:00:00.000000",
                        "comment_content": "this is comment",
                        "reactions": {
                           "count": 0,
                           "type": []
                        },
                        "replies_count": 1,
                        "replies": [
                           {
                              "comment_id": 9,
                              "commenter": {
                                 "user_id": 5,
                                 "name": "che quevara",
                                 "profile_pic": "chequeara/profile_pic"
                              },
                              "commented_at": "2012-01-14 00:00:00.000000",
                              "comment_content": "this is comment",
                              "reactions": {
                                 "count": 0,
                                 "type": []
                              }
                           }
                        ]
                     }
                  ],
                  "comments_count": 1
               },
               {
                  "post_id": 10,
                  "posted_by": {
                     "name": "sulthan",
                     "user_id": 1,
                     "profile_pic": "sulthan_babu/profile_pic"
                  },
                  "posted_at": "2012-01-14 00:00:00.000000",
                  "post_content": "empty",
                  "reactions": {
                     "count": 0,
                     "type": []
                  },
                  "comments": [],
                  "comments_count": 0
               }
            ]
    original_replies_list_for_comment = [
                            {'comment_id': 4, 
                            'commenter': {
                                'user_id': 4, 
                                'name': 'sravani', 
                                'profile_pic': 'sravani/profile_pic'
                                },
                            'commented_at': '2012-01-14 00:00:00.000000', 
                            'comment_content': 'this is comment'
                                
                            },
                            
                            {
                            'comment_id': 5,
                            'commenter': {
                                'user_id': 5, 
                                'name': 'che quevara', 
                                'profile_pic': 'chequeara/profile_pic'
                                }, 
                            'commented_at': '2012-01-14 00:00:00.000000',
                            'comment_content': 'this is comment'
                                }
                ]
    original_user_reactions_of_post = [
                                {
                                'user_id': 1, 'name': 'sulthan', 
                                'profile_pic': 'sulthan_babu/profile_pic', 
                                'reaction': 'WOW'
                                }, 
                                
                                {
                                'user_id': 5, 'name': 'che quevara', 
                                'profile_pic': 'chequeara/profile_pic', 
                                'reaction': 'WOW'
                                },
                                {
                                'user_id': 3, 'name': 'elon musk', 
                                'profile_pic': 'elonmusk/profile_pic',
                                'reaction': 'LOVE'
                                }, 
                                {
                                'user_id': 4, 'name': 'sravani',
                                'profile_pic': 'sravani/profile_pic', 
                                'reaction': 'SAD'
                                }
                     ]
  