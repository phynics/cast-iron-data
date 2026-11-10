+++
id = "ref/spell/sepia-snake-sigil"
kind = "spell"
title = "Sepia Snake Sigil"
aon = "SpellDisplay.aspx?ItemName=Sepia%20Snake%20Sigil"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sepia_snake_sigil", path = "json/spells15.json" },
]
[[sources]]
publication = "core-rulebook"
page = "339"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, M (powdered amber worth 500 gp and a snake scale)"
range = "touch"
effects = [
  { label = "Target", value = "one touched book or written work" },
]
duration = "permanent or until discharged; until released or 1d4 days + 1 day/level; see text"
saving_throw = "Reflex negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Bard, Occultist, Skald, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (powdered amber worth 500 gp and a snake scale)
Range: touch
Duration: permanent or until discharged; until released or 1d4 days + 1 day/level; see text
Saving throw: Reflex negates
Spell resistance: no
Target: one touched book or written work
Subschool: Creation
Descriptors: force
:::

You cause a small symbol to appear in the text of a written work. The text containing the symbol
must be at least 25 words long. When anyone reads the text containing the symbol, the sepia snake
sigil springs into being, transforming into a large sepia serpent that strikes at the reader,
provided there is line of effect between the symbol and the reader.

Simply seeing the enspelled text is not sufficient to trigger the spell; the subject must
deliberately read it. The target is entitled to a save to evade the snake's strike. If it succeeds,
the sepia snake dissipates in a flash of brown light accompanied by a puff of dun-colored smoke and
a loud noise. If the target fails its save, it is engulfed in a shimmering amber field of force and
immobilized until released, either at your command or when 1d4 days + 1 day per caster level have
elapsed.

While trapped in the amber field of force, the subject does not age, breathe, grow hungry, sleep, or
regain spells. It is preserved in a state of suspended animation, unaware of its surroundings. It
can be damaged by outside forces (and perhaps even killed), since the field provides no protection
against physical injury. However, a dying subject does not lose hit points or become stable until
the spell ends.

The hidden sigil cannot be detected by normal observation, and
[detect magic](ref/spell/detect-magic) reveals only that the entire text is magical.

A [dispel magic](ref/spell/dispel-magic) can remove the sigil. An [erase](ref/spell/erase) spell
destroys the entire page of text.

Sepia snake sigil can be cast in combination with other spells that hide or garble text, such as
[secret page](ref/spell/secret-page).
