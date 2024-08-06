import psutil   
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percentage = psutil.cpu_percent(interval=1)
    memory_utilization = psutil.virtual_memory().percent
    Message = None
    if cpu_percentage > 80 or memory_utilization > 80:
        Message = 'ALERT! -> High CPU or Memory Utilization'
    return f'CPU Utilization: {cpu_percentage} | Memore Utilization: {memory_utilization}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')