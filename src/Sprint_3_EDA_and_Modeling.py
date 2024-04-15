#!/usr/bin/env python
# coding: utf-8

# <div id="container" style="position:relative;">
# <div style="float:left"><h1> Sprint 3 - EDA & Modeling</h1></div>
# <div style="position:relative; float:right"><img style="height:65px" src="data:image/png;base64,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" />
# </div>
# </div>
# 

# ***

# **Author:** Matt Bonadies  
# **Date:** 4-15-2024  
# **Version:** JupyterLab 3.6.3  

# ***

# ## Table of Contents

# - **Imports**
# - **Data Dictionary**
# - **Data Imports**
# - **Exploratory Data Analysis**
# - **Modeling**
# - **Model Projections**

# ***

# ## Imports

# In[1]:


# Imports all of the libraries that will be utilized throughout this project
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from datetime import datetime, timedelta
from io import StringIO
import requests


# In[2]:


# Imports all of the scikit-Learn libraries that will be utilized throughout this project
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge, Lasso
from sklearn.decomposition import PCA
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.neural_network import MLPRegressor
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.models import load_model
from sklearn.metrics import r2_score
from keras.losses import mean_absolute_error
from tensorflow.keras.optimizers import Adam


# In[3]:


# Enables view of all columns when viewing Pandas DataFrames
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


# ## Data Dictionary

# #### **Round Scoring, Stats, & Strokes Gained**

