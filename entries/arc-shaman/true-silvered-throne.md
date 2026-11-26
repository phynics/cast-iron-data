+++
id = "ref/arc-shaman/true-silvered-throne"
kind = "archetype"
title = "True Silvered Throne"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20True%20Silvered%20Throne"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "true_silvered_throne", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "occult-origins"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "occult-grimoire", level = 1 },
  { anchor = "ritual-hex" },
  { anchor = "scarab-of-the-second-throne", level = 4 },
  { anchor = "wandering-ritual", level = 6 },
  { anchor = "esoteric-rites", level = 8 },
]
trades = [
  { replaces = "Spirit animal", feature = "spirit-animal", by = ["occult-grimoire"] },
  { replaces = "Wandering spirit", feature = "wandering-spirit", by = ["wandering-ritual"] },
  { replaces = "wandering hex", feature = "wandering-hex", by = ["wandering-ritual"] },
  { replaces = "8th-level hex", feature = "hex", levels = [8], by = ["esoteric-rites"] },
  { alters = "Class skills" },
]
+++

Members in good standing who have risen to a prestigious rank within the Esoteric Order of the
Palatine Eye, true silvered thrones have managed to discover rituals and occult secrets within the
lore of their order. They are scholars of ancient mysteries and keepers of forbidden secrets who go
beyond simply learning eldritch traditions to make the occult a part of their very souls.

## Class Skills {#class-skills}

A true silvered throne adds all Knowledge skills, Linguistics, and Sense Motive to his list of class
skills, but loses Handle Animal and Survival as class skills. This alters the shaman's class skills.

## Occult Grimoire (Ex) {#occult-grimoire}

A true silvered throne's divine magic arises from communion with spirits alongside study of archaic
lore compiled into a personal occult grimoire. Unlike a wizard's spellbook, this grimoire doesn't
contain specific spells. By studying his grimoire, a true silvered throne can prepare any spell on
the shaman spell list or provided by his spirit. If this grimoire is lost or destroyed, he cannot
prepare new spells or use his spirit magic class feature until it is replaced, which requires 1 week
of work. This ability replaces spirit animal.

## Ritual Hex {#ritual-hex}

A true silvered throne gains [Ritual Hex](ref/feat/ritual-hex) (see page 24) as a bonus feat.

## Scarab of the Second Throne (Ex) {#scarab-of-the-second-throne}

At 4th level, a true silvered throne successfully constructs a golden scarab that is infused with
some of his occult potential. Treat this construct as a
[clockwork spy](ref/monster/clockwork-clockwork-spy), except it has half its master's total hit
points regardless of its Hit Dice and can write and take dictation rather than record audio. If worn
in the true silvered throne's amulet slot, the golden scarab provides a +4 bonus to AC against sneak
attacks and attacks of opportunity, as the scarab animates and moves to intercept attacks. If lost
or destroyed, the golden scarab can be replaced in a week-long ritual costing 250 gp.

## Wandering Ritual (Su) {#wandering-ritual}

At 6th level, a true silvered throne can attempt to coax a nearby spirit into service with a
1-minute-long ritual once per day, gaining that spirit's spirit ability and adding its list of
spells to those he can cast using his spirit magic. The silvered throne can maintain this bond for 1
hour, or until he dismisses the spirit as a free action. At 12th level, he also gains this spirit's
greater spirit power while bonded, and at 20th level gains its true spirit power as well. He can
perform a wandering ritual one additional time per day at 8th level and 14th level. This ability
replaces wandering spirit and wandering hex.

## Esoteric Rites (Ex) {#esoteric-rites}

At 8th level, a true silvered throne gains a +1 insight bonus on skill checks attempted as part of
an [occult ritual](ref/rule/occult-rituals). This bonus increases by 1 for every 4 shaman levels
beyond 8th (to a maximum of +5 at 20th level). If the true silvered throne is the ritual's primary
caster, he also adds this bonus to the caster level of the ritual's effect. This ability replaces
the 8th-level hex.
