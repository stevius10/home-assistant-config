# Global
EXPR_TIME_DAY = "range(00:00, 24:00)"
EXPR_TIME_DAYTIME = "cron(* 8-22 * * *)"
EXPR_TIME_GENERAL_WORKTIME =  "cron(* 8-20 * * 1-6)"

# Automation

# Auto Motion
EXPR_TIME_RANGE_DAY_MOTION = EXPR_TIME_DAY

# Auto Notify
EXPR_TIME_UPDATE_SENSORS_HOUSING = "cron(30 8-18 * * 1-5)"

# Specific 

# Air Cleaner
EXPR_STATE_AIR_THRESHOLD_SEASON = "sensor.season in ['spring', 'summer']"
EXPR_STATE_AIR_THRESHOLD_TIME = EXPR_TIME_DAYTIME

# Misc
EXPR_STATE_OPEN_WINDOW = "sensor.open_window == 'true'"