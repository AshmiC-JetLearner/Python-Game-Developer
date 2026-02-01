import pgzrun
WIDTH=800
HEIGHT=700
title='Quiz Master'

marquee_box=Rect(0,0 ,800,60 )#Rect(ini_x,ini_y,w,h)
question_box=Rect(20,80 ,500,140)
timer_box=Rect(540,80 ,240,140)
answer_box1=Rect(20,260 ,230,140)
answer_box2=Rect(270,260, 230,140)
answer_box3=Rect(20,450, 230,140)
answer_box4=Rect(270,450, 230,140)
skip_box=Rect(525,280 ,230,300)
score=0
time_left=10
marquee_message=""
is_game_over=False
answer_boxes=[answer_box1,answer_box2,answer_box3, answer_box4]




def draw():
    screen.fill('black')
    screen.draw.filled_rect(marquee_box,'blue')
    screen.draw.filled_rect(question_box,'red')
    screen.draw.filled_rect(timer_box,'green')
    screen.draw.filled_rect(answer_box1,'orange')
    screen.draw.filled_rect(answer_box2,'orange')
    screen.draw.filled_rect(answer_box3,'orange')
    screen.draw.filled_rect(answer_box4,'orange')
    screen.draw.filled_rect(skip_box,'yellow')

    #marquee box with question number
    marquee_message="Welcome to Quiz Master..."


    marquee_message+=f'Q: {question_index} of {question_count}'
    screen.draw.textbox(marquee_message, marquee_box, color='white')
    
    #display timer box text
    screen.draw.textbox(str(time_left),timer_box,color='white',shadow=(0,5,0.5),
                        scolor="dim grey")
    
    #skip box text
    screen.draw.textbox('SKIP',skip_box,color='white')

    #question box text
    screen.draw.textbox(question[0].strip(),question_box,color="white"shadow=(0.5,0,5),
                        scolor="dim grey")
    
    #display answer box
    index=1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color="black")
        index=index+1



pgzrun.go()
