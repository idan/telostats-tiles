import logging
import os
import json

import TileStache

if 'AWS_ACCESS_KEY_ID' in os.environ and \
   'AWS_SECRET_ACCESS_KEY' in os.environ:
        cache = {
            "name": "S3",
            "bucket": "telostats-tiles",
            "access": os.environ['AWS_ACCESS_KEY_ID'],
            "secret": os.environ['AWS_SECRET_ACCESS_KEY']
        }
else:
    cache = {"name": "Test"}


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
