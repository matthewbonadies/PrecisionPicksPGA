# PrecisionPicksPGA
=========================

## Project Overview
... ... ...

### Introduction
The landscape of sports betting has significantly transformed following the Supreme Court's 2018 decision to reverse the federal law banning sports betting. With approximately 38 states legalizing sports betting in various forms and the legal online sports betting market in the U.S. reaching over $10 billion in 2023, there's a growing demand for sophisticated analytical tools to navigate this booming industry. As a former competitive golfer with a deep understanding of the sport and its data, I aim to merge my passion for golf with advanced analytics to develop a machine learning model that predicts the outcomes of PGA Tour Matchups relative to sportsbook projections.

### Problem
The challenge lies in the overwhelming volume of detailed golf data, which, while rich in insights, can be daunting to analyze effectively. This data encapsulates a broad spectrum of performance metrics, making it difficult to discern the critical factors influencing matchup outcomes. These obstacles make it difficult for professionals and fans alike to effectively use the right information to enhance their grasp of the competitive landscape to employ effective betting strategies for the long-term.

### Vision
With this project, our goal is to fill the void in easily accessible, data-driven insights regarding PGA Tour results, providing individuals with the tools needed to confidently understand and navigate the complexities of sports betting. We seek not just to analyze betting intricacies using machine learning but also to deepen the sports community's comprehension and involvement with golf.

## Project Organization
... ... ...

- `Notebooks`
    - Contains all final notebooks involved in the project
- `Data`
    - Contains link to copy of the dataset
- `Data Dictionary`
    - Structure and description of dataset utilized
- `Presentations`
    - Contains final report which summarizes the project
- `src`
    - Contains the project source code
- `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control
- `capstone_env.yml`
    - Conda environment specification
- `Streamlit`
    - Contains code for deploying the Streamlit application
- `README.md`
    - Project landing page (this page)
- `LICENSE`
    - Project license

## Dataset
... ... ...

API Provided by [https://datagolf.com/](https://datagolf.com/)
Sample Data Available in `Data`

## Data Dictionary
... ... ...

`Player Statistics DataFrame`
- tour
- year
- season
- event_completed
- event_name
- event_id
- player_name
- dg_id
- fin_text
- round_num
- course_name
- course_num
- course_par
- start_hole
- teetime
- round_score
- sg_putt
- sg_arg
- sg_app
- sg_ott
- sg_t2g
- sg_total
- driving_dist
- driving_acc
- gir
- scrambling
- prox_rgh
- prox_fw
- great_shots
- poor_shots

`Historical Betting Statistics DataFrame`
- p2_outcome_text
- p2_outcome
- close_time
- bet_type
- p1_outcome_text
- p2_open
- p1_outcome
- tie_rule
- p2_close
- p1_open
- p2_dg_id
- p1_dg_id
- p1_player_name
- open_time
- p2_player_name
- p1_close
- book
- event_completed
- event_name
- season
- year
- event_id

`Player Rankings DataFrame`
- player_name
- dg_id
- country
- am
- primary_tour
- datagolf_rank
- owgr_rank
- dg_skill_estimate
- last_updated
- notes

`Course Statistics DataFrame`
- course
- par
- yardage
- yardage_4_5
- yardage_3
- adj_score_to_par
- adj_par_3_score
- adj_par_4_score
- adj_par_5_score
- adj_driving_distance
- adj_sd_distance
- adj_driving_accuracy
- putt_sg
- arg_sg
- app_sg
- ott_sg
- fw_width
- miss_fw_pen_frac
- adj_gir
- less_150_sg
- greater_150_sg
- arg_fairway_sg
- arg_rough_sg
- arg_bunker_sg
- less_5_ft_sg
- greater_5_less_15_sg
- greater_15_sg
