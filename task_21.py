#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    move_right()
    fill_cell()
    n = 0
    while n <= 11:
        if wall_is_beneath() == True:
            break
        move_down()
        fill_cell()
        n+=1
        for i in range(n):
            move_right()
            fill_cell()
        move_left(n)
    else:
        move_down()


if __name__ == '__main__':
    run_tasks()
