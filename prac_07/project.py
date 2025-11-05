"""
Estimate: 30 mins
Actual: ~2hr30m
"""


class Project:
    """Represent a Project object."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Declare a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __lt__(self, other):
        """Return true if project priority is higher than the other project priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return true if completion is 100 or greater."""
        return self.completion_percentage >= 100

    def __str__(self):
        """Return a string representation of the output."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
