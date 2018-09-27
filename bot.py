from libs import ch
import mlb.mlb
import mlb.mlb_data
import mlbgame
import commands
import smartbot

bot_account = "hackeybot"
bot_password = "matts4selke"

class bot(ch.RoomManager):

    def onMessage(self, room, user, message):
        try:
            cmd, args, player = message.body.split(" ", 2)
        except:
            try:
                cmd, args = message.body.split(" ", 1)
                player = None
            except:
                    cmd = message.body
                    args = None
                    player = None
        if cmd == "@"+bot_account and args != "" and player == None:
            response = smartbot.get_response(args)
            room.message("@"+user.name + " " + response)
        elif cmd == "@"+bot_account and args != "" and player != "":
            message = args + " " + player
            response = smartbot.get_response(message)
            room.message("@"+user.name + " " + response)
        if cmd[0] == "!":
            prfx = True
            cmd = cmd[1:]
        elif cmd[0] == '$' or cmd[0] == '#':
            prfx = True
        else:
            prfx = False
        if prfx:
            room.message(commands.get_message_from_command(cmd, args, player))
            print(cmd,args,player)

# Testing room
# rooms = ["testingbotfam"]

rooms = ["nym69", "nym70", "nym71", "bb6969", "bluejays69",  "testingbotfam"]
username = bot_account
password = bot_password

bot.easy_start(rooms,username,password)
