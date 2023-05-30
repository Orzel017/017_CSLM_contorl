<p>
<center>
  ______         __                    _ 
  | ___ \       / _|                  | |
  | |_/ /_   _ | |_  ___    ___  __ _ | |
  |  __/| | | ||  _|/ _ \  / __|/ _` || |
  | |   | |_| || | | (_) || (__| (_| || |
  \_|    \__, ||_|  \___/  \___|\__,_||_|
          __/ |                          
         |___/                           
  </center>
</p>

<!--<div align = "center">
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)</div>-->

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/mdbackerman/StrapDown.js/graphs/commit-activity)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![GitHub Contributors Image](https://contrib.rocks/image?repo=mdbackerman/017_CSLM_control)
[![GitHub contributors](https://img.shields.io/github/contributors/mdbackerman/badges.svg)](https://GitHub.com/mdbackerman/badges/graphs/contributors/)
[![GitHub issues](https://badgen.net/github/issues/mdbackerman/Strapdown.js/)](https://GitHub.com/mdbackerman/StrapDown.js/issues/)
[![GitHub branches](https://badgen.net/github/branches/mdbackerman/Strapdown.js)](https://github.com/mdbackrman/Strapdown.js/)
[![GitHub commits](https://badgen.net/github/commits/mdbackerman/Strapdown.js)](https://GitHub.com/mdbackerman/StrapDown.js/commit/)

## About

Pyfocal is an open source software package for controlling a confocal laser-scanning microscope (CSLM).

This repository is built from [this repository](https://github.com/mdbackerman/Quantum_optics_control), an original software package to control a CSLM built for the Lukin Group at Harvard University.

This code currently runs an analogous setup in the Orzel Group at Union College.

## How it Works

1. This software uses the National Instruments ([NI-DAQmx](https://nidaqmx-python.readthedocs.io/en/latest/)) API to interface for hardware control. Additional hardware control will be implemented using ThorLab's APIs.
2. A GUI is displayed to allow simple user-control
3. Laser light to sample, emitted light collected. Galvo steers beam

## License

This code is available under the [GNU General Public License v 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) (source [file](https://www.gnu.org/licenses/gpl-3.0.en.html) in GitHub)
