import os

from infrared import api
from infrared.core.plugins import InfraredPlugin


def main():
    specs_manager = api.SpecManager()
    plugin = InfraredPlugin.from_config_file(os.getcwd(), 'infrared.cfg')
    specs_manager.register_spec(api.DefaultInfraredPluginSpec(plugin))
    specs_manager.run_specs()

if __name__ == '__main__':
    main()
