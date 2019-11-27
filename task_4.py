#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if(wall_is_above() == True and wall_is_beneath() == True and wall_is_on_the_left() == True):
        move_right()
    elif(wall_is_above() == True and wall_is_beneath() == True and wall_is_on_the_right() == True):
        move_left()
    elif(wall_is_on_the_left() == True and wall_is_on_the_right() == True and wall_is_above() == True):
        move_down()
    else:
        move_up()


if __name__ == '__main__':
    run_tasks()
