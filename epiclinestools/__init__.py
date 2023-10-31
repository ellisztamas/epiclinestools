"""Top-level package for epiclinestools."""

__author__ = """Tom Ellis"""
__email__ = 'thomas.ellis@gmi.oeaw.ac.at'
__version__ = '0.4.3'

import argparse

from epiclinestools.align_fastq_with_plate_positions import align_fastq_with_plate_positions
from epiclinestools.CytosineCoverageFile import CytosineCoverageFile
from epiclinestools.BismarkSam import *
