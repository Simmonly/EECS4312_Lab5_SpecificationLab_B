## Student Name: Mohsen Maoodhah
## Student ID: 220153425

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    # Checking if resources is a dictionary
    if not isinstance(resources, dict):
        raise ValueError("THe resources must be a dictionary")
    
    # Maps each resource to the total capacity. Initializes each resource in the resources to a value of 0
    total_usage: Dict[str, Number] = {key: 0 for key in resources}

    # Going through the list of dictionaries to calculate the total sum for each resource
    for request in requests:
        # Making sure a request is a dictionary
        if not isinstance(request, dict):
            raise ValueError("each request must be a dict")
        for name, amount in request.items():
            if name not in resources:
                return False
            if not isinstance(amount, (int, float)):
                raise ValueError("requested amount must be a number")
            
            total_usage[name] += amount

    for name, used in total_usage.items():
        if used > resources[name]:
            return False
    return True

"""
The above is almost entirely created by ChatGPT (I didn't just copy it I typed it myself to make sure I understand every line of code).
Here's my explanation of the code and the project requirements. 
The project basically provides a hashmap of resources where each resource is mapped to a capacity. For example, CPU: 10 means that we have 10
CPUs. Then we have a list of requests represented as a list of dictionries. For example, [{'cpu': 3}, {'cpu': 4}]. We want to make sure we can
satisfy the requests give our capacities. For the example I gave we need 3 cpus and 4 cpus from the requests so in total we need 7 cpus, and we
have 10 cpus, so the requests can be satsified. 
For the solution I have a hashmap that maps each resource to how many times they were used. I initiate it with every resource in resources as a 
key, and 0 as its values. Then I go through all requests, add the values for each resources to the hashmap I created. Finally I compare the values
in the hashmap to the values in resources, if for any resource the number of resources I used is larger than the number of resources available, or
if the resource doesn't exist I would return False. Otherwise I would return True.
"""
