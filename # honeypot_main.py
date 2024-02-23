import logging

def honeypot_sensor():
    logging.info("Honeypot event detected.")
    # Add your honeypot logic here

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Start the honeypot sensor
    honeypot_sensor()
