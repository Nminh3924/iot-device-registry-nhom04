# Kiến trúc hệ thống IoT đề xuất
```mermaid
flowchart LR
    Sensor [Sensor Node] --> Gateway [LoRa/WiFi Gateway]
    Gateway --> Cloud [Cloud Broker/Server]
    Cloud --> App [Web/Mobile Dashboard]
