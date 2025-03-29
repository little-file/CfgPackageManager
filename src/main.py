def os_detected():
    import platform
    global os
    os  = platform.system()

def os_reaction():
    import platform
    os_detected()
    global os_pending
    global os_name
    global linux_info

    if os == "Linux":
        print("welcome")
        os_pending = True
        os_name = "linux"
        if platform.system() == "Linux":
            try:
                os_info = platform.freedesktop_os_release()
                if "ID" in os_info:
                    linux_info = os_info["ID"].lower()
                    if linux_info in ["debian", "ubuntu"]:
                        os_pending = False
                        return "Debian/Ubuntu (apt)"
                    elif linux_info == "fedora":
                        os_pending = False
                        return "Fedora (dnf)"
                    else:
                        os_pending = False
                        return f"Diğer Linux ({linux_info})"
                else:
                    return "Linux (Dağıtım bilgisi bulunamadı)"
            except FileNotFoundError:
                return "Linux (os-release dosyası bulunamadı)"

    elif os == "Windows":
        print("We so sorry but not support goodbye")
        os_pending = False
        os_name = "windows"


    elif os == "Darwin":
        print("Wo so sorry but not support goodbye")
        os_pending = False
        os_name = "darwin"
    else:
        print("Wo so sorry but not support goodbye")
        os_pending = False
        os_name = "DK" # Dont Know

def yaml_read():
    import yaml
    global yaml_data

    try:
        with open('config/config.yaml', 'r') as dosya:
            yaml_data = yaml.safe_load(dosya)
    except FileNotFoundError:
        print("YAML not found.")
    except yaml.YAMLError as e:
        print(f"YAML error read: {e}")

# DNF
def dnf_update():
    import subprocess
    makecache = "sudo dnf makecache"
    command = "sudo dnf update -y"
    try:
        print("DNF cache starting...")
        result = subprocess.run(makecache, shell=True, check=True, capture_output=True, text=True)
        print("DNF cache finished.")
        if result.stdout:
            print("DNF cache OUT:")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: DNF cache during a problem.")
        print(f"Rrror code: {e.returncode}")
        if e.stderr:
            print(f"Error OUT:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: 'dnf' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


    try:
        print("system updates starting...")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("system updates finished.")
        if result.stdout:
            print("Updates OUT:")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: System updates during a problem.")
        print(f"Rrror code: {e.returncode}")
        if e.stderr:
            print(f"Error OUT:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: 'dnf' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def dnf_mirror():
    import subprocess
    command = "sudo dnf config-manager --add-repo"
    try:
        print("system mirror starting...")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("system mirror finished.")
        if result.stdout:
            print("mirror OUT:")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: System mirror during a problem.")
        print(f"Rrror code: {e.returncode}")
        if e.stderr:
            print(f"Error OUT:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: 'dnf' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def dnf_install():
    import subprocess
    command = "sudo dnf config-manager --add-repo"
    try:
        print("system installs starting...")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("system installs finished.")
        if result.stdout:
            print("installs OUT:")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: System installs during a problem.")
        print(f"Rrror code: {e.returncode}")
        if e.stderr:
            print(f"Error OUT:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: 'dnf' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def dnf_system():
    dnf_mirror()
    dnf_update()
    dnf_install()

# FLATPAK
def flatpak_update():
    import subprocess
    command = "flatpak update -y"
    try:
        print("flatpak updates starting...")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("flatpak updates finished.")
        if result.stdout:
            print("Updates OUT:")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: flatpak updates during a problem.")
        print(f"Rrror code: {e.returncode}")
        if e.stderr:
            print(f"Error OUT:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: 'flatpak' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def flatpak_mirror():
    import subprocess
    command = "flatpak remote-add --if-not-exists --user"
    try:
        print("flatpak mirror starting...")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("flatpak mirror finished.")
        if result.stdout:
            print("Mirror OUT:")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: flatpak Mirror during a problem.")
        print(f"Rrror code: {e.returncode}")
        if e.stderr:
            print(f"Error OUT:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: 'flatpak' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def flatpak_install():
    import subprocess
    command = "flatpak install -y --user"
    try:
        print("flatpak installing starting...")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("flatpak installing finished.")
        if result.stdout:
            print("installing OUT:")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: flatpak installing during a problem.")
        print(f"Rrror code: {e.returncode}")
        if e.stderr:
            print(f"Error OUT:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: 'flatpak' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def frist():
    os_reaction()
    if os_pending == False:
        exit()
    print(linux_info)
frist()