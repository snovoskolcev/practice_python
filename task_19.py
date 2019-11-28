#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while(wall_is_above() == True and wall_is_on_the_left() == False):
        move_left()
    
    if(wall_is_on_the_left() == True):
        while(wall_is_above() == True and wall_is_on_the_right() == False):
            if(wall_is_above() == True and wall_is_beneath() == True and wall_is_on_the_right() == True):
                break
            else:
                move_right()
    
    while(wall_is_above() == False):
        move_up()
    
    while(wall_is_on_the_left() == False and wall_is_beneath() == False):
        move_left()


if __name__ == '__main__':
    run_tasks()
