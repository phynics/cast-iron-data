+++
id = "ref/spell/amnesia"
kind = "spell"
title = "Amnesia"
aon = "SpellDisplay.aspx?ItemName=Amnesia"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "amnesia", path = "json/spells.json" },
]
[[sources]]
publication = "villain-codex"
page = "8"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Medium\
4: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You cause the target to lose most of its memories; its skills, its past, and even its name become
mysteries to it. While the target can build new memories, it has trouble accessing those gained
before falling victim to the spell. The target can still speak and read any languages it knows and
perform basic tasks, but it loses all class abilities, feats, and skill ranks gained before being
affected by amnesia. It retains its base attack bonus, saving throws bonuses, Combat Maneuver Bonus,
Combat Maneuver Defense, total experience points, Hit Dice, and hit points. If the target gains a
character level while suffering from amnesia, it can use any abilities gained by that class level
normally. If the class level it gained was from a class in which it already has levels, it gains the
abilities of a 1st-level character of that class, even though it is technically of a higher level in
that class.

If the amnesia is cured, the target regains the full abilities of the class, including those gained
from any levels taken while suffering from this condition. Amnesia can be removed only by
[heal](ref/spell/heal), [limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle),
[psychic surgery](ref/spell/psychic-surgery), or [wish](ref/spell/wish).
