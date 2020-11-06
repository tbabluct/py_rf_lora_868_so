import spidev
from . import addr_lookup as al


class sx1272(object):
    """Class representing the state and functionality of the SX1272 chip

    """

    def __init__(self, spi_device):
        """Initialize and instance of the sx1272 class

        Args:
            spi_device (spidev): spidev device for the SX1272
        """
        # Setup deafault state
        self._reset_state()
        self.spi_device = spi_device

    def set_reg(self, addr, value):
        """Change a register on the SX1272

        Args:
            addr (int): Register address
            value (bytearray): The values to be written from the given address onwards
        """
        addr_byte = 0x80
        addr_byte += 0x7F | addr
        if not type(value) is list:
            value = [value]
        
        self._check_byte_arr(value)

        spi_device.xfer2([addr] + value)

    def read_reg(self, addr, length):
        """Read the values from addr for <length> bytes

        Args:
            addr (int): Address from where to start reading
            length (int): The number of bytes to read from the registers

        Returns:
            bytearray: The contents of the addressed register space
        """
        addr_byte = 0x80
        addr_byte += 0x7F | addr

        return spi_device.xfer2([addr_byte] + [0]*length)

    def set_long_range_mode(self, lr_mode):
        """Set the LongRangeMode register on the SX1272

        Args:
            lr_mode (bool): Boolean indicating if LR mode is on or off

        Raises:
            TypeError: When lr_mode is not a boolean value
        """
        if not type(lr_mode) is bool:
            raise TypeError("lr_mode should be either True or False")
        elif lrmode:
            self.LongRangeMode = 1
            self._update_reg_op_mode()
        else:
            self.LongRangeMode = 0
            self._update_reg_op_mode()

            
    def _update_reg_op_mode(self):
        """Update the regOpMode register on the SX1272
        """
        # Setup the byte to send
        val = 0
        val += self.Mode
        val += self.AccesSharedReg << 6
        val += self.LongRangeMode << 7
        self.set_reg(al["RegOpCode"], val)

    def _set_default_state(self):
        """Reset the state representation of the SX1272
        """
        self.LongRangeMode = 0
        self.AccesSharedReg = 0
        self.Mode = 0x01

    def _reset_state(self):
        """Reset the state representation of the SX1272
        """
        self._set_default_state()

    def _check_byte_arr(self, arr):
        """Check if a given value is a bytearray

        Args:
            arr (any): The value to be checked

        Raises:
            Various errors describing the nature of the uncompliance
        """
        if not type(arr) is list:
            raise TypeError("Please pass a list")
        else:
            for item in arr:
                if not type(item) is int:
                    raise TypeError("Please pass all items as integers")
                elif item > 255 or item < 0:
                    raise RangeError("Please pass vallues between 0 and 255 inclusive"

