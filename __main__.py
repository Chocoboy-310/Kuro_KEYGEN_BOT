import telegram
import mysql.connector

# Initialize Telegram Bot
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Initialize MySQL connection
db = mysql.connector.connect(
    host='75.119.138.236',
    user='darkespy_esp',
    password='vignesh799#',
    database='darkespy_dark'
)

# Create a cursor
cursor = db.cursor()

# Define a command to generate a string
def generate_string(update, context):
    # Generate your string
    generated_string = "Your generated string"

    # Insert the string into the database
    sql = "INSERT INTO your_table_name (string) VALUES (%s)"
    val = (generated_string,)
    cursor.execute(sql, val)
    db.commit()

    # Send the generated string as a response
    update.message.reply_text(generated_string)

# Set up the command handler
from telegram.ext import CommandHandler
dp = updater.dispatcher
dp.add_handler(CommandHandler('generatestring', generate_string))

# Start the bot
updater.start_polling()
updater.idle()
