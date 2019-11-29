#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    if wall_is_above() == True and wall_is_beneath() == True and wall_is_on_the_left() == True and wall_is_on_the_right() == True:
        fill_cell()
    while wall_is_beneath() == False:
        while wall_is_on_the_right() == False:
            fill_cell()
            move_right()
            fill_cell()
        move_down()
        while wall_is_on_the_left() == False:
            fill_cell()
            move_left()
            fill_cell()
        else:
            move_down()
    while wall_is_on_the_right() == False:
        fill_cell()
        move_right()
        fill_cell()
    while wall_is_on_the_left() == False:
        fill_cell()
        move_left()
        fill_cell()
        if wall_is_beneath == True and wall_is_on_the_left() == True:
            break


if __name__ == '__main__':
    run_tasks()