# | Column | Type | Description |
# | --- | --- | --- |
# |tour| object | Professional tour that the event was played on. |
# |year| int64 | Calendar year. |
# |season| int64 | Official season as defined by the PGA tour. |
# |event_completed| datetime64[ns] | Official date of the final round of the tournament  |
# |event_name| object | Name of tournament. |
# |event_id| int64 | Unique Tournament ID number. |
# |player_name| object | Name of player. |
# |dg_id| int64 | Unique Player ID number. There is a single dg_id for each player. |
# |round_num| int64 | Round number for the given tournament. Ranges from 1-4. |
# |course_name| object | Name of golf course. |
# |course_num| int64 | Unique Course ID number. |
# |course_par| int64 | Course par - Scoring benchmark. Value is typically 72, but it can range from 70 to 72. |
# |start_hole| int64 | Hole number that player started on. Value is either 1 or 10. |
# |round_score| int64 | Score that was shot for the given round. Our model’s target variable. |
# |sg_putt| float64 | Strokes gained putting.  |
# |sg_arg| float64 | Strokes gained around the green.  |
# |sg_app| float64 | Strokes gained approaching the green. |
# |sg_ott| float64 | Strokes gained off the tee. |
# |sg_t2g| float64 | Strokes gained from tee to green. The sum of sg_ott, sg_app, and sg_arg. |
# |sg_total| float64 | Strokes gained total. Difference between the player’s score and the average score. |
# |driving_dist| float64 | Average distance of every drive hit. |
# |driving_acc| float64 | Fairways in regulation. Percentage of fairways. |
# |gir| float64 | Greens in regulation. Percentage of greens hit. |
# |scrambling| float64 | Percentage of shots  ≤ 50 yards that were holed out in 2 strokes or less. |
# |prox_rgh| float64 | Average proximity of all shots hit from locations other than the fairway. |
# |prox_fw| float64 | Average proximity of all shots hit from the fairway. |
# |great_shots| float64 | Sum of shots that fall into the top 5% of strokes-gained values in each category. |
# |poor_shots| float64 | Sum of shots that fall into the bottom 5% of strokes-gained values in each category. |
# |fin_num| int64 | Official finishing position. |
# |teetime_numeric| float64 | Time a player tee’d off. |
# |round_completed| datetime64[ns] | Date the round was played. |
# |month| int32 | Month the round was played. |
# |day| int32 | Day of month the round was played. |
# |ohe_win| int64 | Binary value if the player won or not. |
# |ohe_top_five| int64 | Binary value if the player finished in the top 5 or not. |
# |ohe_top_ten| int64 | Binary value if the player finished in the top 10 or not. |
# |ohe_top_twenty| int64 | Binary value if the player finished in the top 20 or not. |
# |ohe_make_cut| int64 | Binary value if the player made the cut after 2 rounds or not. |
# |career_moving_avg_sg_putt| float64 | Average strokes gained putting for entire timeframe of dataset.|
# |career_moving_med_sg_putt| float64 | Median strokes gained putting for entire timeframe of dataset.|
# |L44_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 44 rounds. |
# |L44_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 44 rounds. |
# |L36_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 36 rounds. |
# |L36_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 36 rounds. |
# |L28_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 28 rounds. |
# |L28_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 28 rounds. |
# |L24_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 24 rounds. |
# |L24_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 24 rounds. |
# |L20_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 20 rounds. |
# |L20_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 20 rounds. |
# |L16_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 16 rounds. |
# |L16_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 16 rounds. |
# |L12_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 12 rounds. |
# |L12_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 12 rounds. |
# |L8_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 8 rounds. |
# |L8_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 8 rounds. |
# |L4_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 4 rounds. |
# |L4_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 4 rounds. |
# |L3_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 3 rounds. |
# |L3_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 3 rounds. |
# |L2_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 2 rounds. |
# |L2_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 2 rounds. |
# |L45_moving_med_sg_putt| float64 | Median strokes gained putting from last 45 rounds. |
# |L37_moving_med_sg_putt| float64 | Median strokes gained putting from last 37 rounds. |
# |L29_moving_med_sg_putt| float64 | Median strokes gained putting from last 29 rounds. |
# |L21_moving_med_sg_putt| float64 | Median strokes gained putting from last 21 rounds. |
# |L15_moving_med_sg_putt| float64 | Median strokes gained putting from last 15 rounds. |
# |L11_moving_med_sg_putt| float64 | Median strokes gained putting from last 11 rounds. |
# |L9_moving_med_sg_putt| float64 | Median strokes gained putting from last 9 rounds. |
# |L7_moving_med_sg_putt| float64 | Median strokes gained putting from last 7 rounds. |
# |L5_moving_med_sg_putt| float64 | Median strokes gained putting from last 5 rounds. |
# |L3_moving_med_sg_putt| float64 | Median strokes gained putting from last 3 rounds. |
# |career_moving_avg_sg_arg| float64 | Average strokes gained around the green for entire timeframe of dataset.|
# |career_moving_med_sg_arg| float64 | Median strokes gained around the green for entire timeframe of dataset.|
# |L44_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 44 rounds. |
# |L44_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 44 rounds. |
# |L36_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 36 rounds. |
# |L36_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 36 rounds. |
# |L28_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 28 rounds. |
# |L28_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 28 rounds. |
# |L24_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 24 rounds. |
# |L24_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 24 rounds. |
# |L20_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 20 rounds. |
# |L20_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 20 rounds. |
# |L16_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 16 rounds. |
# |L16_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 16 rounds. |
# |L12_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 12 rounds. |
# |L12_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 12 rounds. |
# |L8_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 8 rounds. |
# |L8_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 8 rounds. |
# |L4_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 4 rounds. |
# |L4_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 4 rounds. |
# |L3_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 3 rounds. |
# |L3_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 3 rounds. |
# |L2_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 2 rounds. |
# |L2_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 2 rounds. |
# |L45_moving_med_sg_arg| float64 | Median strokes gained around the green from last 45 rounds. |
# |L37_moving_med_sg_arg| float64 | Median strokes gained around the green from last 37 rounds. |
# |L29_moving_med_sg_arg| float64 | Median strokes gained around the green from last 29 rounds. |
# |L21_moving_med_sg_arg| float64 | Median strokes gained around the green from last 21 rounds. |
# |L15_moving_med_sg_arg| float64 | Median strokes gained around the green from last 15 rounds. |
# |L11_moving_med_sg_arg| float64 | Median strokes gained around the green from last 11 rounds. |
# |L9_moving_med_sg_arg| float64 | Median strokes gained around the green from last 9 rounds. |
# |L7_moving_med_sg_arg| float64 | Median strokes gained around the green from last 7 rounds. |
# |L5_moving_med_sg_arg| float64 | Median strokes gained around the green from last 5 rounds. |
# |L3_moving_med_sg_arg| float64 | Median strokes gained around the green from last 3 rounds. |
# |career_moving_avg_sg_app| float64 | Average strokes gained approaching the green for entire timeframe of dataset.|
# |career_moving_med_sg_app| float64 | Median strokes gained approaching the green for entire timeframe of dataset.|
# |L44_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 44 rounds. |
# |L44_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 44 rounds. |
# |L36_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 36 rounds. |
# |L36_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 36 rounds. |
# |L28_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 28 rounds. |
# |L28_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 28 rounds. |
# |L24_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 24 rounds. |
# |L24_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 24 rounds. |
# |L20_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 20 rounds. |
# |L20_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 20 rounds. |
# |L16_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 16 rounds. |
# |L16_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 16 rounds. |
# |L12_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 12 rounds. |
# |L12_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 12 rounds. |
# |L8_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 8 rounds. |
# |L8_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 8 rounds. |
# |L4_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 4 rounds. |
# |L4_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 4 rounds. |
# |L3_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 3 rounds. |
# |L3_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 3 rounds. |
# |L2_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 2 rounds. |
# |L2_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 2 rounds. |
# |L45_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 45 rounds. |
# |L37_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 37 rounds. |
# |L29_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 29 rounds. |
# |L21_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 21 rounds. |
# |L15_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 15 rounds. |
# |L11_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 11 rounds. |
# |L9_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 9 rounds. |
# |L7_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 7 rounds. |
# |L5_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 5 rounds. |
# |L3_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 3 rounds. |
# |career_moving_avg_sg_ott| float64 | Average strokes gained off the tee for entire timeframe of dataset.|
# |career_moving_med_sg_ott| float64 | Median strokes gained off the tee for entire timeframe of dataset.|
# |L44_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 44 rounds. |
# |L44_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 44 rounds. |
# |L36_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 36 rounds. |
# |L36_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 36 rounds. |
# |L28_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 28 rounds. |
# |L28_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 28 rounds. |
# |L24_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 24 rounds. |
# |L24_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 24 rounds. |
# |L20_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 20 rounds. |
# |L20_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 20 rounds. |
# |L16_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 16 rounds. |
# |L16_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 16 rounds. |
# |L12_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 12 rounds. |
# |L12_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 12 rounds. |
# |L8_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 8 rounds. |
# |L8_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 8 rounds. |
# |L4_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 4 rounds. |
# |L4_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 4 rounds. |
# |L3_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 3 rounds. |
# |L3_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 3 rounds. |
# |L2_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 2 rounds. |
# |L2_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 2 rounds. |
# |L45_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 45 rounds. |
# |L37_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 37 rounds. |
# |L29_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 29 rounds. |
# |L21_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 21 rounds. |
# |L15_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 15 rounds. |
# |L11_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 11 rounds. |
# |L9_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 9 rounds. |
# |L7_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 7 rounds. |
# |L5_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 5 rounds. |
# |L3_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 3 rounds. |
# |career_moving_avg_sg_t2g| float64 | Average strokes gained tee to green for entire timeframe of dataset.|
# |career_moving_med_sg_t2g| float64 | Median strokes gained tee to green for entire timeframe of dataset.|
# |L44_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 44 rounds. |
# |L44_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 44 rounds. |
# |L36_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 36 rounds. |
# |L36_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 36 rounds. |
# |L28_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 28 rounds. |
# |L28_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 28 rounds. |
# |L24_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 24 rounds. |
# |L24_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 24 rounds. |
# |L20_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 20 rounds. |
# |L20_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 20 rounds. |
# |L16_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 16 rounds. |
# |L16_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 16 rounds. |
# |L12_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 12 rounds. |
# |L12_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 12 rounds. |
# |L8_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 8 rounds. |
# |L8_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 8 rounds. |
# |L4_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 4 rounds. |
# |L4_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 4 rounds. |
# |L3_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 3 rounds. |
# |L3_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 3 rounds. |
# |L2_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 2 rounds. |
# |L2_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 2 rounds. |
# |L45_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 45 rounds. |
# |L37_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 37 rounds. |
# |L29_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 29 rounds. |
# |L21_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 21 rounds. |
# |L15_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 15 rounds. |
# |L11_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 11 rounds. |
# |L9_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 9 rounds. |
# |L7_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 7 rounds. |
# |L5_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 5 rounds. |
# |L3_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 3 rounds. |
# |career_moving_avg_sg_total| float64 | Average strokes gained total for entire timeframe of dataset.|
# |career_moving_med_sg_total| float64 | Median strokes gained total for entire timeframe of dataset.|
# |L44_moving_avg_sg_total| float64 | Average strokes gained total from the last 44 rounds. |
# |L44_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 44 rounds. |
# |L36_moving_avg_sg_total| float64 | Average strokes gained total from the last 36 rounds. |
# |L36_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 36 rounds. |
# |L28_moving_avg_sg_total| float64 | Average strokes gained total from the last 28 rounds. |
# |L28_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 28 rounds. |
# |L24_moving_avg_sg_total| float64 | Average strokes gained total from the last 24 rounds. |
# |L24_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 24 rounds. |
# |L20_moving_avg_sg_total| float64 | Average strokes gained total from the last 20 rounds. |
# |L20_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 20 rounds. |
# |L16_moving_avg_sg_total| float64 | Average strokes gained total from the last 16 rounds. |
# |L16_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 16 rounds. |
# |L12_moving_avg_sg_total| float64 | Average strokes gained total from the last 12 rounds. |
# |L12_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 12 rounds. |
# |L8_moving_avg_sg_total| float64 | Average strokes gained total from the last 8 rounds. |
# |L8_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 8 rounds. |
# |L4_moving_avg_sg_total| float64 | Average strokes gained total from the last 4 rounds. |
# |L4_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 4 rounds. |
# |L3_moving_avg_sg_total| float64 | Average strokes gained total from the last 3 rounds. |
# |L3_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 3 rounds. |
# |L2_moving_avg_sg_total| float64 | Average strokes gained total from the last 2 rounds. |
# |L2_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 2 rounds. |
# |L45_moving_med_sg_total| float64 | Median strokes gained total from last 45 rounds. |
# |L37_moving_med_sg_total| float64 | Median strokes gained total from last 37 rounds. |
# |L29_moving_med_sg_total| float64 | Median strokes gained total from last 29 rounds. |
# |L21_moving_med_sg_total| float64 | Median strokes gained total from last 21 rounds. |
# |L15_moving_med_sg_total| float64 | Median strokes gained total from last 15 rounds. |
# |L11_moving_med_sg_total| float64 | Median strokes gained total from last 11 rounds. |
# |L9_moving_med_sg_total| float64 | Median strokes gained total from last 9 rounds. |
# |L7_moving_med_sg_total| float64 | Median strokes gained total from last 7 rounds. |
# |L5_moving_med_sg_total| float64 | Median strokes gained total from last 5 rounds. |
# |L3_moving_med_sg_total| float64 | Median strokes gained total from last 3 rounds. |
# |career_moving_avg_driving_dist| float64 | Average driving distance for entire timeframe of dataset.|
# |career_moving_med_driving_dist| float64 | Median driving distance for entire timeframe of dataset.|
# |L44_moving_avg_driving_dist| float64 | Average driving distance from the last 44 rounds. |
# |L44_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 44 rounds. |
# |L36_moving_avg_driving_dist| float64 | Average driving distance from the last 36 rounds. |
# |L36_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 36 rounds. |
# |L28_moving_avg_driving_dist| float64 | Average driving distance from the last 28 rounds. |
# |L28_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 28 rounds. |
# |L24_moving_avg_driving_dist| float64 | Average driving distance from the last 24 rounds. |
# |L24_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 24 rounds. |
# |L20_moving_avg_driving_dist| float64 | Average driving distance from the last 20 rounds. |
# |L20_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 20 rounds. |
# |L16_moving_avg_driving_dist| float64 | Average driving distance from the last 16 rounds. |
# |L16_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 16 rounds. |
# |L12_moving_avg_driving_dist| float64 | Average driving distance from the last 12 rounds. |
# |L12_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 12 rounds. |
# |L8_moving_avg_driving_dist| float64 | Average driving distance from the last 8 rounds. |
# |L8_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 8 rounds. |
# |L4_moving_avg_driving_dist| float64 | Average driving distance from the last 4 rounds. |
# |L4_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 4 rounds. |
# |L3_moving_avg_driving_dist| float64 | Average driving distance from the last 3 rounds. |
# |L3_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 3 rounds. |
# |L2_moving_avg_driving_dist| float64 | Average driving distance from the last 2 rounds. |
# |L2_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 2 rounds. |
# |L45_moving_med_driving_dist| float64 | Median driving distance from last 45 rounds. |
# |L37_moving_med_driving_dist| float64 | Median driving distance from last 37 rounds. |
# |L29_moving_med_driving_dist| float64 | Median driving distance from last 29 rounds. |
# |L21_moving_med_driving_dist| float64 | Median driving distance from last 21 rounds. |
# |L15_moving_med_driving_dist| float64 | Median driving distance from last 15 rounds. |
# |L11_moving_med_driving_dist| float64 | Median driving distance from last 11 rounds. |
# |L9_moving_med_driving_dist| float64 | Median driving distance from last 9 rounds. |
# |L7_moving_med_driving_dist| float64 | Median driving distance from last 7 rounds. |
# |L5_moving_med_driving_dist| float64 | Median driving distance from last 5 rounds. |
# |L3_moving_med_driving_dist| float64 | Median driving distance from last 3 rounds. |
# |career_moving_avg_driving_acc| float64 | Average driving accuracy for entire timeframe of dataset.|
# |career_moving_med_driving_acc| float64 | Median driving accuracy for entire timeframe of dataset.|
# |L44_moving_avg_driving_acc| float64 | Average driving accuracy from the last 44 rounds. |
# |L44_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 44 rounds. |
# |L36_moving_avg_driving_acc| float64 | Average driving accuracy from the last 36 rounds. |
# |L36_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 36 rounds. |
# |L28_moving_avg_driving_acc| float64 | Average driving accuracy from the last 28 rounds. |
# |L28_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 28 rounds. |
# |L24_moving_avg_driving_acc| float64 | Average driving accuracy from the last 24 rounds. |
# |L24_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 24 rounds. |
# |L20_moving_avg_driving_acc| float64 | Average driving accuracy from the last 20 rounds. |
# |L20_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 20 rounds. |
# |L16_moving_avg_driving_acc| float64 | Average driving accuracy from the last 16 rounds. |
# |L16_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 16 rounds. |
# |L12_moving_avg_driving_acc| float64 | Average driving accuracy from the last 12 rounds. |
# |L12_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 12 rounds. |
# |L8_moving_avg_driving_acc| float64 | Average driving accuracy from the last 8 rounds. |
# |L8_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 8 rounds. |
# |L4_moving_avg_driving_acc| float64 | Average driving accuracy from the last 4 rounds. |
# |L4_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 4 rounds. |
# |L3_moving_avg_driving_acc| float64 | Average driving accuracy from the last 3 rounds. |
# |L3_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 3 rounds. |
# |L2_moving_avg_driving_acc| float64 | Average driving accuracy from the last 2 rounds. |
# |L2_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 2 rounds. |
# |L45_moving_med_driving_acc| float64 | Median driving accuracy from last 45 rounds. |
# |L37_moving_med_driving_acc| float64 | Median driving accuracy from last 37 rounds. |
# |L29_moving_med_driving_acc| float64 | Median driving accuracy from last 29 rounds. |
# |L21_moving_med_driving_acc| float64 | Median driving accuracy from last 21 rounds. |
# |L15_moving_med_driving_acc| float64 | Median driving accuracy from last 15 rounds. |
# |L11_moving_med_driving_acc| float64 | Median driving accuracy from last 11 rounds. |
# |L9_moving_med_driving_acc| float64 | Median driving accuracy from last 9 rounds. |
# |L7_moving_med_driving_acc| float64 | Median driving accuracy from last 7 rounds. |
# |L5_moving_med_driving_acc| float64 | Median driving accuracy from last 5 rounds. |
# |L3_moving_med_driving_acc| float64 | Median driving accuracy from last 3 rounds. |
# |career_moving_avg_gir| float64 | Average GIR for entire timeframe of dataset.|
# |career_moving_med_gir| float64 | Median GIR for entire timeframe of dataset.|
# |L44_moving_avg_gir| float64 | Average GIR from the last 44 rounds. |
# |L44_gir_std_dev| float64 | Standard deviation of GIR from the last 44 rounds. |
# |L36_moving_avg_gir| float64 | Average GIR from the last 36 rounds. |
# |L36_gir_std_dev| float64 | Standard deviation of GIR from the last 36 rounds. |
# |L28_moving_avg_gir| float64 | Average GIR from the last 28 rounds. |
# |L28_gir_std_dev| float64 | Standard deviation of GIR from the last 28 rounds. |
# |L24_moving_avg_gir| float64 | Average GIR from the last 24 rounds. |
# |L24_gir_std_dev| float64 | Standard deviation of GIR from the last 24 rounds. |
# |L20_moving_avg_gir| float64 | Average GIR from the last 20 rounds. |
# |L20_gir_std_dev| float64 | Standard deviation of GIR from the last 20 rounds. |
# |L16_moving_avg_gir| float64 | Average GIR from the last 16 rounds. |
# |L16_gir_std_dev| float64 | Standard deviation of GIR from the last 16 rounds. |
# |L12_moving_avg_gir| float64 | Average GIR from the last 12 rounds. |
# |L12_gir_std_dev| float64 | Standard deviation of GIR from the last 12 rounds. |
# |L8_moving_avg_gir| float64 | Average GIR from the last 8 rounds. |
# |L8_gir_std_dev| float64 | Standard deviation of GIR from the last 8 rounds. |
# |L4_moving_avg_gir| float64 | Average GIR from the last 4 rounds. |
# |L4_gir_std_dev| float64 | Standard deviation of GIR from the last 4 rounds. |
# |L3_moving_avg_gir| float64 | Average GIR from the last 3 rounds. |
# |L3_gir_std_dev| float64 | Standard deviation of GIR from the last 3 rounds. |
# |L2_moving_avg_gir| float64 | Average GIR from the last 2 rounds. |
# |L2_gir_std_dev| float64 | Standard deviation of GIR from the last 2 rounds. |
# |L45_moving_med_gir| float64 | Median GIR from last 45 rounds. |
# |L37_moving_med_gir| float64 | Median GIR from last 37 rounds. |
# |L29_moving_med_gir| float64 | Median GIR from last 29 rounds. |
# |L21_moving_med_gir| float64 | Median GIR from last 21 rounds. |
# |L15_moving_med_gir| float64 | Median GIR from last 15 rounds. |
# |L11_moving_med_gir| float64 | Median GIR from last 11 rounds. |
# |L9_moving_med_gir| float64 | Median GIR from last 9 rounds. |
# |L7_moving_med_gir| float64 | Median GIR from last 7 rounds. |
# |L5_moving_med_gir| float64 | Median GIR from last 5 rounds. |
# |L3_moving_med_gir| float64 | Median GIR from last 3 rounds. |
# |career_moving_avg_scrambling| float64 | Average scrambling for entire timeframe of dataset.|
# |career_moving_med_scrambling| float64 | Median scrambling for entire timeframe of dataset.|
# |L44_moving_avg_scrambling| float64 | Average scrambling from the last 44 rounds. |
# |L44_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 44 rounds. |
# |L36_moving_avg_scrambling| float64 | Average scrambling from the last 36 rounds. |
# |L36_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 36 rounds. |
# |L28_moving_avg_scrambling| float64 | Average scrambling from the last 28 rounds. |
# |L28_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 28 rounds. |
# |L24_moving_avg_scrambling| float64 | Average scrambling from the last 24 rounds. |
# |L24_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 24 rounds. |
# |L20_moving_avg_scrambling| float64 | Average scrambling from the last 20 rounds. |
# |L20_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 20 rounds. |
# |L16_moving_avg_scrambling| float64 | Average scrambling from the last 16 rounds. |
# |L16_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 16 rounds. |
# |L12_moving_avg_scrambling| float64 | Average scrambling from the last 12 rounds. |
# |L12_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 12 rounds. |
# |L8_moving_avg_scrambling| float64 | Average scrambling from the last 8 rounds. |
# |L8_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 8 rounds. |
# |L4_moving_avg_scrambling| float64 | Average scrambling from the last 4 rounds. |
# |L4_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 4 rounds. |
# |L3_moving_avg_scrambling| float64 | Average scrambling from the last 3 rounds. |
# |L3_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 3 rounds. |
# |L2_moving_avg_scrambling| float64 | Average scrambling from the last 2 rounds. |
# |L2_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 2 rounds. |
# |L45_moving_med_scrambling| float64 | Median scrambling from last 45 rounds. |
# |L37_moving_med_scrambling| float64 | Median scrambling from last 37 rounds. |
# |L29_moving_med_scrambling| float64 | Median scrambling from last 29 rounds. |
# |L21_moving_med_scrambling| float64 | Median scrambling from last 21 rounds. |
# |L15_moving_med_scrambling| float64 | Median scrambling from last 15 rounds. |
# |L11_moving_med_scrambling| float64 | Median scrambling from last 11 rounds. |
# |L9_moving_med_scrambling| float64 | Median scrambling from last 9 rounds. |
# |L7_moving_med_scrambling| float64 | Median scrambling from last 7 rounds. |
# |L5_moving_med_scrambling| float64 | Median scrambling from last 5 rounds. |
# |L3_moving_med_scrambling| float64 | Median scrambling from last 3 rounds. |
# |career_moving_avg_round_score| float64 | Average round score for entire timeframe of dataset.|
# |career_moving_med_round_score| float64 | Median round score for entire timeframe of dataset.|
# |L44_moving_avg_round_score| float64 | Average round score from the last 44 rounds. |
# |L44_round_score_std_dev| float64 | Standard deviation of round score from the last 44 rounds. |
# |L44_moving_min_round_score| float64 | Minimum round score from the last 44 rounds. |
# |L44_moving_max_round_score| float64 | Maximum round score from the last 44 rounds. |
# |L36_moving_avg_round_score| float64 | Average round score from the last 36 rounds. |
# |L36_round_score_std_dev| float64 | Standard deviation of round score from the last 36 rounds. |
# |L36_moving_min_round_score| float64 | Minimum round score from the last 36 rounds. |
# |L36_moving_max_round_score| float64 | Maximum round score from the last 36 rounds. |
# |L28_moving_avg_round_score| float64 | Average round score from the last 28 rounds. |
# |L28_round_score_std_dev| float64 | Standard deviation of round score from the last 28 rounds. |
# |L28_moving_min_round_score| float64 | Minimum round score from the last 28 rounds. |
# |L28_moving_max_round_score| float64 | Maximum round score from the last 28 rounds. |
# |L24_moving_avg_round_score| float64 | Average round score from the last 24 rounds. |
# |L24_round_score_std_dev| float64 | Standard deviation of round score from the last 24 rounds. |
# |L24_moving_min_round_score| float64 | Minimum round score from the last 24 rounds. |
# |L24_moving_max_round_score| float64 | Maximum round score from the last 24 rounds. |
# |L20_moving_avg_round_score| float64 | Average round score from the last 20 rounds. |
# |L20_round_score_std_dev| float64 | Standard deviation of round score from the last 20 rounds. |
# |L20_moving_min_round_score| float64 | Minimum round score from the last 20 rounds. |
# |L20_moving_max_round_score| float64 | Maximum round score from the last 20 rounds. |
# |L16_moving_avg_round_score| float64 | Average round score from the last 16 rounds. |
# |L16_round_score_std_dev| float64 | Standard deviation of round score from the last 16 rounds. |
# |L16_moving_min_round_score| float64 | Minimum round score from the last 16 rounds. |
# |L16_moving_max_round_score| float64 | Maximum round score from the last 16 rounds. |
# |L12_moving_avg_round_score| float64 | Average round score from the last 12 rounds. |
# |L12_round_score_std_dev| float64 | Standard deviation of round score from the last 12 rounds. |
# |L12_moving_min_round_score| float64 | Minimum round score from the last 12 rounds. |
# |L12_moving_max_round_score| float64 | Maximum round score from the last 12 rounds. |
# |L8_moving_avg_round_score| float64 | Average round score from the last 8 rounds. |
# |L8_round_score_std_dev| float64 | Standard deviation of round score from the last 8 rounds. |
# |L8_moving_min_round_score| float64 | Minimum round score from the last 8 rounds. |
# |L8_moving_max_round_score| float64 | Maximum round score from the last 8 rounds. |
# |L4_moving_avg_round_score| float64 | Average round score from the last 4 rounds. |
# |L4_round_score_std_dev| float64 | Standard deviation of round score from the last 4 rounds. |
# |L4_moving_min_round_score| float64 | Minimum round score from the last 4 rounds. |
# |L4_moving_max_round_score| float64 | Maximum round score from the last 4 rounds. |
# |L3_moving_avg_round_score| float64 | Average round score from the last 3 rounds. |
# |L3_round_score_std_dev| float64 | Standard deviation of round score from the last 3 rounds. |
# |L3_moving_min_round_score| float64 | Minimum round score from the last 3 rounds. |
# |L3_moving_max_round_score| float64 | Maximum round score from the last 3 rounds. |
# |L2_moving_avg_round_score| float64 | Average round score from the last 2 rounds. |
# |L2_round_score_std_dev| float64 | Standard deviation of round score from the last 2 rounds. |
# |L2_moving_min_round_score| float64 | Minimum round score from the last 2 rounds. |
# |L2_moving_max_round_score| float64 | Maximum round score from the last 2 rounds. |
# |L45_moving_med_round_score| float64 | Median round score from last 45 rounds. |
# |L37_moving_med_round_score| float64 | Median round score from last 37 rounds. |
# |L29_moving_med_round_score| float64 | Median round score from last 29 rounds. |
# |L21_moving_med_round_score| float64 | Median round score from last 21 rounds. |
# |L15_moving_med_round_score| float64 | Median round score from last 15 rounds. |
# |L11_moving_med_round_score| float64 | Median round score from last 11 rounds. |
# |L9_moving_med_round_score| float64 | Median round score from last 9 rounds. |
# |L7_moving_med_round_score| float64 | Median round score from last 7 rounds. |
# |L5_moving_med_round_score| float64 | Median round score from last 5 rounds. |
# |L3_moving_med_round_score| float64 | Median round score from last 3 rounds. |
# |career_min_round_score| float64 | Average round score for entire timeframe of dataset.|
# |career_max_round_score| float64 | Median round score for entire timeframe of dataset.|
# |Days_Since| int64 | Number of days between now and when the round was completed. |
# |Last_365_Days| int64 | Binary column if round was played in the last 365 days or not. |
# |Last_180_Days| int64 | Binary column if round was played in the last 180 days or not. |
# |Last_90_Days| int64 | Binary column if round was played in the last 90 days or not. |
# |Last_60_Days| int64 | Binary column if round was played in the last 60 days or not. |
# |Last_30_Days| int64 | Binary column if round was played in the last 30 days or not. |
# |Last_10_Days| int64 | Binary column if round was played in the last 10 days or not. |
# |Last_5_Days| int64 | Binary column if round was played in the last 5 days or not. |
# |lagged_year| float64 | Previous round year. |
# |lagged_season| float64 | Previous round season. |
# |lagged_event_id| float64 | Previous round event id. |
# |lagged_round_num| float64 | Previous round number. |
# |lagged_course_num| float64 | Previous round course number. |
# |lagged_course_par| float64 | Previous round course par. |
# |lagged_start_hole| float64 | Previous round start hole. |
# |lagged_round_score| float64 | Previous round score. |
# |lagged_sg_putt| float64 | Previous round strokes gained putting. |
# |lagged_sg_arg| float64 | Previous round strokes gained around the green. |
# |lagged_sg_app| float64 | Previous round strokes gained approaching the green. |
# |lagged_sg_ott| float64 | Previous round strokes gained off the tee. |
# |lagged_sg_t2g| float64 | Previous round strokes gained tee to green. |
# |lagged_sg_total| float64 | Previous round strokes gained total. |
# |lagged_driving_dist| float64 | Previous round average driving distance. |
# |lagged_driving_acc| float64 | Previous round driving accuracy. |
# |lagged_gir| float64 | Previous round greens in regulation. |
# |lagged_scrambling| float64 | Previous round scrambling. |
# |lagged_prox_rgh| float64 | Previous round average proximity of all shots hit from locations other than the fairway. |
# |lagged_prox_fw| float64 | Previous round average proximity of all shots hit from the fairway. |
# |lagged_great_shots| float64 | Previous round sum of great shots. |
# |lagged_poor_shots| float64 | Previous round sum of poor shots. |
# |lagged_month| float64 | Previous round month. |
# |lagged_day| float64 | Previous round day of month. |
# |lagged_fin_num| float64 | Previous round finishing position. |
# |lagged_teetime_numeric| float64 | Previous round tee time. |
# |lagged_ohe_win| float64 | Previous round binary value if the player won or not. |
# |lagged_ohe_top_five| float64 | Previous round binary value if the player finished in the top 5 or not. |
# |lagged_ohe_top_ten| float64 | Previous round binary value if the player finished in the top 10 or not. |
# |lagged_ohe_top_twenty| float64 | Previous round binary value if the player finished in the top 20 or not. |
# |lagged_ohe_make_cut| float64 | Previous round binary value if the player made the cut after 2 rounds or not. |![image.png](attachment:e12d1821-e4cb-41ec-882e-34813d093e80.png)![image.png](attachment:acc9d618-92d1-4a22-a185-2a1f7fdde99f.png)![image.png](attachment:af33dbf7-76da-444b-9bd3-e9788ea8227a.png)![image.png](attachment:5ca5905d-d4fe-4506-8658-5985c9cfea25.png)

