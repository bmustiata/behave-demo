from behave import *
import os
import shutil
import subprocess
import unittest
import re

use_step_matcher("re")

test = unittest.TestCase()
assertEquals = test.assertEqual
assertTrue = test.assertTrue


@given(u'I have a copy of my test folder')
def copy_test_folder(context):
    shutil.rmtree("/tmp/test-site", ignore_errors=True)
    shutil.copytree("features/test-site", "/tmp/test-site")
    os.chdir("/tmp/test-site")


@when(u'I execute \'(.*?)\'')
def step_impl(context, command: str):
    command_output = subprocess.check_output(command.split(" ")) # type: bytes
    context.command_output = command_output.decode("utf-8").strip()


@then(u'\'(.*?)\' is in the test folder')
def step_impl(context, file_name: str):
    assertTrue(file_name in context.command_output)


@then(u'\'(.*?)\' is not in the test folder')
def step_impl(context, file_name: str):
    assertTrue(file_name not in context.command_output)


@then(u'I get as output \'(.*?)\'')
def step_impl(context, expected_output: str):
    assertEquals(expected_output, context.command_output)

@step(u'I get the full listing of \'(.*?)\' including attributes')
def step_impl(context, file_name: str):
    TEST_RE = re.compile(r'^-rw-rw-r-- 1 \S+ \S+ 0 \S+ \d+ \d+:\d+ %s$' % file_name)
    assertTrue(TEST_RE.match(context.command_output))
