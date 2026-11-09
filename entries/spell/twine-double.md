+++
id = "ref/spell/twine-double"
kind = "spell"
title = "Twine Double"
aon = "SpellDisplay.aspx?ItemName=Twine%20Double"
source_ids = ["cheliax-empire-of-devils"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "twine_double", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/simulacrum" },
]
[[sources]]
publication = "cheliax-empire-of-devils"
page = "23"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, M (cloth and twine)"
range = "0 ft."
effects = [
  { label = "Effect", value = "one duplicate creature" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 10 minutes
Components: V, S, M (cloth and twine)
Range: 0 ft.
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Effect: one duplicate creature
Subschool: Shadow
:::

As [simulacrum](ref/spell/simulacrum), except you can only duplicate yourself, and the duplicate is
created from cloth and twine rather than ice and snow. The double looks exactly like you except its
eyes are balls of twine (DC 10 Perception check to recognize double's strange eyes). It wears
clothing and gear that appear exactly like what you are wearing at the time of casting. Its copies
of your magic items are non-functional but radiate magic and have the same auras as your items. Its
aura is identical to yours. Attempts to scry you while the double exists have a 50% chance of
targeting the double instead of you.

The double cannot attack, has no special abilities, and has a +0 bonus on all saves and checks. You
may verbally give the double orders as a free action, or control it telepathically as a standard
action. You know what the double is experiencing, and when controlling it telepathically you can see
and hear everything it sees and hears, though events at your location may drown out the sensory
inputs from the double. The double has hit points equal to half your hit points at the time of
casting. If brought to 0 hit points, it is destroyed, reverting to cloth and twine. The double is an
animated object.
