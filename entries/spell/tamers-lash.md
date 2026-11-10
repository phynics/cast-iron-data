+++
id = "ref/spell/tamers-lash"
kind = "spell"
title = "Tamer's Lash"
aon = "SpellDisplay.aspx?ItemName=Tamer%27s%20Lash"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tamers_lash", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "236"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "a whip of magical sound" },
]
duration = "1 round/level (D)"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Bloodrager, Bard, Hunter, Magus, Ranger, Skald
Casting time: 1 standard action
Components: V, S
Range: 0 ft.
Duration: 1 round/level (D)
Saving throw: Will partial (see text)
Spell resistance: yes
Effect: a whip of magical sound
Descriptors: sonic
:::

A 15-foot-long whip of sonic energy springs from your hand, delivering a loud crack when you strike
with it. The tamer's lash acts as a [whip](ref/eq-weapon/whip) that deals 1d4 points of sonic damage
on a hit, but it has no physical substance and you cannot use it to perform combat maneuvers, nor
can it be sundered or disarmed. If you strike an animal with the tamer's lash, the animal must
succeed at a Will saving throw or be unable to attack you for 1d3 rounds. Furthermore, if the
whipped animal starts its turn unable to attack you as a result of this spell and it is within 30
feet of you, it must spend its first action moving away from you, if it is able. Combat-trained
animals, animal companions, and animals with Hit Dice in excess of your caster level + 4 gain a +4
circumstance bonus on their saves to avoid being intimidated in this way. This intimidation effect
is a mind-affecting fear effect.
