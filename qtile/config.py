# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import qtile
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

netDevice = "wlo1"
mod = "mod4"
terminal = guess_terminal()
taskbarColor = "#050014"
taskbarSize=26
defaultFont = "Tinos"
fontSize= 16
activeColor="#e66900"
iconSize=20
fgColor="#ffffff"
fgColor1="#8B8B8B"
bgColor="050014"
inactiveColor="#003770"
groupColor="#13004b"
urgentColor="#ff5555"
textColor="#003770"
groupColor1="#ff7f00" # naranja
groupColor2="#00CBB4" # Azul aguamarina
groupColor3="#7D00FF" # Lila
groupColor4="#D10000" # Rojo
paddingGroup1=-12.8
paddingGroup2=-12.2
paddingGroup3=-12.2
paddingGroup4=-12.2
fontSizeWidgets=14
updateColor= "#ff0000" #Rojo
batteryColor= "#FFE800"

#funcion que genera separadores
def fc_groupSplit():
    return widget.Sep(
            linewidth=0,
            padding=10,
            background=bgColor,        
    )

#funcion que pone triangulos
def fc_triangle(vColor, tipo, tpadding, bColor):
    if tipo == 0:
        icon="" #nf-oct-triangle_left 
    else:
        icon="" #nf-oct-triangle_right
    return widget.TextBox(
        text = icon,
        fontsize = taskbarSize+11.5,
        foreground = vColor,
        background = bColor,
        padding=tpadding,
    ) 

#funcion para escribir un texto o icono
def fc_icon(icon, vColor, fgGround):
    return widget.TextBox(
        text=icon,
        foreground= fgGround,
        background= vColor,
        fontsize= iconSize,
    )

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    #teclas para lanzar menu rofi
    Key(["mod1"], "space", lazy.spawn("rofi -show drun"), desc="Abrir menu"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #Volumen control
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    #Brillo de la pantalla
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([mod], "s", lazy.spawn("scrot"), desc="Take ss"),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s"), desc="Take ss"),



]

#Listado de iconos nerd font

groups = [Group(i) for i in [
    "  ","  "," 3 "," 4 "," 5 "," 6 ","  ", 
    ]]

for i, group in enumerate(groups):
    numeroEscritorio =str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=defaultFont,
    fontsize=fontSize,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=activeColor,
                    border_width=1,
                    disable_drag=True,
                    fontsize=iconSize,
                    foreground=fgColor,
                    highlight_method='block',
                    inactive=inactiveColor,
                    margin_x=0,
                    margin_y=3,
                    padding_x=0,
                    pagging_y=10,
                    this_current_screen_border=groupColor,
                    this_screen_border=groupColor,
                    urgent_alert_method='block',
                    urgent_border=urgentColor,
                ),
                widget.Prompt(),
                widget.WindowName(
                    foreground=textColor,
                    background=bgColor,
                    fontsize=12,
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(
                    icon_size=iconSize,
                    background= bgColor,
                ),

                fc_groupSplit(),
                #grupo1, donde va la parte de temperaturas y consumo de componentes
                fc_triangle(groupColor1, 0, paddingGroup1, bgColor),
                fc_icon("", groupColor1, fgColor), #nf-mdi-memory
                widget.CPU(
                    foreground = fgColor,
                    background = groupColor1,
                    fontsize = fontSizeWidgets,
                    format = 'CPU: {load_percent}% |'
                ),               
                widget.ThermalSensor(
                    foreground = fgColor,
                    background = groupColor1,
                    threshold = 65,
                    tag_sensor = "Core 0",
                    fontsize = fontSizeWidgets,
                    fmt = '{}',
                ),

                fc_icon(" ", groupColor1, fgColor), #nf-cod-dashboard
                widget.Memory(
                    foreground = fgColor,
                    background = groupColor1,
                    fontsize = fontSizeWidgets,
                    format = 'Ram:{MemUsed:.0f}{mm}'
                ),
                #Grupo 2, donde va la fecha
                fc_triangle(groupColor2, 0, paddingGroup2, groupColor1),
                widget.Clock(
                    format= "%a %d/%m/%Y |",
                    background = groupColor2,
                    foreground = fgColor1,
                    fontsize = 13,
                
                ),
                widget.Clock(
                    format="%I:%M %p",
                    background = groupColor2,
                    foreground = fgColor,

                ),


                #Grupo 3, donde van las actualizaciones y el apagado
                fc_triangle(groupColor3, 0, paddingGroup3, groupColor2),
                fc_icon("", groupColor3, fgColor), #nf-mdi-autorenew
                widget.CheckUpdates(
                    background = groupColor3,
                    colour_have_updates = updateColor,
                    colour_no_updates = fgColor,
                    no_update_string = '0',
                    display_format = '{updates}',
                    update_interval = 1800,
                    distro = 'Arch_checkupdates',
                ),
                fc_icon("", groupColor3, batteryColor), #nf-fa-bolt
                widget.Battery(
                    background = groupColor3,
                    foreground = batteryColor,
                    format = '{percent:2.0%}',
                    full_char = "100%",
                    update_interval = 1,
                ),
                fc_icon("", groupColor3, fgColor), #nf-fa-volume_up
                widget.PulseVolume(
                    foreground = fgColor,
                    background = groupColor3,
                    limit_max_volume = True,
                    fontsize=14,
                ),

                #Grupo 4
                fc_triangle(groupColor4, 0, paddingGroup4, groupColor3),
                widget.CurrentLayoutIcon(
                    background = groupColor4,
                    scale = 0.6,
                ),
                widget.CurrentLayout(
                    background = groupColor4,
                    foreground = fgColor
                ),
                


                
                #fc_icon("龍", groupColor2, fgColor), #nf-mdi-speedometer
                #widget.Net(
                #    foreground = fgColor,
                #    background = groupColor2,
                #    format = '{down}{up}',
                #    interfate = netDevice,
                #    use_bits = 'true',
                #),


            ],
            taskbarSize,
            background=taskbarColor,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
