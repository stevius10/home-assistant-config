from secrets import SYSTEM_FILES

# Log
LOG_HA_SIZE = 28
LOG_HA_TAIL = 7
LOG_HA_TRUNCATE_BLOCK_DELAY = 15
LOG_HA_TRUNCATE_IO_RETRY = 3
LOG_HA_ARCHIVE_SIZE = 20 * LOG_HA_SIZE
LOG_LOGGER_SYS = "py"
LOG_LOGGING_LEVEL = "info"

LOG_DEBUG = False
LOG_DEBUG_DEVICES = []
LOG_ENABLED = False

# Path
PATH_LOG_HA_FILE = "home-assistant.log"
PATH_LOG_HA = f"/config/{PATH_LOG_HA_FILE}"
PATH_LOG_TAIL_SUFFIX = "1"
PATH_LOGS = "/config/pyscript/logs/"
PATH_PYLOG_HA = f"{PATH_LOGS}{PATH_LOG_HA_FILE}"

# Pyscript
PYSCRIPT_DIR_NATIVE = "/config/pyscript/python"

# System
SYSTEM_FILES.update({
   "/config/files/.zshrc": "/root"
})

SYSTEM_LINKS = { 
  PATH_LOG_HA: PATH_PYLOG_HA, 
  f"{PATH_LOG_HA}.{PATH_LOG_TAIL_SUFFIX}": f"{PATH_PYLOG_HA}.{PATH_LOG_TAIL_SUFFIX}"
}

SYSTEM_STARTED_EVENT_DELAY = 30

# Automation
AUTO_MOTION_TIMEOUT = 70
AUTO_OFF_AWAY_TRANSITION = 20

# Services
SERVICE_AUTO_CRON_FILEBACKUP = "cron(0 1 * * *)"
SERVICE_GIT_CRON = "cron(15 1 * * *)"
SERVICE_GOOGLE_DRIVE_CRON = "cron(30 1 * * *)"


SERVICES_AUTO = {
  'shell_command.filebackup': SERVICE_AUTO_CRON_FILEBACKUP
}

# Events
EVENT_FOLDER_WATCHER = "folder_watcher"
EVENT_NEVER = "event_never"
EVENT_SYSTEM_PYSCRIPT_RELOADED = "event_system_pyscript_reloaded"
EVENT_SYSTEM_STARTED = "event_system_started"
EVENT_SYSTEM_STARTED_DELAY = 10 