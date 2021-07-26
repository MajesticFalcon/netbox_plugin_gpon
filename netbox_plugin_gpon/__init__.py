from extras.plugins import PluginConfig

class GPONConfig(PluginConfig):
    name = 'netbox_plugin_gpon'
    verbose_name = 'Netbox GPON'
    description = 'Netbox plugin for GPON modeling'
    version = '0.1.0'
    author = 'Schylar Utley'
    author_email = 'schylarutley@hotmail.com'
    base_url = 'gpon'
    required_settings = []
    default_settings = {
        'loud': False
    }

config = GPONConfig
