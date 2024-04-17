# The following code is utilized to deploy PrecisionPicksPGA on Streamlit
# Author: Matt Bonadies

# import libraries
import streamlit as st
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
from PIL import Image
import joblib
import base64
import io
from io import BytesIO
import time

##############################################################################################################
@st.cache_data
def load_data(filedf):
    df = pd.read_csv(filedf)
    return df

def load_model():
    model = keras.models.load_model('Streamlit/pga_nn_1.h5') #
    return model


##############################################################################################################
image_path = 'Streamlit/PrecisionPicksPGA.png' #
image = Image.open(image_path)

def get_image_as_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    encoded_string = base64.b64encode(buffered.getvalue()).decode()
    return encoded_string

base64_image = get_image_as_base64(image)

html_code = f"""
<style>
    .image-container {{
        text-align: center;
        margin-top: -110px;
    }}
</style>
<div class='image-container'>
    <img src='data:image/png;base64,{base64_image}' width='300'>
</div>
"""

st.sidebar.markdown(html_code, unsafe_allow_html=True)
st.sidebar.title("Welcome to PrecisionPicksPGA")

##############################################################################################################

x=0
def home_page():
    st.write("TensorFlow version:", tf.__version__)
    st.write("Keras version:", keras.__version__)
    global x

    st.title("Tournament Prediction Model")

    train_df_sorted = load_data('./data/train_df_sorted.csv')
    test_df_sorted = load_data('./data/test_df_sorted.csv')
    player_df = load_data('./data/player_df.csv')
    field_df = load_data('./data/raw_pga_14_2024.csv')
    total_df_sorted = load_data('./data/total_df_sorted.csv')
    total_df_sorted = total_df_sorted.sort_values(by='round_completed', ascending=True)
    

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
    model = load_model()
    
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


    
    input_iter = st.number_input('Enter Number of Tournament Model Iterations (Recommended Range: 500-10000)', min_value=1, value=10,format="%d")
    if st.button('Run Tournament Simulation'):
        progress_text = "Model in process. Please wait."
        my_bar = st.progress(0, text=progress_text)
        
        

        player_wins = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'wins': 0})
        player_t5 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'top_5': 0})
        player_t10 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'top_10': 0})
        player_t20 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'top_20': 0})
        
        iternum = int(input_iter)
        num_iterations = iternum
        for iteration in range(num_iterations):
            # time.sleep(0.01)
            my_bar.progress((iteration + 1)/num_iterations, text=progress_text)

            sum_scores_df = preserved_ids.copy()
            sum_scores_df['sum_predicted_score'] = 0

            for i in range(4):
                mr_scaled = scaler.transform(most_recent_scores)
                predicted_score = model.predict(mr_scaled)
                noise = np.random.normal(0, 2, predicted_score.shape)
                
                predicted_score_noisy = predicted_score + noise
                predicted_score_noisy = predicted_score_noisy
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
            
        time.sleep(1)
        my_bar.empty()
        player_wins['win_probability'] = (player_wins['wins'] / num_iterations)
        player_t5['t5_probability'] = (player_t5['top_5'] / num_iterations)
        player_t10['t10_probability'] = (player_t10['top_10'] / num_iterations)
        player_t20['t20_probability'] = (player_t20['top_20'] / num_iterations)

        fin_df1 = player_wins.merge(this_week_df[['dg_id', 'player_name']], on='dg_id', how='inner').sort_values(by='wins', ascending=False)
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

        st.dataframe(final_fin_df, height=500)


##############################################################################################################
def two_ball_model():
    global x

    st.title("2-Ball Matchup Model")

    train_df_sorted = load_data('./data/train_df_sorted.csv')
    test_df_sorted = load_data('./data/test_df_sorted.csv')
    player_df = load_data('./data/player_df.csv')
    total_df_sorted = load_data('./data/total_df_sorted.csv')
    total_df_sorted = total_df_sorted.sort_values(by='round_completed', ascending=True)
    

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
    model = load_model()
    
    

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

    player_names = total_df_sorted['player_name'].unique()
    
    ##############################################################################################################
    selected_player = st.selectbox('Select Player 1', np.sort(player_names), index = 799)
    selected_player2 = st.selectbox('Select Player 2', np.sort(player_names), index = 606)
    input_iter2 = st.number_input('Enter Number of Matchup Model Iterations (Recommended Range: 500-10000)', min_value=1, value=10,format="%d")
    if st.button('Run Matchup Simulation'):
        progress_text = "Model in process. Please wait."
        my_bar = st.progress(0, text=progress_text)
        
                 
        p1_df = player_df[player_df['player_name'] == selected_player].loc[:, ['dg_id']]
        p2_df = player_df[player_df['player_name'] == selected_player2].loc[:, ['dg_id']]
        sel_players_df = pd.concat([p1_df, p2_df])

        player_wins2 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'wins': 0})

        iternum2 = int(input_iter2)
        num_iterations2 = iternum2
        for iteration2 in range(num_iterations2):
            my_bar.progress((iteration2 + 1)/num_iterations2, text=progress_text)
            sum_scores_df2 = preserved_ids.copy()
            sum_scores_df2['sum_predicted_score'] = 0

            for i2 in range(4):
                mr_scaled2 = scaler.transform(most_recent_scores)
                predicted_score2 = model.predict(mr_scaled2)
                noise2 = np.random.normal(0, 2, predicted_score2.shape)

                predicted_score_noisy2 = predicted_score2 + noise2
                sum_scores_df2['sum_predicted_score'] += predicted_score_noisy2.flatten()

            result_df2 = sum_scores_df2.merge(player_df[['dg_id', 'player_name']], on='dg_id', how='left')
            this_week_df2 = result_df2.merge(sel_players_df[['dg_id']], on='dg_id', how='inner')

            this_week_df_sorted2 = this_week_df2.sort_values(by='sum_predicted_score', ascending=True)

            lowest_score_dg_id2 = this_week_df_sorted2.iloc[0]['dg_id']
            player_wins2.loc[player_wins2['dg_id'] == lowest_score_dg_id2, 'wins'] += 1
        
        time.sleep(1)
        my_bar.empty()

        player_wins2['win_probability'] = (player_wins2['wins'] / num_iterations2)

        match_win = player_wins2.merge(this_week_df_sorted2[['dg_id', 'player_name']], on='dg_id', how='inner').sort_values(by='wins', ascending=False)
        final_match_win = match_win[['dg_id','player_name','win_probability']].sort_values(by='win_probability', ascending=False)
        final_match_win = final_match_win.style.format({
            'win_probability': '{:.1%}'
            })
        st.dataframe(final_match_win)
        
        ##############################################################################################################

    

