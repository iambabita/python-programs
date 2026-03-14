import logging
import sys

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    try:
        logging.info("Program started")

        #main logic here
        name = input("Enter your name: ")
        print(f"Hello, {name}! Welcome to Python.")

        logging.info("Program finished successfully")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)


 
if __name__ == "__main__":
    main()