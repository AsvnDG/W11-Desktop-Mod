import psutil
import subprocess
import xml.etree.ElementTree as ET
from time import time, sleep
from datetime import datetime

# Define the path to your XML file
xml_file = 'config.xml'

# Initialize counters
previous_io = psutil.net_io_counters()
previous_time = time()

def get_network_speed():
    global previous_io, previous_time

    # Get current counters
    current_io = psutil.net_io_counters()
    current_time = time()

    # Calculate speed
    elapsed_time = current_time - previous_time
    upload_diff = current_io.bytes_sent - previous_io.bytes_sent
    download_diff = current_io.bytes_recv - previous_io.bytes_recv

    # Update previous values
    previous_io = current_io
    previous_time = current_time

    # Calculate speed in bytes per second
    upload_speed = upload_diff / elapsed_time
    download_speed = download_diff / elapsed_time

    # Convert to human-readable format
    def format_speed(bytes_per_sec):
        if bytes_per_sec < 1024:
            return f"{bytes_per_sec:.2f} B/s"
        elif bytes_per_sec < 1_048_576:
            return f"{bytes_per_sec / 1024:.2f} KB/s"
        else:
            return f"{bytes_per_sec / 1_048_576:.2f} MB/s"

    return format_speed(upload_speed), format_speed(download_speed)

def update_xml(download_speed, upload_speed):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Update the last updated time
    last_updated = root.find('LastUpdated')
    last_updated.text = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Update download and upload speeds
    download = root.find('Speed/Download')
    upload = root.find('Speed/Upload')
    
    download.text = download_speed
    upload.text = upload_speed
    
    # Write the updated XML back to the file
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

def main():
    while True:
        download_speed, upload_speed = get_network_speed()
        update_xml(download_speed, upload_speed)
        sleep(1)  # Wait for 1 second before the next update


if __name__ == "__main__":  
    #subprocess.Popen(['python', 'startlocalehost.py'])
    main()
