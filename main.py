# -*- coding: utf-8 -*
from IRreceiver import *
def MP3_player(): 
    import pygame,sys
    from time import sleep

    pygame.init()
    pygame.mixer.init() 
    pygame.time.delay(1000)

    music_volume = 50
    pygame.mixer.music.set_volume(music_volume/100.0)

    path = "/home/pi/Music/"
    FilePath = [path + "Disney_ColoursOfTheWind.mp3",
                path + "Eason_BesideYou.mp3",
                path + "F.I.R_Freedom.mp3",
                path + "Fanfan_Let'sGo.mp3",
                path + "Jay_LoveBallon.mp3",
                path + "JJLin_ThoseWereTheDays.mp3",
                path + "JJLin_YouNMe.mp3",
                path + "Kite.mp3",
                path + "Marshmallow_100SunAndMoon.mp3",
                path + "MayDay_Cheer.mp3",
                path + "MayDay_StarSky.mp3",
                path + "OneDirection_WhatMakesYouBeautiful.mp3",
                path + "OwlCity_WhenCanISeeYouAgain.mp3",
                path + "SHE_When we are young.mp3",
                path + "SodaGreen_WhenWeWalkTogether.mp3"]
    FileName = ["01 - Disney_Colours of the wind",
                "02 - 陳奕迅_讓我留在你身邊",
                "03 - F.I.R.飛兒樂團_自由之歌",
                "04 - 范瑋琪_啟程",
                "05 - 周杰倫_告白氣球",
                "06 - 林俊傑_那些你很冒險的夢",
                "07 - 林俊傑_因你而在",
                "08 - 風箏",
                "09 - 棉花糖_100個太陽月亮",
                "10 - 五月天_乾杯",
                "11 - 五月天_星空",
                "12 - One Direction_What Makes You Beautiful",
                "13 - Owl City_When Can I See You Again",
                "14 - SHE_我們曾是少年",
                "15 - 蘇打綠_當我們一起走過"]

    pygame.mixer.music.load(FilePath[0])
    pygame.mixer.music.play()
    print("------------------------------------------")
    print(FileName[0])
    
    number = ""
    index = 0
    pre_index = index
    check = True
    select_check = False

    while True:
        try:
            Out = IR.nextcode()     # non-block , 欲改為block則至IRreceiver.py , 將"set_blocking"函式註解即可
            if(len(Out)!=0):
                #print (Out[0])
                #number input
                if("BUT" in Out[0]):
                    if(select_check == False):
                        print("------------------------------------------")
                        select_check = True
                    print(Out[0].split("_")[1])
                    number = number + Out[0].split("_")[1]
                #Check Button
                elif(Out[0] == "EQ"): 
                    print("SELECT")
                    index = int(number) - 1
                    if(index > len(FilePath) - 1 or index < 0):
                        print("------------------------------------------")
                        print("No this chapter,select error")
                    else:
                        pygame.mixer.music.load(FilePath[index])
                        pygame.mixer.music.play()
                        print("------------------------------------------")
                        print(FileName[index])
                    number = ""
                #Previous Song
                elif(Out[0] == "PREV"):
                    print("------------------------------------------")
                    print("Previous Song")
                    if(index != 0):
                        index = index - 1
                    else:
                        index = 14
                    pygame.mixer.music.load(FilePath[index])
                    pygame.mixer.music.play()
                    print(FileName[index])
                #Next Song
                elif(Out[0] == "NEXT"):
                    print("------------------------------------------")
                    print("Next Song")
                    if(index != 14):
                        index = index + 1
                    else:
                        index = 0
                    pygame.mixer.music.load(FilePath[index])
                    pygame.mixer.music.play()
                    print(FileName[index])
                #Volume Down
                elif(Out[0] == "VOL_DWN"):
                    if(music_volume > 10):
                        music_volume = music_volume - 10
                    pygame.mixer.music.set_volume(music_volume/100.0)
                    print("------------------------------------------")
                    print("Now volume:" + str(music_volume/10))
                #Volume Up
                elif(Out[0] == "VOL_UP"):
                    if(music_volume < 100):
                        music_volume = music_volume + 10
                    pygame.mixer.music.set_volume(music_volume/100.0)
                    print("------------------------------------------")
                    print("Now volume:" + str(music_volume/10))
                #Play Pause
                elif(Out[0] == "PLAY"):
                    if(check):
                        print("------------------------------------------")
                        print("Pause")
                        pygame.mixer.music.pause() 
                        check = False
                    else:
                        print("------------------------------------------")
                        print("Play")
                        pygame.mixer.music.unpause()
                        check = True
                #Exit MP3
                elif(Out[0] == "CHAN_SEL"):
                    pygame.mixer.music.stop()
                    seven_segment(10)
                    break
            #自動播放下一首         
            if(pygame.mixer.music.get_busy() == 0 and check == True):
                if(index != 14):
                    index = index + 1
                else:
                    index = 0
                pygame.mixer.music.load(FilePath[index])
                pygame.mixer.music.play()
                print("------------------------------------------")
                print(FileName[index])
                
            if(index < 9 and index >= 0):
                seven_segment(index + 1)
                sleep(1)
                seven_segment(10)
                sleep(0.7)
            else:
                seven_segment(1)
                sleep(0.7)
                buffer = index - 9
                seven_segment(buffer)
                sleep(0.7)
                seven_segment(10)
                sleep(0.5)
                
        except Exception as e:
            print ('\n\nEnd of IR receiver.\n')
            print(e)
            break

