+++
id = "ref/spell/detect-mindscape"
kind = "spell"
title = "Detect Mindscape"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_mindscape", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-thoughts" },
]
[[sources]]
publication = "occult-adventures"
page = "164"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 minute/level (D)"
saving_throw = "Will negates, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Medium, Mesmerist, Psychic\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: 60 ft.
Duration: concentration, up to 1 minute/level (D)
Saving throw: Will negates, see text
Spell resistance: no
Area: cone-shaped emanation
:::

This spell functions similarly to [detect thoughts](ref/spell/detect-thoughts), allowing you to
sense when one or more creatures' consciousnesses are inside a [mindscape](ref/rule/mindscapes). The
amount of information revealed depends on how long you study a particular subject.

_First Round:_ You sense the presence or absence of a mindscape. At least one of the creatures
inside the mindscape must be within the cone-shaped area for you to detect the mindscape.

_Second Round:_ You sense the number of consciousnesses inside the mindscape. Not all of the
creatures within the mindscape must be standing inside the cone-shaped area of the spell for you to
count them; only one is required to get this reading. However, you can't determine the location of
the creatures if you can't see the creatures themselves. You sense their presence only in an
abstract way.

_Third Round:_ You sense an image of what's taking place inside the mindscape. The creature
controlling the mindscape can sense your efforts, and if it does not wish you to view the mindscape,
it can prevent this viewing with a successful Will save. Otherwise, you perceive the visuals
remotely, as if watching through a window. If a creature has disguised itself, you see only the
creature's mental mask (not its true form).

Each round, you can turn to detect mindscapes in a new area. The spell can penetrate many barriers,
but 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt blocks
it.

If you are within a mindscape when you cast this spell, you become aware you're in a mindscape. On
the second round, you can still detect how many consciousnesses are inside, but you don't get the
image of the mindscape in the third round.
