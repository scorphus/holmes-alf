#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mock import Mock, patch
from preggy import expect
from unittest import TestCase

from holmesalf import BaseAuthNZWrapper
from holmesalf import AlfAuthNZWrapper


class TestBaseAuthNZWrapper(TestCase):
    def test_raises_on_new_instance(self):
        try:
            BaseAuthNZWrapper(config=Mock())
        except NotImplementedError:
            pass
        else:
            assert False, "Should not have gotten this far"


class TestAlfAuthNZWrapper(TestCase):
    def setUp(self):
        super(TestAlfAuthNZWrapper, self).setUp()

        self.config = {
            'OAUTH_TOKEN_ENDPOINT': 'ENDPOINT',
            'OAUTH_CLIENT_ID': 'ID',
            'OAUTH_CLIENT_SECRET': 'SECRET'
        }

    def test_instantiates_with_config(self):
        config = Mock()

        wrapper = AlfAuthNZWrapper(config=config)

        expect(wrapper.config).to_equal(config)
        expect(wrapper._sync_client).to_be_null()
        expect(wrapper._async_client).to_be_null()

    @patch('holmesalf.AlfSyncClient')
    def test_instantiates_sync_client(self, alf_sync_cli_mock):
        wrapper = AlfAuthNZWrapper(config=self.config)

        expect(wrapper.config).to_equal(self.config)
        expect(alf_sync_cli_mock.call_count).to_equal(0)
        expect(wrapper._sync_client).to_be_null()

        sync_cli = wrapper.sync_client

        expect(alf_sync_cli_mock.call_count).to_equal(1)
        expect(wrapper._sync_client).not_to_be_null()
        expect(wrapper._sync_client).to_equal(sync_cli)

    @patch('holmesalf.AlfSyncClient')
    def test_does_not_reinstantiate_sync_client(self, alf_sync_cli_mock):
        wrapper = AlfAuthNZWrapper(config=self.config)

        expect(wrapper.config).to_equal(self.config)
        expect(alf_sync_cli_mock.call_count).to_equal(0)
        expect(wrapper._sync_client).to_be_null()

        sync_cli = wrapper.sync_client

        expect(alf_sync_cli_mock.call_count).to_equal(1)
        expect(wrapper._sync_client).not_to_be_null()
        expect(wrapper._sync_client).to_equal(sync_cli)

        sync_cli = wrapper.sync_client

        expect(alf_sync_cli_mock.call_count).to_equal(1)
        expect(wrapper._sync_client).not_to_be_null()
        expect(wrapper._sync_client).to_equal(sync_cli)

    @patch('holmesalf.AlfAsyncClient')
    def test_instantiates_async_client(self, alf_async_cli_mock):
        wrapper = AlfAuthNZWrapper(config=self.config)

        expect(wrapper.config).to_equal(self.config)
        expect(alf_async_cli_mock.call_count).to_equal(0)
        expect(wrapper._async_client).to_be_null()

        async_cli = wrapper.async_client

        expect(alf_async_cli_mock.call_count).to_equal(1)
        expect(wrapper._async_client).not_to_be_null()
        expect(wrapper._async_client).to_equal(async_cli)

    @patch('holmesalf.AlfAsyncClient')
    def test_does_not_reinstantiate_async_client(self, alf_async_cli_mock):
        wrapper = AlfAuthNZWrapper(config=self.config)

        expect(wrapper.config).to_equal(self.config)
        expect(alf_async_cli_mock.call_count).to_equal(0)
        expect(wrapper._async_client).to_be_null()

        async_cli = wrapper.async_client

        expect(alf_async_cli_mock.call_count).to_equal(1)
        expect(wrapper._async_client).not_to_be_null()
        expect(wrapper._async_client).to_equal(async_cli)

        async_cli = wrapper.async_client

        expect(alf_async_cli_mock.call_count).to_equal(1)
        expect(wrapper._async_client).not_to_be_null()
        expect(wrapper._async_client).to_equal(async_cli)
