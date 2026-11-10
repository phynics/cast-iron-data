+++
id = "ref/spell/sleepwalk"
kind = "spell"
title = "Sleepwalk"
aon = "SpellDisplay.aspx?ItemName=Sleepwalk"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sleepwalk", path = "json/spells9.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "244"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Inquisitor", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (a sprig of belladonna worth 100 gp)"
range = "touch"
effects = [
  { label = "Target", value = "unconscious creature touched" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Inquisitor, Mesmerist, Psychic, Witch
Casting time: 1 round
Components: V, S, M (a sprig of belladonna worth 100 gp)
Range: touch
Duration: 1 hour/level (D)
Saving throw: Will negates, see text
Spell resistance: yes
Target: unconscious creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

You compel an unconscious or sleeping creature to rise and move in a half-awake state. The target
creature staggers about if led or guided, but remains helpless for all other purposes. The subject
moves at half speed and is limited to a single move action each round. It is not capable of moving
at a higher rate of speed or taking actions other than movement except by magical assistance, and
automatically fails any Dexterity- or Strength-based skill checks. If the creature takes any damage
while sleepwalking it must make a new saving throw or the spell ends and the creature awakes (if it
has more than 0 hit points). When the spell ends or is dismissed, the target remains unconscious and
must be awoken normally. While sleepwalk allows an unconscious creature to move, it does not awaken
the creature, nor does it stabilize or otherwise heal them. A disabled creature that moves about
while under the effects of this spell does not start dying again as a result of this movement.
