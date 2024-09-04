import os
import signal
import psutil
from flask import Flask, render_template, request, redirect, url_for
from blockchain.ganache_connector import connect_to_ganache
from smart_contracts.contract_interaction import interact_with_contract
from web3 import Web3

app = Flask(__name__)

# Replace with your smart contract ABI and address
contract_abi = [...]
contract_address = "0x98Ae4E031A5e9145Ee16C629b2543B74ceC0d333"

#onceki address 0x37D9a2292E42E83E6A4f68d9bC1D975474127Fb9

# Connect to Ganache
print("Before connecting to Ganache")
web3 = connect_to_ganache("http://127.0.0.1:7545")  # Use the correct Ganache URL
print("After connecting to Ganache")

ganache_process = None  # Global variable to store the Ganache process

def start_ganache():
    ganache_cmd = "ganache-cli"
    process = psutil.Popen(ganache_cmd, shell=True, preexec_fn=os.setsid, stdin=psutil.PIPE, stdout=psutil.PIPE, stderr=psutil.PIPE)
    return process

def stop_ganache(process):
    try:
        process.terminate()
        psutil.wait_procs([process], timeout=5)
    except psutil.NoSuchProcess:
        pass

# Close Ganache when the Flask app is stopped
@app.teardown_appcontext
def teardown_ganache(exception=None):
    global ganache_process
    if ganache_process and ganache_process.is_running():
        os.killpg(os.getpgid(ganache_process.pid), signal.SIGTERM)

# Disable favicon request
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Home route
@app.route('/')
def home():
    print("Home route accessed")
    return render_template('index.html')

# User registration route
@app.route('/user_registration', methods=['GET', 'POST'])
def user_registration():
    if request.method == 'POST':
        # Handle user registration logic here
        return render_template('registration_success.html')
    return render_template('user_registration.html')

@app.route('/registration_success')
def registration_success():
    return render_template('registration_success.html')

# Project registration route
@app.route('/project_registration', methods=['GET', 'POST'])
def project_registration():
    if request.method == 'POST':
        # Handle project registration logic here
        project_name = request.form.get('project_name')
        training_data = request.form.get('training_data')
        design_data = request.form.get('design_data')
        material_data = request.form.get('material_data')
        energy_data = request.form.get('energy_data')

        # Assuming 'myFunction' takes parameters, replace these with your actual parameters
        # Call the interact_with_contract function
        parameter_value = 123  # Replace with the actual value you want to pass
        interact_with_contract(web3, project_name, training_data, design_data, material_data, energy_data, parameter_value)

        return redirect(url_for('registration_success'))
    return render_template('project_registration.html')

# External registration route
@app.route('/external_registration', methods=['GET', 'POST'])
def external_registration():
    # Your logic for external registration
    return render_template('external_registration.html')

# Certification route
@app.route('/certification', methods=['GET', 'POST'])
def certification():
    # Your logic for certification
    return render_template('certification.html')

# Training route
@app.route('/training', methods=['GET', 'POST'])
def training():
    # Your logic for training
    return render_template('training.html')

# Payments route
@app.route('/payments', methods=['GET', 'POST'])
def payments():
    # Your logic for payments
    return render_template('payments.html')

# IoT Device registration route
@app.route('/iot_device_registration', methods=['GET', 'POST'])
def iot_device_registration():
    # Your logic for IoT Device registration
    return render_template('iot_device_registration.html')

# Data-Device Tracking route
@app.route('/data_device_tracking', methods=['GET', 'POST'])
def data_device_tracking():
    # Your logic for Data-Device Tracking
    return render_template('data_device_tracking.html')

# Retrieve Records route
@app.route('/retrieve_records', methods=['GET', 'POST'])
def retrieve_records():
    # Your logic for retrieving records
    return render_template('retrieve_records.html')



if __name__ == '__main__':
    app.run(debug=True)