# #### **Player List & IDs**

# | Column | Type | Description |
# | --- | --- | --- |
# | player_name | object | Name of player. |
# | dg_id | int64 | Unique Player ID number. There is a single dg_id for each player. |
# | country | object | Country of player. |
# | country_code | int64 | Numeric Country ID of player. |
# | amateur | int64 | Binary column of whether a player is an amateur or not (Meaning they’re a professional if value is 0). |

# #### **Field Updates**

# | Column | Type | Description |
# | --- | --- | --- |
# | event_name | object | Name of tournament. |
# | current_round | int64 | Upcoming round number. |
# | course | float64 | Name of course. |
# | player_name | object | Name of player. |
# | dg_id | int64 | Unique Player ID number. There is a single dg_id for each player. |
# | country | object | Country of player. |
# | start_hole | int64 | Hole number that player started on. Value is either 1 or 10. |
# | r1_teetime | float64 | Tee time of first round. |
# | r2_teetime | float64 | Tee time of second round. |
# | r3_teetime | float64 | Tee time of third round. |
# | r4_teetime | float64 | Tee time of fourth round. |
# | last_updated | object | Last time the table was refreshed. |
# | early_late | int64 | Not pertinent for this project. |
# | am | int64 | Not pertinent for this project. |
# | flag | object | Not pertinent for this project. |
# | pga_number | int64 | Not pertinent for this project. |
# | yh_salary | int64 | Not pertinent for this project. |
# | dk_salary | int64 | Not pertinent for this project. |
# | fd_id | object | Not pertinent for this project. |
# | fd_salary | int64 | Not pertinent for this project. |
# | dk_id | int64 | Not pertinent for this project. |
# | yh_id | object | Not pertinent for this project. |
# | unofficial | int64 | Not pertinent for this project. |

