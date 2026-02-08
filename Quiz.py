import pgzrun
WIDTH=800
HEIGHT=700
TITLE='Quiz Master'

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
    screen.draw.textbox(question[0].strip(),question_box,color="white",shadow=(0.5,0,5),
                        scolor="dim grey")
    
    #display answer box
    index=1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color="black")
        index=index+1

def update():
    move_marquee()


def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left=WIDTH

question_file_name= 'Quiz master/questions.txt'
questions=[]
question_count=0
question_index=0

def read_question_file():
    global question_count
    global questions
    q_file=open(question_file_name, 'r')
    for question in q_file:
        questions.append(question)
        question_count=question_count+1
    q_file.close()

def read_next_q():
    global question_index
    question_index += 1
    return questions.pop(0).split("|")

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index ==int(question[5]):
                correct_answer()

            else:
                game_over()
        index += 1
    if  skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score,questions,time_left, question
    score +=1
    if questions:
        question=read_next_q
        time_left=10
    else:
        game_over()
    
def game_over():
    global question, time_left, is_game_over
    message=f'Game over!\n You got {score} questions correct!'
    question=[message, "-","-","-","-","-",5]
    time_left=0
    game_over=True
     
def update_time_left():
    global time_left
    if time_left:
        time_left=time_left-1
    else:
        game_over()

read_question_file()
question=read_next_q
clock.schedule_interval(update_time_left, 1)




pgzrun.go()
