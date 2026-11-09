+++
id = "ref/spell/riding-possession"
kind = "spell"
title = "Riding Possession"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "riding_possession", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/possession" },
]
[[sources]]
publication = "occult-adventures"
page = "185"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level (d); see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium\
3: Occultist, Spiritualist\
4: Arcanist, Mesmerist, Psychic, Sorcerer, Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level (d); see text
Saving throw: Will negates
Spell resistance: yes
Target: one creature
:::

You stealthily project your soul into the host's body as an observer, with limited ability to
influence the target. This functions as [possession](ref/spell/possession), except the host is still
in full control of its body and is unaware you are possessing it. You can't communicate with the
host directly, but you can cast mind-affecting spells or riding possession on the host as long as
you can cast these spells as purely mental actions. Even if the spell you cast would normally affect
more than one target or an area, it can affect only the host. If the host succeeds at a saving throw
against a spell that you cast in this way, it immediately becomes aware that it is possessed, and if
it was already aware, it receives another saving throw against riding possession.
[Protection from evil](ref/spell/protection-from-evil) and similar effects don't expel you from the
host, but they do prevent you from casting further spells from within your host until their
durations expire.
