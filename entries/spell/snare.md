+++
id = "ref/spell/snare"
kind = "spell"
title = "Snare"
aon = "SpellDisplay.aspx?ItemName=Snare"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "snare", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "344"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "3 rounds"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "touched nonmagical circle of vine, rope, or thong with a 2 ft. diameter + 2 ft./level" },
]
duration = "until triggered or broken"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Hunter, Ranger\
3: Druid
Casting time: 3 rounds
Components: V, S, DF
Range: touch
Duration: until triggered or broken
Saving throw: none
Spell resistance: no
Target: touched nonmagical circle of vine, rope, or thong with a 2 ft. diameter + 2 ft./level
:::

This spell enables you to make a snare that functions as a magic trap. The snare can be made from
any supple vine, a thong, or a rope. When you cast snare upon it, the cord-like object blends with
its surroundings (DC 23 Perception check for a character with the trapfinding ability to locate).
One end of the snare is tied in a loop that contracts around one or more of the limbs of any
creature stepping inside the circle.

If a strong and supple tree is nearby, the snare can be fastened to it. The spell causes the tree to
bend, straightening when the loop is triggered, dealing 1d6 points of damage to the creature trapped
and lifting it off the ground by the trapped limb or limbs. If no such tree is available, the
cord-like object tightens around the creature, dealing no damage but causing it to be entangled.

The snare is magical. To escape, a trapped creature must make a DC 23 Escape Artist check or a DC 23
Strength check that is a full-round action. The snare has AC 7 and 5 hit points. A successful escape
from the snare breaks the loop and ends the spell.
