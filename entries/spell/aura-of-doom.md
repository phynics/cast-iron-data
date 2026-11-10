+++
id = "ref/spell/aura-of-doom"
kind = "spell"
title = "Aura of Doom"
aon = "SpellDisplay.aspx?ItemName=Aura%20of%20Doom"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aura_of_doom", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "207"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (powdered bone)"
range = "personal"
effects = [
  { label = "Area", value = "20-ft.-radius emanation centered on you" },
]
duration = "10 minutes/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Cleric, Oracle, Psychic, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, M/DF (powdered bone)
Range: personal
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: yes
Area: 20-ft.-radius emanation centered on you
Descriptors: emotion, fear, mind-affecting
:::

You emanate an almost palpable aura of horror. All non-allies within this spell's area, or that
later enter the area, must make a Will save to avoid becoming shaken. A successful save suppresses
the effect. Creatures that leave the area and come back must save again to avoid being affected by
the effect.
