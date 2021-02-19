import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!pid'):
        content = message.content
        splited = content.split()
        if(len(splited) > 1) :
          array_links = []
          array_links_jpeg =[]
          embed=discord.Embed(color=discord.Color.blue())
          pid = splited[1]
          pid= pid.upper()
          pid = pid.replace("-", "_")
          link_to_send_png = "https://images.nike.com/is/image/DotCom/"
          link_to_send_jpg = "https://images.nike.com/is/image/DotCom/PDP_HERO/JORDAN-"
          end_of_link_png = "_PREM?wid=2000&hei=2000&fmt=png-alpha"
          end_of_link_jpg = "_PREM.jpg?wid=2000&hei=2000"
          array_letters = ['A','B','C','D','E','F','G','H']
          for letter in array_letters:
            final_link = link_to_send_png + pid +'_' + letter + end_of_link_png
            final_link_jpg = link_to_send_jpg + pid +'_' + letter + end_of_link_jpg
            array_links.append("[" + letter + "](" + final_link + ")")
            array_links_jpeg.append("[" + letter +"_JPG](" + final_link_jpg + ")")
          url_E = link_to_send_jpg + pid + '_E' + end_of_link_jpg
          embed.set_image(url=url_E)
          embed.add_field(name='NIKE IMAGES', value="\n".join(array_links), inline=True)
          embed.add_field(name='NIKE IMAGES', value="\n".join(array_links_jpeg), inline=True)

          await message.channel.send(embed=embed)
        else:
            await message.channel.send("You should put a PID !")

client.run('ODA4Mjg2NTE0MDI2NjQzNDU2.YCEVeg.xgB_D7i0RIhwo_f1QzmpxyAff9M')