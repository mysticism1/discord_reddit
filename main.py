import discord
import praw
import random

from discord.ext import commands

bot = commands.Bot(command_prefix='~')

reddit = praw.Reddit(client_id='Wu-95k2TYxo_cg',
                     client_secret='gZ5X5PKYNsHc0nWD68TYOjxzwck',
                     user_agent='discord')

sub = reddit.subreddit('showerthoughts')


@bot.command()
async def post(ctx):
    posts = [post for post in sub.hot(limit=100)]
    random_post_number = random.randint(0, 10)
    random_post = posts[random_post_number]
    random_post = random_post.title
    await ctx.send(random_post)


@bot.command()
async def setting(ctx):
    await ctx.send("this is a bot made to boggle with your mind with posts from the r/showerthoughts subreddit")


bot.run('NjkzMzM1NTM4OTU4MjA1MDI4.Xn8DgQ.RDuHV18h60oIlL4GPRKTdQjixBM')