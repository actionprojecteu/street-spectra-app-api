# coding: utf-8

"""
    StreetSpectra API

    API description for StreetSpectra project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: jgcasta@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Login(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'username': 'str',
        '_pass': 'str'
    }

    attribute_map = {
        'username': 'username',
        '_pass': 'pass'
    }

    def __init__(self, username=None, _pass=None):  # noqa: E501
        """Login - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self.__pass = None
        self.discriminator = None

        self.username = username
        self._pass = _pass

    @property
    def username(self):
        """Gets the username of this Login.  # noqa: E501

        Username  # noqa: E501

        :return: The username of this Login.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Login.

        Username  # noqa: E501

        :param username: The username of this Login.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def _pass(self):
        """Gets the _pass of this Login.  # noqa: E501

        Password  # noqa: E501

        :return: The _pass of this Login.  # noqa: E501
        :rtype: str
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """Sets the _pass of this Login.

        Password  # noqa: E501

        :param _pass: The _pass of this Login.  # noqa: E501
        :type: str
        """
        if _pass is None:
            raise ValueError("Invalid value for `_pass`, must not be `None`")  # noqa: E501

        self.__pass = _pass

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Login, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Login):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other