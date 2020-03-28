import discord
import praw

from discord.ext import commands

bot = commands.Bot(command_prefix='>')

reddit = praw.Reddit(client_id='Wu-95k2TYxo_cg',
                     client_secret='gZ5X5PKYNsHc0nWD68TYOjxzwck',
                     user_agent='discord')




# hot_posts = reddit.subreddit('showerthoughts').hot(limit=1)
# for post in hot_posts:
#     print(post.title)
random_submission = reddit.subreddit('showerthoughts').random()
print(random_submission)
# for submission in reddit.subreddit('showerthoughts').random_rising():
#     print(submission.title)



# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')
# 
# bot.run('NjkzMzM1NTM4OTU4MjA1MDI4.Xn8DgQ.RDuHV18h60oIlL4GPRKTdQjixBM')