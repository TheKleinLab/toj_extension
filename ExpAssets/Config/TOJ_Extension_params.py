## KLibs Parameter overrides ##

#########################################
# Runtime Settings
#########################################
collect_demographics = True
manual_demographics_collection = False
manual_trial_generation = False
run_practice_blocks = True
multi_user = False
view_distance = 57 # in centimeters, 57cm = 1 deg of visual angle per cm of screen

#########################################
# Available Hardware
#########################################
eye_tracker_available = False
eye_tracking = False
labjack_available = False
labjacking = False

#########################################
# Environment Aesthetic Defaults
#########################################
default_fill_color = (45, 45, 45, 45)
default_color = (255, 255, 255, 255)
default_font_size = 28
default_font_name = 'Frutiger'

#########################################
# EyeLink Settings
#########################################
manual_eyelink_setup = False
manual_eyelink_recording = False

saccadic_velocity_threshold = 20
saccadic_acceleration_threshold = 5000
saccadic_motion_threshold = 0.15

#########################################
# Experiment Structure
#########################################
multi_session_project = False
trials_per_block = 240
blocks_per_experiment = 2
table_defaults = {}

#########################################
# Development Mode Settings
#########################################
dm_auto_threshold = True
dm_trial_show_mouse = True
dm_ignore_local_overrides = False
dm_show_gaze_dot = True

#########################################
# Data Export Settings
#########################################
primary_table = "trials"
unique_identifier = "userhash"
default_participant_fields = [[unique_identifier, "participant"], "sex", "age", "handedness"]
default_participant_fields_sf = [[unique_identifier, "participant"], "random_seed", "sex", "age", "handedness"]

#########################################
# EXPERIMENT-SPECIFIC PARAMS
#########################################
initial_probe_pos_bias_loc = "LEFT"  # "RIGHT"
toj_judgement = "first"  # "second"
# should match the distribution in trial_type.param of TOJ_Extension_config.csv. they must be floats for accuracy
target_probe_trial_dist = {"PROBE":1.0, "TARGET":2.0}

