import echo_bot


def init_bot(bot):
    bot.polling()


if __name__ == '__main__':
    print('Bot polling...')
    init_bot(echo_bot.bot)
 