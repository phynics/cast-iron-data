+++
id = "ref/arc-alchemist/ragechemist"
kind = "archetype"
title = "Ragechemist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Ragechemist"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ragechemist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-combat"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "rage-mutagen", level = 2 },
  { anchor = "sturdy-rage", level = 6 },
  { anchor = "lumbering-rage", level = 10 },
]
trades = [
  { replaces = "Poison use", feature = "poison-use", by = ["rage-mutagen"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["sturdy-rage"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["lumbering-rage"] },
]
+++

Some alchemists create mutagens that tap into a primal anger that fuels their physical
transformation. These alchemists have little control over their altered selves.

## Rage Mutagen {#rage-mutagen}

At 2nd level, whenever a ragechemist creates a mutagen that improves his Strength, that mutagen's
bonus to Strength increases by 2 and penalizes the alchemist's Intelligence score. Furthermore,
while under the effects of this mutagen, whenever the alchemist takes damage, his rage grows, with
detrimental effects. At the end of each turn that he takes hit point damage, the ragechemist must
succeed at a Will saving throw (DC 15, or DC 20 if any of the damage came from a critical hit that
turn) or take a -2 penalty on Will saving throws and to Intelligence. These penalties end 1 hour
after the mutagen ends and stack with themselves. If the penalty lowers the ragechemist's
Intelligence score to 0, the ragechemist is comatose until 1 hour after the mutagen expires. This
ability replaces poison use.

## Sturdy Rage {#sturdy-rage}

At 6th level, whenever a ragechemist uses his rage mutagen, he also gains a +4 bonus to natural
armor, but the penalty on Will saving throws and to Intelligence for taking damage increases to -4.
This ability replaces swift poisoning.

## Lumbering Rage {#lumbering-rage}

At 10th level, whenever a ragechemist uses his rage mutagen ability, he may have the mutagen also
give him a +2 morale bonus to Constitution, but when he takes a penalty on Will saving throws and to
Intelligence, he also takes a -1 penalty to Dexterity. This ability replaces poison immunity.

## Discoveries {#discoveries}

The following discoveries complement the ragechemist: [feral mutagen](ref/discovery/feral-mutagen),
[grand mutagen](ref/discovery/grand-mutagen), [greater mutagen](ref/discovery/greater-mutagen),
[infuse mutagen](ref/discovery/infuse-mutagen), [tentacle](ref/discovery/tentacle)\*, and
[vestigial arm](ref/discovery/vestigial-arm)\*.
