from src.device_registry import add_device, list_devices

item = add_device("D01", "DHT11", "sensor")

assert item["device_id"] == "D01"
assert len(list_devices()) >= 1

print("PASS")
