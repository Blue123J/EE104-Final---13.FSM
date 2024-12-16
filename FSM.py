# Given a Finite State Machine FSM, write a Python test code to test that FSM (10 points)
# This is similar to a Verilog test bench.
# First name initial A-F: Your FSM will model a credit card reader. If the credit card number matches a stored number, and the pin matches, then output = 1, else output = 0.
# First name initial G-M: Your FSM will model a car licence plate reader. If the licence plate matches a stored number, and the car model matches, then gate_open = 1, else gate_open =0.
# First name initial N-Z: Your FSM will model a Capcha validator using a 3x3 grid and the flatten value is xxxyyyzzz where xxx is the first row, yyy the second row, zzz the third row. If a square matches, that square value is 1, else 0. If your stored pattern needs 3 matches, for example 011000100, and user identifies correctly, then match = 1, else match = 0.

# First name initial: J => Your FSM will model a car licence plate reader.
# If the licence plate matches a stored number, and the car model matches, then gate_open = 1, else gate_open = 0.

class CarLicencePlateFSM:
    def __init__(self, stored_plate, stored_model):
        # The stored license plate number and car model
        self.stored_plate = stored_plate
        self.stored_model = stored_model
        # Gate state (open or closed)
        self.gate_open = 0

    def check_access(self, license_plate, car_model):
        """Check if the license plate and car model match the stored values."""
        if license_plate == self.stored_plate and car_model == self.stored_model:
            self.gate_open = 1  # Match found, gate opens
        else:
            self.gate_open = 0  # No match, gate stays closed

        return self.gate_open


# Example usage
if __name__ == "__main__":
    # Stored license plate and car model
    stored_plate = "JMF4567"
    stored_model = "Toyota"
    
    # Create the FSM
    fsm = CarLicencePlateFSM(stored_plate, stored_model)

    # Continue checking for input
    while True:
        # Ask the user to input a license plate and car model
        license_plate = input("Enter the license plate: ")
        if license_plate.lower() == "exit":
            print("Exiting program.")
            break  # Exit the loop if the user types "exit"
        
        car_model = input("Enter the car model: ")
        if car_model.lower() == "exit":
            print("Exiting program.")
            break  # Exit the loop if the user types "exit"
        
        # Check the access and print the result
        result = fsm.check_access(license_plate, car_model)
        print(f"Gate Open: {result}\n")

