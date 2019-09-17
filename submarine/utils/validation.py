"""
Utilities for validating user inputs such as metric names and parameter names.
"""
import numbers
import re
from submarine.exceptions import SubmarineException
from submarine.store.database.db_types import DATABASE_ENGINES

_VALID_PARAM_AND_METRIC_NAMES = re.compile(r"^[/\w.\- ]*$")

MAX_ENTITY_KEY_LENGTH = 250
MAX_PARAM_VAL_LENGTH = 250


_BAD_CHARACTERS_MESSAGE = (
    "Names may only contain alphanumerics, underscores (_), dashes (-), periods (.),"
    " spaces ( ), and slashes (/)."
)

_UNSUPPORTED_DB_TYPE_MSG = "Supported database engines are {%s}" % ', '.join(DATABASE_ENGINES)


def _validate_param_name(name):
    """Check that `name` is a valid parameter name and raise an exception if it isn't."""
    if not _VALID_PARAM_AND_METRIC_NAMES.match(name):
        raise SubmarineException("Invalid parameter name: '%s'. %s" % (name, _BAD_CHARACTERS_MESSAGE),)


def _validate_metric_name(name):
    """Check that `name` is a valid metric name and raise an exception if it isn't."""
    if not _VALID_PARAM_AND_METRIC_NAMES.match(name):
        raise SubmarineException("Invalid metric name: '%s'. %s" % (name, _BAD_CHARACTERS_MESSAGE),)


def _validate_length_limit(entity_name, limit, value):
    if len(value) > limit:
        raise SubmarineException(
            "%s '%s' had length %s, which exceeded length limit of %s" %
            (entity_name, value[:250], len(value), limit))


def validate_metric(key, value, timestamp, step):
    """
    Check that a param with the specified key, value, timestamp is valid and raise an exception if
    it isn't.
    """
    _validate_metric_name(key)
    if not isinstance(value, numbers.Number):
        raise SubmarineException(
            "Got invalid value %s for metric '%s' (timestamp=%s). Please specify value as a valid "
            "double (64-bit floating point)" % (value, key, timestamp),)

    if not isinstance(timestamp, numbers.Number) or timestamp < 0:
        raise SubmarineException(
            "Got invalid timestamp %s for metric '%s' (value=%s). Timestamp must be a nonnegative "
            "long (64-bit integer) " % (timestamp, key, value),)

    if not isinstance(step, numbers.Number):
        raise SubmarineException(
            "Got invalid step %s for metric '%s' (value=%s). Step must be a valid long "
            "(64-bit integer)." % (step, key, value),)


def validate_param(key, value):
    """
    Check that a param with the specified key & value is valid and raise an exception if it
    isn't.
    """
    _validate_param_name(key)
    _validate_length_limit("Param key", MAX_ENTITY_KEY_LENGTH, key)
    _validate_length_limit("Param value", MAX_PARAM_VAL_LENGTH, str(value))
