import pytest
from simple_iot_device import SimpleIOTDevice


@pytest.fixture()
def simple_test_device():
    device_name = "SIMPLE-TEST"
    device = SimpleIOTDevice(device_name)
    return device


class TestSimpleIOTDevice:
    def test_create_simple_iot_device(self):
        device_name = "SDM-125200"
        device = SimpleIOTDevice(device_name)
        assert isinstance(device, SimpleIOTDevice)
        assert device.name == device_name
        assert device.description == "Simple IOT Device"

    def test_create_simple_iot_device_with_custom_description(self):
        device_name = "SDM-125500"
        device_description = "Simple IOT Device with Custom Description"
        device = SimpleIOTDevice(device_name, device_description)
        assert isinstance(device, SimpleIOTDevice)
        assert device.name == device_name
        assert device.description == device_description

    def test_device_making_measurement_returns_non_empty_dictionary(self, simple_test_device):
        device = simple_test_device
        m = device.make_measurement()
        assert isinstance(m, dict)
        assert m

    def test_device_measurement_data(self, simple_test_device):
        device = simple_test_device
        m = device.make_measurement()
        for v in m.values():
            if not isinstance(v, str):
                assert v > 0
