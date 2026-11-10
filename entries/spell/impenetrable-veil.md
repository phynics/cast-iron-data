+++
id = "ref/spell/impenetrable-veil"
kind = "spell"
title = "Impenetrable Veil"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "impenetrable_veil", path = "json/spells14.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "25"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 9 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 9 },
  { class = "Spiritualist", level = 6 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, M (dust from the Dimension of Dreams worth 1,250 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Bard, Mesmerist, Skald, Spiritualist\
9: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (dust from the Dimension of Dreams worth 1,250 gp)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You enchant the target so it is nearly impossible to detect by both magical and mundane means,
granting it the following benefits. The target gains a bonus on Stealth checks equal to half your
caster level, and can use Stealth to hide from all creatures attempting to perceive it, even when it
lacks concealment or cover. It can attempt a Stealth check to avoid detection from creatures using
[blindsight](ref/rule/blindsight-and-blindsense), blindsense, or any ability that functions as
either (such as lifesense or [tremorsense](ref/umr/tremorsense)). Furthermore, the target leaves no
trail and cannot be tracked unless it chooses to leave a trail. If a creature attempts to discern
the target's presence or location using divination magic (including magic items with a divination
aura such as a crystal ball), that creature must succeed at a caster level check with a DC equal to
the target's Stealth bonus to discern any information about the target, and on a failed check cannot
do so for the spell's duration.
