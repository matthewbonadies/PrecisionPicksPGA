# The following code is utilized to deploy PrecisionPicksPGA on Streamlit
# Author: Matt Bonadies

# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import plotly.express as px
from datetime import datetime, timedelta
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
import streamlit as st
import joblib

def home_page():
    #######################################################################################################################################
    st.title("Tournament Outcomes Model")
    @st.cache_data
    def load_data(filedf):
        df = pd.read_csv(filedf)
        return df

    #######################################################################################################################################
    train_df_sorted = load_data('../data/train_df_sorted.csv')
    test_df_sorted = load_data('../data/test_df_sorted.csv')
    player_df = load_data('../data/player_df.csv')
    field_df = load_data('../data/field_df.csv')

    #######################################################################################################################################
    # Drop the non-numeric and non-lagged columns prior to training our model
    train_df_sorted = train_df_sorted.drop(['tour','event_name','course_name','player_name','round_completed','event_completed','year'
                                            ,'season','event_completed','event_id','dg_id','round_num','course_num','course_par'
                                            ,'start_hole','sg_putt','sg_arg','sg_app','sg_ott','sg_t2g','sg_total','driving_dist'
                                            ,'driving_acc','gir','scrambling','prox_rgh','prox_fw','great_shots','poor_shots'
                                            ,'round_completed','month','day','fin_num','teetime_numeric','ohe_win','ohe_top_five'
                                            ,'ohe_top_ten','ohe_top_twenty','ohe_make_cut'], axis=1)

    predict_df_sorted = test_df_sorted.copy()
    test_df_sorted = test_df_sorted.drop(['tour','event_name','course_name','player_name','round_completed','event_completed','year'
                                            ,'season','event_completed','event_id','dg_id','round_num','course_num','course_par'
                                            ,'start_hole','sg_putt','sg_arg','sg_app','sg_ott','sg_t2g','sg_total','driving_dist'
                                            ,'driving_acc','gir','scrambling','prox_rgh','prox_fw','great_shots','poor_shots'
                                            ,'round_completed','month','day','fin_num','teetime_numeric','ohe_win','ohe_top_five'
                                            ,'ohe_top_ten','ohe_top_twenty','ohe_make_cut'], axis=1)

    # Seperates our features from our target variable
    X_train = train_df_sorted.drop(['round_score'], axis=1)
    y_train = train_df_sorted['round_score']

    X_test = test_df_sorted.drop(['round_score'], axis=1)
    y_test = test_df_sorted['round_score']

    # Scales the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = keras.models.load_model('pga_nn_1')

    #######################################################################################################################################
    sorted_df = predict_df_sorted.sort_values(by=['dg_id', 'round_completed'])
    most_recent_scores = sorted_df.drop_duplicates(subset='dg_id', keep='last').reset_index(drop=True)

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

    #######################################################################################################################################
    player_wins = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'wins': 0})
    player_t5 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'top_5': 0})
    player_t10 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'top_10': 0})
    player_t20 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'top_20': 0})

    input_iter = st.number_input('Enter Number of Model Iterations (Recommended Range: 500-10000)', min_value=1, value=10,format="%d")
    iternum = int(input_iter)

    num_iterations = iternum
    for iteration in range(num_iterations):    
        sum_scores_df = preserved_ids.copy()
        sum_scores_df['sum_predicted_score'] = 0

        for _ in range(4):
            mr_scaled = scaler.transform(most_recent_scores)
            predicted_score = model.predict(mr_scaled)
            noise = np.random.normal(0, 2, predicted_score.shape)
            
            predicted_score_noisy = predicted_score + noise
            predicted_score_noisy = predicted_score_noisy.round()
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
        

    player_wins['win_probability'] = (player_wins['wins'] / num_iterations)
    player_t5['t5_probability'] = (player_t5['top_5'] / num_iterations)
    player_t10['t10_probability'] = (player_t10['top_10'] / num_iterations)
    player_t20['t20_probability'] = (player_t20['top_20'] / num_iterations)

    fin_df1 = player_wins.merge(player_df[['dg_id', 'player_name']], on='dg_id', how='left').sort_values(by='wins', ascending=False)
    fin_df2 = fin_df1.merge(player_t5, on='dg_id', how='left').sort_values(by=['wins','top_5'], ascending=[False,False])
    fin_df3 = fin_df2.merge(player_t10, on='dg_id', how='left').sort_values(by=['wins','top_5','top_10'], ascending=[False,False,False])
    fin_df4 = fin_df3.merge(player_t20, on='dg_id', how='left').sort_values(by=['wins','top_5','top_10','top_20'], ascending=[False,False,False,False])
    final_fin_df = fin_df4[['dg_id','player_name','win_probability','t5_probability','t10_probability','t20_probability']].sort_values(by=['win_probability','t5_probability','t10_probability','t20_probability'], ascending=[False,False,False,False])
    final_fin_df = final_fin_df.style.format({
        'win_probability': '{:.1%}',
        't5_probability': '{:.1%}',
        't10_probability': '{:.1%}',
        't20_probability': '{:.1%}'
        })

    st.dataframe(final_fin_df, height=700)

def stats_page():
    st.title("Player Scoring & Statistics History")
    def load_data(filedf):
        df = pd.read_csv(filedf)
        return df    
    
    total_df_sorted = load_data('../data/total_df_sorted.csv')
    total_df_sorted = total_df_sorted.sort_values(by='round_completed', ascending=True)
    
    total_df_sorted['round_completed'] = pd.to_datetime(total_df_sorted['round_completed'])
    player_names = total_df_sorted['player_name'].unique()
    selected_player = st.selectbox('Select', np.sort(player_names))
    filter_player_df = total_df_sorted[total_df_sorted['player_name'] == selected_player]
    fig = px.line(filter_player_df, x='round_completed', y='L20_moving_avg_round_score', title='Scores Over Time')
    fig.update_xaxes(title_text='Round Date')
    fig.update_yaxes(title_text='L20 Round Scoring Average')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

    fig1 = px.histogram(filter_player_df['round_score'], title='Score Distribution')
    fig1.update_xaxes(title_text='Round Score')
    fig1.update_yaxes(title_text='Frequency')
    st.plotly_chart(fig1)


    filter_player_df['fin_group'] = filter_player_df['fin_num'].apply(lambda x: 41 if x == 0 or x >= 40 else x)
    fig2 = px.histogram(filter_player_df['fin_group'], title='Finish Position Distribution')
    fig2.update_xaxes(title_text='Finish Position')
    fig2.update_yaxes(title_text='Frequency')
    st.plotly_chart(fig2)

st.sidebar.title("Welcome to PrecisionPicksPGA")
page = st.sidebar.radio("Choose a page:", ('Model', 'Player Scoring & Statistics History'))

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")

def load_data(filedf):
        df = pd.read_csv(filedf)
        return df
rank_df = load_data('../data/rank_df.csv')
st.sidebar.title("World Golf Rankings")
rank_df = rank_df.sort_values(by='owgr_rank', ascending=True)
st.sidebar.dataframe(rank_df)

if page == 'Model':
    home_page()
elif page == 'Player Scoring & Statistics History':
    stats_page()
