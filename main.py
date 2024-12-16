import praw

reddit = praw.Reddit(
    client_id="rAIDYUguYJ4f-b17HpRLHg",
    client_secret="DIBIpn74Jx46_eBV82dii7VaZhm14g",
    user_agent="skib skib",
)


x = 0


#goes to r/askreddit and saves the title in title.txxt

for submission in reddit.subreddit("askreddit").hot(limit=1):
    print(submission.title)

    with open("title.txt","w") as f:
        f.write(submission.title)

    



    with open("comments.txt","w") as f:
            
            submission.comments(limit=5)
            for top_level_comment in submission.comments:
                f.write(top_level_comment.body)
                
