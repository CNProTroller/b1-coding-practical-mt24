# Control Module

class PDController:
    def __init__(self, Kp=0.15, Kd=0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0.0

    def control(self, reference, output):
        # Calculate the current error
        error = reference - output
        
        # PD control law
        control_action = self.Kp * error + self.Kd * (error - self.previous_error)
        
        # Update the previous error for the next iteration
        self.previous_error = error
        
        return control_action
