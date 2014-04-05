# Copyright 2013, Benjamin Chretien, CNRS-LIRMM
#
# This file is part of roboptim-analysis.
# roboptim-core is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# roboptim-analysis is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# roboptim-analysis.  If not, see <http://www.gnu.org/licenses/>.

# Requires at least CMake 2.6 to configure the package.
CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

INCLUDE(cmake/base.cmake)
INCLUDE(cmake/python.cmake)

SET(PROJECT_NAME roboptim-analysis)
SET(PROJECT_DESCRIPTION "RobOptim Analysis")
SET(PROJECT_URL "http://github.com/roboptim/roboptim-analysis")

SET(HEADERS
  )

SETUP_PROJECT()

# Search for dependencies.
ADD_REQUIRED_DEPENDENCY("roboptim-core >= 0.5")
ADD_REQUIRED_DEPENDENCY("roboptim-core-python")

# Look for Python 2.7
SET(Python_ADDITIONAL_VERSIONS 2.7)
FINDPYTHON()

# Detect numpy.
EXECUTE_PROCESS(
  COMMAND "${PYTHON_EXECUTABLE}" "-c"
  "import numpy; print (numpy.get_include())"
  OUTPUT_VARIABLE NUMPY_INCLUDE_DIRS
  ERROR_QUIET)

HEADER_INSTALL("${HEADERS}")

INSTALL(FILES
  bin/capsule_display
  bin/distance_to_sphere
  bin/log_to_yaml
  bin/plot_csv
  DESTINATION ${CMAKE_INSTALL_BINDIR})

ADD_SUBDIRECTORY(tests)

SETUP_PROJECT_FINALIZE()
