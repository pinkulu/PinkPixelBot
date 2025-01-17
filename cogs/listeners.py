import asyncio
import datetime
import io
import time

import discord
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.ext import commands


class Listeners(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 681561708052873358:
            if self.bot.user.id == 756153198456340511:
                channel = self.bot.get_channel(681911212740575297)
                img = Image.open("Member.png")
                img2 = Image.open(requests.get(member.avatar_url, stream=True).raw)
                bigger2 = img2.resize((700, 700))
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Minecraftia.ttf",
                                          80)
                fontbig = ImageFont.truetype("Minecraftia.ttf",
                                             200)
                img.paste(bigger2, (900, 600))
                draw.text((600, 0), "A New Member Has Joined", (0, 255, 0), font=font)
                draw.text((900, 200), f"{member}", (0, 255, 0), font=font)
                draw.text((300, 400), f"there currently are {len(member.guild.members)} people here", (0, 255, 0), font=font)

                with io.BytesIO() as image_binary:
                    img.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await channel.send(file=discord.File(fp=image_binary, filename='image.png'))
                await channel.send(f"Welcome <@!{member.id}>, Hope you have a good time here ^^")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 681561708052873358:
            if self.bot.user.id == 756153198456340511:
                channel = self.bot.get_channel(681911212740575297)
                img = Image.open("Member.png")
                img2 = Image.open(requests.get(member.avatar_url, stream=True).raw)
                bigger2 = img2.resize((700, 700))
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Minecraftia.ttf",
                                          80)
                fontbig = ImageFont.truetype("Minecraftia.ttf",
                                             200)
                img.paste(bigger2, (900, 600))
                draw.text((600, 0), "Were sad to see you go", (255, 0, 0), font=font)
                draw.text((900, 300), f"{member}", (255, 0, 0), font=font)

                with io.BytesIO() as image_binary:
                    img.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await channel.send(file=discord.File(fp=image_binary, filename='image.png'))

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == f"<@!{self.bot.user.id}>" or msg.content == f"<@{self.bot.user.id}>":
            if self.bot.user.id == 756153198456340511:
                await msg.channel.send(f"My prefix is `pp>` :), you can start by doing `pp>help`")

            else:
                await msg.channel.send(f"My prefix is `pd>` :), you can start by doing `pd>help`"
                                       f" (this is the development bot, some things could not work)")

def setup(bot):
    bot.add_cog(Listeners(bot))
