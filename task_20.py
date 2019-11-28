#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    i = 0
    move_right()
    while(i < 6):
        while(wall_is_on_the_right() == False):
            fill_cell()
            move_right()
        move_down()
        move_left()
        while(wall_is_on_the_left() == False):
            fill_cell()
            move_left()
        move_down()
        move_right()
        i+=1

        


if __name__ == '__main__':
    run_tasks()
