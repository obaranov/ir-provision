import os

from infrared import api
from infrared.core.services.plugins import InfraredPlugin
from infrared.main import ProfileManagerSpec

def main():
    specs_manager = api.SpecManager()
    plugin = InfraredPlugin.from_config_file(os.getcwd(), 'infrared.cfg')
    specs_manager.register_spec(api.DefaultInfraredPluginSpec(plugin))
    specs_manager.register_spec(ProfileManagerSpec(
        'profile', description="Profile manager. " \
        "Allows to create and use an isolated environement " \
        "for plugins execution."))
    specs_manager.run_specs()

if __name__ == '__main__':
    main()
