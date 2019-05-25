import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Use regex python named capture groups:
# (?P<group_name>regex)
DURATION_FMT_EXTRACT = re.compile("(?:(?P<h>\d+)h)?\s*(?:(?P<m>\d+)m)?")
# Use .format syntax:
# {group_name}
DURATION_FMT = "{h}h {m}m"
