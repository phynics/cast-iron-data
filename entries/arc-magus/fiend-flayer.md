+++
id = "ref/arc-magus/fiend-flayer"
kind = "archetype"
title = "Fiend Flayer"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Fiend%20Flayer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fiend_flayer", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "advanced-race-guide"
page = "170"

[fields]
kind = "archetype"
features = [
  { anchor = "infernal-mortification", level = 1 },
  { anchor = "magus-arcana" },
]
+++

Some tiefling magi can tap the dark energy of their fiendish blood to enhance their arcane and
combat talents. By physically carving away their tainted flesh, they can use its dark energies to
enhance their powers, call forth weapons from thin air, and bypass enemies' strongest defenses. A
fiend flayer has the following class features.

## Infernal Mortification (Su) {#infernal-mortification}

At 1st level, a fiend flayer can sacrifice some of his own infernal blood to add to his arcane pool.
Sacrificing blood in this way is a standard action. For every 2 points of
[Constitution damage](ref/rule/ability-damage-drain) the fiend flayer takes in this way, his arcane
pool increases by 1 point. Any arcane pool points gained in this way and not spent disappear the
next time the magus prepares his spells. Unlike normal ability score damage, this damage cannot be
healed by way of _[lesser restoration](ref/spell/restoration-lesser)_. Only time can heal the
Constitution damage taken by way of infernal mortification. This ability cannot be used if the fiend
flayer's Constitution damage is equal to or greater than 1/2 his Constitution score.

## Magus Arcana {#magus-arcana}

A fiend flayer gains access to the following magus arcana. He cannot select any arcana more than
once.

### Fiendblade (Su) {#fiendblade}

As a swift action, as long as the fiend flayer used infernal mortification that day to increase his
arcane pool, he can conjure forth a weapon using this arcana. Doing so costs 2 points from his
arcane pool. The weapon can take the form of any single one-handed melee weapon the fiend flayer is
proficient with. This weapon starts as a weapon with a +1 enhancement bonus, but for every four
levels beyond 3rd the fiend flayer possesses, the weapon gains another +1 enhancement bonus, to a
maximum of +5 at 19th level. This summoned weapon lasts for 1 minute.

At 5th level, these bonuses can be used to add any of the following weapon properties to the
fiendblade: _[anarchic](ref/magic-enh/anarchic)_, _[axiomatic](ref/magic-enh/axiomatic)_,
_[dancing](ref/magic-enh/dancing)_, _[flaming](ref/magic-enh/flaming)_, _burst_,
_[frost](ref/magic-enh/frost)_, _[icy burst](ref/magic-enh/icy-burst)_,
_[keen](ref/magic-enh/keen)_, _[shock](ref/magic-enh/shock)_,
_[shocking burst](ref/magic-enh/shocking-burst)_, _[speed](ref/magic-enh/speed)_, or
_[unholy](ref/magic-enh/unholy)_.

These bonuses and properties are decided when the arcane pool points are spent and cannot be changed
until the next time the fiend flayer uses this arcana. Another creature cannot wield the fiendblade;
if it leaves the hand of the fiend flayer, it dissipates in a wisp of red smoke that smells of
burning blood.

A fiend flayer can only have one fiendblade in existence at a time. If he uses this ability again,
the first fiendblade disappears.

### Bypassing Strike (Su) {#bypassing-strike}

The fiend flayer can expend 1 point from his arcane pool as a swift action to allow one melee or
spellstrike attack he makes before the end of his turn to ignore an evil outsider target's
[damage reduction](ref/rule/damage-reduction).
