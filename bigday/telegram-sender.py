# import time
# import schedule
import requests


def telegram_bot_sendtext(bot_message):
    
    bot_token = "1421246533:AAFfDG-UkW4WbwGxSAcbRhDwUrZN492-LhA"
    bot_chatID = "-425483778"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()



test = telegram_bot_sendtext("Testing Telegram bot")
print(test)

# def report():
#     # my_balance = 10   ## Replace this number with an API call to fetch your account balance
#     my_message = "Current balance is:"   ## Customize your message
#     telegram_bot_sendtext(my_message)
#     print(my_message)

print("End")

# def external(request):
#     inp=request.POST.get('keyword')
#     out= run([sys.executable, 'telegram-sender.py' ,inp],shell=False, stdout=PIPE)
#     print(out)
#     return render(request, 'home.html',{'data':data})


# print(my_message)
    
# schedule.every().day.at("12:00").do(report)

# while True:
#     schedule.run_pending()
#     time.sleep(1)