import pgzrun, random
WIDTH=700
HEIGHT=600

CENTRE_X=WIDTH/2
CENTRE_Y=HEIGHT/2
CENTRE=(CENTRE_X,CENTRE_Y)
FINAL_LEVEL=8

START_SPEED=10
game_over=False
game_complete=False
current_level=1

#list of extra items
ITEMS=['cake','ice_cream','bottle','chips','lollipop','soda']

items_list=[]
animations_list=[]
carrot_clicked = False

def draw():

    global items_list, game_over, game_complete,current_level
    screen.clear()
    screen.blit('bground(1)',(0,0))

    if game_over:
       display_message("GAME OVER","Try again.")
    
    elif game_complete:
       display_message("CONGRATS!","You have won the game!")

    else:
        for item in items_list:
            item.draw()

        


def update():
    global items_list
    if len(items_list) == 0:
        items_list = make_items(current_level)
        

def make_items(number_of_extra_items):

    items_to_create=get_option_to_create(number_of_extra_items)
    new_items= create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create=["carrot"]
    for i in range(0,number_of_extra_items):
        random_option= random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for pic in items_to_create:
        item= Actor(pic+'img')
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    num_of_gaps= len(items_to_layout)+1
    gap_size=WIDTH // num_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos=(index+1)*gap_size
        item.x=new_x_pos
        item.y = 0



def animate_items(items_to_animate):
    global animations_list
    for item in items_to_animate:
        duration=max(2, START_SPEED-current_level)
        item.anchor=('center','bottom')
        animation=animate(item, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations_list.append(animation)


def handle_game_over():
    global game_over, carrot_clicked
    if not carrot_clicked and not game_over:
        game_over= True
        stop_animations(animations_list)

def on_mouse_down(pos):
    global items_list,current_level,carrot_clicked
    for item in items_list:
        if item.collidepoint(pos):
            if 'carrot' in item.image:
                carrot_clicked = True
                handle_game_complete()
            else:
                handle_game_over()
            
def handle_game_complete():
    global game_complete, current_level, items_list, animations_list, carrot_clicked
    stop_animations(animations_list)
    if current_level == FINAL_LEVEL:
        game_complete=True
    else:
        current_level+=1
        items_list=[]
        animations_list=[]
        carrot_clicked = False



def stop_animations(animation_to_stop):
    for animation in animation_to_stop:
        if animation.running == True:
            animation.stop()


def display_message(heading_text,sub_heading_text):
    screen.draw.text(heading_text,fontsize=60,center=CENTRE,color='black')
    screen.draw.text(sub_heading_text,fontsize=35,center=(CENTRE_X,CENTRE_Y+40),color='brown')




pgzrun.go()
