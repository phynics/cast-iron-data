+++
id = "ref/spell/judgment-light"
kind = "spell"
title = "Judgment Light"
aon = "SpellDisplay.aspx?ItemName=Judgment%20Light"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "judgment_light", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "232"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Inquisitor", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "30-ft.-radius burst" },
]
duration = "instantaneous, see text"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Inquisitor
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: instantaneous, see text
Saving throw: see text
Spell resistance: yes
Area: 30-ft.-radius burst
Descriptors: light
:::

An inquisitor may only cast this spell while she has a judgment active. When she does cast this
spell, it causes one or more of the following effects based on the inquisitor's active judgments.

_Destruction:_ Red light erupts from the caster. Enemies in the area take 4d8 points of damage and
become shaken for 1d4 rounds. A successful Will saving throw halves the damage and negates the
shaken effect.

_Healing:_ Green light erupts from the caster. Allies in the area regain a number of hit points
equal to 1d8 + the caster's Wisdom modifier.

_Justice:_ Blue light erupts from the caster, revealing hidden and invisible creatures to all. The
light outlines such creatures for 1 round per caster level, imposing a -20 penalty on Stealth checks
on those creatures.

_Piercing:_ Violet light erupts from the caster, reducing the
[spell resistance](ref/rule/spell-resistance) of enemies within the burst by 5 for 1 round per
caster level.

_Protection:_ Amber light erupts from the caster, granting allies in the burst a +2 sacred bonus to
AC and CMD, and a +4 bonus to AC against critical confirmation attack rolls for 1 round per caster
level.

_Purity:_ White light erupts from the caster, allowing each ally within the burst to attempt a
saving throw against a single effect that allows a saving throw with a +2 sacred bonus on the roll.

_Resiliency:_ Golden light erupts from the caster, granting allies within the burst DR 3/magic or
the alignment your judgment allows for 1 round per caster level.

_Resistance:_ Copper light erupts from the caster, granting allies within the burst resistance 5
against the energy the judgment protects the inquisitor against when she casts this spell for 1
round per caster level.

_Smiting:_ Silver light erupts from the caster, making allies' weapons within the burst count as
magic, the alignment her weapon is, and adamantine for purposes of overcoming
[damage reduction](ref/rule/damage-reduction) for 1 round per caster level.
