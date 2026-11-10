+++
id = "ref/spell/planar-inquiry"
kind = "spell"
title = "Planar Inquiry"
aon = "SpellDisplay.aspx?ItemName=Planar%20Inquiry"
source_ids = ["core-rulebook", "adventurers-guide", "arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_inquiry", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/planar-ally-lesser" },
]
[[sources]]
publication = "adventurers-guide"
page = "125"
[[sources]]
publication = "arcane-anthology"
page = "14"

[fields]
kind = "spell"
school = "conjuration [see text]"
subschools = ["Calling"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (offerings worth 500 gp plus payment, see text)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one called outsider of 6 HD or less" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text\]
Level: 3: Medium\
4: Cleric, Oracle, Psychic, Shaman, Warpriest
Casting time: 10 minutes
Components: V, S, DF, M (offerings worth 500 gp plus payment, see text)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one called outsider of 6 HD or less
Subschool: Calling
:::

### Planar Inquiry

Although he was hardly the first to turn to the Outer Planes for answers, Jatembe's dealings with
outsiders in his pursuit of enlightenment are legendary, and the Magaambya credits the Old-Mage with
the creation of this spell.

This spell calls a creature from another plane to your precise location, functioning like
_[lesser planar ally](ref/spell/planar-ally-lesser)_ except as noted. When you call a creature using
_planar inquiry,_ the only task that you can ask of the creature is for it to answer questions or
gather information regarding a specific topic (a person, a place, or a thing). After hearing your
request, if the creature has an appropriate Knowledge skill, it can attempt a check to provide the
information it has. If it lacks such a skill, the called creature leaves for 1d4 hours to gather
this information. Upon its return, you roll 1d20 + your caster level, and use the result to
determine what information the creature has gathered about the subject (as if using Diplomacy). The
called creature stays for up to 10 minutes as it relays this information to you, after which it
departs to its home plane. If the creature is attacked or damaged at any time during the spell's
duration, the spell ends and the creature returns to the plane from which you summoned it.

When you cast this spell, you can choose a specific kind of outsider to call, even calling an
individual creature by name. The kind of outsider called doesn't alter the effects of the spell, but
when you use planar inquiry to summon a creature with an alignment or elemental subtype, the spell
gains that descriptor. You cannot call an outsider whose Hit Dice exceed your caster level (maximum
18 HD) and you cannot use this spell to contact a unique outsider (such as a deity's herald) or an
outsider with mythic ranks.
