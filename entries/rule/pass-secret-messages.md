+++
id = "ref/rule/pass-secret-messages"
kind = "rule"
title = "Pass Secret Messages"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pass_secret_messages", path = "json/rules_opt_skills01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 60

You can use innuendo to pass a hidden message to another character. If you succeed, the target
automatically understands you if you're communicating in a language it understands. If you fail by 5
or more, you deliver the wrong message. Other creatures that receive the message can decipher it by
succeeding at opposed Perception checks to [sense motive](ref/rule/sense-motive) against your
result. See the discern secret message function of [Perception](ref/skill/perception) to determine
when a secret message is intercepted.

|Secret Message|Influence DC|
| --- | --- |
|Simple message|15|
|Complex message|20|

**Action:** Twice as long as it would take to convey the message normally.

**Try Again:** Yes.
