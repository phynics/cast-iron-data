+++
id = "ref/spell/secluded-grimoire"
kind = "spell"
title = "Secluded Grimoire"
aon = "SpellDisplay.aspx?ItemName=Secluded%20Grimoire"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "secluded_grimoire", path = "json/spells15.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "17"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "spellbook touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 round
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: spellbook touched
Subschool: Summoning
:::

This spell sends a spellbook into a random but safe location on the Ethereal Plane, where it remains
indefinitely. When you cast this spell, the target spellbook dissolves into quickly fading lines of
energy and runes that reflect all of the spells stored within. Thereafter, you can retrieve the
spellbook by concentrating as a standard action, causing it to reappear in your hands. You cannot
cast this spell on another spellbook if you currently have a spellbook in the Ethereal Plane. No
other creatures or objects accompany the spellbook you send away, and the duration of any spells
currently affecting the spellbook continue normally.
