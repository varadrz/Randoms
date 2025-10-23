# EV Charging Station Controller using Finite State Machine (FSM)

class EVChargingStationFSM:
    def __init__(self):
        self.state = "Idle"  # initial state

    def transition(self, event):
        if self.state == "Idle":
            if event == "plug_in":
                self.state = "Connected"
                print("Vehicle plugged in → Authenticating connection...")
            else:
                print("Invalid action! Waiting for vehicle to plug in.")

        elif self.state == "Connected":
            if event == "auth_ok":
                self.state = "Charging"
                print("Authentication successful → Charging started...")
            elif event == "unplug":
                self.state = "Idle"
                print("Vehicle unplugged → Back to Idle.")
            else:
                print("Invalid action! Waiting for authentication.")

        elif self.state == "Charging":
            if event == "battery_full":
                self.state = "Fully Charged"
                print("Battery full → Stopping power flow.")
            elif event == "unplug":
                self.state = "Disconnected"
                print("Charging interrupted → Vehicle disconnected.")
            else:
                print("Charging in progress...")

        elif self.state == "Fully Charged":
            if event == "unplug":
                self.state = "Disconnected"
                print("Vehicle unplugged after full charge.")
            else:
                print("Waiting for vehicle to unplug...")

        elif self.state == "Disconnected":
            if event == "reset":
                self.state = "Idle"
                print("System reset → Ready for next vehicle.")
            else:
                print("Invalid action! Please reset to Idle.")

        print(f"Current State: {self.state}\n")


# ---- Simulation Example ----
if __name__ == "__main__":
    station = EVChargingStationFSM()

    sequence = [
        "plug_in",
        "auth_ok",
        "battery_full",
        "unplug",
        "reset"
    ]

    print("=== EV Charging Station FSM Simulation ===\n")
    for event in sequence:
        station.transition(event)
