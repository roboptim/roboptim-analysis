INCLUDE_DIRECTORIES(SYSTEM ${PYTHON_INCLUDE_PATH})
INCLUDE_DIRECTORIES(SYSTEM ${NUMPY_INCLUDE_DIRS})

PYTHON_INSTALL_ON_SITE(roboptim/analysis __init__.py)
PYTHON_INSTALL_ON_SITE(roboptim/analysis distance_to_sphere.py)
PYTHON_INSTALL_ON_SITE(roboptim/analysis log_to_yaml.py)
PYTHON_INSTALL_ON_SITE(roboptim/analysis plot_csv.py)
