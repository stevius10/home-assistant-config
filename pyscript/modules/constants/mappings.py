from homeassistant.const import STATE_ON, STATE_OFF, STATE_UNAVAILABLE, STATE_UNKNOWN

# Home Assistant

STATES_HA_UNDEFINED = [STATE_UNAVAILABLE, STATE_UNKNOWN]

STATE_HA_TIMER_STOPPED = "idle"

SERVICE_HA_TURN_OFF = "homeassistant.turn_off"

# Events

EVENT_FOLDER_WATCHER = "EVENT_FOLDER_WATCHER"
EVENT_HOUSING_INITIALIZED = "EVENT_HOUSING_INITIALIZED"
EVENT_NEVER = "EVENT_NEVER"
EVENT_SYSTEM_STARTED = "EVENT_SYSTEM_STARTED"

# Notifications

NOTIFICATION_ID_CHANGE_DETECTION = "changedetection"

# Persistence

PERSISTENCE_GENERAL_TIMER_PREFIX = "timer"

PERSISTENCE_SCRAPE_HOUSING_SENSOR_PREFIX = "v_scrape"

# Shortcuts

SHORTCUT_HOUSING_NAME = "SC-HA-Notify-Housing"