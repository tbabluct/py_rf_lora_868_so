import spidev
from . import addr_lookup as al


class sx1272(object):
    """
    docstring
    """

    def __init__(self, spi_device):
        # Setup deafault state
        self._reset_state()
        self.spi_device = spi_device

    def set_reg(self, addr, value):
        addr_byte = 0x80
        addr_byte += 0x7F | addr
        if not type(value) is list:
            value = [value]
        
        self._check_byte_arr(value)

        spi_device.xfer2([addr] + value)

    def read_reg(self, addr, length):
        addr_byte = 0x80
        addr_byte += 0x7F | addr

        return spi_device.xfer2([addr_byte] + [0]*length)

    def set_long_range_mode(self, lr_mode):
        if not type(lr_mode) is bool:
            raise TypeError("lr_mode should be either True or False")
        elif lrmode:
            self.LongRangeMode = 1
            self._update_reg_op_mode()
        else:
            self.LongRangeMode = 0
            self._update_reg_op_mode()

            
    def _update_reg_op_mode(self):
        # Setup the byte to send
        val = 0
        val += self.Mode
        val += self.AccesSharedReg << 6
        val += self.LongRangeMode << 7
        self.set_reg(al["RegOpCode"], val)

    def _set_default_state(self):
        self.LongRangeMode = 0
        self.AccesSharedReg = 0
        self.Mode = 0x01

    def _reset_state(self):
        self._set_default_state()

    def _check_byte_arr(self, arr):
        if not type(arr) is list:
            raise TypeError("Please pass a list")
        else:
            for item in arr:
                if not type(item) is int:
                    raise TypeError("Please pass all items as integers")
                elif item > 255 or item < 0:
                    raise RangeError("Please pass vallues between 0 and 255 inclusive"

