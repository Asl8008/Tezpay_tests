#!/bin/bash

# Default values
DEVICE_NAME=${DEVICE_NAME:-"Android Emulator"}
PLATFORM_NAME=${PLATFORM_NAME:-"Android"}
AUTOMATION_NAME=${AUTOMATION_NAME:-"UiAutomator2"}
APP_PACKAGE=${APP_PACKAGE:-"pro.tezpay.app"}
APP_ACTIVITY=${APP_ACTIVITY:-".MainActivity"}
APPIUM_SERVER_URL=${APPIUM_SERVER_URL:-"http://127.0.0.1:4723"}
NO_RESET=${NO_RESET:-"True"}

echo "Running tests with configuration:"
echo "--------------------------------"
echo "DEVICE_NAME: $DEVICE_NAME"
echo "PLATFORM_NAME: $PLATFORM_NAME"
echo "APP_PACKAGE: $APP_PACKAGE"
echo "APPIUM_SERVER_URL: $APPIUM_SERVER_URL"
echo "--------------------------------"

# Export variables so Python picks them up
export DEVICE_NAME
export PLATFORM_NAME
export AUTOMATION_NAME
export APP_PACKAGE
export APP_ACTIVITY
export APPIUM_SERVER_URL
export NO_RESET
export APP_PATH

# Run pytest
pytest "$@"