##############################################################################################################
def three_ball_model():
    global x

    st.title("3-Ball Matchup Model")

    train_df_sorted = load_data('./data/train_df_sorted.csv')
    test_df_sorted = load_data('./data/test_df_sorted.csv')
    player_df = load_data('./data/player_df.csv')
    total_df_sorted = load_data('./data/total_df_sorted.csv')
    total_df_sorted = total_df_sorted.sort_values(by='round_completed', ascending=True)
    

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
    model = load_model()

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

    player_names = total_df_sorted['player_name'].unique()
    
    ##############################################################################################################
    selected_player = st.selectbox('Select Player 1', np.sort(player_names), index = 799)
    selected_player2 = st.selectbox('Select Player 2', np.sort(player_names), index = 606)
    selected_player3 = st.selectbox('Select Player 3', np.sort(player_names), index = 145)
    input_iter2 = st.number_input('Enter Number of Matchup Model Iterations (Recommended Range: 500-10000)', min_value=1, value=10,format="%d")
    if st.button('Run Matchup Simulation'):
        progress_text = "Model in process. Please wait."
        
        my_bar = st.progress(0, text=progress_text)
                 
        p1_df = player_df[player_df['player_name'] == selected_player].loc[:, ['dg_id']]
        p2_df = player_df[player_df['player_name'] == selected_player2].loc[:, ['dg_id']]
        p3_df = player_df[player_df['player_name'] == selected_player3].loc[:, ['dg_id']]
        sel_players_df = pd.concat([p1_df, p2_df, p3_df])

        player_wins2 = pd.DataFrame({'dg_id': preserved_ids['dg_id'], 'wins': 0})

        iternum2 = int(input_iter2)
        num_iterations2 = iternum2
        for iteration2 in range(num_iterations2):
            my_bar.progress((iteration2 + 1)/num_iterations2, text=progress_text)
            sum_scores_df2 = preserved_ids.copy()
            sum_scores_df2['sum_predicted_score'] = 0

            for i2 in range(4):
                mr_scaled2 = scaler.transform(most_recent_scores)
                predicted_score2 = model.predict(mr_scaled2)
                noise2 = np.random.normal(0, 2, predicted_score2.shape)

                predicted_score_noisy2 = predicted_score2 + noise2
                sum_scores_df2['sum_predicted_score'] += predicted_score_noisy2.flatten()

            result_df2 = sum_scores_df2.merge(player_df[['dg_id', 'player_name']], on='dg_id', how='left')
            this_week_df2 = result_df2.merge(sel_players_df[['dg_id']], on='dg_id', how='inner')

            this_week_df_sorted2 = this_week_df2.sort_values(by='sum_predicted_score', ascending=True)

            lowest_score_dg_id2 = this_week_df_sorted2.iloc[0]['dg_id']
            player_wins2.loc[player_wins2['dg_id'] == lowest_score_dg_id2, 'wins'] += 1
        
        time.sleep(1)
        my_bar.empty()

        player_wins2['win_probability'] = (player_wins2['wins'] / num_iterations2)

        match_win = player_wins2.merge(this_week_df_sorted2[['dg_id', 'player_name']], on='dg_id', how='inner').sort_values(by='wins', ascending=False)
        final_match_win = match_win[['dg_id','player_name','win_probability']].sort_values(by='win_probability', ascending=False)
        final_match_win = final_match_win.style.format({
            'win_probability': '{:.1%}'
            })
        st.dataframe(final_match_win)
        
        ##############################################################################################################


##############################################################################################################
def stats_page():
    st.title("Player Scoring & Statistics History")
    
    total_df_sorted = load_data('./data/total_df_sorted.csv')
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

##############################################################################################################
page = st.sidebar.radio("Choose a page:", ('Tournament Prediction Model', '2-Ball Matchup Model', '3-Ball Matchup Model','Player Scoring & Statistics History'))
##############################################################################################################
def load_data(filedf):
        df = pd.read_csv(filedf)
        return df
rank_df = load_data('./data/rank_df.csv')
st.sidebar.title("World Golf Rankings")
rank_df = rank_df.sort_values(by='owgr_rank', ascending=True)
st.sidebar.dataframe(rank_df, height=200)

if page == 'Tournament Prediction Model':
    home_page()
elif page == '2-Ball Matchup Model':
    two_ball_model()
elif page == '3-Ball Matchup Model':
    three_ball_model()
elif page == 'Player Scoring & Statistics History':
    stats_page()

##############################################################################################################