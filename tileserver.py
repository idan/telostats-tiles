import os
import TileStache

cache = {
    'name': 'Redis',
    'url': os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
}

config_dict = {
  'cache': cache,
  'layers': {
    'telaviv': {
        'provider': {'name': 'mbtiles', 'tileset': 'Telostats.mbtiles'},
        'projection': 'spherical mercator',
        'maximum cache age': 604800,
    }
  }
}

config = TileStache.Config.buildConfiguration(config_dict, '.')

application = TileStache.WSGITileServer(config=config, autoreload=False)
