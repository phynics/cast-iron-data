+++
id = "ref/spell/aura-alteration"
kind = "spell"
title = "Aura Alteration"
aon = "SpellDisplay.aspx?ItemName=Aura%20Alteration"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aura_alteration", path = "json/spells.json" },
]
[[sources]]
publication = "occult-adventures"
page = "157"

[fields]
kind = "spell"
school = "illusion"
levels = [
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Spiritualist", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one object or willing creature" },
]
duration = "1 day/level (D)"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Medium, Mesmerist, Occultist\
4: Psychic, Spiritualist
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 day/level (D)
Saving throw: Will negates (harmless) (object)
Spell resistance: yes
Target: one object or willing creature
:::

You mask and manipulate the target creature's or object's aura, confounding those who would attempt
to discern helpful information from it using the read aura unlock or the analyze aura spell. You can
change each of the following four auras with one casting of aura alteration.

_Alignment Aura:_ You can change the target's apparent alignment to thwart spells that detect
alignment, such as [detect evil](ref/spell/detect-evil). You can alter the alignment by up to one
step on each alignment axis, but can't make the creature appear to have a diametrically opposed
alignment. For instance, you couldn't make a lawful evil character appear to be chaotic or good. You
can also adjust the power of the alignment aura up or down in level by a number of steps equal to
1/2 your level or fewer.

_Emotion Aura:_ Your manipulations mask the true emotions of the target, instead depicting any
combination of colors on the emotional spectrum that you wish. Creatures attempting Bluff,
Diplomacy, Intimidate, or Sense Motive checks against the target receive no bonuses on their checks
based on information gleaned from the target's aura.

_Health Aura:_ You adulterate the target's aura to mask the condition of its physical body,
revealing instead a wounded status, poison or disease status, and conditions of your choice. You
likewise mask the target's available ki points or similar resources, manipulating its aura to
suggest any number within the range normally available to the target.

_Magic Aura:_ You alter a creature or item's magic aura so that it registers to
[detect magic](ref/spell/detect-magic) (and spells with similar capabilities, like
[analyze aura](ref/spell/analyze-aura)) as though it were nonmagical, a magic item of a kind you
specify, or the subject of a spell you specify. A single casting of aura alteration is sufficient to
mask all of the magic auras on the target. If an object bearing aura alteration has
[identify](ref/spell/identify) cast on it or is similarly examined, the examiner recognizes the aura
is false and detects the object's actual qualities if he succeeds at a Will save. If a targeted
item's own aura is overwhelming, aura alteration can't alter it.
