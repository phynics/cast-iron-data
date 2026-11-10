+++
id = "ref/spell/instant-fake"
kind = "spell"
title = "Instant Fake"
aon = "SpellDisplay.aspx?ItemName=Instant%20Fake"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instant_fake", path = "json/spells14.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "217"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of costume jewlery)"
range = "1 object touched"
effects = [
  { label = "Target", value = "one object weighting no more than 1 lb./level" },
]
duration = "1 minute/level"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Bard, Hunter, Inquisitor, Mesmerist, Occultist, Ranger\
4: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of costume jewlery)
Range: 1 object touched
Duration: 1 minute/level
Saving throw: Will disbelief (if interacted with)
Spell resistance: no
Target: one object weighting no more than 1 lb./level
Subschool: Figment
:::

You create an illusory duplicate of the target item. If you hold the charge on this spell, you can
deliver it while touching an object you steal with Sleight of Hand or a steal combat maneuver; in
this case, the illusion phases into existence exactly as you remove the genuine article, allowing
you to instantaneously replace a protected or guarded item with no change in appearance, weight, or
other factors.

The illusion appears to be a perfect replica. Actively examining the fake with an Appraise or
Perception check grants a creature a Will save, but on a failed saving throw, it concludes that the
fake is the genuine article. The illusion isn't a functional item, nor does it have any magical
properties of the original. For example, an instant fake of a set of thieves' tools can't be used to
pick a lock, a false warhammer can't harm a person or break an object, a suit of unreal chainmail
offers no actual protection, and an illusory potion of cure light wounds doesn't heal any hit points
when imbibed.
