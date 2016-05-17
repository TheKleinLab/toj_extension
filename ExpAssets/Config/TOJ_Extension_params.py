# TOJ_Extension Param overrides
#
# Any param that is commented out by default is either deprecated or else not yet implemented--don't uncomment or use

#########################################
# Available Hardware
#########################################
eye_tracker_available = False
eye_tracking = False
labjack_available = True
labjacking = False

#########################################
# Environment Aesthetic Defaults
#########################################
default_fill_color = (45, 45, 45, 45)
default_color = (255, 255, 255, 255)
default_response_color = default_color
default_input_color = default_color
default_font_size = 28
default_font_name = 'Frutiger'
default_timeout_message = "Too slow!"

#########################################
# EyeLink Sensitivities
#########################################
saccadic_velocity_threshold = 20
saccadic_acceleration_threshold = 5000
saccadic_motion_threshold = 0.15

fixation_size = 1 # deg of visual angle
box_size = 1 # deg of visual angle
cue_size = 1 # deg of visual angle
cue_back_size = 1 # deg of visual angle

#########################################
# Experiment Structure
#########################################
collect_demographics = True
trials_per_block = 240
trials_per_practice_block = 0
blocks_per_experiment = 2
trials_per_participant = 0
pre_render_block_messages = False
show_practice_messages = True

#########################################
# Development Mode Settings
#########################################
dm_suppress_debug_pane = False
dm_auto_threshold = True
dm_print_log = False
dm_print_events = False

#########################################
# EXPERIMENT-SPECIFIC PARAMS
#########################################
initial_probe_pos_bias_loc = "LEFT"  # "RIGHT"
toj_judgement = "first"  # "second"
# should match the distribution in trial_type.param of TOJ_Extension_config.csv. they must be floats for accuracy
target_probe_trial_dist = {"PROBE":1.0, "TARGET":2.0}

