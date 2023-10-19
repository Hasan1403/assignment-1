import otp1 as otp
import pytest
import unittest
from otp1 import ValidateEmailID, GenerateOTP, sendOTPOverEmail


class TestProgramFunctions(unittest.TestCase):

    def test_validate_email(self):

        result = ValidateEmailID("jahirhasankureshi@gmail.com")
        expected = True
        self.assertEqual(result, expected)

        result = ValidateEmailID("naikatharva111@gmail.com")
        expected = True
        self.assertEqual(result, expected)

    def test_generate_otp(self):
        otp = GenerateOTP()
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())


if __name__ == '_main_':
  pytest.main()