# #### **Player Rankings**

# | Column | Type | Description |
# | --- | --- | --- |
# | player_name | object | Name of player. |
# | country | object | Country of player. |
# | owgr_rank | int64 | World rank number of player. |

# ####

# ***

# ## Data Imports

# Retrieves all data from our processed CSV files that were created by the "Sprint 3 Data Processing" notebook.

# In[4]:


train_df_sorted = pd.read_csv('train_df_sorted.csv')
test_df_sorted = pd.read_csv('test_df_sorted.csv')
player_df = pd.read_csv('player_df.csv')
field_df = pd.read_csv('field_df.csv')


# In[5]:


print(f'There are {train_df_sorted.shape[0]} rows and {train_df_sorted.shape[1]} columns in the Train DataFrame.')
print(f'There are {test_df_sorted.shape[0]} rows and {test_df_sorted.shape[1]} columns in the Test DataFrame.')


# ***

# ## EDA

# In[6]:


# Creates Seaborn Pairplots to visualize potential relationships with strokes gained statistics
sg_cols = ['sg_putt', 'sg_arg', 'sg_app', 'sg_ott', 'sg_t2g', 'sg_total']
lagged_sg_cols = ['lagged_sg_putt', 'lagged_sg_arg', 'lagged_sg_app', 'lagged_sg_ott', 'lagged_sg_t2g', 'lagged_sg_total']
L4_sg_cols = ['L4_moving_avg_sg_putt', 'L4_moving_avg_sg_arg', 'L4_moving_avg_sg_app', 'L4_moving_avg_sg_ott', 'L4_moving_avg_sg_t2g', 'L4_moving_avg_sg_total']
L20_sg_cols = ['L20_moving_avg_sg_putt', 'L20_moving_avg_sg_arg', 'L20_moving_avg_sg_app', 'L20_moving_avg_sg_ott', 'L20_moving_avg_sg_t2g', 'L20_moving_avg_sg_total']


