# Functions/internet_speed.py
import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Mbps
    upload_speed = st.upload() / 1_000_000      # Mbps
    ping = st.results.ping
    return f"Download speed: {download_speed:.2f} Mbps, Upload speed: {upload_speed:.2f} Mbps, Ping: {ping} ms"
