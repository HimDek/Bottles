# globals.py
#
# Copyright 2022 brombinmirko <send@mirko.pm>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, in version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import shutil
from pathlib import Path
from bottles.backend.utils import yaml, json


class Paths:
    xdg_data_home = os.environ.get(
        "XDG_DATA_HOME", os.path.join(Path.home(), ".local/share")
    )

    if os.path.isdir("/run/host"):
        host = "/run/host"
    else:
        host = "/"

    # Icon paths
    icons_user = f"{xdg_data_home}/icons"

    # Local paths
    base = f"{xdg_data_home}/bottles"

    # User applications path
    applications = f"{xdg_data_home}/applications/"

    temp = f"{base}/temp"
    runtimes = f"{base}/runtimes"
    winebridge = f"{base}/winebridge"
    runners = f"{base}/runners"
    steam_runners = f"{xdg_data_home}/Steam/compatibilitytools.d/"
    usr_steam_runners = f"{host}/usr/share/steam/compatibilitytools.d/"
    bottles = f"{base}/bottles"
    steam = f"{base}/steam"
    dxvk = f"{base}/dxvk"
    vkd3d = f"{base}/vkd3d"
    nvapi = f"{base}/nvapi"
    latencyflex = f"{base}/latencyflex"
    templates = f"{base}/templates"
    library = f"{base}/library.yml"

    @staticmethod
    def is_vkbasalt_available():
        vkbasalt_paths = [
            "/usr/lib/extensions/vulkan/vkBasalt/etc/vkBasalt",
            "/usr/local",
            "/usr/share/vkBasalt",
        ]
        for path in vkbasalt_paths:
            if os.path.exists(path):
                return True
        return False


class TrdyPaths:
    # External managers paths
    wine = f"{Path.home()}/.wine"
    lutris = f"{Path.home()}/Games"
    playonlinux = f"{Path.home()}/.PlayOnLinux/wineprefix"
    bottlesv1 = f"{Path.home()}/.Bottles"


# check if bottles exists in xdg data path
os.makedirs(Paths.base, exist_ok=True)

# Check if some tools are available
gamemode_available = shutil.which("gamemoderun") or False
gamescope_available = shutil.which("gamescope") or False
vkbasalt_available = Paths.is_vkbasalt_available()
mangohud_available = shutil.which("mangohud") or False
obs_vkc_available = shutil.which("obs-vkcapture") or False
vmtouch_available = shutil.which("vmtouch") or False
base_version = ""
if os.path.isfile("/app/manifest.json"):
    with open("/app/manifest.json", encoding="utf-8") as file:
        base_version = (
            json.load(file)  # type: ignore
            .get("base-version", "")
            .removeprefix("stable-")
        )

# encoding detection correction, following windows defaults
locale_encodings: dict[str, str] = {"ja_JP": "cp932", "zh_CN": "gbk"}
