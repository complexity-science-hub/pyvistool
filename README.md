<!-- ABOUT THE PROJECT -->
## About The Project

The pyvistool library is a Python package to create various visualizations offered by the [VisTool](https://vis.csh.ac.at/vistool) of the [Complexity Science Hub Vienna](https://www.csh.ac.at) directly from your Python script.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/complexity-science-hub/pyvistool
   ```
1. Change to the repository directory
   ```sh
   cd pyvistool
   ```
1. Build the package
   ```sh
   python setup.py build
   ```
1. Install the package
   ```sh
   python setup.py install
   ```

<!-- USAGE EXAMPLES -->
## Usage

To use the package, import it to your python script.

   ```py
    from pyvistool import Vistool
   ```

You can find a list of available visualization and information about how to configure them [here](readme/apps.md):

Create a configuration for the visualization you want to use:

   <pre>
    config = {
        "datasets": {
            "<i>nameOfDataset</i>": {
                "options": {
                    ...
                },
                "data": {
                    ...
                }
            }
        },
        "settings": {
            ...
        }
    }
   </pre>
Create and show the visualization ([replace the appId](readme/apps.md)):

   <pre>
    vt = Vistool(<b>appId</b>, config)
    vt.show()
   </pre>

<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information. -->

<!-- CONTACT -->
## Contact

Johannes Sorger - sorger@csh.ac.at<br>
Wolfgang Knecht - knecht@csh.ac.at

Project Link: [https://github.com/complexity-science-hub/pyvistool](https://github.com/complexity-science-hub/pyvistool)