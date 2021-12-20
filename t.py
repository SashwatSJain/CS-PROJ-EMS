from discord.ext.commands import Bot

bot = Bot(command_prefix='')
TOKEN = "ODcwNTE0ODEyMDA0NzU3NTU2.YQN4GA.Kb3L26iP-MfPdutRIfKN0OmUYYc"


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.event
async def on_message(message):
    b = message
    a = b.content
    if ("+" in a or "-" in a or "*" in a or "/" in a) and a[0:6] != "answer":
        print(f"message sent : answer : \n{a} = {eval(a)}")
        await message.channel.send(f"answer : \n{a} = {eval(a)}")

    elif message.content.startswith("spam"):
        msg = str(message.content)
        msg = msg.split(" ")
        for x in range(1, int(msg[1]) + 1):
            await message.channel.send(f"{' '.join(msg[2:])}")

    elif message.content.startswith("help"):
        await message.channel.send("possible commands are : \nspam <number of times> <content>\nclean\n")

    elif message.content.startswith("clean"):
        await message.channel.send("|\n"*50)

    # print(b)

bot.run(TOKEN)

