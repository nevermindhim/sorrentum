#!/usr/bin/env bash

set -e

MOUNT_POINT="/fsx/research"
if [ "$(mount | grep -c $MOUNT_POINT)" -lt 1 ]; then
  echo -e """\e[93mWARNING\e[0m: $MOUNT_POINT not mounted."""
fi