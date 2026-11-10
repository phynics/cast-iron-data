+++
id = "ref/spell/canopic-conversion"
kind = "spell"
title = "Canopic Conversion"
aon = "SpellDisplay.aspx?ItemName=Canopic%20Conversion"
source_ids = ["faction-guide", "osirion-land-of-the-pharaohs"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "canopic_conversion", path = "json/spells2.json" },
]
[[sources]]
publication = "faction-guide"
page = "60"
[[sources]]
publication = "osirion-land-of-the-pharaohs"
page = "26"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "evil"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 round"
components = "V, S, M (black onyx worth 100 gp per hit die of the target), F (four alabaster canopic jars worth 100 gp each)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living humanoid" },
]
duration = "instantaneous and see text"
saving_throw = "Fortitude half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 9: Arcanist, Cleric, Oracle, Sorcerer, Wizard
Casting time: 1 round
Components: V, S, M (black onyx worth 100 gp per hit die of the target), F (four alabaster canopic jars worth 100 gp each)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous and see text
Saving throw: Fortitude half
Spell resistance: yes
Target: one living humanoid
Descriptors: death, evil
:::

This spell eviscerates the target, drawing forth its life essence as well as its internal organs.
The target takes 1d6 hit points of damage per caster level (maximum 20d6). If this damage kills the
target, the spell pulls the creature's organs into a set of 4 canopic jars and seals them; 1d4
rounds later, the corpse revives as a mummy (if 8 HD or fewer) or an advanced mummy (if 9 HD or
more).

The mummy is not under your control, but the canopic jars give the bearer certain powers over it.
Anyone holding one of the jars can communicate with the mummy as if the two shared a common
language. The bearer gains the benefits of [protection from evil](ref/spell/protection-from-evil)
and [sanctuary](ref/spell/sanctuary), but only against that mummy. Unsealing or breaking a jar is a
standard action, which dissipates its power (and protection) but lets the bearer issue a short
command to the mummy, similar to a suggestion spell (Will DC 23 negates). You (and only you) may
unseal all 4 jars in a 10-minute ritual to control the mummy with an effect similar to geas (Will DC
23 negates); most casters typically include a restriction that the mummy will not harm them, as
unsealing the jars leaves them vulnerable.

The pharaohs of ancient Osirion sometimes used this spell to punish their enemies. The
[Risen Guard](ref/rule/f-second-life) does not use the spell (though they have access to it),
preferring trustworthy living guardians for the Ruby Prince. The
[Whispering Way](ref/rule/f-gravepath) may have copies of the spell.
