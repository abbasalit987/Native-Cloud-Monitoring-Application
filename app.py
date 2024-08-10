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
    return render_template("index.html", cpu_metric=cpu_percentage, mem_metric=memory_utilization, message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')