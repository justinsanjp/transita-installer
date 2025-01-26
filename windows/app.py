import os
import sys
import platform
import subprocess
import tkinter as tk
import asyncio
import aiohttp
import random
import zipfile
import shutil
from pathlib import Path

class MinecraftModInstaller:
    def __init__(self):
        self.system = platform.system().lower()
        self.windows_version = platform.win32_ver()[0] if self.system == 'windows' else None
        self.minecraft_dir = self.get_minecraft_directory()

    def get_minecraft_directory(self):
        if self.system == 'windows':
            return os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', '.minecraft')
        elif self.system == 'darwin':  # macOS
            return os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'minecraft')
        elif self.system == 'linux':
            return os.path.join(os.path.expanduser('~'), '.minecraft')
        else:
            raise OSError(f"Unsupported operating system: {self.system}")

    def check_windows_11_compatibility(self):
        if self.system == 'windows' and self.windows_version.startswith('10'):
            print("\n" + "=" * 80)
            print("⚠️ WARNUNG ⚠️".center(80))
            print("=" * 80)
            print("\nDieses Script könnte auf Windows 11 NICHT FUNKTIONIEREN!")
            print("Bekannte Kompatibilitätsprobleme mit Minecraft und Fabric auf Windows 11:")
            print("- Mögliche Installationsfehler")
            print("- Unerwartete Systeminteraktionen")
            print("- Potenziell fehlerhafte Mod-Installationen")
            print("\nBitte seien Sie vorsichtig und überprüfen Sie jede Installationsschritt manuell!")
            print("=" * 80 + "\n")
            input("Drücken Sie ENTER, um fortzufahren...")

    def show_fabric_dialog(self):
        root = tk.Tk()
        root.title("Fabric Installation")
        
        label = tk.Label(root, text="Select Minecraft version 1.18.2 and click OK")
        label.pack(padx=20, pady=10)
        
        root.after(60000, root.destroy)  # Close after 60 seconds
        root.mainloop()

    def install_fabric(self):
        if self.system == 'windows':
            fabric_installer_url = 'https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.1/fabric-installer-1.0.1.exe'
            fabric_installer_path = os.path.join(os.getcwd(), 'fabric-installer.exe')
            
            # Download Fabric Installer
            asyncio.run(self.download_file(fabric_installer_url, fabric_installer_path))
            
            # Show Tkinter dialog
            self.show_fabric_dialog()
            
            # Run Fabric Installer
            input("Press ENTER to start Fabric installation...")
            subprocess.run([fabric_installer_path], shell=True)
        else:
            print("Please download Fabric manually from https://fabricmc.net/")
            input("Press ENTER after downloading Fabric...")

    async def download_file(self, url, filename):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                with open(filename, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)

    async def download_mods_and_textures(self):
        mods_url = 'http://app.justinsanjp.de/transita/mods.zip'
        textures_url = 'http://app.justinsanjp.de/transita/resourcepacks.zip'

        mods_path = os.path.join(self.minecraft_dir, 'mods.zip')
        textures_path = os.path.join(self.minecraft_dir, 'resourcepacks.zip')

        # Backup existing mods folder
        mods_dir = os.path.join(self.minecraft_dir, 'mods')
        if os.path.exists(mods_dir):
            random_number = random.randint(1000, 9999)
            backup_name = f'mods_{random_number}'
            backup_path = os.path.join(self.minecraft_dir, backup_name)
            shutil.move(mods_dir, backup_path)

        # Download files
        await asyncio.gather(
            self.download_file(mods_url, mods_path),
            self.download_file(textures_url, textures_path)
        )

        # Extract files
        os.makedirs(os.path.join(self.minecraft_dir, 'mods'), exist_ok=True)
        os.makedirs(os.path.join(self.minecraft_dir, 'resourcepacks'), exist_ok=True)

        with zipfile.ZipFile(mods_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.join(self.minecraft_dir, 'mods'))

        with zipfile.ZipFile(textures_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.join(self.minecraft_dir, 'resourcepacks'))

        # Remove zip files
        os.remove(mods_path)
        os.remove(textures_path)

    def run(self):
        # Windows 11 Kompatibilitätswarnung
        self.check_windows_11_compatibility()

        # Install Fabric
        self.install_fabric()

        # Download and install mods/textures
        asyncio.run(self.download_mods_and_textures())
        print("Installation complete!")

def main():
    installer = MinecraftModInstaller()
    installer.run()

if __name__ == '__main__':
    main()
