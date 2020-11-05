=====
Usage
=====

Send Message

.. code-block:: python

    from py_rf_lora_868_so import rf_lora
    import RPi.GPIO as GPIO
    import spidev

    # Set up GPIO
    GPIO.setmode(GPIO.BOARD)
    
    # Set up SPI
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.mode = 0b00

    lora_module = rf_lora(spi_device = spi,
                    rx_sw = 11,
                    tx_sw = 13,
                    dio0 = 15,
                    reset = 29)
    
    lora_module.send(binary_payload=[0x01, 0x02, 0x03])

Receive Message

.. code-block:: python

    from py_rf_lora_868_so import rf_lora
    import RPi.GPIO as GPIO
    import spidev

    # Set up GPIO
    GPIO.setmode(GPIO.BOARD)
    
    # Set up SPI
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.mode = 0b00

    lora_module = rf_lora(spi_device = spi,
                    rx_sw = 11,
                    tx_sw = 13,
                    dio0 = 15,
                    reset = 29)
    
    def rx_callback_func(message):
        print(message)

    lora_module.set_rx_callback(rx_callback_func)
    lora_module.receive_mode()
    lora_module.block_until_receive()