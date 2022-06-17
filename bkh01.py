import logging
import random
from datetime import timedelta

from bokeh.models import Toggle
from bokeh.plotting import figure, show
from bokeh.layouts import layout

logging.basicConfig(level=logging.DEBUG)
logger = logging


def get_ts_data(f):
    all_minutes = range(24*60)
    x_list = []
    y_list = []
    for x in all_minutes:
        td = timedelta(minutes=x)
        mn = str(td).split(':')[-2].zfill(2)
        hr = str(td).split(':')[-3].zfill(2)
        hrmn = hr + mn
        v = 1 if random.random() > f else 0
        x_list.append(hrmn)
        y_list.append(v)
    return x_list, y_list


def main():
    logger.info('Started')
    p = figure()
    x1, y1 = get_ts_data(.98)
    x2, y2 = get_ts_data(.80)
    l1 = p.step(x=x1, y=y1, line_color='blue')
    l2 = p.step(x=x2, y=y2, line_color='green')
    toggle1 = Toggle(label="Blue Line", active=True)
    toggle2 = Toggle(label="Green Line", active=True)
    toggle1.js_link('active', l1, 'visible')
    toggle2.js_link('active', l2, 'visible')
    show(layout([p], [toggle1, toggle2]))
    logger.info('Completed')


if __name__ == '__main__':
    main()
