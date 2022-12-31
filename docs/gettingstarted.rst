Getting Started with planetscope
=====================================================


The planetscope package is a tool for reading, plotting, and processing data from the PlanetScope satellite imaging system. It is available on PyPI and can be installed using pip.

Installation
=====================================================

To install the latest version of planetscope from PyPI, use the following command:

.. code-block:: bash

    pip install planetscope



Alternatively, you can install the package from the source code by cloning the Git repository and using pip to install it in editable mode:


.. code-block:: bash

    git clone https://github.com/NASA-IMPACT/planet_utils
    cd planetscope
    python3 setup.py install
    cd ..
  


The PlanetScope package can be installed with pip directly from the github:

.. code-block:: bash

    pip install git+https://github.com/NASA-IMPACT/planet_utils




Dependencies
=====================================================

The planetscope package has the following dependencies:

*    NumPy
*    GDAL
*    Matplotlib
*    Scikit-learn (optional, for generating training data)

These dependencies will be installed automatically when you install the planetscope package using pip.
 
Usage
=====================================================

Here is a simple example of how to use the planetscope package to read and plot a PlanetScope image:

.. code-block:: python

    import planetscope as ps
    #Read in the image data
    data, metadata = ps.read("path/to/image.tif")
    #Plot the image
    ps.plot(data)

For more information on the available functions and how to use them, see the documentation for each module in the package:

    :mod:planetscope.reader: functions for reading and parsing the raw data files.
    :mod:planetscope.plotter: functions for generating plots and maps from the data.
    :mod:planetscope.processor: functions for processing the data, such as image cropping, resampling, and band math.
    :mod:planetscope.training_data: functions for generating training data for machine learning algorithms.

Support
=====================================================

If you have any questions or encounter any issues while using the planetscope package, please file an issue on the package's GitHub repository: https://github.com/NASA-IMPACT/planet_utils/issues.


