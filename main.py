import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Бот увійшов як {bot.user}')

# Команда для масового бану
@bot.command()
@commands.has_permissions(administrator=True)  # Перевірка на права адміністратора
async def mass_ban(ctx):
    try:
        # Підтвердження перед початком
        await ctx.send("Напиши 'yes' зоб забанити всіх учасників сервера ")

        def check(m):
            return m.author == ctx.author and m.content.lower() == "yes"

        await bot.wait_for("message", check=check, timeout=30)

        # Бан усіх учасників, окрім бота та автора команди
        for member in ctx.guild.members:
            if member != ctx.author and not member.bot:
                try:
                    await member.ban(reason="Масовий бан за запитом адміністратора.")
                    print(f"{member.name} забанений.")
                except Exception as e:
                    print(f"Не вдалося забанити {member.name}: {e}")
        await ctx.send("Масовий бан завершено.")
    except Exception as e:
        await ctx.send(f"Сталася помилка: {e}")

# Запуск бота
bot.run('YOU BOT TOKEN')
