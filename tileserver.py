import logging
import os
import json

import TileStache

cache = {
    "name": "Redis",
    "url": os.getenv('REDISTOGO_URL')
}

config_dict = {
  "cache": cache,
  "layers": {
    "telaviv": {
        "provider": {"name": "mbtiles", "tileset": "Telostats.mbtiles"},
        "projection": "spherical mercator"
    }
  }
}

config = TileStache.Config.buildConfiguration(config_dict, '.')

application = TileStache.WSGITileServer(config=config, autoreload=False)
