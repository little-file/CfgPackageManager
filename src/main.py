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

def frist():
    os_reaction()
    if os_pending == False:
        exit()
    print(linux_info)
frist()