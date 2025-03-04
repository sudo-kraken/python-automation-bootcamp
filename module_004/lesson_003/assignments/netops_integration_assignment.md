# Practice Exercise: Integrating Network Automation into DevOps Workflows

## Objective
Practice combining API data retrieval with network automation in a single Python script.

## Tasks
1. Create a new file named `netops_integration_exercise.py`.
2. In your script:
   - Use the requests library to fetch data from a public API (for example, the jsonplaceholder API).
   - Parse the JSON response to extract a relevant value (e.g., a boolean flag).
   - Based on the extracted value, choose a network command (e.g., "show version" or "show ip interface brief").
   - Use Netmiko to attempt a connection to a network device (or simulate the connection if you don't have access) and execute the command.
3. Experiment by changing the API endpoint, parsing different data, or adjusting the command logic.

This exercise will help you understand how to integrate multiple automation components in a DevOps workflow.
