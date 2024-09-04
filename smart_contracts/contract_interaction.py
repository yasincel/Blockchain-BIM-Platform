# smart_contracts/contract_interaction.py
import json
from web3 import Web3


def interact_with_contract(web3, project_name, training_data, design_data, material_data, energy_data, parameter_value, x_value=None):
    # Load the smart contract ABI from my_contract_abi.json
    with open('smart_contracts/my_contract_abi.json', 'r') as file:
        contract_abi = json.load(file)

    # Load the smart contract address from my_contract_address.txt
    with open('smart_contracts/my_contract_address.txt', 'r') as file:
        contract_address = file.read().strip()  # Strip leading/trailing whitespaces or newlines

    my_contract = web3.eth.contract(abi=contract_abi, address=contract_address)

    try:
        if x_value is not None:
            my_contract.functions.set(x_value).transact()
         # Example: Call storedData function
        result = my_contract.functions.storedData().call()
        print("Stored Data in Smart Contract:", result)
        # Assuming myFunction takes a uint256 parameter
        result = my_contract.functions.myFunction(parameter_value).call()

        print("Smart Contract Result:", result)

        # Add logic to store project details on the blockchain
        # For example, you can call another function in your smart contract to store project details
        transaction_hash = my_contract.functions.storeProjectDetails(
            project_name, training_data, design_data, material_data, energy_data
        ).transact()

        # Wait for the transaction to be mined
        web3.eth.waitForTransactionReceipt(transaction_hash)

        print("Project details stored on the blockchain.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
# connect_to_ganache() and interact_with_contract(web3) should be called in bim_platform_web.py
