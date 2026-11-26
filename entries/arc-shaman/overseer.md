+++
id = "ref/arc-shaman/overseer"
kind = "archetype"
title = "Overseer"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Overseer"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "overseer", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "controlling-magic" },
  { anchor = "spirit-surge", level = 3 },
]
trades = [
  { replaces = "Spirit magic spells gained from the shaman's spirit", feature = "spirit-magic", by = ["controlling-magic"] },
  { alters = "Deliver touch spells spirit animal ability", by = ["spirit-surge"] },
]
+++

While all shamans use their connection to the spirits of the world to draw upon otherworldly magic
powers, the shamans of the Lands of the Linnorm Kings have a unique tradition in which they use the
power of patron spirits to directly control their enemies. Such overseers may assume roles as
religious leaders and protectors of their tribes, turning foes into short-term allies for the
tribe's greater good. Other overseers become tyrants who enforce their will upon the weak for
personal gain. In combat, an overseer manages the battlefield by debilitating foes using her hexes
and specialized spells.

## Controlling Magic (Su) {#controlling-magic}

The overseer adds the following spells to the list of spells she can cast using spirit magic: _charm
person_ (1st), _hideous laughter_ (2nd), _hold person_ (3rd), _crushing despair_ (4th), _feeblemind_
(5th), _mass suggestion_ (6th), _power word blind_ (7th), _irresistible dance_ (8th), and _dominate
monster_ (9th).

This ability replaces the spirit magic spells gained from the shaman's spirit.

## Spirit Surge (Ex) {#spirit-surge}

At 3rd level, an overseer gains the ability to cast any of her mind-affecting spells that target a
single creature through her spirit animal. When she's using this ability, the selected spell's range
becomes touch, and she must deliver the spell through the spirit animal via the spirit animal's
deliver touch spells supernatural ability. The shaman's effective caster level for these spells is 2
higher than her normal caster level. The overseer can deliver any other spells via the deliver touch
spells spirit animal ability.

This alters the deliver touch spells spirit animal ability.
