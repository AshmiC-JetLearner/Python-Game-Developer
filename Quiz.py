import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "quizmaster game"

marquee_box = Rect(0,0, 800,60)# initial x and y coordinate and width and height

question_box = Rect(20,80 ,510,140)

timer_box = Rect(550,80 ,200,140)

ans_box_1 = Rect(20,260 ,250,150)
ans_box_2 = Rect(280,260 ,250,150)
ans_box_3 = Rect(20,430 ,250,150)
ans_box_4 = Rect(280,430 ,250,150)

skip_box = Rect(550,260 ,200,320)

answer_boxes = [ans_box_1,ans_box_2,ans_box_3,ans_box_4]

score = 0

time_left = 10

marquee_message = ""

is_game_over = False

def draw():
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"yellow")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_box,"white")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"red")
    
    marquee_message = "Welcome to quizmaster game..."
    marquee_message += f"Q:{question_index} of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color = "white")

    screen.draw.textbox(str(time_left),timer_box,color = "white", shadow = (0.5,0.5), scolor = "grey")

    screen.draw.textbox("skip",skip_box, color = "black", angle = -90)

    screen.draw.textbox(question[0].strip(),question_box,color = "blue",shadow = (0.5,0.5),scolor = "dim grey")

    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(), answer_box, 
                            color="black")
        index = index + 1



def update():
    move_marquee()

def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

question_file_name = 'Quiz master/questions.txt'

questions = []# lsit of questions

question_count = 0# total number of questions

question_index = 0# current question number


def read_question_file():
    global question_count
    global questions
    q_file = open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    q_file.close()

def read_next_ques():
    global question_index
    question_index += 1
    return questions.pop(0).split("|")


def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index == int(question[5]):
                correct_ans()
            else:
                game_over()
        index += 1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_ans():
    global score,time_left,question,questions
    score += 1
    if questions:
        question = read_next_ques()
        time_left = 10
    else:
        game_over()

def game_over():
    global time_left,question,is_game_over
    message = f"Game over!\nYou got {score} questions correct!"
    question = [message,"-","-","-","-",5]
    time_left = 0
    is_game_over = True

def skip_question():
    global question,time_left
    if question and not is_game_over:
        question = read_next_ques()
        time_left = 10
    else:
        game_over()
    


def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()

read_question_file()
question = read_next_ques()
clock.schedule_interval(update_time_left,1)

pgzrun.go()