sns.pairplot(data=train_df_sorted, x_vars=sg_cols, y_vars='round_score', plot_kws={'color': 'magenta'})
sns.pairplot(data=train_df_sorted, x_vars=lagged_sg_cols, y_vars='round_score')
sns.pairplot(data=train_df_sorted, x_vars=L4_sg_cols, y_vars='round_score')
sns.pairplot(data=train_df_sorted, x_vars=L20_sg_cols, y_vars='round_score')


# The pairplots provided offer insight into the linear connections among various strokes gained statistics and their impact on a player's score. The magenta pairplot illustrates that an uptick in positive statistics inversely affects the round score, which is preferable because lower scores signify better performance in golf. By modifying the x variables to include data from the previous round, the average of the last 4 rounds, and the average of the last 20 rounds, we examine their association with the players' subsequent round scores. From this analysis, it emerges that long-term averages have a stronger correlation with future performance scores. This suggests that while professional players generally maintain consistent performance over the long haul, short-term fluctuations—represented by outlier rounds—may not be as predictive of their forthcoming scores.

# In[7]:


# Creates Seaborn Pairplots to visualize potential relationships with additional statistics
t_cols = ['driving_dist', 'driving_acc', 'gir', 'scrambling']
lagged_t_cols = ['lagged_driving_dist', 'lagged_driving_acc', 'lagged_gir', 'lagged_scrambling']
L4_t_cols = ['L4_moving_avg_driving_dist', 'L4_moving_avg_driving_acc', 'L4_moving_avg_gir', 'L4_moving_avg_scrambling']
L20_t_cols = ['L20_moving_avg_driving_dist', 'L20_moving_avg_driving_acc', 'L20_moving_avg_gir', 'L20_moving_avg_scrambling']

sns.pairplot(data=train_df_sorted, x_vars=t_cols, y_vars='round_score', plot_kws={'color': 'magenta'})
sns.pairplot(data=train_df_sorted, x_vars=lagged_t_cols, y_vars='round_score')
sns.pairplot(data=train_df_sorted, x_vars=L4_t_cols, y_vars='round_score')
sns.pairplot(data=train_df_sorted, x_vars=L20_t_cols, y_vars='round_score')


