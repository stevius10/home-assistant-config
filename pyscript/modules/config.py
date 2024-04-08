import secrets

import datetime

# System
SYSTEM_FILES = secrets.SYSTEM_FILES.update({
  "/config/files/.zshrc": "/root"
})

# Path
PATH_LOG_HA = "/config/home-assistant.log"
PATH_LOGS = "/config/pyscript/logs/"

# Log
LOG_HA_SIZE = 20
LOG_HA_TAIL = 5
LOG_HA_TRUNCATE_BLOCK_DELAY = 5
LOG_HA_TRUNCATE_IO_RETRY = 3
LOG_HA_ARCHIVE_SIZE = 10 * LOG_HA_SIZE
LOG_ARCHIVE_SUFFIX = "1"
LOG_SYS_LOGGER = "py.log"

LOG_DEBUG = True
LOG_DEBUG_DEVICES = []

# Time
EXPR_TIME_ACTIVE =  "cron(* 9-19 * * 1-6)"
EXPR_TIME_RANGE_DAY = "range(00:00, 24:00)"
EXPR_TIME_SEASON_POLLEN = "sensor.season in ['spring', 'summer']"
EXPR_TIME_UPDATE_SENSORS = "cron(30 16 * * 1-5)"

# Automation
AUTO_MOTION_TIMEOUT = 60
AUTO_OFF_AWAY_TRANSITION = 90

AUTO_TIMER_DURATION_LUFTREINIGER = 5400
AUTO_TIMER_DURATION_SZ_VENTILATOR = 5400
AUTO_TIMER_DURATION_SCHLAFZIMMER = 5400

# Scripts
SCRIPT_AIR_CLEANER_THRESHOLD_START = 15
SCRIPT_AIR_CLEANER_THRESHOLD_STOP = 5
SCRIPT_AIR_CLEANER_PERCENTAGE_CLEAN = 100
SCRIPT_AIR_CLEANER_TIMEOUT_CLEAN = 600

# Services
SERVICE_GOOGLE_DRIVE_CRON = "cron(30 1 * * *)"
SERVICE_GIT_CRON = "cron(15 1 * * *)"

# Events
EVENT_FOLDER_WATCHER = "folder_watcher"
EVENT_SYSTEM_PYSCRIPT_RELOADED = "event_system_pyscript_reloaded"

# States
STATE_HA_NONE = "None"
STATE_HA_UNAVAILABLE = "unavailable"
STATE_HA_UNKNOWN = "unknown"
STATES_HA_UNDEFINED = [STATE_HA_NONE, STATE_HA_UNAVAILABLE, STATE_HA_UNKNOWN]
STATE_HA_TIMER_STOPPED = "idle"

# Secrets

SERVICE_GOOGLE_DRIVE_LOCAL_FOLDER = secrets.SERVICE_GOOGLE_DRIVE_LOCAL_FOLDER
SERVICE_GOOGLE_DRIVE_REMOTE_FOLDER = secrets.SERVICE_GOOGLE_DRIVE_REMOTE_FOLDER
SERVICE_GOOGLE_DRIVE_TRASH_FOLDER = secrets.SERVICE_GOOGLE_DRIVE_TRASH_FOLDER
SERVICE_GOOGLE_DRIVE_IGNORE_FOLDERS = secrets.SERVICE_GOOGLE_DRIVE_IGNORE_FOLDERS
SERVICE_GOOGLE_DRIVE_CREDENTIALS_FILE = secrets.SERVICE_GOOGLE_DRIVE_CREDENTIALS_FILE

SERVICE_GIT_GITHUB_PR_BODY = secrets.SERVICE_GIT_GITHUB_PR_BODY
SERVICE_GIT_GITHUB_PR_TITLE = secrets.SERVICE_GIT_GITHUB_PR_TITLE
SERVICE_GIT_GITHUB_TOKEN = secrets.SERVICE_GIT_GITHUB_TOKEN
SERVICE_GIT_GITHUB_USER = secrets.SERVICE_GIT_GITHUB_USER
SERVICE_GIT_REPO_BASE = secrets.SERVICE_GIT_REPO_BASE
SERVICE_GIT_REPO_BRANCH = secrets.SERVICE_GIT_REPO_BRANCH
SERVICE_GIT_REPO_MESSAGE = secrets.SERVICE_GIT_REPO_MESSAGE
SERVICE_GIT_REPO_NAME = secrets.SERVICE_GIT_REPO_NAME
SERVICE_GIT_REPO_TARGET = secrets.SERVICE_GIT_REPO_TARGET
SERVICE_GIT_REPO_URL = secrets.SERVICE_GIT_REPO_URL
SERVICE_GIT_SETTINGS_CONFIG = secrets.SERVICE_GIT_SETTINGS_CONFIG
SERVICE_GIT_SETTINGS_CREDENTIALS = secrets.SERVICE_GIT_SETTINGS_CREDENTIALS