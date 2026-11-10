+++
id = "ref/spell/mad-sultans-melody"
kind = "spell"
title = "Mad Sultan's Melody"
aon = "SpellDisplay.aspx?ItemName=Mad%20Sultan%27s%20Melody"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mad_sultans_melody", path = "json/spells6.json" },
]
[[sources]]
publication = "horror-adventures"
page = "122"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting", "sonic"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (masterwork flute, pipe, or string instrument)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/2 levels, no two of which can be more than 30 ft. apart (see text)" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard\
4: Arcanist, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (masterwork flute, pipe, or string instrument)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature/2 levels, no two of which can be more than 30 ft. apart (see text)
Subschool: Compulsion
Descriptors: mind-affecting, sonic
:::

You imitate the mad cacophony created by the awful beings associated with the Outer God, Azathoth.
This spell targets only creatures with the ooze type, creatures with the amorphous special ability,
and non-bipedal creatures with a special association with the Outer Gods. This music draws the
targets' attention to the caster, as per the fascinate bardic performance. It affects mindless
creatures despite the mindless quality typically granting immunity to mind-affecting effects, though
it doesn't ignore any other immunity to mind-affecting effects the creature might have. The caster
doesn't have to maintain the effect each round - the music continues for the duration of the spell.
Creatures fascinated by mad sultan's melody become immune to any other casting of the spell for 24
hours after the spell ends, and the spell ends if the fascination breaks on any of its targets for
any reason (such as an attack).

If you have the bardic performance class feature and the fascinate bardic performance, you can
choose to use the spell's saving throw DC or a DC equal to 10 + 1/2 your levels in the class that
grants you bardic performance + your Charisma modifier, whichever is higher. If you choose to use
the latter DC, each round of the melody costs 1 round of bardic performance and it counts as an
active performance for determining how many performances you can have active.

This spell takes a toll on the caster. Each time you cast it, you take 1d4 points of Wisdom damage.
If your campaign uses [the sanity system](ref/rule/sanity), you instead take 2d6 points of sanity
damage.
