from constants.config import *
from constants.entities import *
from constants.expressions import *
from constants.mappings import *
from constants.settings import *

from utils import *

entities = AIR_CONTROL_ENTITIES

@state_trigger(expr([entity["sensor"] for entity in entities.values()], SERVICE_AIR_CONTROL_THRESHOLD_START, comparator=">"))
@state_active(f"{EXPR_STATE_AIR_AUTOMATION_SEASON} and {expr([entity['fan'] for entity in entities.values()], STATE_OFF)}" if SERVICE_AIR_CONTROL_ENABLED else "False")
@time_active(EXPR_TIME_AIR_AUTOMATION)
@debugged
def air_control_threshold_on(var_name=None):
  air_control_sleep(entities.get(var_name.split(".")[1]).get("fan"))

@state_trigger(expr([entity["sensor"] for entity in entities.values()], SERVICE_AIR_CONTROL_THRESHOLD_STOP, comparator=">"))
@state_active(f"{EXPR_STATE_AIR_AUTOMATION_SEASON} and {expr([entity['fan'] for entity in entities.values()], STATE_ON)}" if SERVICE_AIR_CONTROL_ENABLED else "False")
@time_active(EXPR_TIME_AIR_AUTOMATION)
@debugged
def air_control_threshold_off(var_name=None):
  air_control_turn_off(entities.get(var_name.split(".")[1]).get("fan"))

@event_trigger(EVENT_NEVER) # required for service
@debugged
@service
def air_control_clean(conditioned=False, entity=[entity["fan"] for entity in entities.values()]):
  for item in entity:
    air_control_turn_on(item)
    fan.set_percentage(entity_id=item, percentage=get_clean_percentage(item.split(".")[1]) if conditioned else 100)
    air_control_helper_air(entity=item, check=True)

@state_trigger(expr([entity["fan"] for entity in entities.values()], STATE_ON)) # reset
@state_trigger(expr([f"'{entity['fan']}.percentage'" for entity in entities.values()],
  SERVICE_AIR_CONTROL_SLEEP_MODE_PERCENTAGE, comparator='>').replace("'", ""), # prevent interpretation \
  state_hold=SERVICE_AIR_CONTROL_TIMEOUT_CLEAN, state_check_now=True)
@debugged
@service
def air_control_sleep(entity=[entity["fan"] for entity in entities.values()], var_name=None, value=None, state_check_now=True):
  if var_name: 
    entity = ".".join(var_name.split(".")[:2]) # handle percentage trigger
  if isinstance(entity, str) and value != STATE_OFF: # prevent off turned to trigger "or" expression
    air_control_turn_on(entity)
    if air_control_feature_supported(entity):
       fan.set_preset_mode(entity_id=entity, preset_mode=SERVICE_AIR_CONTROL_MODE_SLEEP)
    else:
      fan.set_percentage(entity_id=entity, percentage=SERVICE_AIR_CONTROL_SLEEP_MODE_PERCENTAGE)
    air_control_turn_off(entities[entity.split(".")[1]]["luftung"])
  elif isinstance(entity, list):
    for item in entity: 
      air_control_sleep(entity=item, var_name=item)

@debugged
def air_control_turn_on(entity=[entity["fan"] for entity in entities.values()]):
  if isinstance(entity, list):
    for item in entity:
      air_control_turn_on(item)
  else:
    if state.get(entity) != "on": # and not air_control_feature_supported(entity):
      fan.turn_on(entity_id=entity)
      task.sleep(SERVICE_AIR_CONTROL_WAIT_ACTIVE_DELAY)

@debugged
@service
def air_control_turn_off(entity=[entity["fan"] for entity in entities.values()]):
  if isinstance(entity, list):
    for item in entity:
      air_control_turn_off(item)
  else:
    pyscript.turnoff_air(entity=entity)

def get_clean_percentage(name):
  return min(max(SERVICE_AIR_CONTROL_CLEAN_MODE_PERCENTAGE, (int(state.get(entities[name].get("sensor"))) * 10)), 100)

@debugged
@service
def air_control_helper_air(entity=[entity["fan"] for entity in entities.values()], helper=[entity["luftung"] for entity in entities.values()], check=False):
  if (check == False) or (sum([int(state.get(entities[item.split(".")[1]]["sensor"])) for item in entity if state.get(entities[item.split(".")[1]]["sensor"]) is not None]) > SERVICE_AIR_CONTROL_HELPER_PM_MINIMUM):
    homeassistant.turn_on(entity_id=helper)

def air_control_feature_supported(entity):
  feature = str(state.get(f"{entity}.supported_features"))
  if feature in ["9", 9]: 
    return True
  if feature in ["1", 1]: 
    return False