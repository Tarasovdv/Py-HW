from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

def create_field():         
    return ["_"]*9

def create_field_plan():         
    return [str(x) for x in range(1,10)]
        
    
async def print_fiels(update: Update,arr):
    for i in range(0,9,3):
        await update.message.reply_text(arr[i]+" " + arr[i+1] + " " + arr[i+2])
    
def check(arr,n):
    for i in range(0,9,3):
        if arr[i]==arr[i+1]==arr[i+2]==n:
            return "Win"
    for i in range(0,3):
        if arr[i]==arr[i+3]==arr[i+6]==n:
            return "Win"
    if arr[0]==arr[4]==arr[8]==n or arr[2]==arr[4]==arr[6]==n:
        return "Win"  
    return "False"
       
        
    
def append(a,s,arr):
    arr[a-1]=s        
         

        
def check2(arr,n):
      if n>0 and n<10:
          if arr[n-1]=="_":
              return True


     
async def step1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global arr
    global player_1
    global player_2
    arr=create_field()
    await update.message.reply_text ("Player number one: choose a symbol X or 0: ")
    player_1=update.message.text
    if player_1=="X":
            player_2="0"
            help=True
    else:
        player_2="X"
    await update.message.reply_text ("Player number two: your symbol: " +  player_2 +'\n'+ 'lets start!') 
    return (arr, player_1,player_2)
                
    
            
async def player_1(update: Update):
    global player_1_turn
    await update.message.reply_text ("\nPlayer one: Enter number of positoin: ")
    player_1_turn=int(update.message.text)
    if not check2(arr,player_1_turn):
        await update.message.reply_text ("\nPlayer number one, you entered wrong number: Enter number of positoin again: ")
        return
    append(player_1_turn,player_1,arr)
    await update.message.reply_text(print_fiels(arr))
    await win(update)
    
async def player_2(update: Update):
    global player_2_turn
    await update.message.reply_text  ("\nPlayer two: Enter number of positoin: ")
    player_2_turn=int(update.message.text)
    if not check2(arr,player_2_turn):
        await update.message.reply_text ("\nPlayer number two, you entered wrong number: Enter number of positoin again: ")
        # player_2_turn=int(update.message.text)
        return
    append(player_2_turn,player_2,arr)
    await update.message.reply_text(print_fiels(arr))
    await win(update)
            
async def win(update: Update,count):
    if check(arr,player_1)=="Win":
        await update.message.reply_text("Player number one: Congratulations!You win!!")
        exit()
    elif check(arr,player_2)=="Win":
        await update.message.reply_text("Player number two: Congratulations!You win!!")
        exit()
      


    

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await step1(update,context)
    # await player_1(update,context)
    # await player_2(update,context)
   



    
