# Prebuilt Wheels for Mac
Including pre-built build wheels for Mac OS is a temporary patch because tksvg is broken and relies on some windows
dependencies.

See:  https://github.com/mcha-forks/python-tksvg/actions/runs/8101063696

Issue is here.  Cannot install tksvg on a mac or linux with pip:
https://github.com/TkinterEP/python-tksvg/pull/6


# Install with Pip
For those on Mac OS, try installing the file corresponding to your Python version.
e.g.
pip install "...path/to/cibw-wheels-macos14-4/tksvg-0.14.0-cp311-cp311-macosx_11_0_arm64.whl"

