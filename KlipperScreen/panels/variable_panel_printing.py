import logging
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Pango
from ks_includes.screen_panel import ScreenPanel

# Import the global variable buffer from gcodes.py
from panels.gcodes import VARIABLE_BUFFER


class Panel(ScreenPanel):

    def __init__(self, screen, title):
        title = title or _("Options: Printing")
        super().__init__(screen, title)
        self.variables = {}

        # Create a grid for all variables
        self.labels['variables'] = Gtk.Grid(valign=Gtk.Align.CENTER)
        self.load_variables()

        scroll = self._gtk.ScrolledWindow()
        scroll.add(self.labels['variables'])

        self.content.add(scroll)
    
    
    def load_variables(self):
        # List of variables to configure
        variable_list = [
            {"name": "sensor_filamento", "description": "Detectar presencia de filamento"},
            {"name": "sensor_movimiento_filamento", "description": "Detectar atascos de filamento"},
            {"name": "variable_enable_purge_clean", "description": "Purgar y limpiar nozzle en cambios"},
            {"name": "variable_turn_off_when_finish", "description": "Apagar maquina al finalizar"},
            {"name": "variable_enable_dual_toolchange", "description": "Habilitar cambios de herramienta sincronizados"}
        ]
    
        for var in sorted(variable_list, key=lambda x: x['description']):
            self.add_variable(var)
    
    def add_variable(self, var):
        # Create a label and switch for each variable
        name_label = Gtk.Label(
            hexpand=True, vexpand=True, halign=Gtk.Align.START, valign=Gtk.Align.CENTER,
            wrap=True, wrap_mode=Pango.WrapMode.WORD_CHAR
        )
        name_label.set_markup(f'\n<big><b>{var["description"]}</b></big>\n')
    
        switch = Gtk.Switch()
    
        # Set default states for sensors and use the buffer for other variables
        if var['name'] == "sensor_filamento" or var['name'] == "sensor_movimiento_filamento":
            switch.set_active(True)  # Sensors always active by default
        else:
            switch.set_active(VARIABLE_BUFFER.get(var['name'], 0))
    
        switch.connect("notify::active", self.set_variable, var['name'])
        self.variables[var['name']] = {"switch": switch}
    
        # Layout the variable row
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        row.add(name_label)
        row.add(switch)
    
        pos = len(self.variables)
        self.labels['variables'].insert_row(pos)
        self.labels['variables'].attach(row, 0, pos, 1, 1)
        self.labels['variables'].show_all()
    
    
    def set_variable(self, widget, event, variable_name):
        # Get the current value of the switch
        value = 1 if widget.get_active() else 0
    
        # If synchronized tool changes are enabled, disable purging and cleaning
        if variable_name == "variable_enable_dual_toolchange" and value == 1:
            self.variables["variable_enable_purge_clean"]["switch"].set_active(False)
    
        # If purging and cleaning are enabled, disable synchronized tool changes
        if variable_name == "variable_enable_purge_clean" and value == 1:
            self.variables["variable_enable_dual_toolchange"]["switch"].set_active(False)
    
        # Existing logic to send GCODE commands
        if variable_name == "variable_enable_purge_clean":
            # Set variables for purge and clean
            self._screen._ws.klippy.gcode_script(
                f'SET_GCODE_VARIABLE MACRO=_PRINT_VARIABLE VARIABLE=enable_toolchange_purge VALUE={value}'
            )
            self._screen._ws.klippy.gcode_script(
                f'SET_GCODE_VARIABLE MACRO=_PRINT_VARIABLE VARIABLE=enable_toolchange_clean VALUE={value}'
            )
        elif variable_name == "variable_enable_dual_toolchange":
            # Set the synchronized toolchange variable
            self._screen._ws.klippy.gcode_script(
                f'SET_GCODE_VARIABLE MACRO=_PRINT_VARIABLE VARIABLE=enable_dual_toolchange VALUE={value}'
            )
        elif variable_name == "sensor_filamento":
            # Enable filament sensors
            self._screen._ws.klippy.gcode_script(
                f'SET_FILAMENT_SENSOR SENSOR=sensor_filamento_0 ENABLE={value}'
            )
            self._screen._ws.klippy.gcode_script(
                f'SET_FILAMENT_SENSOR SENSOR=sensor_filamento_1 ENABLE={value}'
            )
        elif variable_name == "sensor_movimiento_filamento":
            # Enable movement filament sensors
            self._screen._ws.klippy.gcode_script(
                f'SET_FILAMENT_SENSOR SENSOR=sensor_movimiento_filamento_0 ENABLE={value}'
            )
            self._screen._ws.klippy.gcode_script(
                f'SET_FILAMENT_SENSOR SENSOR=sensor_movimiento_filamento_1 ENABLE={value}'
            )
        else:
            # Set other variables
            macro_variable = variable_name.replace("variable_", "")
            self._screen._ws.klippy.gcode_script(
                f'SET_GCODE_VARIABLE MACRO=_PRINT_VARIABLE VARIABLE={macro_variable} VALUE={value}'
            )