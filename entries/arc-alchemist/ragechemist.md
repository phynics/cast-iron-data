+++
id = "ref/arc-alchemist/ragechemist"
kind = "archetype"
title = "Ragechemist"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ragechemist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "archetype"
replaces = ["Poison use", "Swift poisoning", "Poison immunity"]
+++

**Sources:** Ultimate Combat pg 25\
Some alchemists create mutagens that tap into a primal anger that fuels their physical
transformation. These alchemists have little control over their altered selves.

**Rage Mutagen**

**Ability:** Whenever a ragechemist creates a mutagen that improves his Strength, that mutagen's
bonus to Strength increases by +2 and penalizes the alchemist's Intelligence score.

**Gained:** At 2nd Level

**Passive:** While under the effects of this mutagen, whenever the alchemist takes damage, his rage
grows, with detrimental effects. At the end of each turn that he takes hit point damage, the
ragechemist must succeed at a Will saving throw (DC 15, or DC 20 if any of the damage came from a
critical hit that turn) or take a -2 penalty on Will saving throws and to Intelligence. These
penalties end 1 hour after the mutagen ends and stack with themselves.

**Replaces:** Poison use

**Special:** If the penalty lowers the ragechemist's Intelligence score to 0, the ragechemist is
comatose until 1 hour after the mutagen expires.

**Sturdy Rage**

**Gained:** At 6th Level

**Passive:** Whenever a ragechemist uses his rage mutagen, he also gains a +4 bonus to natural
armor, but the penalty on Will saving throws and to Intelligence for taking damage increases to -4.

**Replaces:** Swift poisoning

**Lumbering Rage**

**Ability:** Whenever a ragechemist uses his rage mutagen ability, he may have the mutagen also give
him a +2 morale bonus to Constitution, but when he takes a penalty on Will saving throws and to
Intelligence, he also takes a -1 penalty to Dexterity.

**Gained:** At 10th Level

**Replaces:** Poison immunity

**Discoveries:** The following discoveries complement the ragechemist:
[feral mutagen](ref/discovery/feral-mutagen), [grand mutagen](ref/discovery/grand-mutagen),
[greater mutagen](ref/discovery/greater-mutagen), [infuse mutagen](ref/discovery/infuse-mutagen),
[tentacle](ref/discovery/tentacle), and [vestigial arm](ref/discovery/vestigial-arm).
