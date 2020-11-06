=========================
RF-LORA-868-SO Python API
=========================


.. image:: https://img.shields.io/pypi/v/py_rf_lora_868_so.svg
        :target: https://pypi.python.org/pypi/py_rf_lora_868_so

.. image:: https://readthedocs.org/projects/py-rf-lora-868-so/badge/?version=latest
        :target: https://py-rf-lora-868-so.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/tbabluct/py_rf_lora_868_so/shield.svg
     :target: https://pyup.io/repos/github/tbabluct/py_rf_lora_868_so/
     :alt: Updates



Python API for the RF-LORA-


* Free software: MIT license
* Documentation: https://py-rf-lora-868-so.readthedocs.io.


Usage
-----
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
                    reset_pin = 29)
    
    def rx_callback_func(message):
        print(message)

    lora_module.set_rx_callback(rx_callback_func)
    lora_module.receive_mode()
    lora_module.block_until_receive()

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