def Music_Game():
    import random
    import pygame,sys
    import RPi.GPIO as GPIO
    from time import sleep

    pygame.init()
    pygame.mixer.init() 
    pygame.time.delay(1000)
    music_volume = 50
    pygame.mixer.music.set_volume(music_volume/100.0)

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    path = "/home/pi/Music/Questions/"
    FilePath = [path + "告白氣球.mp3",
                path + "WhatsMakeYouBeautiful.mp3",
                path + "一百個太陽月亮.mp3",
                path + "乾杯.mp3",
                path + "ColorsOfTheWind.mp3",
                path + "WhenCanISeeYouAgain.mp3",
                path + "啟程.mp3",
                path + "那些妳很冒險的夢.mp3",
                path + "朋友.mp3",
                path + "紅蜻蜓.mp3"]
    
    sound_path = "/home/pi/Music/Sounds/"
    Sound_FilePath = [sound_path + "small_win.mp3",
                      sound_path + "small_lose.mp3",
                      sound_path + "big_win.mp3",
                      sound_path + "big_lose.mp3"]
    
    led = [2, 3, 7, 12, 16]    
    button_red = 14
    button_green = 15
    button_blue = 23
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(button_red ,GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(button_green ,GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(button_blue ,GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
    #GPIO.PUD_DOWN 下拉電阻(0)

    for index in range(0,5):
        GPIO.output(led[index], True)

    pre_red = 0
    pre_green = 0
    pre_blue = 0

    count = 1
    lose_time = 0

    question_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    #Question
    while True:        
        red = False
        green = False
        blue = False
        red_answer = False
        green_answer = False
        blue_answer = False
        
        answer_index = random.randint(min(question_list),max(question_list))
        while(answer_index not in question_list):
            answer_index = random.randint(min(question_list),max(question_list))
        question_list.remove(answer_index)
            
        pygame.mixer.music.load(FilePath[answer_index])
        pygame.mixer.music.play()
        print("------------------------------------------")
        print("Question" + str(count) + ":")
        if(count != 10):
            seven_segment(count)
        else:
            seven_segment(0)
        count = count + 1 
        
        color = Random_Answer_Array(answer_index)
            
        if(color == 1):
            red_answer = True
        elif(color == 2):
            green_answer = True
        elif(color == 3):
            blue_answer = True

        while True:
            state_red = GPIO.input(button_red)
            if((not pre_red) and state_red):
                print("Select 1")
                red = True
            pre_red = state_red

            state_green = GPIO.input(button_green)
            if((not pre_green) and state_green):
                print("Select 2")
                green = True
            pre_green = state_green

            state_blue = GPIO.input(button_blue)
            if((not pre_blue) and state_blue):
                print("Select 3")
                blue = True
            pre_blue = state_blue

            if(red or green or blue):
                break

        R = red and red_answer
        G = green and green_answer
        B = blue and blue_answer

        if(R or G or B):
            if(count < 11):
                pygame.mixer.music.stop()
                pygame.mixer.music.load(Sound_FilePath[0])
                pygame.mixer.music.play()
        else:
            GPIO.output(led[lose_time], False)
            lose_time = lose_time + 1
            if(lose_time == 5):
                print("輸了TAT 下次再來挑戰吧!")
                pygame.mixer.music.stop()
                pygame.mixer.music.load(Sound_FilePath[3])
                pygame.mixer.music.play()
                sleep(3.5)
                break
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(Sound_FilePath[1])
                pygame.mixer.music.play()

        if(count == 11 and lose_time < 5):
            print("Winner~ 你是音樂小曲庫:3")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(Sound_FilePath[2])
            pygame.mixer.music.play()
            sleep(6.5)
            break
        sleep(2)
                
def Random_Answer_Array(answer_index):
    import random
    FileName = ["周杰倫_告白氣球",
                "One Direction_What Makes You Beautiful",
                "棉花糖_一百個太陽月亮",
                "五月天_乾杯",
                "Disney_Colours of the wind",
                "Owl City_When Can I See You Again",
                "范瑋琪_啟程",
                "林俊傑_那些你很冒險的夢",
                "周華健_朋友",
                "小虎隊_紅蜻蜓"]

    buffer_index_1 = random.randint(0,7)
    while(buffer_index_1 == answer_index):
        buffer_index_1 = random.randint(0,7)
    buffer_index_2 = random.randint(0,7)
    while(buffer_index_2 == answer_index or buffer_index_2 == buffer_index_1):
        buffer_index_2 = random.randint(0,7)

    category = random.randint(0,5)
    
    if(category == 0):
        print("1." + FileName[answer_index])
        print("2." + FileName[buffer_index_1])
        print("3." + FileName[buffer_index_2])
        color = 1 #Red
    elif(category == 1):
        print("1." + FileName[answer_index])
        print("2." + FileName[buffer_index_2])
        print("3." + FileName[buffer_index_1])
        color = 1 #Red
    elif(category == 2):
        print("1." + FileName[buffer_index_1])
        print("2." + FileName[answer_index])
        print("3." + FileName[buffer_index_2])
        color = 2 #Green
    elif(category == 3):
        print("1." + FileName[buffer_index_1])
        print("2." + FileName[buffer_index_2])
        print("3." + FileName[answer_index])
        color = 3 #Blue
    elif(category == 4):
        print("1." + FileName[buffer_index_2])
        print("2." + FileName[answer_index])
        print("3." + FileName[buffer_index_1])
        color = 2 #Green
    elif(category == 5):
        print("1." + FileName[buffer_index_2])
        print("2." + FileName[buffer_index_1])
        print("3." + FileName[answer_index])
        color = 3 #Blue
    return color

def seven_segment(number):
    import RPi.GPIO as GPIO
    from time import sleep

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

          # 0  1  2  3  4  5  6 7
          # a  b  c  d  e  f  g h
    led = [17,27,22,26,18,20,25,19]
    for index in range(0,8):
        GPIO.setup(led[index],GPIO.OUT)

    if(number == 0):
        GPIO.output(led[0],True)
        GPIO.output(led[1],True)
        GPIO.output(led[2],True)
        GPIO.output(led[3],True)
        GPIO.output(led[4],True)
        GPIO.output(led[5],True)
        GPIO.output(led[6],False)
        GPIO.output(led[7],False)
    elif(number == 1):
        GPIO.output(led[0],False)
        GPIO.output(led[1],True)
        GPIO.output(led[2],True)
        GPIO.output(led[3],False)
        GPIO.output(led[4],False)
        GPIO.output(led[5],False)
        GPIO.output(led[6],False)
        GPIO.output(led[7],False)
    elif(number == 2):
        GPIO.output(led[0],True)
        GPIO.output(led[1],True)
        GPIO.output(led[2],False)
        GPIO.output(led[3],True)
        GPIO.output(led[4],True)
        GPIO.output(led[5],False)
        GPIO.output(led[6],True)
        GPIO.output(led[7],False)
    elif(number == 3):
        GPIO.output(led[0],True)
        GPIO.output(led[1],True)
        GPIO.output(led[2],True)
        GPIO.output(led[3],True)
        GPIO.output(led[4],False)
        GPIO.output(led[5],False)
        GPIO.output(led[6],True)
        GPIO.output(led[7],False)
    elif(number == 4):
        GPIO.output(led[0],False)
        GPIO.output(led[1],True)
        GPIO.output(led[2],True)
        GPIO.output(led[3],False)
        GPIO.output(led[4],False)
        GPIO.output(led[5],True)
        GPIO.output(led[6],True)
        GPIO.output(led[7],False)
    elif(number == 5):
        GPIO.output(led[0],True)
        GPIO.output(led[1],False)
        GPIO.output(led[2],True)
        GPIO.output(led[3],True)
        GPIO.output(led[4],False)
        GPIO.output(led[5],True)
        GPIO.output(led[6],True)
        GPIO.output(led[7],False)
    elif(number == 6):
        GPIO.output(led[0],True)
        GPIO.output(led[1],False)
        GPIO.output(led[2],True)
        GPIO.output(led[3],True)
        GPIO.output(led[4],True)
        GPIO.output(led[5],True)
        GPIO.output(led[6],True)
        GPIO.output(led[7],False)
    elif(number == 7):
        GPIO.output(led[0],True)
        GPIO.output(led[1],True)
        GPIO.output(led[2],True)
        GPIO.output(led[3],False)
        GPIO.output(led[4],False)
        GPIO.output(led[5],False)
        GPIO.output(led[6],False)
        GPIO.output(led[7],False)
    elif(number == 8):
        GPIO.output(led[0],True)
        GPIO.output(led[1],True)
        GPIO.output(led[2],True)
        GPIO.output(led[3],True)
        GPIO.output(led[4],True)
        GPIO.output(led[5],True)
        GPIO.output(led[6],True)
        GPIO.output(led[7],False)
    elif(number == 9):
        GPIO.output(led[0],True)
        GPIO.output(led[1],True)
        GPIO.output(led[2],True)
        GPIO.output(led[3],True)
        GPIO.output(led[4],False)
        GPIO.output(led[5],True)
        GPIO.output(led[6],True)
        GPIO.output(led[7],False)
    else:
        GPIO.output(led[0],False)
        GPIO.output(led[1],False)
        GPIO.output(led[2],False)
        GPIO.output(led[3],False)
        GPIO.output(led[4],False)
        GPIO.output(led[5],False)
        GPIO.output(led[6],False)
        GPIO.output(led[7],False)

#main
print("柏瑄與廣仲的音樂小世界ˊˇˋ")
while True:
    print("------------------------------------------")
    print("1.音樂播放器")
    print("2.猜歌小遊戲")
    print("3.離開音樂小世界囉")
    while True:
        try:
            choice = int(input("請輸入你想去哪裡:"))
            if(choice != 1 and choice != 2 and choice != 3):
                print("Error input! It's out of range!")
            else:
                break
        except NameError:
            seven_segment(10)
            print("Error input! It's not a number!!!")

    if(choice == 1):
        MP3_player()
    elif(choice == 2):
        Music_Game()
    elif(choice == 3):
        break
























