#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while(wall_is_on_the_right() == False):
        if(wall_is_above() == True and wall_is_beneath() == True):
            move_right()
        elif(wall_is_beneath() == True and wall_is_above() == False):
            fill_cell()
            move_right()
    else:
        if(wall_is_above() == False):
            fill_cell()

if __name__ == '__main__':
    run_tasks()