# Similar to the strokes gained pairplots, we see a similar trend with these secondary statistics. The magenta pairplot illustrates that an uptick in positive statistics inversely affects the round score. By modifying the x variables to include data from the previous round, the average of the last 4 rounds, and the average of the last 20 rounds, we examine their association with the players' subsequent round scores. Again, it emerges that long-term averages have a stronger correlation with future performance scores.

# In[8]:


# Creates histograms for further analysis
sns.histplot(train_df_sorted,x='round_score', bins=30)
score_mean = train_df_sorted['round_score'].mean()
plt.axvline(score_mean, color='red', label=f'Mean: {score_mean.round(2)}')
plt.axvline(72, color='magenta', label= 'Course Par', linestyle = '--')
plt.xlabel('Round Score')
plt.ylabel('Frequency')
plt.legend()
plt.title('Round Score Histogram')
plt.savefig('Round Score Histogram.png')
plt.show()

sns.histplot(train_df_sorted,x='driving_dist', bins=70)
dist_mean = train_df_sorted['driving_dist'].mean()
plt.axvline(dist_mean, color='red', label=f'Mean: {dist_mean.round(2)}')
plt.xlabel('Driving Distance')
plt.ylabel('Frequency')
plt.legend()
plt.title('Driving Distance Histogram')
plt.savefig('Driving Distance Histogram.png')
plt.show()


# We've provided 2 more important charts above that help us understand our data a bit more.
# 1. The first chart allows us to see the score distribution across all years of our dataset. It's clear that the mean is below the typical course par given that professional golfers tend to shoot under par more often than even or over par.
# 2. The second chart allows us to see the difference in driving distances. For the entire dataset, it appears the average driving distance is around 288 yards.

# In[9]:


# Creates correlation dataframe to analyze top coefficients
num_stat_df = train_df_sorted.copy()
num_stat_df = num_stat_df.drop(['tour','event_name','course_name','player_name','round_completed','event_completed','year'
                                        ,'season','event_completed','event_id','dg_id','round_num','course_num','course_par'
                                        ,'start_hole','sg_putt','sg_arg','sg_app','sg_ott','sg_t2g','sg_total','driving_dist'
                                        ,'driving_acc','gir','scrambling','prox_rgh','prox_fw','great_shots','poor_shots'
                                        ,'round_completed','month','day','fin_num','teetime_numeric','ohe_win','ohe_top_five'
                                        ,'ohe_top_ten','ohe_top_twenty','ohe_make_cut'], axis=1)
corr_df = num_stat_df.corr()


# In[10]:


# Top 20 most correlated features with round score
top_positive = corr_df['round_score'].sort_values(ascending=False).head(11)
top_negative = corr_df['round_score'].sort_values(ascending=True).head(10)


# In[11]:


top_positive.head(10)


# In[12]:


top_negative.head(10)


# In[13]:


# Creates Seaborn heatmap
top_features = pd.Index(top_positive.index.tolist() + top_negative.index.tolist()).drop_duplicates()
filtered_corr_matrix = corr_df.loc[top_features, top_features]
mask = np.triu(filtered_corr_matrix)
plt.figure(figsize=(15,10))
sns.heatmap(filtered_corr_matrix, annot=True, cmap="coolwarm", mask=mask)
plt.title("Heatmap of the Top 20 Correlated Features to 'round_score'")
plt.tight_layout()
plt.savefig('Heatmap of the Top 20 Correlated Features.png')
plt.show()


# The expansion of our feature set to over 470 dimensions presents a significant challenge for data visualization. To facilitate a deeper comprehension of the data prior to model development, we employed a Seaborn heatmap for the 20 most correlated features with round score. The heatmap assists in identifying the features with the greatest potential for predictive power in future models. The results of this analysis yielded some unexpected insights. While initial exploratory data analysis (EDA) led us to believe that longer-term moving averages would be more predictive, the coefficient analysis revealed a stronger influence from shorter-term averages. This underscores the importance of complementing visual analysis with quantitative methods to gain a more comprehensive understanding of complex datasets.

# ## Modeling

# ### Linear Regression

# In[14]:


# Copy test dataset for use later in the modeling process when we want to retrieve all players most recent round to feed to our model
current_df = test_df_sorted.copy()


# In[15]:


# Drop the non-numeric and non-lagged columns prior to training our model
train_df_sorted = train_df_sorted.drop(['tour','event_name','course_name','player_name','round_completed','event_completed','year'
                                        ,'season','event_completed','event_id','dg_id','round_num','course_num','course_par'
                                        ,'start_hole','sg_putt','sg_arg','sg_app','sg_ott','sg_t2g','sg_total','driving_dist'
                                        ,'driving_acc','gir','scrambling','prox_rgh','prox_fw','great_shots','poor_shots'
                                        ,'round_completed','month','day','fin_num','teetime_numeric','ohe_win','ohe_top_five'
                                        ,'ohe_top_ten','ohe_top_twenty','ohe_make_cut'], axis=1)

test_df_sorted = test_df_sorted.drop(['tour','event_name','course_name','player_name','round_completed','event_completed','year'
                                        ,'season','event_completed','event_id','dg_id','round_num','course_num','course_par'
                                        ,'start_hole','sg_putt','sg_arg','sg_app','sg_ott','sg_t2g','sg_total','driving_dist'
                                        ,'driving_acc','gir','scrambling','prox_rgh','prox_fw','great_shots','poor_shots'
                                        ,'round_completed','month','day','fin_num','teetime_numeric','ohe_win','ohe_top_five'
                                        ,'ohe_top_ten','ohe_top_twenty','ohe_make_cut'], axis=1)


# In[16]:


train_df_sorted.head()


# In[17]:


# Seperates our features from our target variable
X_train = train_df_sorted.drop(['round_score'], axis=1)
y_train = train_df_sorted['round_score']

X_test = test_df_sorted.drop(['round_score'], axis=1)
y_test = test_df_sorted['round_score']

# Scales the data with a standard scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Instantiates our linear regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Scores the linear regression model with our scaled train and test data
r2_train = model.score(X_train_scaled,y_train)
r2_test = model.score(X_test_scaled,y_test)

# Caclulates the mean absolute percentage error so we have another metric to evaluate our model on
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)
mape_train = mean_absolute_percentage_error(y_train_pred,y_train)
mape_test = mean_absolute_percentage_error(y_test_pred,y_test)

print(f' Train: \n r2: {r2_train:.4f} \n mape: {mape_train:.4f}')
print(f' Test: \n r2: {r2_test:.4f} \n mape: {mape_test:.4f}')


# **Model Analysis:**

# Upon evaluating our initial linear regression model, it's observed that the model exhibits an R-squared value of 0.2629 for the training dataset and 0.2635 for the testing dataset. This indicates that around 26% of the variability in the outcome variable is accounted for by the model. The consistency of r^2 values between training and testing datasets suggests that the model demonstrates good generalization capabilities, without signs of overfitting or underfitting. Additionally, the Mean Absolute Percentage Error (MAPE) is calculated to be 3.09% for the training and testing data. These percentages reflect that the model's predictions deviate from the actual values by an average of approximately 3.09%, which signifies a relatively high accuracy in predictions.

# ### Linear Pipeline

# In[ ]:


# Creates structure of our pipeline
estimators = [('scaler', StandardScaler()),
              ('reduce_dim', PCA(n_components=0.9)),
              ('model', LinearRegression())]

# Creates pipeline based on the list created above
pipe = Pipeline(estimators)

# Creates a parameter grid defining exactly what hyperparameters to search for during grid search cross-validation
param_grid = [{'scaler':[StandardScaler(), MinMaxScaler()],
               'reduce_dim':[None,PCA(n_components=0.9)],
               'model':[Lasso(max_iter=int(1e9))],
               'model__alpha':np.logspace(-3,2,50)},
              {'scaler':[StandardScaler(), MinMaxScaler()],
               'reduce_dim':[None,PCA(n_components=0.9)],
               'model':[Ridge(max_iter=int(1e9))],
               'model__alpha':np.logspace(0,10,50)},
             {'scaler':[StandardScaler(), MinMaxScaler()],
              'reduce_dim':[None,PCA(n_components=0.9)],
              'model':[LinearRegression()]}
             ]

