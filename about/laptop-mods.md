# Laptop Mods

If you have a computer in your house that isn't your phone, tablet, or TV, it's most likely a laptop. 
They're harder to work in, but the rewards are often worth it.

## Hardware Upgrades
> If it doesn't meet your needs, make it make your needs.

### Storage Upgrades
#### A bigger drive

My personal laptop came with a substantial 256GB Solid State Drive, it's a fast drive, but it doesn't hold enough for all of the apps, homework, and projects I want on it.
So, carefully open the laptop, replace the drive with a bigger one, and move my data over. 
The migration completed happened overnight, and I was ready to go in the morning like nothing had changed.

#### A faster drive

Many older laptops, and even some newer ones, use a Hard Disk Drive for their storage. It's cheap, but compared to the newest tech it's painfully slow.
If you have a laptop that is "just super slow" or takes a *really* long time to boot up all the way, you might have one of these old pieces of hardware.

An SSD upgrade can speed up your computer a *lot*. 
I've done comparisons on family computers after performing the upgrade and found on average a 10x increase in load times.
That's boot up, app loading, websites, downloads, virus scans, and more!

## Charger Mods

USB-C is one of my favorite innovations to come out of the last decade. I can charge, transfer data, add another monitor (or three), and more. 
Frankly, the number one reason I don't buy an iPhone is because it would need its own cable to charge. 
With USB-C, I can bring one charger for my laptop, phone, and headphones. 

So what do I do if I get a free laptop that *can't* charge with USB-C? Well mod it in, of course!

### Chromebook Coversion

Chromebooks are an interesting beast.
As much as Google likes to tout their built-in security, better battery life, and fast boot times, the truth is that those are about the fancy, high-end ones that cost as much as a normal laptop.
The Chromebooks you usually find in use are slow because they're cheap. Their 'security' comes with Google selling your data to anyone with a few bucks.

But, what is a Chromebook but a normal laptop with a few tweaks?

Two problems arise: one is that a Chromebook's keyboard is not the same as a normal laptops. 
Buttons are missing, but for the most part they don't matter, and one can simply write a custom driver binary to change the behavior of the buttons as needed.
The second problem is that of storage. The cheap Chromebooks that you can find all over the used market only has 16GB of storage space, and even the newer ones only have 32 or 64.
64GB is *technically* enough for Windows, but only just barely. You really need a full SSD for Windows, and even some Linux flavors.

#### The SSD Mod

Chromebooks newer than about 2014 all have their storage devices soldered onto the motherboard. 
This is just terrible for many reasons, but chief for me it means I can't do a drop-in storage upgrade.
Instead, I relocated the USB 3.0 daughterboard of the Chromebook to deeper inside and simply plugged in a 120GB M.2 SSD into it. 
Windows isn't a fan of installing to a USB device, so it took some encouraging, but fortunately I only have to do that once...or three times to work out the kinks.

#### The Results

So, if Chromebooks can run Windows, how do the operating systems compare? Do Google's claims of faster boot times and better battery actually hold up?

Truth be told, I it seems like Windows may be better in some ways. Mind you, none of this is thoroughly tested.

Looking at boot times, there are noticable improvements, but because it's a much more complicated operating system it's likely to even out. 
Plus, I can't actuall install ChromeOS on the same upgraded SSD as Windows gets to use, so a fair comparison can't be made this way.

What about battery life? Well there really wasn't a noticable difference. It was about 5-6 hours of screen-on time either way. 
Given that the modding process involves installing a much more power-hungery SSD into the laptop, I suspect Windows could actually have *better* battery life in a fair fight.
I attribute part of this to using Microsoft Edge as my web browser of choice over Google Chrome. 
Edge has several battery-friendly changes compared to its competitor that appear to give it something of an edge.
