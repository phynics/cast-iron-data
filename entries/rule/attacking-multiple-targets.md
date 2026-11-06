+++
id = "ref/rule/attacking-multiple-targets"
kind = "rule"
title = "Attacking Multiple Targets"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "attacking_multiple_targets", path = "json/rules_opt_combat01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 110

If you have more than one maximum hit, you can declare you're making a full attack against more than
one target. In that case, your number of hits is determined by the highest AC among your targets,
and you can allocate your hits however you like among all the targets after determining your total
number of hits - you can even choose not to hit the target whose AC you rolled against. This doesn't
allow you to bypass effects that would prevent you from hitting a creature normally. For instance,
you couldn't assign a hit to a creature under a [sanctuary](ref/spell/sanctuary) effect when making
an attack roll against a different creature (unless you first succeeded on the required Will save).
