"""Main module."""
import RPi.GPIO as GPIO
from .sx1272Driver import sx1272


class rf_lora(object):
    """Class representing the RF-LoRa-868 module

    """
    def __init__(self, spi_device = None,
                    rx_sw = 11, tx_sw = 13,
                    dio0 = 15, reset_pin = 29):
        """Initialize an instance of the rf_lora class

        Args:
            spi_device (spidev, optional): spidev device for the SX1272. Defaults to spi.
            rx_sw (int, optional): Pin number of Rx Switch. Defaults to 11.
            tx_sw (int, optional): Pin number of Tx Switch. Defaults to 13.
            dio0 (int, optional): Pin number of DIO0 to be used for interrupts Defaults to 15.
            reset (int, optional): Pin number for the reset line of the SX1272. Defaults to 29.
        """
        self.spi_device = spi_device
        self.rx_sw = rx_sw
        self.tx_sw = tx_sw
        self.dio0 = dio0
        self.reset_pin = reset_pin

        self.sx1272 = sx1272(spi_device)

    def send_message(self, message):
        """Send a message with the SX1272 

        Args:
            message (bytearray): Byte array of the message payload
        """
        self.sx1272.send_message(message)

    def set_rx_callback(self, rx_callback_func):
        """Set the callback function to be called when a valid LoRa message is received

        Args:
            rx_callback_func (function): function to be called when a valid LoRa message is received
        """
        self.sx1272.set_rx_callback(rx_callback_func)
