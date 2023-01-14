"""
Made: 01-14-2023
"""

def zero_galvo_function():
    zero_galvo_card_name = "cDAQ1Mod2"
    zero_galvo_ao_channels = {f"{zero_galvo_card_name}/ao{i}": i for i in range(4)}
    zero_galvo = test.DAQAnalogOutputs("zero_galvo_name", zero_galvo_card_name, zero_galvo_ao_channels)
    zero_galvo.voltage_cdaq1mod2ao0(0.0)
    zero_galvo.voltage_cdaq1mod2ao0(0.0)
    zero_galvo.close()