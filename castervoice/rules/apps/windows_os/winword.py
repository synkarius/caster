from dragonfly import Dictation, MappingRule
from castervoice.lib.actions import Key
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.merge.state.short import R


class MSWordRule(MappingRule):
    mapping = {
        "insert image": R(Key("alt, n, p")),
    }
    extras = [
        Dictation("dict"),
        IntegerRefST("n", 1, 100),
    ]
    defaults = {"n": 1, "dict": "nothing"}


def get_rule():
    details = RuleDetails(name="Microsoft Word", executable="winword")
    return MSWordRule, details
