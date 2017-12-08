# -*- coding: utf-8 -*-
__author__ = 129
__date__ = 2017 / 11 / 14

_MAX_LENGTH = 80


def safe_repr(obj, short=False):
    try:
        result = repr(obj)
    except Exception:
        result = object.__repr__(obj)
    if not short or len(result) < _MAX_LENGTH:
        return result
    return result[:_MAX_LENGTH] + ' [truncated]...'


# Define an exception of our own, which means failure of test case
class AssertFail(Exception):
    pass


class TestCase():
    def _formatMessage(self, msg, standardMsg):
        if msg is None:
            return standardMsg
        else:
            return '%s : %s' % (standardMsg, msg)

    def fail(self, msg):
        raise AssertFail(msg)

    def assertIn(self, member, container, msg=None):
        """Just like self.assertTrue(a in b), but with a nicer default message."""
        if member not in container:
            standardMsg = '【%s】 not found in 【%s】' % (safe_repr(member), safe_repr(container))
            self.fail(self._formatMessage(msg, standardMsg))
        else:
            info = '【%s】is expected found in【%s】' % (safe_repr(member), safe_repr(container))
            print(self._formatMessage(msg, info))

    def assertNotIn(self, member, container, msg=None):
        """Just like self.assertTrue(a not in b), but with a nicer default message."""
        if member in container:
            standardMsg = '【%s】 unexpectedly found in 【%s】' % (safe_repr(member), safe_repr(container))
            self.fail(self._formatMessage(msg, standardMsg))
        else:
            info = '【%s】expected not found in【%s】' % (safe_repr(member), safe_repr(container))
            print(self._formatMessage(msg, info))

    def assertEqual(self, first, second, msg=None):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        if not first == second:
            standardMsg = '【%s】 != 【%s】' % (safe_repr(first), safe_repr(second))
            self.fail(self._formatMessage(msg, standardMsg))
        else:
            info = '【%s】is expected equal to【%s】' % (safe_repr(first), safe_repr(second))
            print(self._formatMessage(msg, info))

    def assertNotEqual(self, first, second, msg=None):
        """Fail if the two objects are equal as determined by the '!='
           operator.
        """
        if not first != second:
            standardMsg = '【%s】 == 【%s】' % (safe_repr(first), safe_repr(second))
            self.fail(self._formatMessage(msg, standardMsg))
        else:
            info = '【%s】is expected not equal to【%s】' % (safe_repr(first), safe_repr(second))
            print(self._formatMessage(msg, info))

    def assertTrue(self, expr, msg=None):
        """Check that the expression is true."""
        if not expr:
            self.fail(self._formatMessage(msg, "【%s】 is not true" % safe_repr(expr)))
        else:
            print(self._formatMessage(msg, "【%s】 is expected true" % safe_repr(expr)))

    def assertFalse(self, expr, msg=None):
        """Check that the expression is false."""
        if expr:
            self.fail(self._formatMessage(msg, "【%s】 is not false" % safe_repr(expr)))
        else:
            print(self._formatMessage(msg, "【%s】 is expected false" % safe_repr(expr)))

    def assertGreatThan(self, first, second, msg=None):
        """Check first is great than second """
        if not first > second:
            standardMsg = '【%s】 <= 【%s】' % (safe_repr(first), safe_repr(second))
            self.fail(self._formatMessage(msg, standardMsg))
        else:
            info = '【%s】is expected great than【%s】' % (safe_repr(first), safe_repr(second))
            print(self._formatMessage(msg, info))

    def assertNotGreatThan(self, first, second, msg=None):
        """Check first is great than second """
        if not first < second:
            standardMsg = '【%s】 >= 【%s】' % (safe_repr(first), safe_repr(second))
            self.fail(self._formatMessage(msg, standardMsg))
        else:
            info = '【%s】is expected great than【%s】' % (safe_repr(first), safe_repr(second))
            print(self._formatMessage(msg, info))

    def assertNoneOrEmpty(self, item, msg=None):
        if not item or item.strip() != '':
            self.fail(self._formatMessage(msg, "【%s】 is not None or Empty" % safe_repr(item)))
        else:
            print(self._formatMessage(msg, "【%s】 is expected to None or Empty" % safe_repr(item)))

    def assertNotNoneOrNotEmpty(self, item, msg=None):
        if not item or item.strip() == '':
            self.fail(self._formatMessage(msg, "【%s】 is None or Empty" % safe_repr(item)))
        else:
            print(self._formatMessage(msg, "【%s】 is expected not None or not Empty" % safe_repr(item)))