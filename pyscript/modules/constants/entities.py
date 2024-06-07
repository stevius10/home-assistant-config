# Automation

AUTO_ENTITIES = {
  "climate.k": { "default": "off", "func": "climate.turn_off" },
  "media_player.schlafzimmer": { "default": "off", "delay": 7200 },
  "switch.adguard_home_schutz": { "default": "on", "delay": 1800 }, 
  "switch.bett": { "default": "off", "delay": 1800 },
  "switch.heizdecke": { "default": "off", "delay": 1800 }, 
  "switch.sofa": { "default": "off", "delay": 1800 }, 
  "fan.wz_ventilator": { "default": "off", "delay": 5400 }, 
  "fan.sz_ventilator": { "default": "off", "delay": 5400 }, 
  "fan.wz_luft": { "default": "off", "delay": 14400 }, 
  "fan.sz_luft": { "default": "off", "delay": 14400 }, 
  "switch.wz_luftung": { "default": "off", "delay": 600 },
  "switch.sz_luftung": { "default": "off", "delay": 600 }
}

AUTO_MOTION_ENTITIES = { 
  "binary_sensor.g_sensor_occupancy": { "on": "scene.g_tisch", "off": "scene.g_aus" },
  "binary_sensor.k_sensor_occupancy": { "on": "scene.k_normal", "off": "scene.k_aus", "transition": 20, "sun_diff": 30 }
}

CONFIG_CONTROL_ENTITIES = {
  'sensor.wz_schalter_action': {
    'on': 'scene.wz_indirekt',
    'off': ['scene.wz_aus', 'scene.k_aus'],
    'up': 'scene.wz_hell',
    'down': 'scene.wz_schwach'
  }, 
  'sensor.sz_schalter_action': {
    'on': 'scene.sz_indirekt',
    'off': 'scene.sz_aus',
    'up': 'scene.sz_hell',
    'down': 'scene.sz_schwach'
  },
  'sensor.g_schalter_action': {
    'single': 'scene.g_indirekt',
    'double': 'scene.g_aus',
    'long': ''
  }
}

# Script

SCRIPT_AIR_CLEANER_ENTITIES = {
  "wz_luft": {
    "fan": "fan.wz_luft",
    "sensor": "sensor.wz_luft",
    "luftung": "switch.wz_luftung",
    "percentage": "fan.wz_luft.percentage"
  },
  "sz_luft": {
    "fan": "fan.sz_luft", 
    "sensor": "sensor.sz_luft",
    "luftung": "switch.sz_luftung",
    "percentage": "fan.sz_luft.percentage"
  }
}

# Sensors

AUTO_NOTIFY_SENSORS_HOUSING = { 
  "sensor.v_friedrichsheim": { "url": "https://www.friedrichsheim-eg.de/category/freie-wohnungen/" }, 
  "sensor.v_bwv": { "url": "https://www.bwv-berlin.de/wohnungsangebote.html" }, 
  "sensor.v_neukolln": { "url": "https://www.gwneukoelln.de/wohnungen/wohnungsangebote/" }, 
  "sensor.v_wbm": { "url": "https://www.wbm.de/wohnungen-berlin/angebote-wbm/" }, 
  "sensor.v_gewobag": { "url": "https://www.wbm.de/wohnungen-berlin/angebote-wbm/" }, 
  "sensor.v_inberlinwohnen": { "url": "https://www.gewobag.de/fuer-mieter-und-mietinteressenten/mietangebote/?bezirke%5B%5D=charlottenburg-wilmersdorf-charlottenburg&bezirke%5B%5D=friedrichshain-kreuzberg&bezirke%5B%5D=friedrichshain-kreuzberg-friedrichshain&bezirke%5B%5D=friedrichshain-kreuzberg-kreuzberg&bezirke%5B%5D=mitte&bezirke%5B%5D=mitte-gesundbrunnen&bezirke%5B%5D=mitte-wedding&bezirke%5B%5D=neukoelln&bezirke%5B%5D=neukoelln-buckow&bezirke%5B%5D=neukoelln-rudow&bezirke%5B%5D=pankow-prenzlauer-berg&bezirke%5B%5D=tempelhof-schoeneberg-schoeneberg&nutzungsarten%5B%5D=wohnung&gesamtmiete_von=&gesamtmiete_bis=700&gesamtflaeche_von=50&gesamtflaeche_bis=&zimmer_von=2&zimmer_bis=&sort-by=recent" }
}

# Cluster

ENTITIES_AIR = [ 
  "humidifier.luftbefeuchter", 
  "fan.wz_ventilator", "fan.sz_ventilator", 
  "fan.wz_luft", "fan.sz_luft",
  "switch.wz_luftung", "switch.sz_luftung"
]
ENTITIES_HEATING = [ "clima.wz_heizung", "clima.sz_heizung", "clima.k_heizung" ]
ENTITIES_MEDIA= [
  "media_player.bad", "media_player.kueche",
  "media_player.schlafzimmer", "media_player.wohnzimmer",
  "media_player.uberall"
]
ENTITIES_LIGHT = [
  "light.wz_beleuchtung", "light.sz_beleuchtung",
  "light.k_beleuchtung", "light.g_beleuchtung"
]
ENTITIES_SERVICES = []
ENTITIES_SWITCHES = [ "switch.bett", "switch.sofa", "switch.heizdecke" ]
ENTITIES_TV = [ "media.wz_fernseher", "media.sz_fernseher" ]
