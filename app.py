from flask import Flask 
import psutil
app = flask(__name__)
@app.route('/system_info')
def index():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    return {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage
    }
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)