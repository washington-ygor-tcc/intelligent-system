import unittest

from unittest.mock import Mock
from src.core.use_cases.predict_use_case import PredictUseCase
from src.core.ports.model_gateway_port import ModelGatewayPort


class TestPredictUseCase(unittest.TestCase):
    def test_handle(self):
        model_gateway_port_mock = Mock(spec=ModelGatewayPort)
        predict_use_case = PredictUseCase(model_gateway_port_mock)
        features = {"age": 26, "smoke": "no"}

        model_gateway_port_mock.predict.return_value = "yes"

        prediction = predict_use_case.handle(features)

        model_gateway_port_mock.predict.assert_called_once_with(features)
        self.assertEqual(prediction, "yes")


if __name__ == "__main__":
    unittest.main()
