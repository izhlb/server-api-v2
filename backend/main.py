from api_modules import *
from flask import Flask, jsonify
from flask_cors import CORS
import threading

app = Flask(__name__)
CORS(app)



@app.route('/api/users')
def get_users():
    
    users = {
        "cpu":{
            "threads":f"{api.cpu_threads()}",
            "architecture":f"{api.cpu_architecture()}",
            "brand":f"{api.cpu_name()}",
            "clock":f"{api.cpu_clock()}"
        },
        "disk":{
            "total":f"{api.disk_primary_total()}",
            "used":f"{api.disk_primary_used()}",
            "free":f"{api.disk_primary_free()}",
            "percent":f"{api.disk_primary_percent()}",
            "mount":f"{api.disk_partition().mountpoint}",
            "filesystem": f"{api.disk_partition().fstype}",
    
        },
        "memory":{
            "total":f"{api.mem_total()}",
            "used":f"{api.mem_used()}",
            "percent":f"{api.mem_percent()}"
        },
        "net":{
            "data_sent":f"{api.net_sent_data_gb()}",
            "data_recieved":f"{api.net_reci_data_gb()}",
            "public_ip":f"{api.public_ip()}",
            "local_ip":f"{api.local_ip()}"
        },
        "other":{
            "username":f"{api.username()}",
            "hostname":f"{api.hostname()}",
            "startup":f"{api.startup()}"
        },
        "graphs":{
            "cpu":f"{cpu}",
            "mem":[]
        }

        }

    return jsonify(users)

if __name__ == '__main__':
    cpu_thread = threading.Thread(target=api.cpu_graph)
    cpu_thread.daemon = True
    cpu_thread.start()
    cpu_thread = threading.Thread(target=api.mem_graph)
    cpu_thread.daemon = True
    cpu_thread.start()
    app.run(port=5000, debug=True)