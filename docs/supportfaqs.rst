
Support
=====================================================


If you have any questions or encounter any issues while using the planetscope package, there are several ways you can get help:

*    Consult the documentation: The documentation for the planetscope package should provide detailed information on how to use the package and troubleshoot common issues. You can find the documentation at https://github.com/NASA-IMPACT/planet_utils/.
*    Check the FAQs: We have compiled a list of common questions and issues that users may encounter while using the planetscope package. You can find the FAQs at https://docs.planetscope.org/faqs/.
*    File an issue on GitHub: If you are unable to find a solution to your issue in the documentation or FAQs, you can file an issue on the package's GitHub repository at https://github.com/NASA-IMPACT/planet_utils/issues. When filing an issue, please include as much information as possible, such as the version of the package you are using, the Python version you are using, and any error messages you are seeing.
*    Contact the maintainers: If you have a question or issue that is not covered in the documentation or FAQs, or if you would like to request a new feature, you can contact the maintainers of the planetscope package by emailing support@planetscope.org.

We strive to provide timely and helpful support for the planetscope package and appreciate your feedback and contributions.


FAQs
=====================================================

This section covers some common questions and issues that users may encounter while using the planetscope package.
Error while loading data

Q: I am getting an error when trying to load a PlanetScope image file using the read function. What could be causing this?

There are a few possible reasons why you may encounter an error when trying to load a PlanetScope image file:

*    The file path is incorrect or the file does not exist. Make sure that you are providing the correct path to the image file and that the file exists on your system.
*    The file is not in a supported format. The planetscope package can only read TIFF files. If you are trying to load a file in a different format, you will need to convert it to TIFF first.
*    The file is damaged or corrupt. If the file has been damaged or is otherwise not readable, you may get an error when trying to load it.

To troubleshoot the error, you can try the following:

*    Check the file path and make sure that it is correct and that the file exists on your system.
*    Check the file format and make sure that it is a TIFF file.
*    Try opening the file with another tool, such as a TIFF viewer or editor, to see if it is readable.

If you are still unable to load the file after trying these steps, you may need to try a different file or contact support for further assistance.


Q: How do I generate training data from a PlanetScope image using the planetscope package?

To generate training data from a PlanetScope image using the planetscope package, you can use the following steps:

    Load the image data using the read function.
    Extract the data for the feature(s) you want to use for training. For example, you might use the extract_land_cover function to extract land cover types from the image.
    Format the data as training data using the format_training_data function. This function expects a 2D array of data and will return X and y arrays suitable for use with a machine learning model.

Here is an example of how to generate training data for land cover classification using the planetscope package:

.. code-block:: python

   import planetscope as ps
   #Read in the image data
   data, metadata = ps.read("path/to/image.tif")
   #Extract land cover types
   land_cover = ps.extract_land_cover(data)
   #Format as training data
   X, y = ps.format_training_data(land_cover)

For more information on generating training data with the planetscope package, see the documentation for the :mod:planetscope.training_data module.



