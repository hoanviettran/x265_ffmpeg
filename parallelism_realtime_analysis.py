import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-name", "--name-figure", default=' Avg WPP',
	help="Name of figure")
ap.add_argument("-csv", "--csv-file", default='/media/hoantranviet/data/Video test/sample_video/log.csv',
	help="Path to log csv file")
ap.add_argument("-kind", "--kind-plot", default='line',
	help="Kind of plot")  

args = vars(ap.parse_args())

pre_df_lenght = 0

# if(args['kind_plot']=='line'):
if True:
    plt.ion()
    fig, ax = plt.subplots()
    while True:
        df = pd.read_csv(args["csv_file"])
        current_df_len = len(df)
        if(current_df_len == pre_df_lenght):
            break
        pre_df_lenght = current_df_len
    #     avg_wpp = df[' Avg WPP']
    #     total_ctu_time = df[' Total CTU time (ms)']
        ax.clear()
        if(args['kind_plot']=='bar'):
            df2 = df[current_df_len -2:current_df_len-1]
            df2.plot(y=args["name_figure"], ax=ax, kind='bar')
        else:
            df.plot(y=args["name_figure"], ax=ax)
        plt.draw()
        plt.pause(1)    
    plt.show()

# elif args['kind_plot']=='bar':
#     fig, ax = plt.subplots()
#     plot_bar = plt.bar(1, 4)
#     while True:
#         df = pd.read_csv(args["csv_file"])
#         current_df_len = len(df)
#         if(current_df_len == pre_df_lenght):
#             break
#         pre_df_lenght = current_df_len
#         plot_bar[0].set_height(df[args["name_figure"]][current_df_len-1])
#         fig.canvas.draw_idle()
#         plt.pause(0.2)
