+++
id = "ref/arc-oracle/warsighted"
kind = "archetype"
title = "Warsighted"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Warsighted"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "warsighted", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "advanced-class-guide"
page = "106"

[fields]
kind = "archetype"
features = [
  { anchor = "martial-flexibility", level = 1 },
]
trades = [
  { replaces = "Revelations gained at 1st, 7th, 11th, and 15th levels", feature = "revelation", levels = [1, 7, 11, 15], by = ["martial-flexibility"] },
]
+++

A warsighted's unique gifts are not in strange magical revelations, but in her ability to adapt in
the midst of a battle with new fighting techniques. The warsighted is a master of combat, as
dedicated as a fighter and as flexible as a brawler.

## Martial Flexibility (Ex) {#martial-flexibility}

At 1st level, a warsighted can use a move action to gain the benefit of a combat feat she doesn't
possess. This effect lasts for 1 minute. The warsighted must otherwise meet all the feat's
prerequisites. She can use this ability a number of times per day equal to 3 + 1/2 her oracle level.

The warsighted can use this ability again before the duration expires in order to replace the
previous combat feat with another choice.

If a combat feat has a daily use limitation (for example, [Stunning Fist](ref/feat/stunning-fist)),
any uses of that combat feat while using this ability count toward that feat's daily limit. At later
levels, when she gains multiple feats through this ability, she can use those feats to meet the
prerequisites of other feats she gains with this ability. Doing so means that she cannot replace a
feat currently fulfilling another's prerequisite without also replacing those feats that require it.
Each individual feat selected counts toward her daily uses of this ability.

At 7th level, a warsighted can use this ability to gain the benefit of two combat feats at the same
time. She can select one feat as a swift action or two feats as a move action.

At 11th level, a warsighted can use this ability to gain the benefits of three combat feats at the
same time. She can select one feat as a free action, two feats as a swift action, or three feats as
a move action.

At 15th level, a warsighted can use this ability to gain the benefit of one combat feat as an
immediate action or three combat feats as a swift action.

This ability replaces the revelations gained at 1st, 7th, 11th, and 15th levels.

## Recommended Mysteries {#recommended-mysteries}

[Battle](ref/mystery/battle), [bones](ref/mystery/bones), [nature](ref/mystery/nature),
[metal](ref/mystery/metal).
