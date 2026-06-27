devices = []

def add_device(device_id, name, device_type):
    device = {
        "device_id": device_id,
        "name": name,
        "type": device_type
    }
    devices.append(device)
    return device

def list_devices():
    return devices
