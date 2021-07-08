## Resources 
# https://unicode.org/emoji/charts/full-emoji-list.html
# https://stackoverflow.com/questions/49327296/how-can-i-write-bold-in-python-telegram-bot
# https://trumail.io/


import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update ,User, ParseMode ,ForceReply, KeyboardButton ,ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext , Filters , MessageHandler
import requests
import telegram
from TempMail import temp
import time


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_chat_id(update:Update, _:CallbackContext):
    chat_id = -1

    if update.message is not None:
        chat_id = update.message.chat.id
    elif update.callback_query is not None:
        chat_id = update.callback_query.message.chat.id
    elif update.poll is not None:
        chat_id = _.bot_data[update.poll.id]

    return chat_id

def start(update: Update, _: CallbackContext) -> None:
    user = update.message.from_user
    print(user)
    update.message.reply_text((f'Hello\U0001F44B <b>{user.first_name}</b>, \nWelcome to Temp-e-mail\U0001F916. I can help you by generating login details for websites you dont want to share data with'
                               '\n\nI can generate <b>Name, Temporary valid email & Password.</b>'),parse_mode=ParseMode.HTML) 
    keyboard = [
        [
            KeyboardButton("Name"),
            KeyboardButton("Password"),
            KeyboardButton("Email"),
        ],
        [KeyboardButton("Get all three!")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True) 
    update.message.reply_text('Please choose:', reply_markup=reply_markup)                     

def button(update: Update, _: CallbackContext) -> None:
    query = update.message.text
    print(query)

    add_typing(update,_)

    if query == 'Name':
        msg = temp.generateNames()
        update.message.reply_text(f" {msg}",parse_mode=ParseMode.HTML)
    
    elif query == "Password":
        msg = temp.generatePassword(8)
        update.message.reply_text(f"{msg}")

    elif query == 'Email':
        email , email_url = temp.generateEmailIdAndLink()
        update.message.reply_text(f'Email : {email}')
        update.message.reply_text(f'Click here to access your 10min email: {email_url}')

    
    elif query == "Get all three!":
        name = temp.generateNames()
        password = temp.generatePassword(8)
        email , email_url = temp.generateEmailIdAndLink()
        update.message.reply_text(f'{name}')
        update.message.reply_text(f'{password}')
        update.message.reply_text(f'{email}')
        update.message.reply_text(f'{email_url}')
        #msg = f'<b>UserName :</b>{name}\n<b>Password :</b>{password}\n<b>email :</b>{email}\n<b>Link to email : {email_url}</b>'
    else :
        msg = 'Invalid Option, Please choose from the option available!'
        update.message.reply_text(msg)
    
    

def get_name(update:Update, _: CallbackContext) -> None:
    name = temp.generateNames()
    update.message.reply_text('Here is the a name')
    update.message_reply_text(name)

def get_password(update:Update, _: CallbackContext) -> None:
    password = temp.generatePassword(8)
    update.message.reply_text('Here is the a random password')
    update.message_reply_text(password)
    

def get_email(update:Update, _: CallbackContext) -> None:
    email, email_link = temp.generateEmailIdAndLink()


def add_typing(update: Update, _: CallbackContext) -> None:
    _.bot.send_chat_action(chat_id=get_chat_id(update,_), action=telegram.ChatAction.TYPING, timeout=1)
    time.sleep(1)
    

def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("") #API Token here

    updater.dispatcher.add_handler(CommandHandler('start', start))
    #updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, button))
    
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

#app = main()

if __name__ == '__main__':
    main()
