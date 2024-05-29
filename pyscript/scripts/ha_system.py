from config import *
from utils import *

from events import EVENT_SYSTEM_STARTED

from homeassistant.const import EVENT_HOMEASSISTANT_STARTED

import shutil
import os

# Event

@time_trigger
@event_trigger(EVENT_HOMEASSISTANT_STARTED)
def event_system_started(delay=SYSTEM_CONFIG_EVENT_STARTED_DELAY): 
  task.sleep(delay)
  event.fire(EVENT_SYSTEM_STARTED)

# Setup

@event_trigger(EVENT_SYSTEM_STARTED)
def ha_setup():
  if PATH_DIR_PY_NATIVE not in sys.path:
    sys.path.append(PATH_DIR_PY_NATIVE)
    
  ha_setup_environment()
  ha_setup_files()
  ha_setup_links()
  ha_setup_logging()

# Tasks
  
@pyscript_executor
def ha_setup_environment(variables=SYSTEM_ENVIRONMENT):
  for variable in variables:
    os.environ[variable] = variables[variable]
  
@pyscript_executor
def ha_setup_files(files=SYSTEM_FILES):
  for file in files:
    shutil.copy2(file, files[file])

@pyscript_executor
def ha_setup_links(links=SYSTEM_LINKS):
  for source, target in links.items():
    tmp_target = f"{target}.tmp"
    # shortcut to overwrite symlink
    os.symlink(source, tmp_target)
    os.rename(tmp_target, target)

# synchronous task for logging scope
def ha_setup_logging():
  logger.set_level(**{LOG_LOGGER_SYS: LOG_LOGGING_LEVEL})