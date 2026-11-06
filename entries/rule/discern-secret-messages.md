+++
id = "ref/rule/discern-secret-messages"
kind = "rule"
title = "Discern Secret Messages"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "discern_secret_messages", path = "json/rules_opt_skills01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 61

You can use Perception to detect that a secret message is being transmitted by someone using the
Influence skill. Your Perception check is opposed by the sender's Influence check. You take a -2
penalty for each piece of information you lack relating to the message. If you succeed by 4 or less,
you know there's a hidden message but don't know its content. If you exceed the DC by 5 or more, you
intercept and understand the message. If you fail by 4 or less, you don't detect any hidden
communication. If you fail by 5 or more, you might infer false information. See the
[pass secret message](ref/rule/pass-secret-messages) function of Influence for rules on sending a
secret message.

**Action:** None. This function is included in the time spent receiving the message.

**Try Again:** No, though you can attempt a check against another hidden message.
