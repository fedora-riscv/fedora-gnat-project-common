# Make the host platform available to GNAT project files, as they don't have a
# shell-out feature.
setenv HARDWARE_PLATFORM `uname -m`
