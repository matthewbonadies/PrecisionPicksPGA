| Column | Type | Description |
| --- | --- | --- |
|tour| object | Professional tour that the event was played on. |
|year| int64 | Calendar year. |
|season| int64 | Official season as defined by the PGA tour. |
|event_completed| datetime64[ns] | Official date of the final round of the tournament  |
|event_name| object | Name of tournament. |
|event_id| int64 | Unique Tournament ID number. |
|player_name| object | Name of player. |
|dg_id| int64 | Unique Player ID number. There is a single dg_id for each player. |
|round_num| int64 | Round number for the given tournament. Ranges from 1-4. |
|course_name| object | Name of golf course. |
|course_num| int64 | Unique Course ID number. |
|course_par| int64 | Course par - Scoring benchmark. Value is typically 72, but it can range from 70 to 72. |
|start_hole| int64 | Hole number that player started on. Value is either 1 or 10. |
|round_score| int64 | Score that was shot for the given round. Our model’s target variable. |
|sg_putt| float64 | Strokes gained putting.  |
|sg_arg| float64 | Strokes gained around the green.  |
|sg_app| float64 | Strokes gained approaching the green. |
|sg_ott| float64 | Strokes gained off the tee. |
|sg_t2g| float64 | Strokes gained from tee to green. The sum of sg_ott, sg_app, and sg_arg. |
|sg_total| float64 | Strokes gained total. Difference between the player’s score and the average score. |
|driving_dist| float64 | Average distance of every drive hit. |
|driving_acc| float64 | Fairways in regulation. Percentage of fairways. |
|gir| float64 | Greens in regulation. Percentage of greens hit. |
|scrambling| float64 | Percentage of shots  ≤ 50 yards that were holed out in 2 strokes or less. |
|prox_rgh| float64 | Average proximity of all shots hit from locations other than the fairway. |
|prox_fw| float64 | Average proximity of all shots hit from the fairway. |
|great_shots| float64 | Sum of shots that fall into the top 5% of strokes-gained values in each category. |
|poor_shots| float64 | Sum of shots that fall into the bottom 5% of strokes-gained values in each category. |
|fin_num| int64 | Official finishing position. |
|teetime_numeric| float64 | Time a player tee’d off. |
|round_completed| datetime64[ns] | Date the round was played. |
|month| int32 | Month the round was played. |
|day| int32 | Day of month the round was played. |
|ohe_win| int64 | Binary value if the player won or not. |
|ohe_top_five| int64 | Binary value if the player finished in the top 5 or not. |
|ohe_top_ten| int64 | Binary value if the player finished in the top 10 or not. |
|ohe_top_twenty| int64 | Binary value if the player finished in the top 20 or not. |
|ohe_make_cut| int64 | Binary value if the player made the cut after 2 rounds or not. |
|career_moving_avg_sg_putt| float64 | Average strokes gained putting for entire timeframe of dataset.|
|career_moving_med_sg_putt| float64 | Median strokes gained putting for entire timeframe of dataset.|
|L44_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 44 rounds. |
|L44_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 44 rounds. |
|L36_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 36 rounds. |
|L36_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 36 rounds. |
|L28_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 28 rounds. |
|L28_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 28 rounds. |
|L24_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 24 rounds. |
|L24_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 24 rounds. |
|L20_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 20 rounds. |
|L20_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 20 rounds. |
|L16_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 16 rounds. |
|L16_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 16 rounds. |
|L12_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 12 rounds. |
|L12_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 12 rounds. |
|L8_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 8 rounds. |
|L8_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 8 rounds. |
|L4_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 4 rounds. |
|L4_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 4 rounds. |
|L3_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 3 rounds. |
|L3_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 3 rounds. |
|L2_moving_avg_sg_putt| float64 | Average strokes gained putting from the last 2 rounds. |
|L2_sg_putt_std_dev| float64 | Standard deviation of strokes gained putting from the last 2 rounds. |
|L45_moving_med_sg_putt| float64 | Median strokes gained putting from last 45 rounds. |
|L37_moving_med_sg_putt| float64 | Median strokes gained putting from last 37 rounds. |
|L29_moving_med_sg_putt| float64 | Median strokes gained putting from last 29 rounds. |
|L21_moving_med_sg_putt| float64 | Median strokes gained putting from last 21 rounds. |
|L15_moving_med_sg_putt| float64 | Median strokes gained putting from last 15 rounds. |
|L11_moving_med_sg_putt| float64 | Median strokes gained putting from last 11 rounds. |
|L9_moving_med_sg_putt| float64 | Median strokes gained putting from last 9 rounds. |
|L7_moving_med_sg_putt| float64 | Median strokes gained putting from last 7 rounds. |
|L5_moving_med_sg_putt| float64 | Median strokes gained putting from last 5 rounds. |
|L3_moving_med_sg_putt| float64 | Median strokes gained putting from last 3 rounds. |
|career_moving_avg_sg_arg| float64 | Average strokes gained around the green for entire timeframe of dataset.|
|career_moving_med_sg_arg| float64 | Median strokes gained around the green for entire timeframe of dataset.|
|L44_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 44 rounds. |
|L44_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 44 rounds. |
|L36_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 36 rounds. |
|L36_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 36 rounds. |
|L28_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 28 rounds. |
|L28_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 28 rounds. |
|L24_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 24 rounds. |
|L24_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 24 rounds. |
|L20_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 20 rounds. |
|L20_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 20 rounds. |
|L16_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 16 rounds. |
|L16_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 16 rounds. |
|L12_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 12 rounds. |
|L12_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 12 rounds. |
|L8_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 8 rounds. |
|L8_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 8 rounds. |
|L4_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 4 rounds. |
|L4_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 4 rounds. |
|L3_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 3 rounds. |
|L3_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 3 rounds. |
|L2_moving_avg_sg_arg| float64 | Average strokes gained around the green from the last 2 rounds. |
|L2_sg_arg_std_dev| float64 | Standard deviation of strokes gained around the green from the last 2 rounds. |
|L45_moving_med_sg_arg| float64 | Median strokes gained around the green from last 45 rounds. |
|L37_moving_med_sg_arg| float64 | Median strokes gained around the green from last 37 rounds. |
|L29_moving_med_sg_arg| float64 | Median strokes gained around the green from last 29 rounds. |
|L21_moving_med_sg_arg| float64 | Median strokes gained around the green from last 21 rounds. |
|L15_moving_med_sg_arg| float64 | Median strokes gained around the green from last 15 rounds. |
|L11_moving_med_sg_arg| float64 | Median strokes gained around the green from last 11 rounds. |
|L9_moving_med_sg_arg| float64 | Median strokes gained around the green from last 9 rounds. |
|L7_moving_med_sg_arg| float64 | Median strokes gained around the green from last 7 rounds. |
|L5_moving_med_sg_arg| float64 | Median strokes gained around the green from last 5 rounds. |
|L3_moving_med_sg_arg| float64 | Median strokes gained around the green from last 3 rounds. |
|career_moving_avg_sg_app| float64 | Average strokes gained approaching the green for entire timeframe of dataset.|
|career_moving_med_sg_app| float64 | Median strokes gained approaching the green for entire timeframe of dataset.|
|L44_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 44 rounds. |
|L44_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 44 rounds. |
|L36_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 36 rounds. |
|L36_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 36 rounds. |
|L28_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 28 rounds. |
|L28_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 28 rounds. |
|L24_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 24 rounds. |
|L24_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 24 rounds. |
|L20_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 20 rounds. |
|L20_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 20 rounds. |
|L16_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 16 rounds. |
|L16_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 16 rounds. |
|L12_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 12 rounds. |
|L12_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 12 rounds. |
|L8_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 8 rounds. |
|L8_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 8 rounds. |
|L4_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 4 rounds. |
|L4_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 4 rounds. |
|L3_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 3 rounds. |
|L3_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 3 rounds. |
|L2_moving_avg_sg_app| float64 | Average strokes gained approaching the green from the last 2 rounds. |
|L2_sg_app_std_dev| float64 | Standard deviation of strokes gained approaching the green from the last 2 rounds. |
|L45_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 45 rounds. |
|L37_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 37 rounds. |
|L29_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 29 rounds. |
|L21_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 21 rounds. |
|L15_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 15 rounds. |
|L11_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 11 rounds. |
|L9_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 9 rounds. |
|L7_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 7 rounds. |
|L5_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 5 rounds. |
|L3_moving_med_sg_app| float64 | Median strokes gained approaching the green from last 3 rounds. |
|career_moving_avg_sg_ott| float64 | Average strokes gained off the tee for entire timeframe of dataset.|
|career_moving_med_sg_ott| float64 | Median strokes gained off the tee for entire timeframe of dataset.|
|L44_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 44 rounds. |
|L44_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 44 rounds. |
|L36_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 36 rounds. |
|L36_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 36 rounds. |
|L28_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 28 rounds. |
|L28_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 28 rounds. |
|L24_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 24 rounds. |
|L24_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 24 rounds. |
|L20_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 20 rounds. |
|L20_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 20 rounds. |
|L16_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 16 rounds. |
|L16_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 16 rounds. |
|L12_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 12 rounds. |
|L12_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 12 rounds. |
|L8_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 8 rounds. |
|L8_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 8 rounds. |
|L4_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 4 rounds. |
|L4_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 4 rounds. |
|L3_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 3 rounds. |
|L3_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 3 rounds. |
|L2_moving_avg_sg_ott| float64 | Average strokes gained off the tee from the last 2 rounds. |
|L2_sg_ott_std_dev| float64 | Standard deviation of strokes gained off the tee from the last 2 rounds. |
|L45_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 45 rounds. |
|L37_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 37 rounds. |
|L29_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 29 rounds. |
|L21_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 21 rounds. |
|L15_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 15 rounds. |
|L11_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 11 rounds. |
|L9_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 9 rounds. |
|L7_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 7 rounds. |
|L5_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 5 rounds. |
|L3_moving_med_sg_ott| float64 | Median strokes gained off the tee from last 3 rounds. |
|career_moving_avg_sg_t2g| float64 | Average strokes gained tee to green for entire timeframe of dataset.|
|career_moving_med_sg_t2g| float64 | Median strokes gained tee to green for entire timeframe of dataset.|
|L44_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 44 rounds. |
|L44_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 44 rounds. |
|L36_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 36 rounds. |
|L36_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 36 rounds. |
|L28_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 28 rounds. |
|L28_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 28 rounds. |
|L24_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 24 rounds. |
|L24_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 24 rounds. |
|L20_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 20 rounds. |
|L20_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 20 rounds. |
|L16_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 16 rounds. |
|L16_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 16 rounds. |
|L12_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 12 rounds. |
|L12_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 12 rounds. |
|L8_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 8 rounds. |
|L8_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 8 rounds. |
|L4_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 4 rounds. |
|L4_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 4 rounds. |
|L3_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 3 rounds. |
|L3_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 3 rounds. |
|L2_moving_avg_sg_t2g| float64 | Average strokes gained tee to green from the last 2 rounds. |
|L2_sg_t2g_std_dev| float64 | Standard deviation of strokes gained tee to green from the last 2 rounds. |
|L45_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 45 rounds. |
|L37_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 37 rounds. |
|L29_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 29 rounds. |
|L21_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 21 rounds. |
|L15_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 15 rounds. |
|L11_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 11 rounds. |
|L9_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 9 rounds. |
|L7_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 7 rounds. |
|L5_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 5 rounds. |
|L3_moving_med_sg_t2g| float64 | Median strokes gained tee to green from last 3 rounds. |
|career_moving_avg_sg_total| float64 | Average strokes gained total for entire timeframe of dataset.|
|career_moving_med_sg_total| float64 | Median strokes gained total for entire timeframe of dataset.|
|L44_moving_avg_sg_total| float64 | Average strokes gained total from the last 44 rounds. |
|L44_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 44 rounds. |
|L36_moving_avg_sg_total| float64 | Average strokes gained total from the last 36 rounds. |
|L36_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 36 rounds. |
|L28_moving_avg_sg_total| float64 | Average strokes gained total from the last 28 rounds. |
|L28_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 28 rounds. |
|L24_moving_avg_sg_total| float64 | Average strokes gained total from the last 24 rounds. |
|L24_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 24 rounds. |
|L20_moving_avg_sg_total| float64 | Average strokes gained total from the last 20 rounds. |
|L20_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 20 rounds. |
|L16_moving_avg_sg_total| float64 | Average strokes gained total from the last 16 rounds. |
|L16_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 16 rounds. |
|L12_moving_avg_sg_total| float64 | Average strokes gained total from the last 12 rounds. |
|L12_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 12 rounds. |
|L8_moving_avg_sg_total| float64 | Average strokes gained total from the last 8 rounds. |
|L8_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 8 rounds. |
|L4_moving_avg_sg_total| float64 | Average strokes gained total from the last 4 rounds. |
|L4_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 4 rounds. |
|L3_moving_avg_sg_total| float64 | Average strokes gained total from the last 3 rounds. |
|L3_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 3 rounds. |
|L2_moving_avg_sg_total| float64 | Average strokes gained total from the last 2 rounds. |
|L2_sg_total_std_dev| float64 | Standard deviation of strokes gained total from the last 2 rounds. |
|L45_moving_med_sg_total| float64 | Median strokes gained total from last 45 rounds. |
|L37_moving_med_sg_total| float64 | Median strokes gained total from last 37 rounds. |
|L29_moving_med_sg_total| float64 | Median strokes gained total from last 29 rounds. |
|L21_moving_med_sg_total| float64 | Median strokes gained total from last 21 rounds. |
|L15_moving_med_sg_total| float64 | Median strokes gained total from last 15 rounds. |
|L11_moving_med_sg_total| float64 | Median strokes gained total from last 11 rounds. |
|L9_moving_med_sg_total| float64 | Median strokes gained total from last 9 rounds. |
|L7_moving_med_sg_total| float64 | Median strokes gained total from last 7 rounds. |
|L5_moving_med_sg_total| float64 | Median strokes gained total from last 5 rounds. |
|L3_moving_med_sg_total| float64 | Median strokes gained total from last 3 rounds. |
|career_moving_avg_driving_dist| float64 | Average driving distance for entire timeframe of dataset.|
|career_moving_med_driving_dist| float64 | Median driving distance for entire timeframe of dataset.|
|L44_moving_avg_driving_dist| float64 | Average driving distance from the last 44 rounds. |
|L44_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 44 rounds. |
|L36_moving_avg_driving_dist| float64 | Average driving distance from the last 36 rounds. |
|L36_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 36 rounds. |
|L28_moving_avg_driving_dist| float64 | Average driving distance from the last 28 rounds. |
|L28_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 28 rounds. |
|L24_moving_avg_driving_dist| float64 | Average driving distance from the last 24 rounds. |
|L24_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 24 rounds. |
|L20_moving_avg_driving_dist| float64 | Average driving distance from the last 20 rounds. |
|L20_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 20 rounds. |
|L16_moving_avg_driving_dist| float64 | Average driving distance from the last 16 rounds. |
|L16_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 16 rounds. |
|L12_moving_avg_driving_dist| float64 | Average driving distance from the last 12 rounds. |
|L12_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 12 rounds. |
|L8_moving_avg_driving_dist| float64 | Average driving distance from the last 8 rounds. |
|L8_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 8 rounds. |
|L4_moving_avg_driving_dist| float64 | Average driving distance from the last 4 rounds. |
|L4_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 4 rounds. |
|L3_moving_avg_driving_dist| float64 | Average driving distance from the last 3 rounds. |
|L3_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 3 rounds. |
|L2_moving_avg_driving_dist| float64 | Average driving distance from the last 2 rounds. |
|L2_driving_dist_std_dev| float64 | Standard deviation of driving distance from the last 2 rounds. |
|L45_moving_med_driving_dist| float64 | Median driving distance from last 45 rounds. |
|L37_moving_med_driving_dist| float64 | Median driving distance from last 37 rounds. |
|L29_moving_med_driving_dist| float64 | Median driving distance from last 29 rounds. |
|L21_moving_med_driving_dist| float64 | Median driving distance from last 21 rounds. |
|L15_moving_med_driving_dist| float64 | Median driving distance from last 15 rounds. |
|L11_moving_med_driving_dist| float64 | Median driving distance from last 11 rounds. |
|L9_moving_med_driving_dist| float64 | Median driving distance from last 9 rounds. |
|L7_moving_med_driving_dist| float64 | Median driving distance from last 7 rounds. |
|L5_moving_med_driving_dist| float64 | Median driving distance from last 5 rounds. |
|L3_moving_med_driving_dist| float64 | Median driving distance from last 3 rounds. |
|career_moving_avg_driving_acc| float64 | Average driving accuracy for entire timeframe of dataset.|
|career_moving_med_driving_acc| float64 | Median driving accuracy for entire timeframe of dataset.|
|L44_moving_avg_driving_acc| float64 | Average driving accuracy from the last 44 rounds. |
|L44_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 44 rounds. |
|L36_moving_avg_driving_acc| float64 | Average driving accuracy from the last 36 rounds. |
|L36_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 36 rounds. |
|L28_moving_avg_driving_acc| float64 | Average driving accuracy from the last 28 rounds. |
|L28_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 28 rounds. |
|L24_moving_avg_driving_acc| float64 | Average driving accuracy from the last 24 rounds. |
|L24_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 24 rounds. |
|L20_moving_avg_driving_acc| float64 | Average driving accuracy from the last 20 rounds. |
|L20_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 20 rounds. |
|L16_moving_avg_driving_acc| float64 | Average driving accuracy from the last 16 rounds. |
|L16_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 16 rounds. |
|L12_moving_avg_driving_acc| float64 | Average driving accuracy from the last 12 rounds. |
|L12_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 12 rounds. |
|L8_moving_avg_driving_acc| float64 | Average driving accuracy from the last 8 rounds. |
|L8_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 8 rounds. |
|L4_moving_avg_driving_acc| float64 | Average driving accuracy from the last 4 rounds. |
|L4_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 4 rounds. |
|L3_moving_avg_driving_acc| float64 | Average driving accuracy from the last 3 rounds. |
|L3_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 3 rounds. |
|L2_moving_avg_driving_acc| float64 | Average driving accuracy from the last 2 rounds. |
|L2_driving_acc_std_dev| float64 | Standard deviation of driving accuracy from the last 2 rounds. |
|L45_moving_med_driving_acc| float64 | Median driving accuracy from last 45 rounds. |
|L37_moving_med_driving_acc| float64 | Median driving accuracy from last 37 rounds. |
|L29_moving_med_driving_acc| float64 | Median driving accuracy from last 29 rounds. |
|L21_moving_med_driving_acc| float64 | Median driving accuracy from last 21 rounds. |
|L15_moving_med_driving_acc| float64 | Median driving accuracy from last 15 rounds. |
|L11_moving_med_driving_acc| float64 | Median driving accuracy from last 11 rounds. |
|L9_moving_med_driving_acc| float64 | Median driving accuracy from last 9 rounds. |
|L7_moving_med_driving_acc| float64 | Median driving accuracy from last 7 rounds. |
|L5_moving_med_driving_acc| float64 | Median driving accuracy from last 5 rounds. |
|L3_moving_med_driving_acc| float64 | Median driving accuracy from last 3 rounds. |
|career_moving_avg_gir| float64 | Average GIR for entire timeframe of dataset.|
|career_moving_med_gir| float64 | Median GIR for entire timeframe of dataset.|
|L44_moving_avg_gir| float64 | Average GIR from the last 44 rounds. |
|L44_gir_std_dev| float64 | Standard deviation of GIR from the last 44 rounds. |
|L36_moving_avg_gir| float64 | Average GIR from the last 36 rounds. |
|L36_gir_std_dev| float64 | Standard deviation of GIR from the last 36 rounds. |
|L28_moving_avg_gir| float64 | Average GIR from the last 28 rounds. |
|L28_gir_std_dev| float64 | Standard deviation of GIR from the last 28 rounds. |
|L24_moving_avg_gir| float64 | Average GIR from the last 24 rounds. |
|L24_gir_std_dev| float64 | Standard deviation of GIR from the last 24 rounds. |
|L20_moving_avg_gir| float64 | Average GIR from the last 20 rounds. |
|L20_gir_std_dev| float64 | Standard deviation of GIR from the last 20 rounds. |
|L16_moving_avg_gir| float64 | Average GIR from the last 16 rounds. |
|L16_gir_std_dev| float64 | Standard deviation of GIR from the last 16 rounds. |
|L12_moving_avg_gir| float64 | Average GIR from the last 12 rounds. |
|L12_gir_std_dev| float64 | Standard deviation of GIR from the last 12 rounds. |
|L8_moving_avg_gir| float64 | Average GIR from the last 8 rounds. |
|L8_gir_std_dev| float64 | Standard deviation of GIR from the last 8 rounds. |
|L4_moving_avg_gir| float64 | Average GIR from the last 4 rounds. |
|L4_gir_std_dev| float64 | Standard deviation of GIR from the last 4 rounds. |
|L3_moving_avg_gir| float64 | Average GIR from the last 3 rounds. |
|L3_gir_std_dev| float64 | Standard deviation of GIR from the last 3 rounds. |
|L2_moving_avg_gir| float64 | Average GIR from the last 2 rounds. |
|L2_gir_std_dev| float64 | Standard deviation of GIR from the last 2 rounds. |
|L45_moving_med_gir| float64 | Median GIR from last 45 rounds. |
|L37_moving_med_gir| float64 | Median GIR from last 37 rounds. |
|L29_moving_med_gir| float64 | Median GIR from last 29 rounds. |
|L21_moving_med_gir| float64 | Median GIR from last 21 rounds. |
|L15_moving_med_gir| float64 | Median GIR from last 15 rounds. |
|L11_moving_med_gir| float64 | Median GIR from last 11 rounds. |
|L9_moving_med_gir| float64 | Median GIR from last 9 rounds. |
|L7_moving_med_gir| float64 | Median GIR from last 7 rounds. |
|L5_moving_med_gir| float64 | Median GIR from last 5 rounds. |
|L3_moving_med_gir| float64 | Median GIR from last 3 rounds. |
|career_moving_avg_scrambling| float64 | Average scrambling for entire timeframe of dataset.|
|career_moving_med_scrambling| float64 | Median scrambling for entire timeframe of dataset.|
|L44_moving_avg_scrambling| float64 | Average scrambling from the last 44 rounds. |
|L44_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 44 rounds. |
|L36_moving_avg_scrambling| float64 | Average scrambling from the last 36 rounds. |
|L36_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 36 rounds. |
|L28_moving_avg_scrambling| float64 | Average scrambling from the last 28 rounds. |
|L28_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 28 rounds. |
|L24_moving_avg_scrambling| float64 | Average scrambling from the last 24 rounds. |
|L24_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 24 rounds. |
|L20_moving_avg_scrambling| float64 | Average scrambling from the last 20 rounds. |
|L20_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 20 rounds. |
|L16_moving_avg_scrambling| float64 | Average scrambling from the last 16 rounds. |
|L16_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 16 rounds. |
|L12_moving_avg_scrambling| float64 | Average scrambling from the last 12 rounds. |
|L12_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 12 rounds. |
|L8_moving_avg_scrambling| float64 | Average scrambling from the last 8 rounds. |
|L8_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 8 rounds. |
|L4_moving_avg_scrambling| float64 | Average scrambling from the last 4 rounds. |
|L4_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 4 rounds. |
|L3_moving_avg_scrambling| float64 | Average scrambling from the last 3 rounds. |
|L3_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 3 rounds. |
|L2_moving_avg_scrambling| float64 | Average scrambling from the last 2 rounds. |
|L2_scrambling_std_dev| float64 | Standard deviation of scrambling from the last 2 rounds. |
|L45_moving_med_scrambling| float64 | Median scrambling from last 45 rounds. |
|L37_moving_med_scrambling| float64 | Median scrambling from last 37 rounds. |
|L29_moving_med_scrambling| float64 | Median scrambling from last 29 rounds. |
|L21_moving_med_scrambling| float64 | Median scrambling from last 21 rounds. |
|L15_moving_med_scrambling| float64 | Median scrambling from last 15 rounds. |
|L11_moving_med_scrambling| float64 | Median scrambling from last 11 rounds. |
|L9_moving_med_scrambling| float64 | Median scrambling from last 9 rounds. |
|L7_moving_med_scrambling| float64 | Median scrambling from last 7 rounds. |
|L5_moving_med_scrambling| float64 | Median scrambling from last 5 rounds. |
|L3_moving_med_scrambling| float64 | Median scrambling from last 3 rounds. |
|career_moving_avg_round_score| float64 | Average round score for entire timeframe of dataset.|
|career_moving_med_round_score| float64 | Median round score for entire timeframe of dataset.|
|L44_moving_avg_round_score| float64 | Average round score from the last 44 rounds. |
|L44_round_score_std_dev| float64 | Standard deviation of round score from the last 44 rounds. |
|L44_moving_min_round_score| float64 | Minimum round score from the last 44 rounds. |
|L44_moving_max_round_score| float64 | Maximum round score from the last 44 rounds. |
|L36_moving_avg_round_score| float64 | Average round score from the last 36 rounds. |
|L36_round_score_std_dev| float64 | Standard deviation of round score from the last 36 rounds. |
|L36_moving_min_round_score| float64 | Minimum round score from the last 36 rounds. |
|L36_moving_max_round_score| float64 | Maximum round score from the last 36 rounds. |
|L28_moving_avg_round_score| float64 | Average round score from the last 28 rounds. |
|L28_round_score_std_dev| float64 | Standard deviation of round score from the last 28 rounds. |
|L28_moving_min_round_score| float64 | Minimum round score from the last 28 rounds. |
|L28_moving_max_round_score| float64 | Maximum round score from the last 28 rounds. |
|L24_moving_avg_round_score| float64 | Average round score from the last 24 rounds. |
|L24_round_score_std_dev| float64 | Standard deviation of round score from the last 24 rounds. |
|L24_moving_min_round_score| float64 | Minimum round score from the last 24 rounds. |
|L24_moving_max_round_score| float64 | Maximum round score from the last 24 rounds. |
|L20_moving_avg_round_score| float64 | Average round score from the last 20 rounds. |
|L20_round_score_std_dev| float64 | Standard deviation of round score from the last 20 rounds. |
|L20_moving_min_round_score| float64 | Minimum round score from the last 20 rounds. |
|L20_moving_max_round_score| float64 | Maximum round score from the last 20 rounds. |
|L16_moving_avg_round_score| float64 | Average round score from the last 16 rounds. |
|L16_round_score_std_dev| float64 | Standard deviation of round score from the last 16 rounds. |
|L16_moving_min_round_score| float64 | Minimum round score from the last 16 rounds. |
|L16_moving_max_round_score| float64 | Maximum round score from the last 16 rounds. |
|L12_moving_avg_round_score| float64 | Average round score from the last 12 rounds. |
|L12_round_score_std_dev| float64 | Standard deviation of round score from the last 12 rounds. |
|L12_moving_min_round_score| float64 | Minimum round score from the last 12 rounds. |
|L12_moving_max_round_score| float64 | Maximum round score from the last 12 rounds. |
|L8_moving_avg_round_score| float64 | Average round score from the last 8 rounds. |
|L8_round_score_std_dev| float64 | Standard deviation of round score from the last 8 rounds. |
|L8_moving_min_round_score| float64 | Minimum round score from the last 8 rounds. |
|L8_moving_max_round_score| float64 | Maximum round score from the last 8 rounds. |
|L4_moving_avg_round_score| float64 | Average round score from the last 4 rounds. |
|L4_round_score_std_dev| float64 | Standard deviation of round score from the last 4 rounds. |
|L4_moving_min_round_score| float64 | Minimum round score from the last 4 rounds. |
|L4_moving_max_round_score| float64 | Maximum round score from the last 4 rounds. |
|L3_moving_avg_round_score| float64 | Average round score from the last 3 rounds. |
|L3_round_score_std_dev| float64 | Standard deviation of round score from the last 3 rounds. |
|L3_moving_min_round_score| float64 | Minimum round score from the last 3 rounds. |
|L3_moving_max_round_score| float64 | Maximum round score from the last 3 rounds. |
|L2_moving_avg_round_score| float64 | Average round score from the last 2 rounds. |
|L2_round_score_std_dev| float64 | Standard deviation of round score from the last 2 rounds. |
|L2_moving_min_round_score| float64 | Minimum round score from the last 2 rounds. |
|L2_moving_max_round_score| float64 | Maximum round score from the last 2 rounds. |
|L45_moving_med_round_score| float64 | Median round score from last 45 rounds. |
|L37_moving_med_round_score| float64 | Median round score from last 37 rounds. |
|L29_moving_med_round_score| float64 | Median round score from last 29 rounds. |
|L21_moving_med_round_score| float64 | Median round score from last 21 rounds. |
|L15_moving_med_round_score| float64 | Median round score from last 15 rounds. |
|L11_moving_med_round_score| float64 | Median round score from last 11 rounds. |
|L9_moving_med_round_score| float64 | Median round score from last 9 rounds. |
|L7_moving_med_round_score| float64 | Median round score from last 7 rounds. |
|L5_moving_med_round_score| float64 | Median round score from last 5 rounds. |
|L3_moving_med_round_score| float64 | Median round score from last 3 rounds. |
|career_min_round_score| float64 | Average round score for entire timeframe of dataset.|
|career_max_round_score| float64 | Median round score for entire timeframe of dataset.|
|Days_Since| int64 | Number of days between now and when the round was completed. |
|Last_365_Days| int64 | Binary column if round was played in the last 365 days or not. |
|Last_180_Days| int64 | Binary column if round was played in the last 180 days or not. |
|Last_90_Days| int64 | Binary column if round was played in the last 90 days or not. |
|Last_60_Days| int64 | Binary column if round was played in the last 60 days or not. |
|Last_30_Days| int64 | Binary column if round was played in the last 30 days or not. |
|Last_10_Days| int64 | Binary column if round was played in the last 10 days or not. |
|Last_5_Days| int64 | Binary column if round was played in the last 5 days or not. |
|lagged_year| float64 | Previous round year. |
|lagged_season| float64 | Previous round season. |
|lagged_event_id| float64 | Previous round event id. |
|lagged_round_num| float64 | Previous round number. |
|lagged_course_num| float64 | Previous round course number. |
|lagged_course_par| float64 | Previous round course par. |
|lagged_start_hole| float64 | Previous round start hole. |
|lagged_round_score| float64 | Previous round score. |
|lagged_sg_putt| float64 | Previous round strokes gained putting. |
|lagged_sg_arg| float64 | Previous round strokes gained around the green. |
|lagged_sg_app| float64 | Previous round strokes gained approaching the green. |
|lagged_sg_ott| float64 | Previous round strokes gained off the tee. |
|lagged_sg_t2g| float64 | Previous round strokes gained tee to green. |
|lagged_sg_total| float64 | Previous round strokes gained total. |
|lagged_driving_dist| float64 | Previous round average driving distance. |
|lagged_driving_acc| float64 | Previous round driving accuracy. |
|lagged_gir| float64 | Previous round greens in regulation. |
|lagged_scrambling| float64 | Previous round scrambling. |
|lagged_prox_rgh| float64 | Previous round average proximity of all shots hit from locations other than the fairway. |
|lagged_prox_fw| float64 | Previous round average proximity of all shots hit from the fairway. |
|lagged_great_shots| float64 | Previous round sum of great shots. |
|lagged_poor_shots| float64 | Previous round sum of poor shots. |
|lagged_month| float64 | Previous round month. |
|lagged_day| float64 | Previous round day of month. |
|lagged_fin_num| float64 | Previous round finishing position. |
|lagged_teetime_numeric| float64 | Previous round tee time. |
|lagged_ohe_win| float64 | Previous round binary value if the player won or not. |
|lagged_ohe_top_five| float64 | Previous round binary value if the player finished in the top 5 or not. |
|lagged_ohe_top_ten| float64 | Previous round binary value if the player finished in the top 10 or not. |
|lagged_ohe_top_twenty| float64 | Previous round binary value if the player finished in the top 20 or not. |
|lagged_ohe_make_cut| float64 | Previous round binary value if the player made the cut after 2 rounds or not. |