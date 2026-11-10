+++
id = "ref/spell/call-animal"
kind = "spell"
title = "Call Animal"
aon = "SpellDisplay.aspx?ItemName=Call%20Animal"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "call_animal", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "209"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "see text"
effects = [
  { label = "Effect", value = "one animal whose CR is equal or less than your caster level" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Druid, Hunter, Mesmerist, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: see text
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Effect: one animal whose CR is equal or less than your caster level
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell calls the nearest wild animal of a particular type you designate (provided the animal's
CR is equal to or less than your caster level) to seek you out. The animal moves toward you under
its own power, so the time it takes to arrive depends on how close an animal of the desired type is
when you cast the spell. If there is no animal of that type capable of reaching you within the
spell's duration, you are aware of this fact, but the spell is wasted. Knowledge of the local fauna
makes this spell more effective, and the GM may permit a Knowledge (nature) skill check (DC 15) to
know what animals can be found in an area.

When the called animal arrives, it approaches to within 5 feet of you and remains nearby for the
duration of the spell. Its starting attitude is indifferent, modified by circumstances and
interaction. Other than starting attitude, this spell gives you no special influence or ability to
communicate with the called animal, although you may use other spells or abilities to do so.

Once the spell's duration expires, the animal acts in accordance with its attitude. Most animals
will likely wander off, but a hostile predatory animal may attack, especially if it is hungry or
provoked.

Domesticated animals or animals trained by someone else, including such creatures as familiars or
animal companions, are unaffected by call animals.
