+++
id = "ref/arc-kineticist/dark-elementalist"
kind = "archetype"
title = "Dark Elementalist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Dark%20Elementalist"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dark_elementalist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "horror-adventures"
page = "56"

[fields]
kind = "archetype"
features = [
  { anchor = "dark-studies" },
  { anchor = "soul-power" },
]
trades = [
  { replaces = "Internal buffer", feature = "internal-buffer", by = ["soul-power"] },
  { alters = "Base saving throws", by = ["dark-studies"] },
  { alters = "the key ability score of wild talents", by = ["dark-studies"] },
  { alters = "Burn", feature = "burn", by = ["soul-power"] },
  { alters = "elemental overflow", feature = "elemental-overflow", by = ["soul-power"] },
  { alters = "Class skills", by = ["dark-studies"] },
]
+++

Some kineticists who are loathe to suffer the consequences of channeling their power study the
darkest esoteric energies of the planes and use souls to fuel their occult might. The spiritual
tortures these dark elementalists inflict upon their victims' souls are horrifically selfish acts on
par with the actions of [daemons](ref/family/daemon).

## Alignment {#alignment}

Since harming souls is a wicked act, a dark elementalist must be of an evil alignment. If she
becomes nonevil, she can't use any of her dark elementalist abilities other than dark studies,
though she can still use her other kineticist class features.

## Dark Studies {#dark-studies}

A dark elementalist's base Will save bonus from the kineticist class is equal to 2 + 1/2 her
kineticist level, and her base Reflex and Fortitude save bonuses are equal to 1/3 her kineticist
level. She gains all Knowledge skills as class skills.

A dark elementalist uses her Intelligence modifier instead of her Constitution modifier to determine
her damage with wild talents, the DCs of Constitution-based wild talents, the durations of wild
talents with Constitution-based durations, her bonus on [concentration](ref/rule/concentration)
checks for wild talents, and any other Constitution-based effects of all her wild talents.

This alters the kineticist's class skills and base saving throws and the key ability score of wild
talents.

## Soul Power {#soul-power}

A dark elementalist uses the souls of others to protect herself from the dangers of burn. She can't
choose to accept burn if doing so would raise her total number of points of burn above 3. However, a
number of times per day equal to her Intelligence modifier, as a full-round action she can gather up
the soul of a sentient creature with a CR equal to or higher than her character level, as long as
that creature died in the past minute. When she does, some of her existing burn is unloaded into the
departing soul, racking it with unspeakable torment, but reducing her current burn total by 1 point.
A soul used in this way cannot be brought back to life as if it died of a death effect. Using a soul
like this doesn't heal the nonlethal damage from that point of burn immediately, but does enable the
dark elementalist to heal the nonlethal damage from that point of burn normally.

At 6th level, racking a soul in this way forces anyone trying to bring the creature back to life to
succeed at a caster level check (DC = 10 + the dark elementalist's kineticist level) or the attempt
fails. At 11th level, even if the creature returns from the dead, its soul is so damaged by the
agony that it takes 2d6 points of [Wisdom damage](ref/rule/ability-damage-drain) (or 3d10 points of
sanity damage if using the [sanity system](ref/rule/sanity) found on page 12). At 16th level, the
soul is destroyed in the process, and the creature can be restored only by a
_[miracle](ref/spell/miracle)_ or _[wish](ref/spell/wish)_.

A dark elementalist gains attack and damage bonuses from elemental overflow based on how many times
that day she has used soul power to rack a soul, rather than based on her current burn total. For
instance, a 9th-level dark elementalist who used soul power to rack three or more souls during the
course of the day would add a +3 bonus on attack rolls and a +6 bonus on damage rolls. A dark
elementalist does not gain size bonuses to physical ability scores or a chance to ignore critical
hits and sneak attacks from elemental overflow.

This ability alters burn and elemental overflow and replaces internal buffer.
