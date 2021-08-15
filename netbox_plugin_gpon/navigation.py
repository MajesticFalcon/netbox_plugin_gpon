from extras.plugins import PluginMenuItem



menu_items = (
    PluginMenuItem(
        link="plugins:netbox_plugin_gpon:home",
        link_text="Home",
    ),
    PluginMenuItem(
        link="plugins:netbox_plugin_gpon:olt_list",
        link_text="OLTs",
    ),
    PluginMenuItem(
        link="plugins:netbox_plugin_gpon:ont_list",
        link_text="ONTs",
    ),
    PluginMenuItem(
        link="plugins:netbox_plugin_gpon:gponsplitter_list",
        link_text="Splitters",
    ),
)