# Sets up a grid search with the above pipeline, parameters, 5-fold cross validation, enables the use of all available CPUs, specifes the scoring metrics, and refits the final model based on the r^2 value
grid = GridSearchCV(pipe, param_grid,verbose=20,
                    scoring=["r2","neg_mean_absolute_percentage_error"],refit='r2')

# Fits the model on the training data to determine the optimal hyperparameters
fittedgrid = grid.fit(X_train, y_train)


# In[ ]:


# Finds optimal alpha range for our lasso parameters in the pipeline
results = pd.DataFrame(fittedgrid.cv_results_)
str(results.loc[0,"param_model"])
lasso_sel = results["param_model"].apply(lambda x:str(x).startswith("Lasso"))
lasso_results = results.loc[lasso_sel,["param_model__alpha","mean_test_r2","mean_test_neg_mean_absolute_percentage_error"]]
plt.figure()
plt.plot(lasso_results["param_model__alpha"],lasso_results["mean_test_r2"])
plt.xscale("log")
plt.xlabel("alpha")
plt.ylabel("R2")
ax2 = plt.gca().twinx()
ax2.plot(lasso_results["param_model__alpha"],lasso_results["mean_test_neg_mean_absolute_percentage_error"],color='red')


# In[ ]:


# Finds optimal alpha range for our ridge parameters in the pipeline
ridge_sel = results["param_model"].apply(lambda x:str(x).startswith("Ridge"))
ridge_results = results.loc[ridge_sel,["param_model__alpha","mean_test_r2","mean_test_neg_mean_absolute_percentage_error"]]
plt.figure()
plt.plot(ridge_results["param_model__alpha"],ridge_results["mean_test_r2"])
plt.xscale("log")
plt.xlabel("alpha")
plt.ylabel("R2")
ax2 = plt.gca().twinx()
ax2.plot(ridge_results["param_model__alpha"],ridge_results["mean_test_neg_mean_absolute_percentage_error"],color='red')


# The two charts above were employed to identify the ideal range for testing various alpha values in both Lasso and Ridge regression models.

# In[ ]:


# Retrieves best model from our grid search
fittedgrid.best_estimator_.get_params()


# In[ ]:


lp_r2_train = fittedgrid.best_estimator_.score(X_train,y_train)
lp_r2_test = fittedgrid.best_estimator_.score(X_test,y_test)

lp_y_train_pred = fittedgrid.best_estimator_.predict(X_train)
lp_y_test_pred = fittedgrid.best_estimator_.predict(X_test)

lp_mape_train = mean_absolute_percentage_error(y_train_pred,y_train)
lp_mape_test = mean_absolute_percentage_error(y_test_pred,y_test)

print(f' Train: \n r2: {lp_r2_train:.4f} \n mape: {lp_mape_train:.4f}')
print(f' Test: \n r2: {lp_r2_test:.4f} \n mape: {lp_mape_test:.4f}')


# **Model Analysis:**

# Through the application of a pipeline combined with grid search cross-validation, we successfully assessed various preprocessing and modeling options to identify the optimal configuration. Our exploration covered a range of parameters, including the choice between StandardScaler and MinMaxScaler for scaling, the decision to use PCA or bypass it for dimensionality reduction, different alpha values, and three distinct models. The outcome of this process revealed that the most effective model is a Lasso regression, characterized by an alpha value of 0.0065, employing a StandardScaler for data normalization, and opting out of PCA for dimensionality reduction. This model achieved an R-squared value of 0.2641 on the test data, which signifies that it can explain approximately 26% of the variance in the dependent variable.

# ### Random Forest Regressor

# In[18]:


# Creates structure of our pipeline
# Scalers removed based on educator suggestion on 4.12.24
estimators2 = [('reduce_dim', PCA(n_components=0.9)),
              ('model', RandomForestRegressor())]

# Creates pipeline based on the list created above
pipe2 = Pipeline(estimators2)

# Creates a parameter grid defining exactly what hyperparameters to search for during grid search cross-validation
param_grid2 = [{'reduce_dim': [None, PCA(n_components=0.9)],
                'model':[RandomForestRegressor()],
                'model__max_depth':[15]}
              ]

# Sets up a grid search with the above pipeline, parameters, 5-fold cross validation, enables the use of all available CPUs, specifes the scoring metrics, and refits the final model based on the r^2 value
grid2 = GridSearchCV(pipe2, param_grid2, cv=5,verbose=20,n_jobs=-1,
                    scoring=["r2","neg_mean_absolute_percentage_error"],refit='r2')

# Fits the model on the training data to determine the optimal hyperparameters
fittedgrid2 = grid2.fit(X_train, y_train)


# In[19]:


results2 = pd.DataFrame(fittedgrid2.cv_results_)


# In[20]:


results2[["param_reduce_dim","param_model__max_depth","mean_test_r2"]]


# In[21]:


fittedgrid2.best_estimator_


# In[27]:


fittedgrid2.best_estimator_.score(X_test,y_test)


# In[28]:


from joblib import dump, load


# In[29]:


dump(fittedgrid2.best_estimator_, 'random_forest_regressor.joblib')


# **Model Analysis:**

# Upon executing a random forest regressor pipeline, we observed an approximate 9% enhancement in our r^2 value. This signifies that the model now explains about 34.6% of the variation in the dependent variable, marking a significant improvement over our prior linear models. However, the primary drawback of employing this model lies in its substantial computational demands and the extended duration needed for training. Despite leveraging all available CPU cores, training times exceed 30 minutes and are expected to increase with the addition of more data for a relatively modest improvement in r^2. In summary, while the increase in r^2 is good, it comes at the expense of considerable computational resources and time.
# 
# Since sprint 2, we have refined this model based on feedback aimed at enhancing its performance. Initially, we removed scaling from the pipeline as it was deemed unnecessary for this type of model. Additionally, we reduced some of the initial maximum depths. This adjustment was made after gaining a clearer understanding of the optimal range from the initial r^2 values, which has expedited the training process by reducing the number of hyperparameter combinations the gridsearch needs to evaluate.

# ### Neural Network

# In[30]:


# Seperates our features from our target variable
X_train = train_df_sorted.drop(['round_score'], axis=1)
y_train = train_df_sorted['round_score']

X_test = test_df_sorted.drop(['round_score'], axis=1)
y_test = test_df_sorted['round_score']

# Scales the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[81]:


# Instantiates Keras Neural Network
model = keras.Sequential()


# Creates a regularizer with a factor of 0.0001 and apply it to all hidden layers
regularizer = keras.regularizers.l1(0.0001)

# Declares the hidden layers
model.add(layers.Dense(40, activation="relu", kernel_regularizer=regularizer))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(40, activation="relu", kernel_regularizer=regularizer))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(40, activation="relu", kernel_regularizer=regularizer))
model.add(layers.Dropout(0.2))


# Declares the output layer
model.add(layers.Dense(1))

# Compiles the model
optimizer = keras.optimizers.Adam()
loss=keras.losses.MeanSquaredError()

model.compile(optimizer=optimizer,
              loss=loss)

history = model.fit(X_train_scaled, y_train, epochs=100)


# In[82]:


# Evaluate the model using the test data and generate predictions
train_loss = history.history["loss"][-1]
result = model.evaluate(X_test_scaled, y_test, verbose=0)

print(f"Train Loss: {train_loss:.4f}")
print(f"Test Loss: {result:.4f}")

y_train_pred_nn = model.predict(X_train_scaled)
y_pred_nn = model.predict(X_test_scaled)


# In[83]:


print(f'Train r2: {r2_score(y_train,y_train_pred_nn):.4f}')
print(f'Test r2: {r2_score(y_test,y_pred_nn):.4f}')


# In[84]:


model.save('pga_nn_1')


# **Model Analysis:**

