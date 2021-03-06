#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketShopModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketShopModifyResponse, self).__init__()
        self._apply_id = None
        self._audit_desc = None
        self._audit_status = None
        self._is_online = None
        self._is_show = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def audit_desc(self):
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, value):
        self._audit_desc = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def is_show(self):
        return self._is_show

    @is_show.setter
    def is_show(self, value):
        self._is_show = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketShopModifyResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'audit_desc' in response:
            self.audit_desc = response['audit_desc']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'is_online' in response:
            self.is_online = response['is_online']
        if 'is_show' in response:
            self.is_show = response['is_show']
