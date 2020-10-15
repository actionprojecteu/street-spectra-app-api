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


class UserRanking(object):
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
        'order': 'float',
        'user_data': 'UserData'
    }

    attribute_map = {
        'order': 'order',
        'user_data': 'user_data'
    }

    def __init__(self, order=None, user_data=None):  # noqa: E501
        """UserRanking - a model defined in Swagger"""  # noqa: E501

        self._order = None
        self._user_data = None
        self.discriminator = None

        if order is not None:
            self.order = order
        if user_data is not None:
            self.user_data = user_data

    @property
    def order(self):
        """Gets the order of this UserRanking.  # noqa: E501

        Ranking order  # noqa: E501

        :return: The order of this UserRanking.  # noqa: E501
        :rtype: float
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this UserRanking.

        Ranking order  # noqa: E501

        :param order: The order of this UserRanking.  # noqa: E501
        :type: float
        """

        self._order = order

    @property
    def user_data(self):
        """Gets the user_data of this UserRanking.  # noqa: E501


        :return: The user_data of this UserRanking.  # noqa: E501
        :rtype: UserData
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this UserRanking.


        :param user_data: The user_data of this UserRanking.  # noqa: E501
        :type: UserData
        """

        self._user_data = user_data

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
        if issubclass(UserRanking, dict):
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
        if not isinstance(other, UserRanking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other