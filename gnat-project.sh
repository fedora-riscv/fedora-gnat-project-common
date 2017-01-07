# Make the host platform available to GNAT project files, as they don't have a
# shell-out feature.
HARDWARE_PLATFORM=`uname -i`
export HARDWARE_PLATFORM