# After implementing a Keras sequential neural network, we noted an 16% increase in our r^2 value. This improvement means the model accounts for roughly 41% of the variance in the target variable, a substantial leap from the performance of our previous linear models. Moreover, this model operates within an acceptable timeframe and offers enhanced flexibility for customization and fine-tuning. Given these advantages, we've identified it as the most viable option available.
# 
# Since sprint 2, we have been meticulously adjusting various parameters of the neural network, including different alpha values for L1 regularization, dropout rates, the number and density of layers, and the number of epochs. We settled on this particular model configuration because it is the simplest, fastest, and most accurate version we tested. Adding complexity did not yield significant improvements, which led us to adopt the current iteration of the model.

# ***

# ## Model Projections

# In[85]:


# Retrieves every players most recent record
sorted_df = current_df.sort_values(by=['dg_id', 'round_completed'])
most_recent_scores = sorted_df.drop_duplicates(subset='dg_id', keep='last').reset_index(drop=True)


# In[86]:


most_recent_scores[most_recent_scores['player_name']== 'Scheffler, Scottie']


# In[87]:


# Drops the necessary columns prior to feeding the dataframe into our model
most_recent_scores = most_recent_scores.drop(['tour','event_name','course_name','player_name','round_completed','event_completed','year'
                                        ,'season','event_completed','event_id','round_num','course_num','course_par'
                                        ,'start_hole','sg_putt','sg_arg','sg_app','sg_ott','sg_t2g','sg_total','driving_dist'
                                        ,'driving_acc','gir','scrambling','prox_rgh','prox_fw','great_shots','poor_shots'
                                        ,'round_completed','month','day','fin_num','teetime_numeric','ohe_win','ohe_top_five'
                                        ,'ohe_top_ten','ohe_top_twenty','ohe_make_cut'], axis=1)

# Removes player IDs before modelling
preserved_ids = most_recent_scores[['dg_id']].copy()
most_recent_scores = most_recent_scores.drop(['dg_id','round_score'], axis=1)


# In[93]:


# Loops through predictions 4 times to simulate a full tournament and adds noise to output score to account for golfer variability day-to-day
sum_scores_df = preserved_ids.copy()
sum_scores_df['sum_predicted_score'] = 0

for i in range(4):
        mr_scaled = scaler.transform(most_recent_scores)
        predicted_score = model.predict(mr_scaled)
        noise = np.random.normal(0, 2, predicted_score.shape)

        predicted_score_noisy = predicted_score + noise
        predicted_score_noisy = predicted_score_noisy.round()
        sum_scores_df['sum_predicted_score'] += predicted_score_noisy.flatten()

result_df = sum_scores_df.merge(player_df[['dg_id', 'player_name']], on='dg_id', how='left')
this_week_df = result_df.merge(field_df[['dg_id', 'event_name']], on='dg_id', how='inner')

this_week_df_sorted = this_week_df.sort_values(by='sum_predicted_score', ascending=True)
this_week_df_sorted.head(10)


# Above, you can see an example of our model processing the latest data for each golfer, predicting their performance over four consecutive rounds, and then summing the scores to simulate a full tournament. In this simulation, Scottie Scheffler emerges as the winner, having recorded the lowest combined score across the four rounds.

# In[96]:


player_wins = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'wins': 0})
player_t5 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'top_5': 0})
player_t10 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'top_10': 0})
player_t20 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'top_20': 0})

num_iterations = 1000
for iteration in range(num_iterations):
    sum_scores_df = preserved_ids.copy()
    sum_scores_df['sum_predicted_score'] = 0

    for i in range(4):
        mr_scaled = scaler.transform(most_recent_scores)
        predicted_score = model.predict(mr_scaled)
        noise = np.random.normal(0, 2, predicted_score.shape)

        predicted_score_noisy = predicted_score + noise
        sum_scores_df['sum_predicted_score'] += predicted_score_noisy.flatten()

    result_df = sum_scores_df.merge(player_df[['dg_id', 'player_name']], on='dg_id', how='left')
    this_week_df = result_df.merge(field_df[['dg_id', 'event_name']], on='dg_id', how='inner')

    this_week_df_sorted = this_week_df.sort_values(by='sum_predicted_score', ascending=True)

    lowest_score_dg_id = this_week_df_sorted.iloc[0]['dg_id']
    t5_dg_ids = this_week_df_sorted.iloc[:5]['dg_id'].values
    t10_dg_ids = this_week_df_sorted.iloc[:10]['dg_id'].values
    t20_dg_ids = this_week_df_sorted.iloc[:20]['dg_id'].values


    player_wins.loc[player_wins['dg_id'] == lowest_score_dg_id, 'wins'] += 1
    player_t5.loc[player_t5['dg_id'].isin(t5_dg_ids), 'top_5'] += 1
    player_t10.loc[player_t10['dg_id'].isin(t10_dg_ids), 'top_10'] += 1
    player_t20.loc[player_t20['dg_id'].isin(t20_dg_ids), 'top_20'] += 1


player_wins['win_probability'] = (player_wins['wins'] / num_iterations)*100
player_t5['t5_probability'] = (player_t5['top_5'] / num_iterations)*100
player_t10['t10_probability'] = (player_t10['top_10'] / num_iterations)*100
player_t20['t20_probability'] = (player_t20['top_20'] / num_iterations)*100

fin_df1 = player_wins.merge(player_df[['dg_id', 'player_name']], on='dg_id', how='left').sort_values(by='wins', ascending=False)
fin_df2 = fin_df1.merge(player_t5, on='dg_id', how='left').sort_values(by=['wins','top_5'], ascending=[False,False])
fin_df3 = fin_df2.merge(player_t10, on='dg_id', how='left').sort_values(by=['wins','top_5','top_10'], ascending=[False,False,False])
fin_df4 = fin_df3.merge(player_t20, on='dg_id', how='left').sort_values(by=['wins','top_5','top_10','top_20'], ascending=[False,False,False,False])
final_fin_df = fin_df4[['dg_id','player_name','win_probability','t5_probability','t10_probability','t20_probability']].sort_values(by=['win_probability','t5_probability','t10_probability','t20_probability'], ascending=[False,False,False,False])


# In[99]:


final_fin_df.head(10)


# To improve the initial output, we've incorporated nested loops that enable us to simulate a tournament multiple times using our models. By introducing variability into the output, we can mimic the inherent randomness observed in each round of golf. This enhanced setup allows us to calculate the probabilities of various outcomes, much like how sportsbooks offer odds for golf tournaments. Using a different player from the previous example, Xander Schauffele has a 13.8% chance of winning, a 56.6% chance of finishing in the Top 5, a 85.3% chance of being in the Top 10, and a 99.5% chance of finishing within the Top 20, based on 1,000 simulations of the next tournament.

# ***

# ## Conclusion

# We have effectively optimized and refined our models since their initial deployment in sprint 2. Additionally, we expanded on their practical application by generating tournament outcome probabilities for each player for the upcoming tournament, enabling us to deploy our models in a real-world environment. We intend to continue fine-tuning these models and also plan to develop variations of the program, such as predicting outcomes of matchups between two players, another common type of golf wager.
# 
# Given the robust use case now established for our model, we have developed the first version of our Streamlit app, which is available on my GitHub. It will soon be deployed publicly for consumer use.

# ***

# ## Citations

# #### Links:
#     - https://docs.python.org/3/library/datetime.html
#     - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
#     - https://github.com/mwaskom/seaborn/issues/2726
# #### ChatGPT Prompts:
#     - "How to create rolling average functions in pandas dataframes?"
#     - "Subtracting an integer from a date column in pandas based on conditions where we would use nested ifs?"
#     - "What is the following warning: PerformanceWarning: DataFrame is highly fragmented.  This is usually the result of calling `frame.insert` many times, which has poor performance.  Consider joining all columns at once using pd.concat(axis=1) instead. To get a de-fragmented frame, use `newframe = frame.copy()`"
#     - "How to retrieve the last instance of a record in pandas dataframe based on specific criteria?"
#     - "How to create a seaborn heatmap with the 10 most correlated features?"
#     - "Best ways to add noise to output of machine learning model to simulate variability?"

# ***
